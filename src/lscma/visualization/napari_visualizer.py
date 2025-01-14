"""Module for visualizing 3D images in napari"""
import napari

class NapariViewer:
    def __init__(self):
        self.viewer = napari.Viewer()
    
    def visualize_image(self, array):
        self.viewer.add_image(array)
    
    def visualize_label(self, array):
        self.viewer.add_label(array)
    
    def visualize_graph(self, graph):
        pass
