from distutils.core import setup

setup(
    name='py-li',
    version='0.0.8',
    packages=['li'],
    license='MIT',
    author='Casey Thomas',
    author_email='casey@axisphilly.org',
    description="A Python wrapper for the City of Philadelphia L&I API",
    long_description="A Python wrapper for the City of Philadelphia Licenses & Inspections API",
    url='http://github.com/AxisPhilly/py-li',
    classifiers=[
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: MIT License',
                 'Natural Language :: English',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        'argparse==1.2.1',
        'requests==1.2.3',
        'wsgiref==0.1.2'
    ]
)
