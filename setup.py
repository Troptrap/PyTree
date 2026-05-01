from setuptools import setup, find_packages

setup(
    name='pytree',
    version='0.1.0',
    description='An ultra-fast terminal utility that generates a visual tree structure of public functions within your Python projects.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Troptrap',
    author_email='your_email@example.com',
    url='https://github.com/Troptrap/PyTree',
    license='MIT',
    packages=find_packages(),
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'pytree=pytree:main',
        ],
    },
    keywords=['python', 'analysis', 'ast', 'tree', 'visualization', 'functions'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)