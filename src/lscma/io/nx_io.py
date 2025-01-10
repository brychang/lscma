"""Module for handling I/O operations related to the NX file format."""
import pickle
import networkx as nx

def read_nx(path):
    """
    Read a NetworkX graph from a pickle file.

    Parameters:
        path (str): Path to the pickle file.

    Returns:
        nx.Graph: The NetworkX graph object.
    """
    with open(path, 'rb') as f:
        graph = pickle.load(f)
    return graph

def write_nx(path, graph):
    """
    Write a NetworkX graph to a pickle file.

    Parameters:
        path (str): Path where the pickle file will be saved.
        graph (nx.Graph): The NetworkX graph object to save.

    Returns:
        None
    """
    with open(path, 'wb') as f:
        pickle.dump(graph, f)
