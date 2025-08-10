import pyvista as pv

class Renderer:
    def __init__(self, bodies, distance_scale=1.0, size_scale=1.0):
        self.distance_scale = distance_scale
        self.size_scale = size_scale
        
        self.plotter = pv.Plotter()
        self.spheres = []

        for i, body in enumerate(bodies):
            scaled_pos = [coord * self.distance_scale for coord in body.state_vector.position]
            scaled_radius = body.r * self.size_scale
            sphere = pv.Sphere(radius=scaled_radius, center=scaled_pos)
            color = 'blue' if i == 0 else 'grey'
            actor = self.plotter.add_mesh(sphere, color=color)
            self.spheres.append(actor)
        
        self.plotter.camera_position = [(0, 0, 50), (0, 0, 0), (0, 1, 0)]
        self.plotter.show(interactive_update=True,auto_close=False)

    def start(self):
        """Open the rendering window, blocks until closed."""
        

    def update(self, bodies):
        for i, body in enumerate(bodies):
            scaled_pos = [coord * self.distance_scale for coord in body.state_vector.position]
            self.spheres[i].SetPosition(scaled_pos)
        self.plotter.render()
