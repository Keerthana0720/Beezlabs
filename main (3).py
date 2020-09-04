'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
# print ('Hello World')
s_range=1
e_range=10
count=0
for i in range(s_range,e_range+1):
    if '1' in str(i):
        count+=1
print("The number of ones present from",s_range,"to",e_range,"is",count,"one's.")
