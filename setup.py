from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in investigation_app/__init__.py
from investigation_app import __version__ as version

setup(
	name="investigation_app",
	version=version,
	description="This app is for testing purposes",
	author="Sofian Saleh",
	author_email="sofiane.saleh11@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
