from setuptools import setup, find_packages

VERSION = '0.0.2' 
DESCRIPTION = 'coolprint is a library that prints coolly.'
LONG_DESCRIPTION = """
# coolprint

coolprint is a library that prints coolly.

### Installation

```
pip install coolprint
```

### Usage
```
from coolprint import coolprint, dullprint, starprint, coolstarprint

## coolprint
coolprint("Mission Impossible...?", 0.05)
# or 
coolprint("This is so cool!")

## dullprint
dullprint("This is a dull print")

## starprint
starprint("This is a star print") 

## coolstarprint
coolstarprint("This is a cool star print" 0.05)
# or 
coolstarprint("This is another cool star print")

```
"""

# Setting up
setup(

        name="coolprint", 
        version=VERSION,
        author="bichanna",
        author_email="nobu.bichanna@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type="text/markdown",
        url="https://github.com/bichanna/coolprint",
        packages=find_packages(),
        install_requires=[], 
		license="MIT",
        keywords=["python", "cool", "print", "coolprint"],
        classifiers= [
            "Programming Language :: Python :: 3",
        ]
)