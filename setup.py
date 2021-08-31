from setuptools import setup, find_packages

VERSION = '0.0.2' 
DESCRIPTION = 'coolprint is a library that prints coolly.'

# Setting up
setup(
	# the name must match the folder name 'verysimplemodule'
        name="coolprint", 
        version=VERSION,
        author="bichanna",
        author_email="nobu.bichanna@gmail.com",
        description=DESCRIPTION,
        packages=find_packages(),
        install_requires=[], 
		license="MIT",
        keywords=["python", "cool", "print", "coolprint"],
        classifiers= [
            "Programming Language :: Python :: 3",
        ]
)