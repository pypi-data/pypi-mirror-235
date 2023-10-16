from setuptools import setup, find_packages

setup(
    name='openface_test',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'Utilities': ['*.pyd'],
    },
    data_files=[('', ['opencv_world410.dll'])],
)