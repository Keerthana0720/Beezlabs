'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
import re
t=3:30
k=re.split("[:]",t)
h=int(k[0])
m=int(k[1])
m/=5
if(h>12):
    h=h-12;
dif=abs(h-m)
ang=dif*30
print(round(ang),"degree")
