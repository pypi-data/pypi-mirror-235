from setuptools import setup, find_packages

setup(
    name="django-crm-events",
    version="0.0.4",
    packages=find_packages(),
    install_requires=["Django", "requests"],
)
