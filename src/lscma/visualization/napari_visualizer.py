"""Module for visualizing 3D images in napari"""
import numpy as np
import napari
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.patches import Patch

class NapariViewer:
    def __init__(self):
        self.viewer = napari.Viewer()

    def visualize_image(self, array):
        self.viewer.add_image(array)

    def visualize_label(self, array):
        self.viewer.add_labels(array)

    def visualize_graph(self, graph, label):
        positions = np.array([data['center_of_mass'] for node, data in graph.nodes(data=True)])
        labels = [data[label] for node, data in graph.nodes(data=True)]

        # Assign unique colors to labels
        unique_labels = sorted(set(labels))
        cmap = cm.get_cmap('tab20', len(unique_labels))  # Use a colormap
        label_to_color = {label: cmap(i) for i, label in enumerate(unique_labels)}
        colors = np.array([label_to_color[label] for label in labels])

        # Add Points layer
        self.viewer.add_points(
            positions,
            size=10,  # Adjust size as needed
            border_color=colors,
            face_color=colors,
            name='Nodes',
            scale=(4,1,1)
        )

        # Create a legend with label-color mappings
        legend_handles = [Patch(color=cmap(i), label=f'Label {label}') for i, label in enumerate(unique_labels)]

        # Plot legend using matplotlib
        plt.figure(figsize=(5, 3))
        plt.legend(handles=legend_handles, loc='center', title="Unknown Population Labels")
        plt.axis('off')  # Hide axes for the legend plot
        plt.show()
