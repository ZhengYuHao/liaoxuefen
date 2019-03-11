#python的错误报警机制

if __name__=="__main__":
    try:
        print("Try...")
        r=10/0
        print("result:",r)
    except ZeroDivisionError as e:
        print(e)
    finally:
        print("finally")
    print("END")
