from setuptools import setup, find_packages

def read(filename: str):
    return [req.strip("\n") for req in open(filename).readlines()]

setup(
    name="atados_api",
    version="0.1.0",
    description="API para o processo seletivo na empresa Atados",
    packages=find_packages(),
    include_packages=True,
    install_requires=read("requirements.txt")
)
