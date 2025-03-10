import platform
import socket
import os
import sys


print(platform.machine()) # returns the machine type
print(platform.architecture()) # returns the architecture

print(socket.getdefaulttimeout()) # returns the default timeout
socket.setdefaulttimeout(50) # sets the default timeout to 50 seconds
print(socket.getdefaulttimeout()) # returns the default timeout

print(os.name) # returns the name of the operating system dependent module imported
print(platform.system()) # returns the system/OS name

print(os.getpid()) # returns the process ID of the current process


f_name = "fdpractice.txt"


f=os.open(f_name, os.O_RDWR|os.O_CREAT)  # opens the file in read and write mode and creates the file if it does not exist

print(f) # returns the file descriptor

f_obj = os.fdopen(f, "a+") # opens the file descriptor in append and read mode
print(f_obj) # returns the file object
print()

#forking a child process
print("Before fork :",os.getpid())
p=os.fork()
print("after fork :",os.getpid())

if p==0:
    print("Parent process")
    print("Parent process id:",os.getpid())
else:
    print("Child process")
    os.wait()
    print("Child process id:",p)



print("last Linae")

