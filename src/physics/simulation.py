class Simulation():
    def __init__(self, bodies, timestep):
        self.bodies = bodies
        self.timestep = timestep
    
    def step(self):
        self.bodies[1].state_vector.position[1]+=3844000

    def get_bodies(self):
        return self.bodies