from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'JoySpace - Multimodal AI APIs'
LONG_DESCRIPTION = 'Get started with multimodal AI quickly. Get Multimodal Search, Multimodal Recommendation, Training Data for LLMs, Embedding Store out of the box.'


setup(
       # the name must match the folder name 'verysimplemodule'
        name="joyspace", 
        version=VERSION,
        author="JoySpace AI",
        author_email="<sagar@joyspace.ai>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional needed packages 
                
        keywords=['python', 'joyspace', 'multimodal ai', 'NLP', 'Computer Vision'],
        classifiers= [
            "Development Status :: 2 - Pre-Alpha",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 3 :: Only",
            "Programming Language :: Python :: 3",
            "Operating System :: Unix",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
            "Topic :: Scientific/Engineering :: Artificial Intelligence"
        ]
)