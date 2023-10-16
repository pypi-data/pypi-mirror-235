from setuptools import setup, find_packages

setup(
    name='lagran_admin_panel',
    version='0.1',
    packages=find_packages(),
    package_data={
        '': ['templates/*', 'static/*'],
    },
    
)