"""EGE NUM 2 auto solve"""

"¬x ∧ y ∨ z ∧ ¬y ∨ ¬z ∧ w"
f_lam = lambda x, y, z, w: (not x) and y or z and (not y) or (not z) and w
f_res = 0
tab = """
1	0	*	*
*	1	0	*
*	*	1	0
"""
ar_tab = [st.split() for st in tab.split("\n") if st]
print("Table", *ar_tab, sep="\n")
cnt_alpha = len(ar_tab[0])

# st_a = "abcd"
st_a = "xyzw"


def st_in_list(st, list_st):
    for st2 in list_st:
        for i in range(len(st)):
            if not (st[i] == "*" or st[i] == str(st2[i])):
                break
        else:
            return True
    return False


def itern(n):
    for x in range(n):
        for y in range(n):
            for z in range(n):
                if n == 3:
                    if len(set((x, y, z))) == n:
                        yield x, y, z
                else:
                    for w in range(n):
                        if len(set((x, y, z, w))) == n:
                            yield x, y, z, w


def replace(ar_a, iter_a):
    res = [ar_a[a_list[iter_a][i]] for i in range(cnt_alpha)]
    return res


"bdca"

d = {i: st_a[i] for i in range(len(st_a))}
a_list = list(itern(cnt_alpha))
iter_a = 0
print(a_list)

nt = lambda i: not i
print("a_list", a_list)
solve = None
cnt_solve = 0
for iter_a in range(len(a_list)):
    print("=======", iter_a, "=======")
    res_ar = []
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    # ((x ∧ y) → (¬z ∨ w)) ∧ ((¬w → x) ∨ ¬y)
                    f = f_lam(x, y, z, w)
                    r_st = replace((x, y, z, w), iter_a)
                    if int(f) == f_res:
                        #print(r_st, "sum:", sum(r_st))
                        res_ar.append(r_st)
    for st in ar_tab:
        if not st_in_list(st, res_ar):
            break
    else:
        print(*res_ar, sep="\n")
        print("+" * 10, "SOLVE")
        solve = [d[ii] for ii in a_list[iter_a]]
        print(solve)
        cnt_solve += 1
print("Result", cnt_solve)
print(*solve)

"""
x y z w
1 1 1 0 sum: 3
0 1 0 0 sum: 1
0 1 1 0 sum: 2

1	2	3	4	Функция
z   w   y   x  
1	0	1	1	
0	0	1	0	
1	0	1	0	
zwyx

"""
