def to2(i):
    num = []
    while i != 0:
        num.append(i % 2)
        i //= 2
    return num[::-1]

_implication = "<="
_not = " not "
_and = " and "
_or = " or "
opers = {
    "¬": _not,
    "∧": _and,
    "∨": _or,
    "→": _implication,
    "  ": " "}
input_str = "¬x ∧ y ∧ (z → w)"
input_str = input(":")
for k, v in opers.items():
    input_str = input_str.replace(k, v)
name_vars = ("x", "y", "z", "w", "v")
var = {v:0 for v in name_vars if v in input_str}
n = len(var)
lst = [[], []]
print(*var.keys())
for i in range(2 ** n):
    num = to2(i)
    num = [0] * (n - len(num)) + num
    for i in range(n):
        var[name_vars[i]] = bool(num[i])
    print(*num, end=" ")
    res = eval(input_str, var)
    lst[int(res)].append((num, res))
    print(res)
    
print("False:", *lst[0], sep="\n")
print("True:", *lst[1], sep="\n")

