# 1
def PAD(N: int):
    if N in (0,1,2):
        return 1
    return PAD(N-2) + PAD(N-3)

# print(PAD(0))
# print(PAD(1))
# print(PAD(2))
# print(PAD(5))
# print(PAD(3))
# print(PAD(4))

# 2
def SUMS(N: int):
    if N in (0,1,2):
        return 0
    return 1 + SUMS(N-2) + SUMS(N-3)

# print(SUMS(0))
# print(SUMS(1))
# print(SUMS(2))
# print(SUMS(5))
# print(SUMS(3))
# print(SUMS(4))

# 3
def ANON(TREE: tuple):
    if type(TREE) is not tuple: # single leaf node
        return "?"
    else: # more than one node
        res = []
        for subtree in TREE:
            res.append(ANON(subtree))
        return tuple(res)

# print(ANON(42))
# print(ANON("FOO"))
# print(ANON(((("L", "E"), "F"), "T")))
# print(ANON((5, "FOO", 3.1, -0.2)))
# print(ANON((1, ("FOO", 3.1), -0.2)))
# print(ANON((((1, 2), ("FOO", 3.1)), ("BAR", -0.2))))
# print(ANON(("R", ("I", ("G", ("H", "T"))))))

# 4
def TREE_HEIGHT(TREE: tuple):
    if type(TREE) is not tuple:
        return 0
    else:
        max_height = 0
        for subtree in TREE:
            height = TREE_HEIGHT(subtree)
            if height > max_height:
                max_height = height
        return 1 + max_height

# print(TREE_HEIGHT(1))
# print(TREE_HEIGHT((5, "FOO", 3.1, -0.2)))
# print(TREE_HEIGHT((1, ("FOO", 3.1), -0.2)))
# print(TREE_HEIGHT(("R", ("I", ("G", ("H", "T"))))))

# 5
def TREE_ORDER(TREE):
    if type(TREE) is int:
        return (TREE,)
    else:
        left, m, right = TREE
        return TREE_ORDER(left) + TREE_ORDER(right) + (m,)

# print(TREE_ORDER(42))
# print(TREE_ORDER(((1, 2, 3), 7, 8)))
# print(TREE_ORDER(((3, 7, 10), 15, ((16, 18, 20), 30, 100))))