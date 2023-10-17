from setuptools import setup, find_packages
with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()
setup(
    name="chatnoti",
    version="0.1",
    description=" a common version for different notify platform",
    author= "skyLew",
    packages=find_packages(),
    install_requires=requirements
)
