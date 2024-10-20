import setuptools

setuptools.setup(
    name='I Hear You (An audio-speech-to-sign-language-converter)',
    version='0.1.0',
    description='HackOdisha4 Project',
    author='Rohit Singh',
    url='',
    packages=setuptools.find_packages(),
    setup_requires=['nltk', 'joblib','click','regex','sqlparse','setuptools'],
)