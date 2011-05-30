#!/usr/bin/env python
import sys, os, re
# change the path (reverse line order! last line is the first path searched)
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '_thirdparty'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../django-trunk'))
sys.path.insert(0, '')

from django.core.management import execute_manager
#try:
    #import settings # Assumed to be in the same directory.
#except ImportError:
    #sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    #sys.exit(1)
import settings # Assumed to be in the same directory.
#import appsignals

if len(sys.argv) > 1 and  re.match(r'^(update_|migrate_|runserver|shell)', sys.argv[1]):
    __builtins__.DEVSERVER = True

if __name__ == "__main__":
    execute_manager(settings)
