import subprocess


print "inside compile.py"

'''This file assumes that required kernel files have already been downloaded 
   and you are just going to be giving the various make commands'''

#as a subprocess cant change other subprocess's directory using cd command, we will use some other function here to change the current working directory

'''
in case the kernel used is a different version or is extracted in a different folder , put that version / folder name there
i.e. subprocess.call('cd FOLDER_CONTAINING_LINUX_KERNEL',shell=True)
'''

@profile
def compile_kernel():
	subprocess.call('sudo make clean && make mrproper',shell=True)
	subprocess.call('sudo make defconfig',shell=True)
	subprocess.call('sudo make',shell=True)


subprocess.call('ls',shell=True)
print "inside the kernel resouces folder"


compile_kernel() #call to above function
