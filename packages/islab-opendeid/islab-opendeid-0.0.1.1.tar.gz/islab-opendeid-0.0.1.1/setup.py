from setuptools import setup, find_packages

VERSION = '0.0.1.1' 
DESCRIPTION = 'ISLab-OpenDeid Sample Code'
LONG_DESCRIPTION = 'The sample code provided for the AICUP 2023 challenge organized by NKUST-ISLab'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="islab-opendeid", 
        version=VERSION,
        author="Hong-Jie Dai",
        author_email="<hjdai@nkust.edu.tw>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['aicup', 'opendeid'],
        classifiers= [            
        ]
)