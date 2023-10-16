from setuptools import setup, find_packages

setup(
    name='electricity-bill',  # Change the package name to use hyphens instead of underscores
    version='0.1',
    description='Electricity bill calculation for monthly domestic use',
    author='ivankostark',
    packages=find_packages(),  # Use find_packages to automatically discover packages
    install_requires=[
        # List your package dependencies here
    ],
    zip_safe=False,
)
