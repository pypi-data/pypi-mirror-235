import io
from os.path import abspath, dirname, join
from setuptools import find_packages, setup


HERE = dirname(abspath(__file__))
LOAD_TEXT = lambda name: io.open(join(HERE, name), encoding='UTF-8').read()
DESCRIPTION = '\n\n'.join(LOAD_TEXT(_) for _ in [
    'README.rst'
])

setup(
  name = 'OCR_GLS_G6',      
  packages = ['OCR_GLS_G6'], 
  version = '0.0.1',  
  license='MIT', 
  description = 'Test Create Package for learning',
  long_description=DESCRIPTION,
  author = 'Burin Panchat',                 
  author_email = 'burin.gbp@gmail.com',     
  url = 'https://git.bdms.co.th/Burin.Pa/ocr_gls_g6',  
  download_url = 'https://git.bdms.co.th/Burin.Pa/ocr_gls_g6/-/archive/v0.0.1/ocr_gls_g6-v0.0.1.zip',  
  keywords = ['test', 'gls', 'gls g6'],   
  classifiers=[
    'Development Status :: 3 - Alpha',     
    'Intended Audience :: Education',     
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
  install_requires=[
          'ironpdf',
      ],
)