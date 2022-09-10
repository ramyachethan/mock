#program:1
palindrome:

x = "ramya"
new = ""
def pali(x):
    for i in x[::-1]:
        yield i
for i in pali(x):
    new += i
if new == x:
    print("yes ,it is Palindrome")
else:
    print("No ,it is not Palindrome")


#program2:
Adding two list
#x = [1,2,3,4]
#y = [9,9,9,9]
a=int(input("enter the value:"))
b=int(input("enter the value:"))
X=str(a)
Y=str(b)
x=list(X)
y=list(Y)
res = []
sum=0
for i in range(0, len(x)):
    res.append(int(x[i]) + int(y[i]))
print("Addition of the  x and y is: " + str(res))
for z in res:
       sum+=z
print("sum of given two values:",sum)

#program:3
#remove "0" from ip address
# o/p =  216.8.94.196
x = "216.08.094.196"
y=""

for i in x:
    if i=='0':
        continue
    y+=i
print(y)

#program:4
#reverse only alphbets:
#st = "ab@#cd!ef"
#Output: fe @  # dc!ba
s="ab@cd!ef"
l=list(s)
#print(l)
i=0
j=len(l)-1
while i < j:
    if not l[i].isalpha():
        i += 1
    elif not l[j].isalpha():
        j -= 1
    else:
        l[i], l[j] = l[j], l[i]
        i += 1
        j -= 1

res = ''.join(l)
print(res)

#program:5
#duplicate count:
#findout elements duplicate count output in  dict format
list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]
new = {}
for a in list:
    if a in list:
        new[a]=new.get(a,0)+1
        pass
    else:
        new[a]=new.count(a)
print(new)

#program:6
#add alphbets and integer

# t1 = (1, 2, 3, "a", "c")
# t2 = ("b", "d", 9, 8, 7)
# Output: (10,10,10,"ab","cd")
t1 = (1, 2, 3, "a", "c")
t2 = ("b", "d", 9, 8, 7)
Output = []
x = []
y = []
r = []
for i in list(t2):
    if type(i) == int:
        x.append(i)
    else:
        y.append(i)

z = x + y

for i in range(len(t1)):
    k = list(t1)
    m = k[i] + z[i]
    r.append(m)
output = tuple(r)
print(output)

#program:7
#adding nested list:
l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
new = []

for i in l:
    if type(i) == list:
        for j in i:
            if type(j) == list:
                for k in j:
                    new.append(k)
            else:
                new.append(j)

    else:
        new.append(i)
print(new)



