from __future__ import annotations

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "SeaDex Data Refinement"
copyright = "2025-present, Ravencentric"
author = "Ravencentric"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser", "sphinx_inline_tabs", "sphinx_new_tab_link"]
source_encoding = "utf-8"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_favicon = "./static/logo.png"
html_static_path = ["static"]
html_theme = "furo"
html_title = "SeaDex Data Refinement"
html_theme_options = {
    "source_repository": "https://github.com/Ravencentric/seadex-data-refinement",
    "source_branch": "main",
    "source_directory": "docs/",
}
html_last_updated_fmt = "%b %d, %Y"
