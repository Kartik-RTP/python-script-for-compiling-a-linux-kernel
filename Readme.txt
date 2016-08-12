Readme

#####################################

@author : Kartik Gupta
@email : kartik.gupta@iitrpr.ac.in

#####################################

Note : Before you run the scripts , please make sure that the following assumptions are met:-
0)the scripts are using unix commands to do the various work , hence the program might not work on a Windows platform.Hence it is suggested to run the program on linux environment.Originally it was tested on ubuntu.

1)the folder containing the scripts (test.py , compile.py & download.py) contains the tar file containing the kernel resources named 'kernel.tar.xz'
If suppose you don't have the kernel sources file , then please first execute the "download.py" script and it will download the required tar files.
Or suppose you have the tar file but having some other name , then please rename that file as "kernel.tar.xz"
Or if it is of a different format , then please covert it into tar.xz form as the program has been written using that name

2)Suppose if you are not using  'download.py'  to download the kernel source files , then it may happen that you might download a different version of kernel , then after extracting the source files from "kernel.tar.xz"(READ point 1 regarding this) the folder that might be extracted might be having some name like
"linux-3.19.12" . In this case the program will fail to compile the kernel , as it assumes that folder to be having the name "linux-3.18.38" (the version which was originally compiled at development phase) . So to overcome this , please replace "linux-3.18.38" with the now "FOLDER_NAME" in all instances occuring in both 'test.py' and 'compile.py'.This can easily be done by using "find & replace" option existing in all modern text editors.

3)In case you are running the program as a root user , you need to remove the word "sudo" from all places where it is occuring in compile.py 

4)Suppose you are using "download.py" (Read point 1) for downloading the kernel source file and some errors are coming in program , then I suugest you manually download that file 
using the link "https://cdn.kernel.org/pub/linux/kernel/v3.x/linux-3.18.38.tar.xz" .To do this paste this link in browser and enter.The first time "404 Error " might come and link must have changed to something like "https://cdn.kernel.org/pub/linux/kernel/v3.x/linux%A2%c23.18.38.tar.xz".now just remove everything in between "linux" and "3.18.38" i.e. remove "%A2%C2" or whatever is there and press enter .Now you will be able to download it.
Then copy it to the folder in which you have the test.py and compile.py  and
rename the copied file as "kernel.tar.xz".This file must be there in order for program to execute.

Prerequisites for running the program :-
The program required the following python modules:
*subprocess(comes by default)
*psutil (used by memory_profiler to work smoothly)
*memory_profiler (used for getting the memory usage information for compiling the kernel)


How to execute Program ?

Assuming the above preconditions and prerequisites are met

Just run the test.py script using root permissions (required for make commands) by writing "sudo python test.py"
and it will take care of the rest.

Basic flow of program:
1)get the kernel resources from internet using wget [OPTIONAL] (Read NOTE at the start of document)
2)Extract the kernel resources folder
3)Copy compile.py into that folder (this is so that subprocess module can work in that directory.There must be other alternatives , but I couln't get them at the time of writing the scripts)
4) the copied compile.py script is executed to compile the kernel and also this is done  using the 'time' Unix command and 'memory_profiler' as to obtain the information regarding memory usage , cpu utilisation and time taken.
5)Cleans up by deleting the extracted folder.




