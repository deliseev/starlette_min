from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='app',
    description='Starlette minimal app',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/deliseev/starlette_min',
    author='A. Random Developer',
    author_email='author@example.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GPL v2 License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='sample, microservice',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.6, <4',
    install_requires=[
        'starlette==0.16.0',
        'uvicorn==0.15.0',
        'sqlalchemy==1.4.23',
        'alembic==1.6.5',
        'asyncpg==0.24.0',
    ],
    extras_require={
        'dev': [
            'sqlalchemy2-stubs',
        ],
        'test': [
            'flake8',
            'pytest',
            'coverage',
            'requests',
        ],
    },
    entry_points={
        'console_scripts': [
            'run=app.main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/deliseev/starlette_min/issues',
        'Source': 'https://github.com/deliseev/starlette_min',
    },
)
