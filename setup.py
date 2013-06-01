from distutils.core import setup
import li

setup(
    name='py-li',
    version=li.__version__,
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
)
