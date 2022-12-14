"""
    Smartphone Test Farm

    Control and manages real Smartphone devices from browser and restful apis  # noqa: E501

    The version of the OpenAPI document: 2.4.0
    Contact: contact@openstf.io
    Generated by: https://openapi-generator.tech
"""

from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
]

setup(
    name="stf-client",
    use_scm_version=True,
    description="Smartphone Test Farm client library",
    author="Jussi Vatjus-Anttila",
    author_email="jussiva@gmail.com",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Smartphone Test Farm", "stf", "devicefarm", "openstf"],
    python_requires=">=3.7",
    setup_requires=["setuptools_scm"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Apache-2.0",
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
)
