from setuptools import setup, find_packages

setup(
    name='trust-track-api',
    version='0.9.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=['requests-cache', 'pytz'],
    url='',
    license='',
    author='Lyubomir Traykov',
    author_email='lyubomir.traykov@traykovtrans.com',
    description='TrustTrack Ruptela API Wrapper',
)
