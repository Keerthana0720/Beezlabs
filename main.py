'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
print ('Hello World')
string="Intelligent platform focusing on AI"
count=0
for i in range(0,len(string)):
    if string[i].isalpha()==True:
        count+=1
print("Number of Characters :",count)
