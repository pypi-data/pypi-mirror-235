from setuptools import setup 
  
setup( 
    name='testlambda', 
    version='0.2', 
    description='A sample Python package', 
    author='John Doe', 
    author_email='jdoe@example.com', 
    packages=['testlambda'], 
    install_requires=[ 
        'requests', 
        'boto3', 
    ], 
) 