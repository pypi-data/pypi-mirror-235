from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  long_description_content_type = "text/markdown",
  name='jdocdb',
  version='0.0.1',
  description='A simple and lightweight JSON mock database for small projects',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Abhay S Prasad (KingCosma)',
  author_email='abhaygorur@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords=['datbase', 'json', 'data'],
  packages=find_packages()
)