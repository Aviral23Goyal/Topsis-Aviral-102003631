# import pathlib
# from setuptools import setup

# # The directory containing this file
# HERE = pathlib.Path(__file__).parent

# # The text of the README file
# README = (HERE / "README.md").read_text()

# # This call to setup() does all the work
# setup(
#     name="Topsis-Aviral-102003631",
#     version="1.0.0",
#     description="It give a priority order to the dataset rows.",
#     long_description=README,
#     long_description_content_type="text/markdown",
#     url="https://github.com/uditvashisht/saral-square",
#     author="Aviral Goyal",
#     author_email="agoyal3_be20@thapar.edu",
#     license="MIT",
#     classifiers=[
#         "License :: OSI Approved :: MIT License",
#         "Programming Language :: Python :: 3.6",
#         "Programming Language :: Python :: 3.7",
#         "Programming Language :: Python :: 3.8",
#     ],
#     packages=["Topsis-Aviral-102003631"],
#     include_package_data=True,
#     install_requires="pandas",
#     entry_points={
#         #"console_scripts": [
#         #    "Topsis-Aviral-102003631=Topsis-Aviral-102003631.__main__.parent:main",
#         #]
#     },
# )


import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="Topsis-Aviral-102003631",
    version="1.0.0",
    description="It is a method of compensatory aggregation that compares a set of alternatives by identifying weights for each criterion, normalising scores for each criterion and calculating the geometric distance between each alternative and the ideal alternative, which is the best score in each criterion.",
    long_description=README,
    long_description_content_type="text/markdown",
    url=" ",
    author="Aviral Goyal",
    author_email="agoyal3_be20@thapar.edu",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["Topsis-Aviral-102003631"],
    include_package_data=True,
    install_requires="pandas",
    entry_points={
        
    },
)