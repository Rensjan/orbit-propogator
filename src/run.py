from physics.simulation import Simulation
from physics.body import Body, StateVector
from render.render import Renderer
import time
from collections import deque
earth_state = StateVector(5.9722e24, [0,0,0],[0,0,0])
moon_state = StateVector(7.3e22, [384400000,0,0], [1022,0,0])

earth = Body(6371000, earth_state)
moon = Body(1737400, moon_state)
sim = Simulation(bodies=[earth, moon], timestep=3600)  # 1 hour steps

distance_scale = 1 / 1e8   # scale down distances by 10 million
size_scale = 1 / 1e7     # scale down radii by 1 thousand
renderer = Renderer(sim.get_bodies(), distance_scale, size_scale)
renderer.start()


frame_duration = 1 / 60  # target frame duration
frame_times = deque(maxlen=30)  # store last 30 frame durations

last_fps_print = time.perf_counter()

for frame_count in range(3600):
    start_time = time.perf_counter()

    renderer.update(sim.get_bodies())
    sim.step()

    elapsed = time.perf_counter() - start_time
    sleep_time = frame_duration - elapsed
    if sleep_time > 0:
        time.sleep(sleep_time)

    total_frame_time = time.perf_counter() - start_time
    frame_times.append(total_frame_time)

    # Print average FPS every second
    if time.perf_counter() - last_fps_print >= 1.0:
        avg_frame_time = sum(frame_times) / len(frame_times)
        avg_fps = 1.0 / avg_frame_time if avg_frame_time > 0 else float('inf')
        print(f"Average FPS: {avg_fps:.2f}")
        last_fps_print = time.perf_counter()
