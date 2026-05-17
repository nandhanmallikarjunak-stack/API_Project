print ("python automation testing")


"""
Data types:
1)mutable :list,dic,set
2)immutable:string,tuple,int
"""
#list ===== 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
stlist=["america","india","africa","india"]
# print(dir(str))
stlist.append("Europe") # end of the list it will add the given value
print(stlist)

# stlist.clear() # it will clear the given the list items
# print(stlist)

stlist.copy()  # it will copy the entire list
print(stlist)

c = stlist.count("india") # It will get the given values count in a string
print(c)

d = stlist.extend("1")
print(d)

"""
operators
"""

# Arithmetic Operators

# + (Addition) → 5 + 3 = 8
# - (Subtraction) → 5 - 3 = 2
# * (Multiplication) → 5 * 3 = 15
# / (Division) → 5 / 2 = 2.5
# // (Floor Division) → 5 // 2 = 2
# % (Modulus) → 5 % 2 = 1
# ** (Exponent) → 2 ** 3 = 8

a = 5
b = 4

print (f'addition:=,{a+b}')
print(f'Subtraction:=,{a-b}')
print(f'Multiplication:=,{a*b}')
print (f'Division:=,{a/b}')
print (f'Floor Division:=,{a//b}')
print (f'Modulus:=,{a%b}')
print (f'Exponent:=,{a**b}')
# print(f'Hi, {name}')\

"""
2. Comparison (Relational) Operators
Used to compare values (returns True/False)
== (Equal)
!= (Not equal)
> (Greater than)
< (Less than)
>= (Greater than or equal)
<= (Less than or equal)
Example: 5 > 3 → True
"""

# a = 5
# b = 4
# print (f'Comparison operators[Equal]:=,{a==b}')
# print(a)

l1 = [10,20,33,44,55,66]
print(l1)
print(l1[1:4])
print(l1[2:])
print(l1[:5])
print(l1[::2])
print(l1[:-2])


"""
1).logical operators 
2).arthametic operators:+,-,/,*,**,//
3).assignment operators:=,+=,*=
4).membership operators"in ,not in
5).identity operators:is ,is not
6).comparision operators:==,!=,<=,>=,<,>
"""