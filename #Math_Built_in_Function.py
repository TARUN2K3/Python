#Math Built-in Function
#abs --> Return absolute value and return magnitue of complex number
print(abs(-1.0))
print(abs(-1))
print(abs(3+4j))
print('--------------------------------')
#pow(base, exp, mod = None) --> Return power of the no. with optional modulo for large no.
print(pow(10,2))
print(pow(10,-2))
print(pow(10,0.2))
print(pow(10,2,3))
print('-------------------------------')
#ronud(number, ndigit=None) --> round the number till nearest integer and till the decimal no. provided and follows bankers rounding algorithm
print(round(3.4))
print(round(3.6))
print(round(4.5))
print(round(5.5))
print(round(5.524124, 2))
print(round(1843902, -1))
print(round(1313124, -2))
print('--------------------------------')
#divmod --> return quotient and remainder in tuple
print(divmod(10,2))
print(divmod(100,3))
print('---------------------------------')
#min(iterable, key=None, default=None) --> Return min value form iterable key is the function like "abs" default is return if iterable is empty
a = [12,2,-3,56,1,-2,4.56,0.1,-0.2] 
print(min(a))
print(min(a, key=abs))
print('----------------------------------')
#max(iterable, key=None, default=None) --> Return Max value form iterable key is the function like "len" default is return if iterable is empty
b = ['Tarun', 'banana', 'default', 'none', 'a', 'ab']
print(max(b))
print(max(b,key=len))
print('-----------------------------------')
#sum(iterable, start=0) -->Return sum of the no. by default start is zero 
print(sum([1,2,3,4,5,6,7,8,9]))
print(sum([1,2,3,4,5,6,7,8,9], start=10)) # sum iterable + 10
print('------------------------------------')
#eval -- > evaluate expression string dynamically with variable context dictionaries
a1 = {"a":1,"b":2}
b1 = {"c":3}
c = "a + b + c"
print(eval(c, a1 , b1))