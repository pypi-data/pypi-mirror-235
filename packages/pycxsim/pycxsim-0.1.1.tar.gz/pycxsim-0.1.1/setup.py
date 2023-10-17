from setuptools import setup, find_packages

# Read the contents of your requirements.txt file
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

print(requirements)

setup(
    name='pycxsim',
    version="0.1.1",
    license="MIT",
    author="Aaron Tamte",
    author_email="aaron2804@gmail.com",
    packages=find_packages(where='src'),
    install_requires=requirements,  # List of dependencies
    url="https://github.com/Aatamte/PyCxsim",
    download_url="https://github.com/Aatamte/PyCxsim/archive/refs/tags/v0.1.tar.gz",
    keywords=["Artificial Intelligence"],
    package_dir={'': 'src'},
    # other parameters...
)
