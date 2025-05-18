from setuptools import setup, find_packages

version = "0.1.0"

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()


setup(
        name="PyRDB",
        url="https://github.com/LucaBonamino/PyRDB.git",
        author="LucaBonamino",
        version=version,
        description="A dummy relational database in Python",
        packages=find_packages(where="src", include=("PyRDB",), exclude=("tests",)),
        package_dir={"": "src"},
        install_requires=requirements
)
