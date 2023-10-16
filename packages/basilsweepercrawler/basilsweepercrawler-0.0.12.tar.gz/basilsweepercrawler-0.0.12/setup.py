import setuptools
with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name="basilsweepercrawler",
    version="0.0.12",
    author="James Baker",
    author_email="james@talentium.io",
    license="MIT",
    packages=["basilsweepercrawler", "basilsweepercrawler.format_data"],
    install_requires=[
        required
    ],
    # classifiers like program is suitable for python3, just leave as it is.
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
