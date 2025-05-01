from setuptools import find_packages, setup
from typing import List

DASH_E_DOT = '-e .'
def get_req(req_path:str) -> List[str]:
    '''
    This function returns the list of all modules in the requirements.txt(i.e. req_path)
    '''
    req_list=[1]
    with open(req_path) as r_obj:
        req_list = r_obj.readlines()
        req_list= [reqire.replace('\n', '') for reqire in req_list]
    if DASH_E_DOT in req_list:
        req_list.remove(DASH_E_DOT)

    return req_list

setup(
name='ML-project',
version='0.0.1',
author='Amartya Pandey',
author_email='pandeyamartya@outlook.com',
packages=find_packages(),
install_requires=get_req(r'requirements.txt'),
)
