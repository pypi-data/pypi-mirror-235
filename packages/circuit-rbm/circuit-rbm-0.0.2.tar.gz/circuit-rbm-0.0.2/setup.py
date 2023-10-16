from setuptools import setup, find_packages

VERSION = '0.0.2' 
DESCRIPTION = 'Train a RKM'
LONG_DESCRIPTION = 'A Python package to simulate and train a RKM model'

# Setting up
setup(
        name="circuit-rbm", 
        version=VERSION,
        author="Simone Ciarella",
        author_email="<simoneciarella@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'statistical physics', 'machine learning', 'rbm'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            # "Operating System :: MacOS :: MacOS X",
            # "Operating System :: Microsoft :: Windows",
        ]
)
