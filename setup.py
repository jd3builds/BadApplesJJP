import setuptools
import os

folder = os.path.dirname(os.path.realpath(__file__))
req_path = folder + '/requirements.txt'
install_requires = []

if os.path.isfile(req_path):
    with open(req_path) as file:
        install_requires = file.read().splitlines()

setuptools.setup(
    name="BA-produce-tracker",
    version="0.0.1",
    author="Brody, Joseph // Dillon, John // Estrada, Pablo // Todd, Alexis // Garcia, Marissa",
    description="Produce expiration tracker",
    python_requires='>=3.8',
    install_requires=install_requires
)