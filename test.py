# -*- coding: utf-8 -*-
import subprocess



#subprocess.call('mkdir kernelbuild',shell=True)
#subprocess.call('cd kernelbuild',shell=True)
#subprocess.call('ls',shell=True)



#linux-3.18.38 - folder containing the kernel , if the kernel is obtained using the above wget statement
#in case , its some other folder , please replace linux-3.18.38 with that FOLDER_NAME in all commands of this script and compile.py as well

subprocess.call(' tar -xvf kernel.tar.xz   ',shell=True)
subprocess.call('cp compile.py linux-3.18.38',shell=True)

#now we have got the kernel file , now we can start doing the steps to compile it

subprocess.call('time python -m memory_profiler compile.py',shell=True,cwd="linux-3.18.38/")
print "Cleaning up the kernel extracted"
subprocess.call('rm -rf linux-3.18.38',shell=True)



#To delete the kernel.tar.xz as well , uncomment the below command
# subprocess.call('rm  kernel.tar.xz',shell=True) 





