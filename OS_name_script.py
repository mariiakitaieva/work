import platform
OS_info = platform.uname()
#OS_info2 = platform.system()
#OS_info3 = platform.release()
#OS_info4 = platform.os.name
print(OS_info)
print("the name of OS is: ", OS_info[0], OS_info[2])
