"""
Configuration file for the Sphinx documentation builder.

For the full list of built-in configuration values, see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""
import codecs
import os
import re
import sys

sys.path.append(".")  # links
sys.path.insert(0, os.path.abspath(".."))  # sphinx utils
sys.path.insert(0, os.path.abspath("../.."))  # task runner docs and utils
sys.path.insert(0, os.path.abspath("../../src"))
# pylint: disable=import-error, wildcard-import, wrong-import-position, unused-wildcard-import
from links import *
from links.link import *
from docs.utils import contributors


def find_version(*file_paths):
    """Find project version in `src/__init__.py`

    Returns
    -------
    _type_
        _description_

    Raises
    ------
    RuntimeError
        _description_
    """
    version_match = r"^__version__ = ['\"]([^'\"]*)['\"]"
    here = os.path.join(os.path.join(os.path.dirname(__file__), os.pardir), os.pardir)
    parent = os.path.abspath(here)
    version_file = read(*file_paths, here=parent)
    version_match = re.search(version_match, version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


def read(*parts, here):
    """_summary_

    Parameters
    ----------
    here : _type_
        _description_

    Returns
    -------
    _type_
        _description_
    """
    return codecs.open(os.path.join(here, *parts), "r").read()


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

PROJECT = "arteklabs-docs"
# pylint: disable=redefined-builtin, invalid-name
copyright = "2023, Arteklabs"
author = "arteklabs"
release = find_version("src", "__init__.py")

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    # display docs build time
    "sphinx.ext.duration",
    # process python docstrings in src
    "sphinx.ext.autodoc",
    # test code snippets
    "sphinx.ext.doctest",
    # adding an explicit target to each section and making sure is unique
    "sphinx.ext.autosectionlabel",
    # link to source code
    # 'sphinx.ext.viewcode',
    "sphinx.ext.autodoc",
    "sphinx.ext.linkcode",
    # markdown support
    "m2r2",
]
autosectionlabel_prefix_document = True
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = "furo"
html_static_path = ["_static"]
html_theme_options = {
    "light_logo": "logo-light-mode.svg",
    "dark_logo": "logo-dark-mode.svg",
}
html_css_files = [
    "css/custom.css",
]
html_title = PROJECT

# variables
rst_epilog = f"""
.. |project| replace:: ``{PROJECT}``
"""

# hyperlinks
# :nnedh:`github <>`
extlinks = {"github": ("https://github.com/%s", "%s")}


def linkcode_resolve(domain, info):
    """source code url resolver

    .. note::

       the release branch is 'latest', this information could be fetched from the repo
       programatically.

    Parameters
    ----------
    domain : _type_
        _description_
    info : _type_
        _description_

    Returns
    -------
    _type_
        _description_
    """
    url = None
    if domain == "py" and info["module"]:
        src = info["module"].replace(".", "/")
        repo = "https://github.com/arteklabs/docs"
        url = f"{repo}?path=/{src}&version=GBdev&_a=contents"

    return url
