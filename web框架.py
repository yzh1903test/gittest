#��/usr/bin/python
#-*-c0ding:utf-8-*-
#flask web���
'''
django
flask
bottle
tormdon
'''
#web ҳ��һ�����
'''
1.��̬��,ҳ�治�����䶯
2.��̬��,ҳ�������ʵʱˢ��
'''
#flask --->python��������web��ҳ�����ݽ�����web���
from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello():
    return 'hello flask'
if __name__=='__main__':
    app.run(host='127.0.0.1',port=6000)
