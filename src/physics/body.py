import numpy as np
class Body:
    def __init__(self, r, state_vector):
        self.r=r
        self.state_vector = state_vector
        self.force = np.zeros(3, dtype=float)
class StateVector:
    def __init__(self, mass, position, velocity):
        self.mass = mass
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)


    def __repr__(self) -> str:
        return f"StateVector(position={self.position}, velocity={self.velocity})"