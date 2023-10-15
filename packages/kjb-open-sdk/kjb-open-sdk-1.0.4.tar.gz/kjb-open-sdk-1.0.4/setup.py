import os
from setuptools import setup, find_packages
path = os.path.abspath(os.path.dirname(__file__))

try:
  with open(os.path.join(path, 'README.md')) as f:
    long_description = f.read()
except Exception as e:
  long_description = "kjb-open-sdk"

setup(
    name="kjb-open-sdk",
    version="1.0.4",
    keywords=["pip", "kjb-open-sdk"],
    description = "kjb-open-sdk from kjingbao open platform",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Zhang yu",
    author_email="zhangyu@kjingbao.com",
    packages=find_packages(),
    install_requires=['pydantic > 2.0', 'requests'],
    include_package_data=True,
    platforms="any",

)
