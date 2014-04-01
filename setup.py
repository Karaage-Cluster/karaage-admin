#!/usr/bin/env python

# Copyright 2012-2014 VPAC
#
# This file is part of django-tldap.
#
# django-tldap is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# django-tldap is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with django-tldap  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup, find_packages

with open('VERSION.txt', 'r') as f:
    version = f.readline().strip()

setup(
    name="karaage-admin",
    version=version,
    url='https://github.com/Karaage-Cluster/karaage',
    author='Brian May',
    author_email='brian@v3.org.au',
    description='Admin interface to karaage',
    packages=find_packages(),
    license="GPL3+",
    long_description=open('README.rst').read(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v3 "
            "or later (GPLv3+)",
        "Operating System :: OS Independent"
        "Programming Language :: Python"
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    keywords="karaage cluster user administration",
    data_files=[
        ('/etc/karaage', [
            'conf/admin_settings.py',
            'conf/admin_urls.py',
            'conf/karaage-admin.wsgi',
            'conf/kgadmin-apache.conf',
            ])
    ],
    install_requires=[
        'karaage >= 3.0.3',
    ],
)
