
from pathlib import Path

import toml
from setuptools import setup, find_packages

pyproject = toml.load('pyproject.toml')

this_directory = Path(__file__).parent
long_description = (this_directory / 'README.md').read_text()
long_description_content_type = 'text/markdown'

setup(
    name=pyproject["project"]["name"],
    version=pyproject["project"]["version"],
    author=pyproject["project"]["authors"][0]["name"],
    author_email=pyproject["project"]["authors"][0]["email"],
    description=pyproject["project"]["description"],
    keywords=pyproject["project"]["keywords"],
    license=pyproject["project"]["license"],
    project_urls=pyproject["project"]["urls"],
    url=pyproject["project"]["urls"]["repository"],

    long_description=long_description,
    long_description_content_type=long_description_content_type,

    python_requires=pyproject["project"]["requires-python"],
    install_requires=pyproject["project"]["dependencies"],
    include_package_data=True,
    packages=find_packages(include=['dtaianomaly', 'dtaianomaly.*']),

    setup_requires=pyproject["build-system"]["requires"],
    zip_safe=False,
)
