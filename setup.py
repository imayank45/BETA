from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT ='-e .'
def get_requirements(file_path:str)->List:
    """_
    this function will return list of the requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements

setup(
    name='beta',
    version='0.0.1',
    author='Mayank',
    author_email='mkathane84@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)