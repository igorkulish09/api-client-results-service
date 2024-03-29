"""Setup script for api-client-result."""

from setuptools import find_packages, setup

setup(
    name='rest_clients_example',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests>=2.26.0',
        'httpx',
        'wemake-python-styleguide',
        'pydantic',
    ],
)
