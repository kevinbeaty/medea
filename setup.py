import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as README:
    long_description = README.read()

setup(
    name='Medea',
    version='0.3.2',
    url='http://github.com/kevinbeaty/medea',
    license='MIT',
    author='Kevin Beaty',
    author_email='kevin@simplectic.com',
    description='JSON Object Mapper / Encoder',
    long_description=long_description,
    packages=['medea'],
    include_package_data=False,
    zip_safe=False,
    platforms='any',
    install_requires=['singledispatch>=3.4.0'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Markup'],
    cmdclass={},
    test_suite=''
)
