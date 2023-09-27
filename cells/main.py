class Cell:
    def __init__(self, x, y, code, energy, size):
        # global physical properties - can't change them, but it's used for simulation purposes
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0

        # internal physical properties - can't change but can influence them
        self.code = code
        self.energy = energy
        self.size = size
        self.age = 0
        self.life_level = 1

        # actuable properties - can change them
        self.division_level = 0
        self.grow_rate = 0
        self.ax = 0
        self.ay = 0

    def act(self, chemicals):
        # change actuable properties based on internal properties
        action_from_chemicals = code.signal_to_action * chemicals.to_vector()
        action_from_internal_state = code.internal_state_to_action * internal_state
        action = action_from_signals + action_from_internal_state

        self.division_level = action[0]
        self.auto_destruction_level = action[1]
        self.ax = action[2]
        self.ay = action[3]

    def update(self, chemicals):
        # change internal properties based on physical principles and resilience
        self.age += 1

        # negative it consumes, positive it adds
        if(self.code.energy_consumption_factor > 0.5):
            self.code.energy_consumption_factor = 0.5
        
        energy_rate = - age * 0.01 * size + chemicals.food
        energy_rate += abs(energy_rate) * self.code.energy_consumption_factor 
        self.energy += energy_rate - chemicals.digestive_enzyme

        # grows according to the grow rate
        self.size += grow_rate

        # life level is based on energy
        self.life_level += (self.code.energy_threshold - self.energy)/self.code.nergy_threshold
        if(self.life_level > 1):
            self.life_level = 1

        # change global physical properties based on actuable properties
        self.x += self.vx
        self.y += self.vy

        self.vx += self.ax
        self.vy += self.ay

class Code:
    def __init__(self, energy_consumption_factor, signal_to_action_matrix, internal_state_to_action_matrix):
        self.energy_consumption_factor = energy_consumption_factor
        self.signal_to_action_matrix = signal_to_action_matrix
        self.internal_state_to_action_matrix = internal_state_to_action_matrix

class Chemicals:
    def __init__(self, digestive_enzyme, food, signals):
        self.digestive_enzyme = digestive_enzyme
        self.food = food
        self.signals = signals

    def to_vector(self):
        vector_signals = self.signals.map(lambda signal: signal.to_vector())
        return self.digestive_enzyme.to_vector() + self.food.to_vector() + self.signals.to_vector

class Signal:
    # represents the gradient of x and y of a chemical signal
    def __init__(self, value, gx, gy):
        self.value = value
        self.gx = gx
        self.gy = gy
    
    def to_vector(self):
        return [value, self.gx, self.gy]