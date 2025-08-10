class Body:
    def __init__(self, r, state_vector):
        self.r=r
        self.state_vector = state_vector

class StateVector:
    def __init__(self, mass, position, velocity):
        self.mass = mass
        self.position = position
        self.velocity = velocity

    def __repr__(self) -> str:
        return f"StateVector(position={self.position}, velocity={self.velocity})"