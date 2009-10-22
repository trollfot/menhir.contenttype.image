from setuptools import setup, find_packages
from os.path import join

name = 'menhir.contenttype.image'
version = '0.1'
readme = open("src/menhir/contenttype/image/README.txt").read()
history = open("docs/HISTORY.txt").read()

setup(name = name,
      version = version,
      description = 'Dolmen contenttype extension : image',
      long_description = readme[readme.find('\n\n'):] + '\n' + history,
      keywords = 'Grok Zope3 CMS Dolmen',
      author = 'Souheil Chelfouh',
      author_email = 'souheil@chelfouh.com',
      url = 'http://tracker.trollfot.org/',
      download_url = 'http://pypi.python.org/pypi/menhir.contenttype.image',
      license = 'GPL',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      namespace_packages = ['menhir', 'menhir.contenttype'],
      include_package_data = True,
      platforms = 'Any',
      zip_safe = False,
      install_requires=[
          'setuptools',
          'grok',
          'dolmen.file',
          'dolmen.blob',
          'dolmen.content',
          'dolmen.thumbnailer',
          'dolmen.app.content',
          'dolmen.app.security',
          'dolmen.widget.image',
          'menhir.library.jquery',
          'megrok.resourcelibrary',
      ],
      classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Grok',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
      ],
)
