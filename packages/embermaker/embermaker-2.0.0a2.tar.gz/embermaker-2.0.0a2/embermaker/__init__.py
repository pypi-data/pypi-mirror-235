"""
EmberMaker is a cientific graphic library aimed at (re)producing "burning ember" diagrams
of the style used in IPCC (Intergovernmental Panel on Climate Change) reports.
"""
import toml  # Get version from pyproject.toml
from pathlib import Path
pyproject = toml.load(Path(__file__).parent.parent / "pyproject.toml") # This is in a nested directory, 2 directories down
__version__ = pyproject["tool"]["poetry"]["version"]
