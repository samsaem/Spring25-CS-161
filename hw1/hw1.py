def PAD(N: int):
    # base case: PAD(O) = PAD(1) = PAD(2) = 1
    if N in (0,1,2):
        return 1
    # recursive case: instead of PAD(n + 1) = PAD(n− 1) + PAD(n− 2)
    # we subtract 1 for each index, so we'll get PAD(N) = PAD(N-2) + PAD(N-3) in return
    return PAD(N-2) + PAD(N-3)

def SUMS(N: int):
    # base case
    if N in (0,1,2):
        return 0
    # recursive case: since PAD(O...2) = 1 for each call, we add 1 for any N > 2
    return 1 + SUMS(N-2) + SUMS(N-3)

def ANON(TREE: tuple):
    # TREE is a single leaf node L when it's a non-tuple object
    if type(TREE) is not tuple:
        return "?"
    # TREE is a tuple when there's more than one node
    else:
        # return the result of TREE in tuple recursively
        res = []
        for subtree in TREE:
            res.append(ANON(subtree))
        return tuple(res)

def TREE_HEIGHT(TREE: tuple):
    # TREE is a non-tuple object when TREE is a single leaf node
    # height is 0
    if type(TREE) is not tuple:
        return 0
    # TREE is a tuple, height > 0
    # traverse through tree, if height > max_height, update max_height
    # return 1 + max_height since each tuple is an additional +1 height
    else:
        max_height = 0
        for node in TREE:
            height = TREE_HEIGHT(node)
            if height > max_height:
                max_height = height
        return 1 + max_height

def TREE_ORDER(TREE):
    # TREE is a number `m`
    if type(TREE) is int:
        return (TREE,)
    # TREE is a tuple (L, m R)
    # - based on the test cases, each tuple is arranged with the order of (left, right, m)
    # For example     :       ((1, 2, 3), 7, 8)
    # start with              ((1, 2, 3),...  ) where L = 1, m = 2, R = 3
    # change to (L, R, m)  => (1, 3, 2, 7, 8)
    #                         (1, 3, 2, 7, 8)   where L = (1, 3, 2), m = 7, R = 8
    # change to (L, R, m)  => (1, 3, 2, 8, 7)
    else:
        left, m, right = TREE
        return TREE_ORDER(left) + TREE_ORDER(right) + (m,)