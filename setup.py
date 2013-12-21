from setuptools import setup
README = open('README.rst').read()

setup(
    name='Medea',
    version='0.3',
    url='http://github.com/kevinbeaty/medea',
    license='MIT',
    author='Kevin Beaty',
    author_email='kevin@simplectic.com',
    description='JSON Object Mapper / Encoder',
    long_description=README,
    packages=['medea'],
    include_package_data=False,
    zip_safe=False,
    platforms='any',
    install_requires=[],
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
