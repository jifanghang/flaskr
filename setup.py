# to setup the project into a package - for installation
from setuptools import find_packages, setup

setup(
	name = 'jBlogger',
	version = '1.0.0',
	packages = find_packages(),
	include_package_data = True,
	zip_safe = False,
	install_requires = [ 'flask', ],
)