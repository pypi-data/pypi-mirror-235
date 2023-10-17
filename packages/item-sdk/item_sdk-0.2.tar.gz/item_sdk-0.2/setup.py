from setuptools import setup, find_packages

setup(
    name="item_sdk",
    version="0.2",
    packages=find_packages(),
    install_requires=["requests"],
    author="Rany ElHousieny",
    author_email="ranyel@msn.com",
    description="SDK for interacting with FastAPI items API",
    license="MIT",
    keywords="sdk fastapi items",
    url="https://github.com/ranyelhousieny/items-sdk",
)
