from setuptools import setup, find_packages

setup(
    name='mirageml',
    version='0.0.9',
    author='Aman Kishore',
    author_email='aman@mirageml.com',
    description='A basic pip package with basic commands like help and hello world',
    packages=find_packages(),
    install_requires=[
        # List your package's dependencies here
    ],
    entry_points={
        'console_scripts': [
            'mirageml=mirageml_pip.__main__:main'
        ]
    }
)