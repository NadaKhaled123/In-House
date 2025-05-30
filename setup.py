from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in wo_workflow/__init__.py
from wo_workflow import __version__ as version

setup(
	name="wo_workflow",
	version=version,
	description="Wo Workflow",
	author="nada",
	author_email="nada@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
