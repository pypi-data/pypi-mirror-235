"""
az_sights
-----------
This is a package can be used to query Azure Application Insights.
`````

* Source
https://github.com/kouroshparsa/az_sights
"""
from setuptools import setup, find_packages

version = '1.0.0'
setup(
    name='az_sights',
    version=version,
    url='https://github.com/kouroshparsa/az_sights',
    download_url='https://github.com/kouroshparsa/az_sights/packages/%s' % version,
    license='GNU',
    author='Kourosh Parsa',
    author_email="kouroshtheking@gmail.com",
    description='This is a package can be used to query Azure Application Insights.',
    long_description='This is a package can be used to query Azure Application Insights.',
    packages=find_packages(),
    install_requires = [],
    include_package_data=True,
    package_data = {'az_sights': []},
    zip_safe=False,
    platforms='all',
    classifiers=[
        'Programming Language :: Python',
    ]
)
