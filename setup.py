from setuptools import setup, find_packages

setup(name='instrosetta',
      version='0.1',
      description='Python implementations of the instrosetta project.',
      url='http://github.com/jmosbacher/instrosetta',
      author='Yossi Mosbacher',
      author_email='joe.mosbacher@gmail.com',
      license='MIT',
      packages=find_packages(where="instrosetta"),
      install_requires=[
          'grpcio',
          'pint',
          'protobuf',
      ],
      extra_requires={
          "server": ['pyserial']
      },
      zip_safe=False)