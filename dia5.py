"""
A spy detected
You are given an array a consisting of n (n≥3) positive integers. 
It is known that in this array, all the numbers except one are the 
same (for example, in the array [4,11,4,4] all numbers except one are equal to 4).

Print the index of the element that does not equal others. The numbers in the 
array are numbered from one.

Input
The first line contains a single integer t(1≤t≤100). Then t test cases follow.

The first line of each test case contains a single integer n (3≤n≤100) — the length of the array a.

The second line of each test case contains n integers a1,a2,…,an (1≤ai≤100).

It is guaranteed that all the numbers except one in the a array are the same.

Output
For each test case, output a single integer — the index of the element that is not equal to others.

"""
#a es la longitud del array
#t es el numero casos de prueba

t = int(input())

for _ in range(t):
    a = int(input())
    array = list(map(int, input().split()))
    if array[0] != array[2] and array[0] != array[1]:
        print(1)
    else:
        for i in range(a):
            if array[i] != array[0]:
                print(i+1)
                break

