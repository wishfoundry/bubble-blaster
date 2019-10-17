from setuptools import setup

with open("README", 'r') as f:
    long_description = f.read()

setup(
   name='py-qml',
   version='1.0',
   description='more awesomeness ',
   long_description=long_description,
   author='Man Foo',
   packages=['py-qml'],  #same as name
   install_requires=['bar', 'greek'], #external packages as dependencies
)