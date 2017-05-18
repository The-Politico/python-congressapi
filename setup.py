from setuptools import setup

setup(
    name='python-congressapi',
    version='0.0.1',
    description='A Python wrapper for ProPublica\'s congress API',
    author='Jon McClure',
    author_email='jon.r.mcclure@gmail.com',
    url='',
    license="MIT",
    packages=("congressapi",),
    test_suite="",
    include_package_data=True,
    install_requires=(
        'python-dateutil>=2.1',
        'six>=1.4.1',
        'rfc3987',
        'marshmallow>=2.13.5',
        'requests>=2.13.0'
    ),
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
    ),
)
