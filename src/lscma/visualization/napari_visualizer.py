"""Module for visualizing 3D images in napari"""
import numpy as np
import napari
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.patches import Patch

class NapariViewer:
    """
    This class contains the napari visualization.
    It can visualize arrays as images or labels.
    It can visualize networkx graphs.
    """
    def __init__(self):
        """
        Initializes the Napari viewer.
        """
        self.viewer = napari.Viewer()

    def visualize_image(self, array):
        """
        Visualizes a 2D or 3D image array in the Napari viewer.
        
        Parameters:
        -----------
        array : numpy.ndarray
            The image data to be visualized.
        """
        self.viewer.add_image(array)

    def visualize_label(self, array):
        """
        Visualizes a label array (for segmentation) in the Napari viewer.
        
        Parameters:
        -----------
        array : numpy.ndarray
            The label data (segmentation or classification labels) to be visualized.
        """
        self.viewer.add_labels(array)

    def visualize_graph(self, graph, label):
        """
        Visualizes a networkx graph in the Napari viewer, where nodes are displayed as points 
        and labeled with distinct colors. It also displays a legend for the labels.
        
        Parameters:
        -----------
        graph : networkx.Graph
            The graph whose nodes and edges will be visualized.
        label : str
            The attribute name in the graph nodes used for labeling and coloring the nodes.
        """
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
