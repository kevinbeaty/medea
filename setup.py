"""
Medea
-----
"""
from setuptools import setup

setup(
    name='Medea',
    version='0.1-pre',
    url='http://github.com/kevinbeaty/medea',
    license='MIT',
    author='Kevin Beaty',
    description='JSON Sorcery',
    long_description=__doc__,
    packages=['medea'],
    include_package_data=False,
    zip_safe=True,
    platforms='any',
    install_requires=[],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Object Brokering'
        'Topic :: Text Processing :: Markup'],
    cmdclass={},
    test_suite=''
)
