# function 函式

# 定義
def foo():
    print('foo')

def bar():
    return 'bar'

def dollar(a):
    return a * 32

def greeting(name='Guest'):
    return f'Hello, {name}!'


def account(money, tax=1.1):
    return money * tax

# print(account(100, 1.1))
print(account(123))
print(account(123, 2))
print(account(tax=2.5,money=666))