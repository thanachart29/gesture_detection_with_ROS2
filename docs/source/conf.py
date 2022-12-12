import datetime
import string
import sys
import os

sys.path.append(os.path.abspath('sphinxext'))


# Package information
project = "CACAO@HOME Robot"
author = "Cacao Team"
copyright = f"2022-{datetime.date.today().year}, {author}"

# extensions = ['breathe', 'sphinx.ext.graphviz', 'sphinxcontrib.plantuml', 'sphinx.ext.extlinks']
extensions = ['sphinx_tabs.tabs']
sphinx_tabs_valid_builders = ['linkcheck']
sphinx_tabs_disable_tab_closing = True
sphinx_tabs_disable_css_loading = True
source_suffix = ".rst"
pygments_style = "sphinx"

master_doc = "index"
language = 'en'

# Output options
#html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_style = "css/style.css"
# html_logo = "logo_catoct.jpg"
html_show_sphinx = False

# Doc version sidebar
templates_path = ["_templates"]
