from setuptools import setup, find_packages

setup(
    name='fpbot',
    version='0.0.1',
    author='PJ',
    author_email='piyankara.jayadewa@gmail.com',
    description='Helpfull finance buddy for fiancial accountents, auditors and consultants',
    license='MIT',
    install_requires=['ctransformers==0.2.27',
              'sentence-transformers==2.6.1',
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

    