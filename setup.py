#    Copyright 2015 Pure Storage Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
"""Installation for Pure Storage Plugin for Flocker."""

from setuptools import find_packages
from setuptools import setup

setup(
    name='purestorage_driver',
    version='0.1',
    description='Pure Storage Plugin for Flocker',
    license='Apache 2.0',

    classifiers=[
        'Development Status :: 1 - Alpha',
        'Programming Language :: Python :: 2.7',
    ],

    install_requires=[
        'requests>=2.5.2',
        "purestorage>=1.4.0",
        'six',
        'bitmath'],

    keywords='backend, plugin, flocker, docker, python',
    packages=find_packages(exclude=['test*']),
    author='Simon Dodsley',
    author_email='simon@purestorage.com',
    url='https://github.com/purestorage/purestorage-flocker-driver',
    download_url='https://github.com/purestorage/purestorage-flocker-driver/tarball/0.1',
    data_files=[('/etc/flocker', ['example.pure_agent.yml'])]
)
