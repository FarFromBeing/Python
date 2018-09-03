import pickle
import json
##-------------序列化
d=dict(name='JACK',age=20,score=22)
print(pickle.dumps(d))
#b'\x80\x03}q\x00(X\x04\x00\x00\x00nameq\x01X\x04\x00\x00\x00JACKq\x02X\x03\x00\x00\x00ageq\x03K\x14X\x05\x00\x00\x00scoreq\x04K\x16u.'
'''pickle.dumps()方法
把任意对象序列化成一个byte'''
f = open('dump.txt', 'wb')
'''pickle.dump(d, f)直接把对象序列化后
写入file-like Object'''
pickle.dump(d, f)
f.close()
##------------反序列化
f1=open('dump.txt','rb')
d=pickle.load(f1)
f.close()
print(d)
#{'name': 'JACK', 'age': 20, 'score': 22}
#----------------json序列化
print(json.dumps(d))
str1=json.dumps(d)
print(type(str1))
#{"name": "JACK", "age": 20, "score": 22}
#<class 'str'>