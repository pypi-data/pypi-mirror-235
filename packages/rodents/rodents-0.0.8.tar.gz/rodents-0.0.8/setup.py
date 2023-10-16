from setuptools import setup, find_packages

setup(
    name="rodents",
    version="0.0.8",
    packages=find_packages(),
    entry_points={"console_scripts": ["rodents = rodents.rodents.jiggler:run_giggler"]},
    install_requires=open("requirements.txt", encoding="utf-8").readlines(),
)
