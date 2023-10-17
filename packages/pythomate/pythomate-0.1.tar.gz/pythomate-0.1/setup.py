from setuptools import setup, find_packages
import codecs
import os
import sys
sys.path.insert(0, os.path.abspath('..'))


INSTALL_REQUIRES = [
    'click==8.1.7',
    'PyAutoGUI==0.9.54',
]

if __name__ == '__main__':
  setup(
      name='pythomate',
      version='0.1',
      author='O Laboratório de Inovação em Governo - LAB.mg',
      author_email='simplificacao@planejamento.mg.gov.br',
      description='Automatiza acionamento de fluxos Power Automate.',
      long_description_content_type='text/markdown',
      long_description=open('README.md', encoding='utf-8').read() + '\n\n' + open('CHANGELOG.md', encoding='utf-8').read(),
      url='https://github.com/lab-mg/pythomate',
      packages=find_packages(),
      install_requires=INSTALL_REQUIRES,
      keywords=['python', 'power automate', 'automate', 'automação'],
      classifiers=[
          "Development Status :: 1 - Planning",
          "Intended Audience :: Developers",
          "Programming Language :: Python :: 3",
          "Operating System :: Unix",
          "Operating System :: MacOS :: MacOS X",
          "Operating System :: Microsoft :: Windows",
      ],
      entry_points="""
        [console_scripts]
        pythomate=pythomate.cli:cli
      """
  )
