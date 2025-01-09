import zarr

def read_zarr(path):
    """
    Opens a Zarr file in read-only mode.

    Parameters:
    - path (str): Path to the Zarr file.

    Returns:
    - zarr.hierarchy.Group: The Zarr file opened as a group.
    """
    return zarr.open(path, mode='r')

def write_zarr(path, data, key):
    """
    Writes data to a Zarr file under the specified key.

    Parameters:
    - path (str): Path to the Zarr file.
    - data (array-like): The data to write.
    - key (str): The key under which the data will be stored.

    Returns:
    - None
    """
    root = zarr.open(path, mode='a')  # Open file in append mode to avoid overwriting
    root[key] = data
