import re
l=[
    'script',
    'alert',
    'onload',
    'onmouseover',
    'c2NyaXB0',#scprit
    'WVd4bGNuUT0=',#alert
    'b25sb2Fk',#onload
    'b25tb3VzZW92ZXI=',#onmouseover
    'ScRiPt',
    'sCrIpT',
]
with open("xss-20000b.txt",'rb')as f:
    while(True):
        p=0#判断特征值个数
        line=(f.readline().strip()).decode('UTF-8')
        print(line)
        for _ in l:
            print(_)
            search=re.findall(_,line,re.I)
            print("search查找结果:%s"%search)
            if len(search) == 0:
                p=p+1
                continue
        print(p)
        if p == 8:#用于更改特征词个数
            print("该行不存在以上特征词,准备写入...")
            print("开始写入...")
            # with open("问题1.txt",'a') as f1:
            #     f1.write(line+'\n')
        else:print("存在特征词！不写入！")