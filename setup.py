from setuptools import setup

# any dependencies required
requirements = ['gym==0.17.2',
                'numpy==1.19.1',
                'tensorflow==1.15.4']

setup(name='catan_gym',
      version='0.0.1',
      install_requires=requirements
)
