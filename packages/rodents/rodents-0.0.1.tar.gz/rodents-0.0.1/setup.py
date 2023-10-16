from setuptools import setup

setup(
    name="rodents",
    version="0.0.1",
    py_modules=["rodentshaker"],
    entry_points={"console_scripts": ["rodentshaker = jiggler:main"]},
    install_requires=open("requirements.txt", encoding="utf-8").readlines(),
)
