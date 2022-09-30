from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as f:
    required = f.read().splitlines()

exec(open("plotox/__version__.py").read())

setup(
    name="plotox",
    version=__version__,
    description="A naive plotting utility.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NISH1001/plotox",
    author="Nish",
    author_email="nishanpantha@gmail.com",
    license="MIT",
    python_requires=">=3.8",
    packages=["plotox"],
    install_requires=required,
    classifiers=[
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development",
        "Topic :: Data Transfer",
    ],
    zip_safe=False,
)
