from setuptools import setup, find_packages

setup(
    name="autowired",
    version="0.0.4",
    description="A minimalistic dependency injection library for Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Nicolai Großer",
    author_email="nicolai.grosser@googlemail.com",
    packages=find_packages(),
    install_requires=[],
)
