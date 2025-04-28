##############
# Homework 4 #
##############

# Exercise: Fill this function.
# Returns the index of the variable that corresponds to the fact that
# "Node n gets color c" when there are k possible colors
def node2var(n, c, k):
    # node n, color c, k colors being considered
    # variable index = (n-1) * k + c
    return (n-1) * k + c

# Exercise: Fill this function
# Returns *a clause* for the constraint:
# "Node n gets at least one color from the set {1, 2, ..., k}"
def at_least_one_color(n, k):
    clause = []
    for color in range(1, k + 1):
        index = node2var(n, color, k)
        # assign color to clause
        clause.append(index)
    return clause

# Exercise: Fill this function
# Returns *a list of clauses* for the constraint:
# "Node n gets at most one color from the set {1, 2, ..., k}"
def at_most_one_color(n, k):
    # clauses = disjunction of literals
    clauses = []
    for color1 in range(1, k + 1):
        for color2 in range(color1 + 1, k + 1):
            clauses.append([-node2var(n, color1, k), -node2var(n, color2, k)])
    return clauses

# Exercise: Fill this function
# Returns *a list of clauses* for the constraint:
# "Node n gets exactly one color from the set {1, 2, ..., k}"
def generate_node_clauses(n, k):
    # needs to be at least one color
    clauses = [at_least_one_color(n, k)]
    # apply constraint so max color is one per node
    clauses.extend(at_most_one_color(n, k))
    return clauses

# Exercise: Fill this function
# Returns *a list of clauses* for the constraint:
# "Nodes connected by an edge e cannot have the same color"
# The edge e is represented by a tuple
def generate_edge_clauses(e, k):
    # edge = (m, n) -- m, n cannot be the same color
    # edge is a tuple of two
    m, n = e
    clauses = []
    for color in range(1, k + 1):
        clauses.append([-node2var(m, color, k), -node2var(n, color, k)])
    return clauses

# The function below converts a graph coloring problem to SAT
# Return CNF as a list of clauses
# DO NOT MODIFY
def graph_coloring_to_sat(graph_fl, sat_fl, k):
    clauses = []
    with open(graph_fl) as graph_fp:
        node_count, edge_count = tuple(map(int, graph_fp.readline().split()))
        for n in range(1, node_count + 1):
            clauses += generate_node_clauses(n, k)
        for _ in range(edge_count):
            e = tuple(map(int, graph_fp.readline().split()))
            clauses += generate_edge_clauses(e, k)
    var_count = node_count * k
    clause_count = len(clauses)
    with open(sat_fl, 'w') as sat_fp:
        sat_fp.write("p cnf %d %d\n" % (var_count, clause_count))
        for clause in clauses:
            sat_fp.write(" ".join(map(str, clause)) + " 0\n")
    return clauses, var_count




# Example function call
if __name__ == "__main__":
   graph_coloring_to_sat("graph1.txt", "graph1_3.cnf", 3)
   graph_coloring_to_sat("graph1.txt", "graph1_4.cnf", 4)

   graph_coloring_to_sat("graph2.txt", "graph2_4.cnf", 4)
   graph_coloring_to_sat("graph2.txt", "graph2_7.cnf", 7)
   graph_coloring_to_sat("graph2.txt", "graph2_8.cnf", 8)
