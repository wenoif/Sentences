

import os
import re
import time

def yinru():
    f = open('./诗词.txt')
    lines = f.readlines() #整行读取
    f.close()
    for line in lines:
        rs = line.rstrip('\n') #去除原来每行后面的换行符，但有可能是\r或\r\n
        #newname=r'"'+rs+ '"'
        newfile=open('val1.txt','a')
        newfile.write("'" + rs + "',\n")
        newfile.close()

if __name__ == '__main__':
    yinru()