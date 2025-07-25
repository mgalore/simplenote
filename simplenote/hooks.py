from . import __version__ as app_version

app_name = "simplenote"
app_title = "Simple Note"
app_publisher = "Your Name"
app_description = "A simple note-taking app built with Frappe"
app_email = "your.email@example.com"
app_license = "MIT"

# Required apps
required_apps = ["frappe"]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/simplenote/css/simplenote.css"
# app_include_js = "/assets/simplenote/js/simplenote.js"

# include js, css files in header of web template
# web_include_css = "/assets/simplenote/css/simplenote.css"
# web_include_js = "/assets/simplenote/js/simplenote.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "simplenote/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}