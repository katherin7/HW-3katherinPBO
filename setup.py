from setuptools import setup, find_packages

setup(
    name='sort',
    version='0.1.1',
    description='A simple sorting algorithms package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/katherin7/HW-3katherinPBO',  # Update with your repo URL
    author='Katherin PBO',
    author_email='hendrik.gian@gmail.com',
    license='MIT',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.8',
)
