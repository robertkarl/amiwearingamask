import io

from setuptools import find_packages
from setuptools import setup

with io.open("README.md", "rt", encoding="utf8") as f:
    readme = f.read()

setup(
    name="cbr",
    version='0.0.1',
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "flask",
        "torch",
        "torchvision",
        "fastai",
        "werkzeug==0.16.1",
    ],
)
