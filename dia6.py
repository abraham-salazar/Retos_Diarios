"""
Abraham Salazar Montejano
01/02/2024
You are given two positive integers n and k.

Your task is to find a string s such that all possible strings of length n that can be formed using the first k
lowercase English alphabets occur as a subsequence of s.

If there are multiple answers, print the one with the smallest length.
If there are still multiple answers, you may print any of them.

Note: A string a is called a subsequence of another string b if a
can be obtained by deleting some (possibly zero) characters from b 
without changing the order of the remaining characters.

Input
The first line of input contains a single integer t(1≤t≤676) denoting the number of test cases.

Each test case consists of a single line of input containing two integers n (1≤n≤26) and k(1≤k≤26).

Output
For each test case, print a single line containing a single string s
which satisfies the above property. If there are multiple answers, print the one with the smallest length. If there are still multiple answers, you may print any of them.

"""

#t es el numero de casos prueba

alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    for i in range(n):
        for j in range(k):
            print(alfabeto[j], end = "")
    print("")
