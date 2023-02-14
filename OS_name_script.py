if __name__ == '__main__':
    import platform
    os_info = platform.uname()
    print(f'the name of OS is {os_info[0]} {os_info[2]}')