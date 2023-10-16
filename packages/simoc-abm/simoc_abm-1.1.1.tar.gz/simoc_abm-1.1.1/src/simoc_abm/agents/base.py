import math
from copy import deepcopy
from collections import defaultdict

from ..util import evaluate_reference, evaluate_growth, recursively_clear_lists

class BaseAgent:
    """Base class for all agents.

    :ivar str agent_id: A unique string
    :ivar int amount: Starting/Maximum number alive
    :ivar str description: Plaintext description
    :ivar str agent_class: Agent class name
    :ivar dict properties: Static vars, 'volume'
    :ivar dict capacity: Max storage per currency per individual
    :ivar dict thresholds: Env. conditions to die
    :ivar dict flows: Exchanges w/ other agents
    :ivar str cause_of_death: Reason for death
    :ivar int active: Current number alive
    :ivar dict storage: Currencies stored by total amount
    :ivar dict attributes: Dynamic vars, 'te_factor'
    :ivar AgentModel model: AgentModel instance
    :ivar bool registered: Whether agent has been registered
    :ivar dict records: Agent records
    """

    # ------------- SETUP  ------------- #
    def __init__(self, model, agent_id, amount=1, description=None, 
                 agent_class=None, properties=None, capacity=None, 
                 thresholds=None, flows=None, cause_of_death=None, active=None, 
                 storage=None, attributes=None):
        """Create an agent with the given parameters.

        This function is intended to save initial state only. All validation
        and setup should be done in the register() function, after all currencies
        and agents have been added to model.
        
        :param AgentModel model: AgentModel instance
        :param str agent_id: A unique string
        :param int amount: Starting/Maximum number alive
        :param str description: Plaintext description
        :param str agent_class: Agent class name
        :param dict properties: Static vars, 'volume'
        :param dict capacity: Max storage per currency per individual
        :param dict thresholds: Env. conditions to die
        :param dict flows: Exchanges w/ other agents
        :param str cause_of_death: Reason for death
        :param int active: Current number alive
        :param dict storage: Currencies stored by total amount
        :param dict attributes: Dynamic vars, 'te_factor'
        """
        # -- STATIC
        self.agent_id = agent_id
        self.amount = 1 if amount is None else amount 
        self.description = '' if description is None else description 
        self.agent_class = '' if agent_class is None else agent_class 
        self.properties = {} if properties is None else deepcopy(properties)
        self.capacity = {} if capacity is None else deepcopy(capacity)
        self.thresholds = {} if thresholds is None else deepcopy(thresholds)
        self.flows = {'in': {}, 'out': {}}
        for direction in ('in', 'out'):
            if flows is not None and direction in flows:
                self.flows[direction] = deepcopy(flows[direction])
        # -- DYNAMIC
        self.cause_of_death = cause_of_death
        self.active = amount if active is None else deepcopy(active)
        self.storage = {} if storage is None else deepcopy(storage)
        self.attributes = {} if attributes is None else deepcopy(attributes)
        # -- NON-SERIALIZED
        self.model = model
        self.registered = False
        self.records = {}

    def register(self, record_initial_state=False):
        """Validate inputs and setup agent.

        Called automatically by Agent.step() if self.registered is false. 
        
        :param bool record_initial_state: Whether to record initial state (i.e. step 0)
        """
        if self.registered:
            return
        if 'age' not in self.attributes:
            self.attributes['age'] = 0
        for currency in self.storage:
            if currency not in self.capacity:
                raise ValueError(f'Agent {self.agent_id} has storage for '
                                 f'{currency} but no capacity.')
            elif self.storage[currency] > self.capacity[currency] * self.active:
                raise ValueError(f'Agent {self.agent_id} has more storage '
                                 f'for {currency} than capacity.')
        # Initialize flow attributes and records, check connections
        flow_records = {'in': defaultdict(dict), 'out': defaultdict(dict)}
        for direction, flows in self.flows.items():
            for currency, flow in flows.items():
                self.register_flow(direction, currency, flow)
                for conn in flow['connections']:
                    agent = self.model.agents[conn]
                    for _currency in agent.view(currency):
                        record = [] if not record_initial_state else [0]
                        flow_records[direction][_currency][conn] = record

        # Initialize records skeleton
        self.records = {
            'active': [] if not record_initial_state else [self.active],
            'cause_of_death': self.cause_of_death,
        }
        if self.capacity:
            self.records['storage'] = {currency: [] if not record_initial_state 
                                       else [self.storage.get(currency, 0)] 
                                       for currency in self.capacity}
        if self.attributes:
            self.records['attributes'] = {attr: [] if not record_initial_state 
                                          else [self.attributes[attr]] 
                                          for attr in self.attributes}
        if flow_records['in'] or flow_records['out']:
            self.records['flows'] = flow_records
        self.registered = True

    def register_flow(self, direction, currency, flow):
        """Validate and setup flow.
        
        :param str direction: 'in' or 'out'
        :param str currency: Currency name
        :param dict flow: Flow dict, see Agent.flows
        """
        # Check flow fields
        allowed_fields = {'value', 'flow_rate', 'criteria', 'connections', 
                          'deprive', 'weighted', 'requires', 'growth'}
        for field in flow:
            if field not in allowed_fields:
                raise ValueError(f'Flow field {field} not allowed')
        # Initialize attributes
        if 'criteria' in flow:
            for path, criterion in flow['criteria'].items():
                if 'buffer' in criterion:
                    buffer_attr = f'{direction}_{currency}_criteria_{path}_buffer'
                    self.attributes[buffer_attr] = criterion['buffer']
        if 'deprive' in flow:
            deprive_attr = f'{direction}_{currency}_deprive'
            self.attributes[deprive_attr] = flow['deprive']['value']
        if 'growth' in flow:
            for mode, params in flow['growth'].items():
                growth_attr = f'{direction}_{currency}_{mode}_growth_factor'
                self.attributes[growth_attr] = evaluate_growth(self, mode, params)
        # Check flow connections
        for agent in flow['connections']:
            if agent not in self.model.agents:
                raise ValueError(f'Agent {agent} not registered')
            currency_type = self.model.currencies[currency]['currency_type']
            if currency_type == 'currency':
                if currency not in self.model.agents[agent].capacity:
                    raise ValueError(f'Agent {agent} does not store {currency}')
            else:
                cat_currencies = self.model.currencies[currency]['currencies']
                if not any(c in self.model.agents[agent].capacity 
                           for c in cat_currencies):
                    raise ValueError(f'Agent {agent} does not store any '
                                     f'currencies of category {currency}')

    # ------------- INSPECT ------------- #
    def view(self, view):
        """Return a dict with storage amount for single currency or all of a class

        :param str view: Currency or currency class name.

        :return: Dict with currency or class currencies as keys and storage amount as values. Includes all currencies for which the agent has capacity.
        """
        currency_type = self.model.currencies[view]['currency_type']
        if currency_type == 'currency':
            if view not in self.storage:
                return {view: 0}
            return {view: self.storage[view]}
        elif currency_type == 'category':
            cat_currencies = self.model.currencies[view]['currencies']
            return {currency: self.storage.get(currency, 0)
                    for currency in cat_currencies
                    if currency in self.capacity}
        
    def serialize(self):
        """Return json-serializable dict of agent attributes"""
        serializable = {'agent_id', 'amount', 'description', 'agent_class', 
                        'properties', 'capacity', 'thresholds', 'flows',
                        'cause_of_death', 'active', 'storage', 'attributes'}
        output = {k: deepcopy(getattr(self, k)) for k in serializable}
        return output

    def get_records(self, static=False, clear_cache=False):
        """Return records dict and optionally clear cache
        
        By default, only return fields which change over time. If static is True,
        return non-changing fields as well under the key 'static'. 

        :param bool static: Whether to return non-changing fields
        :param bool clear_cache: Whether to clear the records cache

        :return: Records dict
        """
        output = deepcopy(self.records)
        if static:
            static_records = self.serialize()
            non_static = ('cause_of_death', 'active', 'storage', 'attributes')
            for k in non_static:
                del static_records[k]
            output['static'] = static_records
        if clear_cache:
            self.records = recursively_clear_lists(self.records)
        return output

    def save(self, records=False):
        """Return a serializable copy of the agent
        
        :param bool records: Whether to include records
        
        :return: Dict with all agent attributes
        """
        output = self.serialize()
        if records:
            output['records'] = self.get_records()
        return output

    # ------------- UPDATE ------------- #
    def increment(self, currency, value):
        """Increment currency in storage as available, return actual receipt

        For positive values, add currency to internal storage up to capacity.
        For negative values, remove currency from internal storage down to 0.
        For negative values where currency is a currency class, remove 
        from all currencies in class proportional to their availability.
        
        :param str currency: Currency name or (negative value only) currency class
        :param float value: Amount to add (positive) or remove (negative) from internal storage

        :return: Dict with currency names as keys and actual amount added as values
        """
        if value == 0:  # If category, return dict of currencies
            available = self.view(currency)
            return {k: 0 for k in available.keys()}
        elif value < 0:  # Can be currency or category
            available = self.view(currency)
            total_available = sum(available.values())
            if total_available == 0:
                return available
            actual = -min(-value, total_available)
            increment = {currency: actual * stored/total_available
                         for currency, stored in available.items()}
            for _currency, amount in increment.items():
                if amount != 0:
                    self.storage[_currency] += amount
            return increment
        elif value > 0:  # Can only be currency
            if self.model.currencies[currency]['currency_type'] != 'currency':
                raise ValueError(f'Cannot increment agent by currency category ({currency})')
            if currency not in self.capacity:
                raise ValueError(f'Agent does not store {currency}')
            if currency not in self.storage:
                self.storage[currency] = 0
            total_capacity = self.capacity[currency] * self.active
            remaining_capacity = total_capacity - self.storage[currency]
            actual = min(value, remaining_capacity)
            self.storage[currency] += actual
            return {currency: actual}
        
    def get_flow_value(self, dT, direction, currency, flow, influx):
        """Return target flow value for a given time step

        :param float dT: Time step
        :param str direction: 'in' or 'out'
        :param str currency: Currency or currency class name
        :param dict flow: Flow dict
        :param dict influx: Dict of currencies and amounts already consumed this step

        :return: Float with target flow value (per individual)
        
        """
        # Baseline
        step_value = flow['value'] * dT
        # Adjust
        requires = flow.get('requires')
        if step_value > 0 and requires:
            if any(_currency not in influx for _currency in requires):
                step_value = 0
            else:
                for _currency in requires:
                    step_value *= influx[_currency]  # Scale flows to requires
        criteria = flow.get('criteria')
        if step_value > 0 and criteria:
            for path, criterion in criteria.items():
                buffer_attr = f'{direction}_{currency}_criteria_{path}_buffer'
                kwargs = {k: v for k, v in criterion.items() if k != 'buffer'}
                if evaluate_reference(self, path, **kwargs):
                    if 'buffer' in criterion and self.attributes[buffer_attr] > 0:
                        self.attributes[buffer_attr] -= dT
                        step_value = 0
                else:
                    step_value = 0
                    if 'buffer' in criterion and self.attributes[buffer_attr] == 0:
                        self.attributes[buffer_attr] = criterion['buffer']
        growth = flow.get('growth')
        if step_value > 0 and growth:
            for mode, params in growth.items():
                growth_attr = f'{direction}_{currency}_{mode}_growth_factor'
                growth_factor = evaluate_growth(self, mode, params)
                self.attributes[growth_attr] = growth_factor
                step_value *= growth_factor
        weighted = flow.get('weighted')
        if step_value > 0 and weighted:
            for field in weighted:
                if field in self.capacity:  # e.g. Biomass
                    weight = self.view(field)[field] / self.active
                elif field in self.properties:  # e.g. 'mass'
                    weight = self.properties[field]['value']
                elif field in self.attributes:  # e.g. 'te_factor'
                    weight = self.attributes[field]
                else:
                    raise ValueError(f'Weighted field {field} not found in '
                                     f'{self.agent_id} storage, properties, or attributes.')
                step_value *= weight
        return step_value
    
    def process_flow(self, dT, direction, currency, flow, influx, target, actual):
        """Update flow state post-exchange. Overloadable by subclasses.
        
        :param float dT: Time step
        :param str direction: 'in' or 'out'
        :param str currency: Currency or currency class name
        :param dict flow: Flow dict
        :param dict influx: Dict of currencies and amounts already consumed this step
        :param float target: Target flow value, as returned by get_flow_value, multiplied by active
        :param float actual: Actual flow value, as incremented from connections
        """
        available_ratio = round(0 if target == 0 else actual/target, 
                                self.model.floating_point_precision)
        if direction == 'in':
            influx[currency] = available_ratio
        if 'deprive' in flow:
            deprive_attr = f'{direction}_{currency}_deprive'
            if available_ratio < 1:
                deprived_ratio = 1 - available_ratio
                remaining = self.attributes[deprive_attr] - (deprived_ratio * dT)
                self.attributes[deprive_attr] = max(0, remaining)
                if remaining < 0:
                    n_dead = math.ceil(-remaining * self.active)
                    self.kill(f'{self.agent_id} deprived of {currency}', n_dead=n_dead)
            else:
                self.attributes[deprive_attr] = flow['deprive']['value']


    def step(self, dT=1):
        """Advance agent state by one step.

        If overloading this method, be sure to check if agent is registered
        interacting with state.
        
        :param float dT: Time step
        """
        if not self.registered:
            self.register()
        if self.active:
            self.attributes['age'] += dT
            # Check thresholds
            for currency, threshold in self.thresholds.items():
                if evaluate_reference(self, **threshold):
                    self.kill(f'{self.agent_id} passed {currency} threshold')

        # Execute flows
        influx = {}  # Which currencies were consumed, and what fraction of baseline
        for direction in ['in', 'out']:
            for currency, flow in self.flows[direction].items():

                # Calculate Target Value
                if self.active and 'value' in flow:
                    target = self.active * self.get_flow_value(dT, direction, currency, flow, influx)
                else:
                    target = 0

                # Process Flow
                remaining = float(target)
                for connection in flow['connections']:
                    agent = self.model.agents[connection]
                    if remaining > 0:
                        multiplier = {'in': -1, 'out': 1}[direction]
                        exchange = agent.increment(currency, multiplier * remaining)
                        exchange_value = sum(exchange.values())
                        remaining -= abs(exchange_value)
                    else:
                        exchange = {k: 0 for k in agent.view(currency).keys()}
                    # NOTE: This must be called regardless of whether the agent is active
                    for _currency, _value in exchange.items():
                        self.records['flows'][direction][_currency][connection].append(abs(_value))
                actual = target - remaining
                # TODO: Handle excess outputs; currently ignored

                # Respond to availability
                if self.active and 'value' in flow:
                    self.process_flow(dT, direction, currency, flow, influx, target, actual)

        # Update remaining records
        self.records['active'].append(self.active)
        for currency in self.capacity:
            self.records['storage'][currency].append(self.storage.get(currency, 0))
        for attribute in self.attributes:
            self.records['attributes'][attribute].append(self.attributes[attribute])
        self.records['cause_of_death'] = self.cause_of_death

    def kill(self, reason, n_dead=None):
        """Kill n_dead agents, or all if n_dead is None.
        
        :param str reason: Cause of death
        :param int n_dead: Number of agents to kill
        """
        n_dead = self.active if n_dead is None else n_dead
        self.active = max(0, self.active - n_dead)
        if self.active <= 0:
            self.cause_of_death = reason
