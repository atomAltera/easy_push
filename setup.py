from setuptools import setup

setup(name='easy_push',
      version='0.1',
      description='Python library for sending push notification to Android and iOS',
      url='https://github.com/atomAltera/easy_push',
      author='Konstantin Alikhanov',
      author_email='atomAltera@gmail.com',
      license='MIT',
      packages=['easy_push'],
      install_requires=[
          'pyfcm',
      ],
      zip_safe=False)
