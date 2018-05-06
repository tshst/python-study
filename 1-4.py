def f(x):
    return x * 2

print(f(10))

# 引数を取らない関数
def ff():
    return 1 + 1

print(ff())

def fff(x, y, z):
    return x + y + z

print(fff(1,2,3))

# 組込関数

print(str(1000))
print(int("1"))
print(float(100))

age = input("Enter your age: ")
int_age = int(age)
if int_age < 21:
    print("You are Young!")
else:
    print("Wow, you are Old!")

def even_odd(x):
    if x % 2 == 0:
        print("偶数")
    else:
        print("奇数")


even_odd(2)
even_odd(3)

# オプション引数

def fx(x=2):
    return x ** x

print(fx())
print(fx(4))

def add_it(x, y=10):
    return x + y

result = add_it(2)
print(result)

# スコープ
x = 1
y = 2
z = 3

def fy():
    print(x)
    print(y)
    print(z)

fy()

def fz():
    xx = 1
    yy = 2
    zz = 3
    print(xx)
    print(yy)
    print(zz)

fz()

# 関数内からグローバル変数に書き込む例

x = 100
def fa():
    global x
    x += 1
    print(x)

fa()

# 例外処理
a = input("type a number: ")
b = input("type another: ")
a = int(a)
b = int(b)
try:
    print(a / b)
except ZeroDivisionError:
    print("b cannot be zero.")

a = input("type a number: ")
b = input("type another: ")
try:
    a = int(a)
    b = int(b)
    print(a / b)
except (ZeroDivisionError, ValueError):
    print("Invalid Input")

# ドキュメンテーション文字列

def add(x, y):
    """
    Returns x + y.
    :param x: int.
    :param y: int.
    :return: int sum of x and y.
    """
    return x + y

print(add(1, 2))


# charange
## 1

def charange1(x):
    return x ** 2

x = input("type a number: ")
print(type(x))
int_x = int(x)
print(type(int_x))
print(charange1(int_x))


## 2

def charange2(x):
    print(x)

x = input("type strings")
charange2(x)
