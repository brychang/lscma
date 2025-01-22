# **LSCMA: Light Scanning Confocal Microscopy Analysis**

![License](https://img.shields.io/badge/license-MIT-green)  
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)  
![Build Status](https://img.shields.io/badge/build-passing-brightgreen)

## **Overview**

**NOTICE**: This is only public because Github restricts Github Pages to public repositories. I am using this project to explore writing a python package.

**NOTICE**: This placeholder description was written by ChatGPT and should be reviewed and updated by the project maintainers to ensure accuracy and completeness.

`lscma` (Light Scanning Confocal Microscopy Analysis) is a Python package for analyzing large datasets generated from light scanning confocal microscopy (LSCM). The package provides tools to streamline workflows, including:

- **Data Preprocessing**: Import, reorganize, and store 4D microscopy datasets as `.zarr` files for efficient handling.
- **Segmentation**: Apply segmentation algorithms like PlantSeg to extract cellular regions.
- **Graph-Based Analysis**: Convert segmented images into graph representations (NetworkX), with nodes representing cells and edges denoting physical interactions.
- **Classification**: Classify cells using KNN, random forests, and emerging techniques like graph neural networks (GNNs).
- **Visualization**: Extend tools like Napari for interactive visualization and annotation.

Although designed with pancreatic islets in mind, the package is flexible enough to be adapted for other tissues and research contexts.

---

## **Features**

- **File Handling**
  - Read proprietary Carl Zeiss `.czi` files and extract metadata.
  - Reorganize datasets into `.zarr` format for efficient storage and analysis.

- **Data Processing**
  - Apply segmentation algorithms (e.g., PlantSeg).
  - Generate metadata-rich Pandas DataFrames linking tissue samples to their properties.

- **Graph Representations**
  - Convert segmented images into graph structures with detailed node and edge attributes.
  - Analyze tissue organization using graph metrics.

- **Classification**
  - Classify cells using built-in methods or integrate new machine learning models.

- **Visualization**
  - Interactive visualization with Napari, including annotation capabilities.

---

## **Installation**

### **Dependencies**
`lscma` requires Python 3.8 or later. Key dependencies include:
- `numpy`
- `scipy`
- `pandas`
- `zarr`
- `networkx`
- `napari`
- `plantseg`
- `sklearn`

To install, clone the repository and install the package using `pip`:

```bash
git clone https://github.com/your-username/lscma.git
cd lscma
pip install .
```

---

## **Usage**

### **Example Workflow**

Below is a simplified pipeline for analyzing pancreatic islet tissue samples:

1. **Reorganize Raw Data**
   ```python
   from lscma.io import czi_reader, zarr_writer
   raw_data = czi_reader.load_czi("path/to/file.czi")
   zarr_writer.save_as_zarr(raw_data, "path/to/output.zarr")
   ```

2. **Segmentation**
   ```python
   from lscma.preprocessing import segmentation
   segmentation.apply_plantseg("path/to/output.zarr", config="plantseg_config.json")
   ```

3. **Graph Representation**
   ```python
   from lscma.analysis import graph_utils
   graph = graph_utils.create_cell_graph("path/to/output.zarr")
   ```

4. **Classification**
   ```python
   from lscma.analysis import classification
   classified_graph = classification.knn_classifier(graph, k=5)
   ```

5. **Visualization**
   ```python
   from lscma.analysis import visualization
   visualization.plot_graph(classified_graph)
   ```

For more detailed examples, check the [examples directory](examples/).

---

## **Documentation**

Comprehensive documentation is available [here](./docs/_build/html/index.html). It includes:

- Installation instructions
- API references
- Example workflows
- Advanced usage and configuration

---

## **Contributing**

Contributions are welcome! If you find a bug, have a feature request, or want to contribute code, please:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/my-feature`).
3. Submit a pull request.

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Acknowledgments**

- PlantSeg developers for their segmentation tools.
- Napari for interactive visualization capabilities.
- Contributors to scientific Python libraries like NumPy, SciPy, and NetworkX.
