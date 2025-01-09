from pathlib import Path
import pandas as pd
import networkx as nx
import numpy as np
import zarr

from lscma.io.pd_io import read_csv, write_csv
from lscma.io.nx_io import read_nx, write_nx
from lscma.io.zarr_io import read_zarr, write_zarr

def test_pd_io():
    # Test CSV I/O
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    csv_path = Path("test.csv")
    write_csv(csv_path, df)
    loaded_df = read_csv(csv_path)
    assert df.equals(loaded_df), "CSV I/O test failed"
    csv_path.unlink()  # Remove the file

def test_nx_io():
    # Test NetworkX I/O
    graph = nx.Graph()
    graph.add_node(1, label="A")
    graph.add_edge(1, 2, weight=0.5)
    nx_path = Path("test_graph.pkl")
    write_nx(nx_path, graph)
    loaded_graph = read_nx(nx_path)
    assert nx.is_isomorphic(graph, loaded_graph), "NetworkX I/O test failed"
    nx_path.unlink()  # Remove the file

def test_zarr_io():
    # Test Zarr I/O
    data = np.random.rand(3, 3)
    zarr_path = Path("test.zarr")
    key = "test_key"
    write_zarr(zarr_path, data, key)
    loaded_data = read_zarr(zarr_path)[key][:]
    assert np.array_equal(data, loaded_data), "Zarr I/O test failed"
    # Remove Zarr directory
    for item in zarr_path.rglob('*'):  # Recursively remove all files and directories
        if item.is_file():
            item.unlink()
        elif item.is_dir():
            item.rmdir()
    zarr_path.rmdir()

if __name__ == "__main__":
    test_pd_io()
    test_nx_io()
    test_zarr_io()
    print("All I/O tests passed.")
