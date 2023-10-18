from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Package that converts int into roman numbers and vice versa'
LONG_DESCRIPTION = ('If at some point you are stucked because your programming teacher asked you to create a programm'
                    'that turns ints to roman numbers and vice versa, you can just use this')

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="tolonteria",
    version=VERSION,
    author="Felipe Kautzmann",
    author_email="<recuerdaesto@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'

    keywords=['python', 'first package'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)