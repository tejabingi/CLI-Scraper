from setuptools import setup
setup(
    name="cli_scraper",
    version="0.1",
    py_modules=["main", "scraper"],
    install_requires=[
        "requests"
    ],
)