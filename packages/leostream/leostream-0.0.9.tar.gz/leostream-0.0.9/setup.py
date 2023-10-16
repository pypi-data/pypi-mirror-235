from setuptools import setup, find_packages

VERSION = '0.0.9' 
DESCRIPTION = 'Leostream Python client'
LONG_DESCRIPTION = 'Leostream REST API client written in Python'

# Setting up
setup(
        name="leostream", 
        version=VERSION,
        author="Joost Evertse",
        author_email="<joustie@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'leostream', 'rest', 'api', 'client'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
