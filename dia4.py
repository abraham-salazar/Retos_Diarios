"""
There are three cards with letters a, b, c
 placed in a row in some order. You can do the following operation at most once:
Pick two cards, and swap them.
Is it possible that the row becomes abc after the operation? Output "YES" if it is possible, and "NO" otherwise.
Input
The first line contains a single integer t(1≤t≤6) — the number of test cases.

The only line of each test case contains a single string consisting of each of the three characters a, b, and c
exactly once, representing the cards.

Output
For each test case, output "YES" if you can make the row abc
with at most one operation, or "NO" otherwise.

You can output the answer in any case (for example, the strings "yEs", "yes", "Yes" and "YES" will be recognized as a positive answer).
"""

samples = int(input())
for i in range(samples):
    a = list(input())

    if a[0] == "a" or a[1] == "b" or a[2] == "c":
        print("YES")
    else:
        print("NO")
