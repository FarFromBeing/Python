#传入函数
# x=abs(-10)
# # print(x)
# #可以把函数赋值给变量
# f=abs
# # print(f(-20))
# 
# def add_f(x,y,f):
#     return f(x)+f(y)
# if __name__=='__main__':
#     print('main')
#     print(add_f(5,-10,abs))
#-----------------------------------------
#切片
# l=list(range(100))
# t=tuple(l)
# l_st='qhurhnbukahzcbn,ajzjilo'
'''
[起始点:个数:具体操作（每2步取一个等）]
'''
# print(l[:1222])
# print(t[2:100:2])
# print(l_st[::2])
#实现strip()
def my_strip(str1):
    new_str=str1
    if new_str=='':
        return None
    elif str1[:1]==' ':
        new_str=my_strip(str1[1::])
    elif str1[-1:]==' ':
        new_str=my_strip(str1[:-1])
    return new_str
def sum_blank(str1):
    counter=0
    for _ in str1:
        if _ ==' ':
            counter=counter+1
    return counter
#还没有考虑有效str的长度问题
# def center_blank(str1):
#     p=0
#     new_str=str1
#     for _ in new_str:
#         if _ ==' ':
#             str_p=new_str[:p]
#             new_str=str_p+new_str[p+1:]
#         p=p+1
#     return new_str
if __name__=='__main__':
    str1_nob='          ajdoijuoihn        '#10+11+8
    # print("center_blank测试：%s"%(center_blank(str1_nob)))
    print("空格数测试：%s"%(sum_blank(str1_nob)))
    print("旧str:%s字符数 "%(len(str1_nob)))
    print("旧str:%s"%(str1_nob))
    strn=my_strip(str1_nob) 
    print("新str:%s"%(strn))
    print("结果字符数：%s"%(len(strn)))
    
