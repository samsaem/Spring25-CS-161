# ******* QUESTION 1 *******
# Arguments: TREE
# Return: a tuple of leaf nodes in the order that they visited from left-to-right BFS
def BFS(TREE):
    # queue: FIFO
    queue = [TREE]
    leaves = []
    while queue:
        node = queue.pop(0)
        # TREE only has a single-node when it's a non-tuple object
        # push to top of stack -> added to list of leaves
        if type(node) is not tuple:
            leaves.append(node)
        # TREE is a tuple and has more than one node
        # added to list of queue
        else:
            queue.extend(node)
    return tuple(leaves)

# print(BFS("ROOT"))
# print(BFS(((("L", "E"), "F"), "T")))
# print(BFS(("R", ("I", ("G", ("H", "T"))))))
# print(BFS((("A", ("B",)), ("C",), "D")))
# print(BFS(("T", ("H", "R", "E"), "E")))
# print(BFS(("A", (("C", (("E",), "D")), "B"))))

# ******* QUESTION 2 *******
# Arguments: TREE
# Return: a tuple of leaf nodes in the order that they visited from left-to-right DFS
def DFS(TREE):
    # stack: LIFO
    stack = [TREE]
    leaves = []
    while stack:
        node = stack.pop()
        # TREE only has a single-node when it's a non-tuple object
        # added to list of leaves
        if type(node) is not tuple:
            leaves.append(node)
        # TREE is a tuple and has more than one node
        # added to list of stack in reverse order so leftmost get processed first
        else:
            stack.extend(reversed(node))
    return tuple(leaves)

# print(DFS("ROOT"))
# print(DFS(((("L", "E"), "F"), "T")))
# print(DFS(("R", ("I", ("G", ("H", "T"))))))
# print(DFS((("A", ("B",)), ("C",), "D")))
# print(DFS(("T", ("H", "R", "E"), "E")))
# print(DFS(("A", (("C", (("E",), "D")), "B"))))

# ******* QUESTION 3 *******
def DFID_helper(TREE,depth):
    # ensure that depth doesn't go less than 0
    if depth < 0:
        return []
    # TREE only has a single-node when it's a non-tuple object
    if type(TREE) is not tuple:
        return (TREE,)

    result = []
    # use reversed built-in function to process right-to-left
    for subtree in reversed(TREE):
        result.extend(DFID_helper(subtree, depth - 1))
    return result

# Argument 1: TREE
# Argument 2: D (depth)
# Return: a tuple of leaf nodes in the order that they visited from right-to-left depth-first iterative-deepening search
def DFID(TREE,D):
    nodes = []
    for d in range(D + 1):
        nodes.extend(DFID_helper(TREE, d))
    return tuple(nodes)

# print(DFID("ROOT", 0))
# print(DFID(((("L", "E"), "F"), "T"), 3))
# print(DFID(("R", ("I", ("G", ("H", "T")))), 4))
# print(DFID(((("A", ("B",)), ("C",), "D")), 3))
# print(DFID(("T", ("H", "R", "E"), "E"), 2))
# print(DFID(("A", (("C", (("E",), "D")), "B")), 5))

# ******* QUESTION 4 *******
# First, we define the helper functions of DFS_SOL.
def FINAL_STATE(S):
    # goal state S == (homer, baby, dog, poison)
    return S == (True, True, True, True)

# NEXT_STATE returns the state that results from applying an operator to the current state.
def NEXT_STATE(S, A):
    # (homer, baby, dog, poison)
    h, b, d, p = S
    # homer moves west himself
    if A == "h":
        nh, nb, nd, np = not h, b, d, p
    # homer with baby move west
    elif A == "b" and h == b:
        nh, nb, nd, np = not h, not b, d, p
    # homer with dog move west
    elif A == "d" and h == d:
        nh, nb, nd, np = not h, b, not d, p
    # homer with poison move west
    elif A == "p" and h == p:
        nh, nb, nd, np = not h, b, d, not p
    else:
        return []

    new_state = (nh, nb, nd, np)
    # dog with baby, homer not with baby
    if nd == nb and nh != nb:
        return []
    # poison with baby, homer not with baby:
    if np == nb and nh != nb:
        return []

    return [new_state]

# SUCC_FN returns all of the possible legal successor states to the current state.
def SUCC_FN(S):
    return NEXT_STATE(S, "h") + NEXT_STATE(S, "b") + NEXT_STATE(S, "d") + NEXT_STATE(S, "p")

# ON_PATH checks whether the current state is on the stack of states visited by this depth-first search.
def ON_PATH(S, STATES):
    return S in STATES

# MULT_DFS is a helper function for DFS_SOL.
def MULT_DFS(STATES, PATH):
    if not STATES:
        return []
    # if there's valid first state
    first = STATES[0]
    first_state = DFS_SOL(first, PATH)
    if first_state:
        return first_state
    else:
        rest = STATES[1:]
    return MULT_DFS(rest, PATH)

# DFS_SOL does a depth first search from a given state to the goal state.
def DFS_SOL(S, PATH):
    # If S is the initial state in our search, PATH is set to []
    if ON_PATH(S, PATH):
        return []
    # return full path if there exists a final state
    if FINAL_STATE(S):
        return PATH + [S]
    # generate next state
    next_state = SUCC_FN(S)
    return MULT_DFS(next_state, PATH + [S])






