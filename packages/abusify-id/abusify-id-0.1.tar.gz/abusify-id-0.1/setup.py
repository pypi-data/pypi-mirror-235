from setuptools import setup, find_packages

setup(
    name='abusify-id',
    version='0.1',
    packages=find_packages(),
    package_data={
        'abusify-id': ['model.pkl', 'tfidf_vectorizer.pkl'],
    },
    install_requires=[
        'scikit-learn',
        'pandas',
        'nltk',
    ],
)
