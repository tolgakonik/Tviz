
import sys
import logging

import os
from os import makedirs
from os.path import join, dirname 

from genericpath import exists
from shutil import copyfileobj, copyfile

LOGGING_LEVEL = logging.DEBUG


if getattr(sys, 'frozen', None):
    _ROOT = dirname(sys.argv[0])
else:
    _ROOT = join(dirname(__file__), '..')

_HTML = join(_ROOT, 'tviz_html') 


RESOURCES = join(_ROOT, 'resources')
USER = join(_ROOT, 'user')
DEFAULT_IMAGES = join(RESOURCES, 'images')
TEMPLATES = join(RESOURCES, 'templates')
LOGFILE = join(_ROOT, 'debug.log')

def template_file(name):
    return join(TEMPLATES, name)
    
def html_file(name):
    if exists(_HTML):
        pass
    else:
        makedirs(_HTML)

    return join(_HTML, name)

def options_file(name):    
    return join(USER, name + '.ini')
    
def mapping_file(name):    
    return join(USER, name + '.py')

if os.path.exists(LOGFILE):
    copyfile(LOGFILE, LOGFILE+'.bkp')
    
logging.basicConfig(filemode='w', level=LOGGING_LEVEL, format = '%(levelname)s %(asctime)s : %(name)s : %(message)s', filename=LOGFILE)

logging.info('started logging')

     
if __name__ == '__main__':
    
    print '_ROOT: ', _ROOT
    print 'RESOURCES: ', RESOURCES
    print 'TEMPLATES: ', TEMPLATES
    
    print 'template_file(sample): ', template_file('sample')
    print 'html_file(sample): ', html_file('sample')
    
    print 'options_file(sample)', options_file('sample')    
    print 'mapping_file(sample)', mapping_file('sample')

    