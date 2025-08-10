from itertools import combinations
import numpy as np
class Simulation():
    def __init__(self, bodies, timestep):
        self.bodies = bodies
        self.timestep = timestep
    
    def step(self):
        G = 6.67430e-11

        # Step 1: Calculate forces & accelerations at current positions
        for body in self.bodies:
            body.force[:] = 0

        for b1, b2 in combinations(self.bodies, 2):
            r_vec = b2.state_vector.position - b1.state_vector.position
            r_mag = np.linalg.norm(r_vec)
            if r_mag == 0:
                continue
            r_hat = r_vec / r_mag
            force_mag = G * b1.state_vector.mass * b2.state_vector.mass / (r_mag**2)
            force = force_mag * r_hat
            b1.force += force
            b2.force -= force

        accelerations_current = [body.force / body.state_vector.mass for body in self.bodies]

        for i, body in enumerate(self.bodies):
            body.state_vector.velocity += accelerations_current[i] * self.timestep
            body.state_vector.position += body.state_vector.velocity * self.timestep

        
       


    def get_bodies(self):
        return self.bodies