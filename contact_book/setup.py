from setuptools import setup
setup(name='useful',
      version='1',
      description='Very useful code',
      url='http://github.com/dummy_user/useful',
      author='Flying Circus',
      author_email='flyingcircus@example.com',
      license='MIT',
      packages=['useful'],
      include_package_data=True,
      install_requires=['markdown'],
      entry_points={'console_scripts': ['helloworld = useful.some_code:hello_world']})
