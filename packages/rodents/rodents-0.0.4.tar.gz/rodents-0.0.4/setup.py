from setuptools import setup

setup(
    name="rodents",
    version="0.0.4",
    py_modules=["rodentshaker"],
    entry_points={"console_scripts": ["rodents = rodents:run_jiggler"]},
    install_requires=open("requirements.txt", encoding="utf-8").readlines(),
)
