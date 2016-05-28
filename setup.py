from setuptools import setup

exec(compile(open('zeus/_version.py').read(), 'zeus/_version.py', 'exec'))

setup(name='zeus',
      version = __version__,
      description = 'general tools: cryptography, file, parsing, log',
      url = 'https://github.com/cfauchard/zeus',
      author = 'Christophe Fauchard',
      author_email = 'christophe.fauchard@gmail.com',
      license = 'GPLV3',
      packages = ['zeus'],
      scripts = ['bin/zkey.py', 'bin/zcrypt.py'],
      zip_safe = False)
