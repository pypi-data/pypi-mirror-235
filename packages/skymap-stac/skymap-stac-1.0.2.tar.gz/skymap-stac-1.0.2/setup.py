from setuptools import setup, find_packages

VERSION = '1.0.2' 
DESCRIPTION = 'Skymap STAC package'
LONG_DESCRIPTION = 'Python package for reading datacube from rolodex'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="skymap-stac", 
        version=VERSION,
        author="Hai Anh Do",
        author_email="haianhdo193@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['python-dotenv'], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'stac', 'skymap', 'rolodex'],
        classifiers= [
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: Unix",
        ]
)