for i in range(100):
    print("Hello, world!")

print("""これはとてもとても、
とてもとても長い複数行の
コードです。""")

print("2.2 + 2.2 = %2.1f" % (2.2 + 2.2) )

x = 10
y = 10
z = x + y
print(z)

a = x - y
print(a)

x = x + 1
print(x)

x += 1
print(x)

x -= 1
print(x)

print(100>10)
print(100<10)
print(1 == 1 and 2 == 2)
print(1 == 0 and 2 == 2)
print(1 == 0 or 2 == 2)
print(1 == 0 or 2 == 1)
print(1 == 1 or 2 == 2)
print(1 == 0 or 2 == 2 and 1 == 1)
print(1 == 0 or 2 == 2 and 3 == 1)
print(1 == 0 or 2 == 1 and 3 == 1)
print(1 == 0 or 2 == 1 and 3 == 3)
print(1 == 1 or 2 == 2 and 1 == 1)
print(1 == 1 or 2 == 2 and 3 == 1)

print("""
演算子の優先順位
  +  -  ~x      (+と-は単項演算子)
  **
  *  /  %  //
  +  -
  <<  >>
  &
  ^
  |
  <  <=  >  >=  ==  !=  <>  is  is not  in  not in
  not
  and
  or
""")

# charenge
## 1
print("Hello, World!")
print("My name is Shuichi")
print("I'm 40 years old")

## 2
a = 9
b = 21

if a < 10:
    print("%dは10未満の数字です。" % a)

## 3

if a <= 10:
    print("%dは10以下の数字です。" % a)
elif a > 10 and a <= 25:
    print("%dは１０よりおおきく２５以下の数字です。" % a)
elif a > 25:
    print("%dは25より大きい数字です。" % a)

## 4
x = 10 % 3
print("10割る３の余りは%dです" % x)

## 5
x = 10 // 3
print("10割る３の商は%dです" % x)

## 6
age = 18

if 6 <= age <= 12:
    print("%d歳は小学生です" % age)
elif 13 <= age <= 15:
    print("%d歳は中学生です" % age)
elif 16 <= age <= 18:
    print("%d歳は高校生です" % age)

