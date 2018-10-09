import re

with open("sql-10000b.txt",'rb')as f:
    while(True):
        line=(f.readline().strip()).decode('UTF-8')
        print(line)
        search=re.findall(r"select",line,re.I)
        print(search)
        if len(search) == 0:
            print("开始输出！")
            with open("问题.txt",'a') as f1:
                f1.write(line+'\n')
    
  