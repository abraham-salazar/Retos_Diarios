"""
You are given an integer n
 and three strings a,b,c, each consisting of n lowercase Latin letters.

Let a template be a string t consisting of n
 lowercase and/or uppercase Latin letters. The string s matches the template t if the following conditions hold for all i from 1 to n
:

if the i-th letter of the template is lowercase, then si must be the same as ti;
if the i-th letter of the template is uppercase, then si must be different from the lowercase version of ti. For example, if there is a letter 'A' in the template, you cannot use the letter 'a' in the corresponding position of the string.
Accordingly, the string doesn't match the template if the condition doesn't hold for at least one i
.

Determine whether there exists a template t such that the strings a and b match it, while the string c does not.

Input
The first line contains an integer t(1≤t≤1000) — the number of test cases.

The first line of each test case contains an integer n(1≤n≤20) — the length of the given strings.

The next three lines contain the strings a,b and c. Each string consists of exactly n lowercase Latin letters.

Output
For each testcase, print "YES" if there exists a template t
such that the strings a and b match it, while the string c does not. Otherwise, print "NO".

"""
t = int(input())
for i in range(t):
    n = int(input())
    a = list(input())
    b = list(input())
    c = list(input())
    exists_template = True        
    for j in range(n):
            if a[j] != c[j] and b[j] != c[j]:
                exists_template = False
                break
            
    if exists_template:
        print("NO")
    else:
        print("YES")

