# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'notes'
copyright = '2026, Katsuya Kondo'
author = 'Katsuya Kondo'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser",
"sphinx.ext.mathjax"]

templates_path = ['_templates']
exclude_patterns = []

source_suffix={".md":"markdown",
".rst": "restructuredtext"}

myst_enable_extensions = [
    "dollarmath",
    "amsmath"
]

mathjax3_config = {
    "tex": {
        "macros": {
            "bm": ["\\boldsymbol{#1}", 1],
        }
    }
}

language = 'jp'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
html_math_renderer="mathjax"