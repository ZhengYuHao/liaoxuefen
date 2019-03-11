#python的调试有4个基本方法，但是记住，最终的必杀技就是loggin
#1--print
#2--断言assert
#3--logging
import logging
logging.basicConfig(level=logging.INFO)
if __name__=="__main__":
    s='0'
    n=int(s)
    logging.info("n=%d"%n)
    print("laji")
    print("jj")
    print(10/n)

#4--pdb使用(可以换成ide的断点)
