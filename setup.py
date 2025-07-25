from setuptools import setup, find_packages

# get version from __version__ variable in simplenote/__init__.py
from simplenote import __version__ as version

setup(
	name="simplenote",
	version=version,
	description="A simple note-taking app built with Frappe",
	author="Your Name",
	author_email="your.email@example.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=[]
)