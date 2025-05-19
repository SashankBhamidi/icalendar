# icalendar documentation build configuration file
import importlib.metadata
import datetime
import os
import sys

sys.path.insert(0, os.path.abspath("../src/"))

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.coverage",
    "sphinx.ext.viewcode",
    "sphinx_copybutton",
    "sphinx_reredirects",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.napoleon",
]
source_suffix = {".rst": "restructuredtext"}
master_doc = "index"

project = "icalendar"
this_year = datetime.date.today().year
copyright = f"{this_year}, Plone Foundation"
release = version = importlib.metadata.version("icalendar")


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "pydata_sphinx_theme"
html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/collective/icalendar",
            "icon": "fa-brands fa-square-github",
            "type": "fontawesome",
            "attributes": {
                "target": "_blank",
                "rel": "noopener me",
                "class": "nav-link custom-fancy-css"
            }
        },
        {
            "name": "PyPI",
            "url": "https://pypi.org/project/icalendar",
            "icon": "fa-solid fa-download",
            "type": "fontawesome",
            "attributes": {
                "target": "_blank",
                "rel": "noopener me",
                "class": "nav-link custom-fancy-css"
            }
        },
    ],
    "navigation_with_keys": True,
    "search_bar_text": "Search",
    "show_nav_level": 2,
    "show_toc_level": 2,
    "use_edit_page_button": True,
}
html_context = {
#     "github_url": "https://github.com", # or your GitHub Enterprise site
    "github_user": "collective",
    "github_repo": "icalendar",
    "github_version": "main",
    "doc_path": "docs",
}
pygments_style = "sphinx"



# -- Intersphinx configuration ----------------------------------

# This extension can generate automatic links to the documentation of objects
# in other projects. Usage is simple: whenever Sphinx encounters a
# cross-reference that has no matching target in the current documentation set,
# it looks for targets in the documentation sets configured in
# intersphinx_mapping. A reference like :py:class:`zipfile.ZipFile` can then
# linkto the Python documentation for the ZipFile class, without you having to
# specify where it is located exactly.
#
# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}


# -- sphinx-reredirects configuration ----------------------------------
# https://documatt.com/sphinx-reredirects/usage.html
redirects = {
    "contributing": "/contribute/index.html",
    "about": "/index.html#about-icalendar",
}


man_pages = [("index", "icalendar", "icalendar Documentation", ["Plone Foundation"], 1)]

htmlhelp_basename = "icalendardoc"
