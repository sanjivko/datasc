# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 08:48:28 2020

@author: ojhas
"""
#!/usr/bin/env python

"""

Semistructured Data: XML, HTML

"""

from lxml import objectify
import os
import sys


#os.path.realpath(sys.argv[0])
os.chdir(os.path.dirname(os.path.realpath(__file__)))
os.getcwd()

xml = objectify.parse("employees.xml")

xml


import xml.etree.ElementTree as ET