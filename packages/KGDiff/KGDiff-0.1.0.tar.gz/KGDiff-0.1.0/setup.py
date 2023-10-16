
__version__ = '0.1.0'
URL = 'https://github.com/CMACH508/KGDiff'

from setuptools import setup, find_packages

setup(name='KGDiff',
      version=__version__,
      description='KGDiff packages',
      url=URL,
      author='qhonearth',
      author_email='qhonearth@sjtu.edu.cn',
      license='MIT',
      download_url=f'{URL}/archive/{__version__}.tar.gz',
      keywords=['pytorch', 'KGDiff', 'drug design', 'diffusion model'],
    #   packages=['KGDiff'],
      packages=find_packages(),
      entry_points={
          'console_scripts': [
              'kg_gen = scripts.sample_diffusion:main',
              'kg_gen4poc = scripts.sample_for_pocket:main',
              'kg_train = scripts.train_diffusion:main',
              'kg_eval = scripts.evaluate_diffusion:main',
          ],
      },
      zip_safe=False)