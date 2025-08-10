from physics.simulation import Simulation
from physics.body import Body, StateVector
from render.render import Renderer
import time
import numpy as np
earth_state = StateVector(5.9722e24, [0,0,0],[0,0,0])
moon_state = StateVector(7.34767309e22, [363300000, 0, 0], [0, 1075.9, 0])

earth = Body(6371000, earth_state)
moon = Body(1737400, moon_state)
sim = Simulation(bodies=[earth, moon], timestep=600)  # 1 hour steps

distance_scale = 1 / 1e8   # scale down distances by 10 million
size_scale = 1 / 1e7     # scale down radii by 1 thousand
renderer = Renderer(sim.get_bodies(), distance_scale, size_scale)


min_distance = float('inf')
max_distance = float('-inf')


for i in range(100000):
    if i % 10 == 0:
        renderer.update(sim.get_bodies())
    
    earth_pos = sim.get_bodies()[0].state_vector.position
    moon_pos = sim.get_bodies()[1].state_vector.position
    
    relative_pos = moon_pos - earth_pos
    distance = np.linalg.norm(relative_pos)
    
    if distance < min_distance:
        min_distance = distance
    if distance > max_distance:
        max_distance = distance
    
    sim.step()
    time.sleep(1/1000)

    print(f"Min distance (perigee): {min_distance:.6e} m")
    print(f"Max distance (apogee): {max_distance:.6e} m")