# import jieba
'''
print('hello,world')

import keyword
print(keyword.kwlist)
'''
# input("\n\n输入")
'''
a = 1
if a:
	print(a)
else:
	print("aaa")
'''
'''age = int(input("请输入"))
print(age)
input("点击ente退出")
'''
'''def printme(a):
	print("hello"+a)
	return
printme("你好")
'''
'''
TempStr = input()
if TempStr[0:3] in ["RMB"]:	
	c = eval(TempStr[3:])/6.78
	print("USD{:.2f}".format(c))
elif TempStr[0:3] in ["USD"]:
	F = eval(TempStr[3:])*6.78
	print("RMB{:.2f}".format(F))
else:
	print("输入格式错误")    	
for x in ['H','e','l','l','o',' ','W','o','r','l','d']:
	print(x)
a = input()
print(eval(a)**0,eval(a)**1,eval(a)**2,eval(a)**3,eval(a)**4,eval(a)**5) 
'''
'''
import turtle
turtle.setup(650,350,200,200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("purple")
turtle.seth(-40)
for i in range(4):
	turtle.circle(40,80)
	turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.done()
'''
'''
import turtle
for i in range(4):
	turtle.circle(40+i*10)
turtle.done()
'''
'''
a = input()
if a[-2:] in ['in']:
	m = eval(a[0:-2])/39.37
	print("{:.3f}m".format(m))
elif a[-1] in ['m']:
	m = eval(a[0:-1])*39.37
	print("{:.3f}in".format(m))
'''
'''
import time
scale=50
print("执行开始".center(scale//2, "-"))
start = time.perf_counter()
for i in range(scale + 1):
	a = '*' * i
	b = '.' * (scale -i)
	c = (i/scale)*100
	dur = time.perf_counter() - start
	print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end="")
	time.sleep(0.1)
print("\n"+"执行结束".center(scale//2, '-'))
'''
'''
#平方值格式化
N = input()
d = eval(N)
e = str(d*d)
c = 20-(len(e))
for i in range(c//2):
	a = "-" * i
if 20-(len(e))%2!=0:
	b = a + "-"
else:
	b = a
print("{}{}{}".format(a,e,b))
'''
'''
#同符号数学运算
N = input()
a = abs(eval(N))
b = a+10
c = a-10
d = a*10 
if eval(N)>0:
	print("{}"" ""{}"" ""{}"" ""{}".format(a,b,c,d))
else:
	print("{}"" ""{}"" ""{}"" ""{}".format(a,-abs(b),-abs(c),-abs(d)))
'''
'''
#天天向上力量3
N = eval(input())
dayup = 1.0
daydown = 1.0
for i in range(365):
	dayup = dayup * (1+N*0.001)
	daydown = daydown * (1-N*0.001)
print("{:.2f}"",""{:.2f}"",""{:.0f}".format(dayup,daydown,dayup//daydown))
'''
'''
#星号三角形
N = eval(input())
a = -1
while a < N :
	a = a+2
	b="*"*a
	print(b.center(N," "))
'''
'''
#凯撒密码
n = input()
b = "abcdefghijklmnopqrstuvwxyz"
for d in n:
	c = 0
	if d !=" ":
		while d !=b[c]:
			c = c+1
		else:
			if c+3>=26:
				c=abs(26-(c+3))
			else:
				c=c+3
			print(b[c],end="")
	else:
		print(" ",end="")

'''
'''
#整数加减和
sum = 0
for i in range(967):
	if i % 2 ==0:
		sum = sum - i
		i = i + 1
	else:
		sum = sum + i
		i = i + 1
print(sum)
'''
'''
#一百以内素数之和
sum = 0
for i in range(1,100):
	b = 0
	for a in range(1,i+1):
		if i % a ==0:
			b = b+1
	if b ==2:
		sum = sum+i
print(sum)
'''
'''
#合格率计算
a = []
c = 0
d = 0
var = 1
while var == 1:
	b = input()
	if b == "":
		if c < 2:
			c = 2
			if d < 1:
				d = 1
		break
	else:
		a.append(b)
		c = c+1
		if c > 1:
			if a[c-1]>=a[0]:
				d = d+1
print("合格率为{:.2f}%".format(d/(c-1)*100))
'''
'''
#四叶玫瑰数
for i in range(1000,10000):
	a = "{}".format(i)
	sum = 0
	for b in range(len(a)):
		sum = sum + pow(eval(a[b]),len(a))
	if sum == i:
		print(i)
'''
'''
for b in range(4):
	if b < 3:	
		a = []
		for i in range(2):
			a.append(input())
		if a[0] == "Kate":
			if a[1] =="666666":
				print("登录成功！")
				break
	else:
		print("3次用户名或者密码均有误！退出程序。")
'''
'''
#科赫雪花
import turtle
def koch(size,n):
	if n == 0:
		turtle.fd(size)
	else:
		for angle in [0,60,-120,60]:
			turtle.left(angle)
			koch(size/3,n-1)
def main():
	turtle.setup(600,600)
	turtle.penup()
	turtle.goto(-200,100)
	turtle.pendown()
	turtle.pensize(2)
	level = 3
	koch(400,level)
	turtle.right(120)
	koch(400,level)
	turtle.right(120)
	koch(400,level)
	turtle.hideturtle()
	turtle.done()
main()
'''
# 三国演义 人物出场次数统计
# text = open("threekingdoms.txt", "r", encoding="utf-8").read()
# excludes = {"将军", "却说", "荆州", "二人", "不可", "不能", "如何", "如此", "商议", "军士"}
# words = jieba.lcut(text)
# counts = {}
# for word in words:
# 	if len(word) == 1:
# 		continue
# 	elif word == "诸葛亮" or word == "孔明曰":
# 		rword = "孔明"
# 	elif word == "关公" or word == "云长":
# 		rword = "关羽"
# 	elif word == "玄德曰" or word == "玄德":
# 		rword = "刘备"
# 	elif word == "丞相曰" or word == "孟德":
# 		rword = "曹操"
# 	else:	
# 		rword = word
# 	counts[rword] = counts.get(rword, 0) + 1
# for word in excludes:
# 	del counts[word]
# items = list(counts.items())
# items.sort(key=lambda x: x[1], reverse=True)
# for i in range(10):
# 	word, count = items[i]
# 	print("{0:<10}{1:>5}".format(word, count))
import turtle
for i in range(4):
	turtle.right(90)
	turtle.fd(80)
turtle.done()