from setuptools import setup

# Read the contents of your README.md file as the long description
with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='midjpy',
    version='1.0.3',
    description='Python client for the MIDJ API',
    long_description=long_description,
    long_description_content_type='text/markdown',  # Specify the content type
    author='dmaxxy',
    author_email='dmaxxy.bhw@gmail.com',
    packages=['midjpy'],
    install_requires=['requests'],
)
