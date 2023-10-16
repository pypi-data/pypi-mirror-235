from setuptools import setup, find_packages

classifiers = {
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    "Operating System :: OS Independent",
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
}
setup(
    name="first_packages_21",
    version="0.1.0",
    description="My first Python package",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url='',
    author="Volkan",
    author_email="volkanr@email.com",
    license='MIT',
    classifiers=classifiers,
    keywords='Hello World',
    packages=find_packages(),
    python_requires=">=3.6",
)