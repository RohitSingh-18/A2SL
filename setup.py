import setuptools

setuptools.setup(
    name='i_hear_you_audio_speech_to_sign_language_converter',
    version='0.1.0',
    description='HackOdisha4 Project',
    author='Gourav Rout',
    url='',
    packages=setuptools.find_packages(),
    setup_requires=['nltk', 'joblib','click','regex','sqlparse','setuptools'],
)
