#!/usr/bin/env python
from distutils.core import setup
import datatrans

setup(name='django-datatrans',
      version=datatrans.__version__,
      description='Translate Django models without changing anything to existing applications and their underlying database.',
      author='City Live nv',
      author_email='jef.geskens@citylive.be',
      url='http://github.com/citylive/django-datatrans/',
      packages=['datatrans', 'datatrans.migrations'],
      license='BSD',
      include_package_data = True,
      package_data = {'datatrans': ['templates/datatrans/*'],},
      zip_safe = False,
      classifiers = [
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python',
          'Operating System :: OS Independent',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Topic :: Software Development :: Internationalization',
      ],
)
