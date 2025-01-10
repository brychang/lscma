import os
import sys
# Add the src directory to the sys.path so Sphinx can find your modules
sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'lscma'
author = 'Bryan Chang'
release = '0.0.1'
copyright = '2025, Bryan Chang'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',  # Core library for html generation from docstrings
    'sphinx.ext.autosummary',  # Create neat summary tables
    'sphinx_rtd_theme'
]
autosummary_generate = True  # Turn on sphinx.ext.autosummary
html_theme = "sphinx_rtd_theme"

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
