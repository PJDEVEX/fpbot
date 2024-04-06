from setuptools import setup, find_packages

setup(
    name='medical-bot',
    version='0.0.1',
    author='PJ',
    author_email='piyankara.jayadewa@gmail.com',
    description='Helpfull medical bot',
    license='MIT',
    install_requires=['ctransformers==0.2.5',
              'sentence-transformers==2.2.2',
              'pinecone-client==3.2.2',
              'langchain==0.1.14',
              'langchain-pinecone',
              'flask==3.0.2',
              'pypdf',
              'python-dotenv',
              'black',
              ],
    packages=find_packages(),
)

    