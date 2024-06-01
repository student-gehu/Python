count=0
count1=0

f1=open("abc.txt","w+")

f1.write("Hello")
c=f1.tell()
print(c)
f1.seek(0)
c=f1.tell()
print(c)
abc=f1.read()
print(abc)
f1.seek(0)
for i in f1:
    print(i)
leng=len(i)
for x in range(0,leng,1):
    if i[x]=='a' or i[x]=='e' or i[x]=='i' or i[x]=='o' or i[x]=='u':
        count=count+1
    else:
        count1=count1+1
print("total vowel=",count)
print("total Consonent=",count1)