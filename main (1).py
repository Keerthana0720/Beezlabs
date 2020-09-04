'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
# print ('Hello World')
array=[1,2,4,6,3,7,8]
array.sort()
for i in range(0,len(array)):
    for j in range(i+1,len(array)):
        if(array[i]+1==array[j]):
           break
        else:
            print("Output:",end=" ")
            print(array[i]+1)
            
        break