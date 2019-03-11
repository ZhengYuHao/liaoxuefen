#文件调用的时候，一般需要写try-catch语句，但是有一种简便方式提供
if __name__=="__main__":
    # try:
    #     f=open("/path/to/file.txt",'r')
    # except IOError as e:
    #     print(e)
    # finally:
    #     print("END")
    #     f.close()
    with open("/path/to/file.txt",'r') as f:
        print(f.read())