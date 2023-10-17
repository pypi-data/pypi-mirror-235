from setuptools import setup, find_packages

setup(
    name="items-sdk",
    version="0.1",
    packages=find_packages(),
    install_requires=["requests"],
    author="Rany ElHousieny",
    author_email="rany@elhousieny.com",
    description="SDK for interacting with FastAPI items API",
    license="MIT",
    keywords="sdk fastapi items",
    url="https://github.com/ranyelhousieny/items-sdk",
)
