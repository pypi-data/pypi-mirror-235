from setuptools import setup, find_packages

setup(
    name="langs_vall", 
    version='0.0.2',
    author="Breyston Gonzalez",
    author_email="<breystonbarton15@gmail.com>",
    description='Paquete de vall-e-x',
    long_description='Packete de vall-e-x para proyecto de traduccion de lenguajes',
    packages=find_packages(),
    install_requires=[
        'soundfile==0.12.1',
        'numpy==1.25.2',
        'torch==2.1.0',
        'torchvision==0.16.0',
        'torchaudio==2.1.0',
        'tokenizers==0.14.1',
        'encodec==0.1.1',
        'langid==1.1.6',
        'wget==3.2',
        'Unidecode==1.3.7',
        'pyopenjtalk-prebuilt==0.3.0',
        'pypinyin==0.49.0',
        'inflect==7.0.0',
        'cn2an==0.5.22',
        'jieba==0.42.1',
        'eng-to-ipa==0.0.2',
        'openai-whisper==20230918',
        'matplotlib==3.8.0',
        'gradio==3.47.1',
        'nltk==3.8.1',
        'SudachiPy==0.6.7', 
        'SudachiDict-core==20230927',
        'vocos==0.0.3',
        'IPython==8.16.1'
    ],
    
    keywords=['python', 'vall-e-x'],
    classifiers= []
)