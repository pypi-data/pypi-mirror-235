from setuptools import setup, find_packages

setup(name='satellite_extractor',
      version='0.1',
      description='Download spatio-temporally aligned satellite imagery with inter-band data augmentation based on hash encryption ',
      author = "Sebastian Cajas",
      email = "ulsordonez@unicauca.edu.co",
      zip_safe=False,
      packages=find_packages(),
      )
