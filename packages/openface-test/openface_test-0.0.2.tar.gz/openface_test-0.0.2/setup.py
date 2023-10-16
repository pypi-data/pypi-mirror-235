from setuptools import setup, find_packages

setup(
    name='openface_test',
    version='0.0.2',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'openface_test': ['Utilities.pyd'],
    },
    data_files=[('', ['opencv_world410.dll'])],
)