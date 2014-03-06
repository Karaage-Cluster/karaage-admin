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

from distutils.core import setup
from distutils.command.install import INSTALL_SCHEMES
import os
import sys
import ast

def fullsplit(path, result=None):
    """
    Split a pathname into components (the opposite of os.path.join) in a
    platform-neutral way.
    """
    if result is None:
        result = []
    head, tail = os.path.split(path)
    if head == '':
        return [tail] + result
    if head == path:
        return result
    return fullsplit(head, [tail] + result)

# Tell distutils to put the data_files in platform-specific installation
# locations. See here for an explanation:
# http://groups.google.com/group/comp.lang.python/browse_thread/thread/35ec7b2fed36eaec/2105ee4d9e8042cb
for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']

# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir != '':
    os.chdir(root_dir)
code_dir = 'kgadmin'

for dirpath, dirnames, filenames in os.walk(code_dir):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if '__init__.py' in filenames:
        packages.append('.'.join(fullsplit(dirpath)))
    elif filenames:
        data_files.append([dirpath, [os.path.join(dirpath, f) for f in filenames]])

with open('VERSION.txt', 'r') as f:
    version = f.readline().strip()

media_files = []
for dirpath, dirnames, filenames in os.walk('media'):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if '__init__.py' in filenames:
        packages.append('.'.join(fullsplit(dirpath)))
    elif filenames:
        media_files.append([dirpath, [os.path.join(dirpath, f) for f in filenames]])

for dirpath, dirnames, filenames in os.walk('templates'):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if '__init__.py' in filenames:
        packages.append('.'.join(fullsplit(dirpath)))
    elif filenames:
        media_files.append([dirpath, [os.path.join(dirpath, f) for f in filenames]])


for i in media_files:
    d = i[0]
    i[0] = '/usr/share/kgadmin/%s' % d


data_files =  media_files
data_files.append(('/usr/sbin', ['sbin/kg-manage', 'sbin/kg-daily-cleanup']))

data_files.append(
    ('/etc/karaage', [
        'conf/admin_settings.py',
        'conf/admin_urls.py',
        'conf/karaage-admin.wsgi',
        'conf/kgadmin-apache.conf',])
)

setup(
    name = "karaage-admin",
    version = version,
    url = 'https://github.com/Karaage-Cluster/karaage',
    author = 'Brian May',
    author_email = 'brian@vpac.org',
    description = 'Admin interface to karaage',
    packages = packages,
    data_files = data_files,
)
