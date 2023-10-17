
import os,subprocess
import glob



import m3gnet.models
data_path=os.path.join(os.path.dirname(__file__), 'MP-2021.2.8-EFS')
model_path=m3gnet.models.__path__[0]
subprocess.call(['mkdir','-p', model_path])
subprocess.call(['cp', '-r', data_path,model_path ])

