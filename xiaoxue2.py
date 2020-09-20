from fractions import Fraction
import random
 
#四则运算
 
def numericalOperation():
 
    sym = ['＋', '－', '×', '÷']
 
    f= random.randint(0, 3)
 
    n1 = random.randint(1, 20)
 
    n2 = random.randint(1, 20)
 
    result = 0
 
    if f== 0:#加法
 
       result  = n1 + n2
 
    elif f == 1:#减法，要先比较大小，防止输出负数
 
        n1, n2 = max(n1, n2), min(n1, n2)
 
        result  = n1 - n2
 
    elif f== 2:#乘法
 
        result  = n1 * n2
 
    elif f == 3:#除法，要比较大小，并循环取整除
 
        n1, n2 = max(n1, n2), min(n1, n2)
 
        while n1 % n2 != 0:
 
            n1 = random.randint(1, 10)
 
            n2 = random.randint(1, 10)
 
            n1, n2 = max(n1, n2), min(n1, n2)
 
        result  = int(n1 / n2)
 
    print(n1, sym[f], n2, '= ', end='')
 
    return result
 
def createF():
    fz1 = random.randint(1, 20)
    if fz1 == 0:
        fm1 = random.randint(1, 20)
    else:
        fm1 = random.randint(1, 20)
    f1 = Fraction(fz1, fm1)
    fz2 = random.randint(1, 20)
    fm2 = random.randint(1, 20)
    f2 = Fraction(fz2, fm2)
    
    f1,f2 = createF()
    return f1,f2
    
def numOper():


    symbol = random.choice(['+','-','*','/'])
    f1,f2 = createF()
    if symbol =='+':
        while f1+f2>1:
            f1,f2 = createF()
        print(f1+'+'+f2+'='+(f1+f2))
        
    elif symbol =='-':
        f1,f2 = max(f1,f2),min(f1,f2)  #防止出现负数
        print(f1+'-'+f2+'='+(f1-f2))
        
    elif symbol == '*':
        while f1*f2>1:
            f1,f2 = createF()
        print(f1+'*'+f2+'='+(f1*f2))
        
    else:
        while f1/f2>1:
            f1,f2=createF()
        print(f1+'/'+f2+'='+(f1/f2))
    j=j+1
 
#制作题库
 
def test():
 
    sym = ['＋', '－', '×', '÷']
 
    print('输入所需要的题目数量')
 
    n=int(input())
 
    result =[]
 
    m=0
 
    while m<=(n-1):
 
        print(m+1,end='、')
 
        result .append(numericalOperation())
 
        print(' ')
 
        m=m+1
 
    m=0
 
    print('对应的答案：')
 
    while m<=(n-1):
 
        print(m+1,'、',result [m])
 
        m=m+1
 
  
 
print('选择想要的模式')
 
print('1、进行四则运算')
 
print('2、制作题库')
print("3,真分数计算")
 
n=int(input())
 
#当输入1时，进行四则运算，调用函数syzs()
 
if n==1:
    print("输入测试的题目数：")
    k=int(input())
    p=0
    q=0
    while p<k:
 
        result  = numericalOperation()
 
        j= input()
        
 
        s= int(j)
 
        if s== result :
            q=q+1
            print('right')
 
        else:
 
            print('error.，the answer is', result )
        p=p+1
    print("成绩为%f分",100*q/k)
 
#当输入2时，进行制作题库
 
if n==2:
 
     test()
if n==3:
    
            
    numOper()
       
