"""
n = 3

*** ***   3 1 3    Total 7 columns (2n+1)
**   **   2 3 2          5 rows    (2n-1)
*     *   1 5 1
**   **   2 3 2
*** ***   3 1 3
"""

"""
n = 7

******* *******
******   ******
*****     *****
****       ****
***         ***
**           **
*             *
**           **
***         ***
****       ****
*****     *****
******   ******
******* *******
"""

def hol_diamond(n):
    col = (2*n+1)
    row = (2*n-1)
    a = 1
    out = []
    for i in range(row):
        out.append('*'*(n) + ' '*a + '*'*(n))
        n -= 1
        a += 2
        if a ==col and n ==1:
            break
    b = out[0:(row//2)]
    lit = out[0:(row//2)+1]+ b[::-1]

    return "\n".join(lit)
print(hol_diamond(4))
