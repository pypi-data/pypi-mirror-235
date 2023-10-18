from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='Sinhala',
  version='1.1.1',
  description='Sinhala Prastha Pirulu Theravili  Thun theravili Sinhalen ',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='https://github.com/dotLK/sinhala',  
  author='https://github.com/dotLK',
  author_email='',
  license='MIT', 
  classifiers=classifiers,
  keywords='Sinhala Prastha Pirulu -Theravili - Thun theravili sinhalen', 
  packages=find_packages(),
  install_requires=[''] 
)
