import shutil
from pathlib import Path
import pandas as pd
import networkx as nx
import numpy as np
import zarr
import pytest

from lscma.io.pd_io import read_csv, write_csv
from lscma.io.nx_io import read_nx, write_nx
from lscma.io.zarr_io import read_zarr, write_zarr

@pytest.fixture
def temp_csv_file():
    temp_path = Path("temp_test_file.csv")
    yield temp_path
    if temp_path.exists():
        temp_path.unlink()

@pytest.fixture
def temp_nx_file():
    temp_path = Path("temp_test_file.nx")
    yield temp_path
    if temp_path.exists():
        temp_path.unlink()

@pytest.fixture
def temp_zarr_dir():
    temp_path = Path("temp_test_dir.zarr")
    yield temp_path
    if temp_path.exists():
        shutil.rmtree(temp_path)

# CSV I/O Tests
def test_pd_io_empty(temp_csv_file):
    df = pd.DataFrame()
    write_csv(temp_csv_file, df)
    loaded_df = read_csv(temp_csv_file)
    assert df.equals(loaded_df), "Empty DataFrame I/O test failed"

def test_pd_io_special_chars(temp_csv_file):
    df = pd.DataFrame({"A@#": [1, 2], "B$%^": [3, 4]})
    write_csv(temp_csv_file, df)
    loaded_df = read_csv(temp_csv_file)
    assert df.equals(loaded_df), "Special characters in DataFrame I/O test failed"

# NetworkX I/O Tests
def test_nx_io_directed(temp_nx_file):
    graph = nx.DiGraph()
    graph.add_node(1, label="A")
    graph.add_edge(1, 2, weight=0.5)
    write_nx(temp_nx_file, graph)
    loaded_graph = read_nx(temp_nx_file)
    assert nx.is_isomorphic(graph, loaded_graph), "Directed graph I/O test failed"

def test_nx_io_empty(temp_nx_file):
    graph = nx.Graph()
    write_nx(temp_nx_file, graph)
    loaded_graph = read_nx(temp_nx_file)
    assert nx.is_isomorphic(graph, loaded_graph), "Empty graph I/O test failed"

# Zarr I/O Tests
def test_zarr_io_multiple_keys(temp_zarr_dir):
    data1 = np.random.rand(3, 3)
    data2 = np.random.rand(2, 2)
    write_zarr(temp_zarr_dir, data1, "key1")
    write_zarr(temp_zarr_dir, data2, "key2")
    loaded_data1 = read_zarr(temp_zarr_dir)["key1"][:]
    loaded_data2 = read_zarr(temp_zarr_dir)["key2"][:]
    assert np.array_equal(data1, loaded_data1), "Multiple keys (key1) test failed"
    assert np.array_equal(data2, loaded_data2), "Multiple keys (key2) test failed"

def test_zarr_io_overwrite(temp_zarr_dir):
    data1 = np.random.rand(3, 3)
    data2 = np.random.rand(3, 3)
    write_zarr(temp_zarr_dir, data1, "key")
    write_zarr(temp_zarr_dir, data2, "key")  # Overwrite
    loaded_data = read_zarr(temp_zarr_dir)["key"][:]
    assert np.array_equal(data2, loaded_data), "Overwrite key test failed"
