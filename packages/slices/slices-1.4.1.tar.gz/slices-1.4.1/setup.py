#!/usr/bin/env python

import os,subprocess
import glob

from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install
from subprocess import check_call
module_dir = os.path.dirname(os.path.abspath(__file__))

class PostDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        #check_call("apt-get install this-package".split())
        develop.run(self)
        # PUT YOUR POST-INSTALL SCRIPT HERE or CALL A FUNCTION
        exec_path = os.path.join(os.path.dirname(__file__), 'invcryrep', 'xtb_noring_nooutput_nostdout_noCN')
        bin_path = '/usr/local/bin/xtb_noring_nooutput_nostdout_noCN'
        if not os.path.exists(bin_path):
            subprocess.call(['cp', exec_path, bin_path])
        subprocess.call(['python', os.path.dirname(__file__)+'/invcryrep/set_path.py'])

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        #check_call("apt-get install this-package".split())
        install.run(self)
        # PUT YOUR POST-INSTALL SCRIPT HERE or CALL A FUNCTION
        exec_path = os.path.join(os.path.dirname(__file__), 'invcryrep', 'xtb_noring_nooutput_nostdout_noCN')
        bin_path = '/usr/local/bin/xtb_noring_nooutput_nostdout_noCN'
        if not os.path.exists(bin_path):
            subprocess.call(['cp', exec_path, bin_path])
        subprocess.call(['python', os.path.dirname(__file__)+'/invcryrep/set_path.py'])



if __name__ == "__main__":
    setup(
        name = 'slices',
        version = '1.4.1',
        setup_requires=[],
        python_requires='>=3.8',
        install_requires=['setuptools>=18.0','numpy==1.23.5','m3gnet==0.2.4','scikit-learn<=1.3.1', 'smact'],
        description=(
          "Invertible crystal representation (SLICES)"),
        author = 'Hang Xiao',
        author_email = 'xiaohang07@live.cn',
        packages = find_packages(),

        package_data={"invcryrep": ["nlopt.h", "xtb_noring_nooutput_nostdout_noCN"]},
        platforms = 'any',
        license="GPL 2.1",
        cmdclass={
            'develop': PostDevelopCommand,
            'install': PostInstallCommand,
        },
    )

