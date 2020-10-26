"""
packing
"""
from ortools.algorithms import pywrapknapsack_solver
from ortools.linear_solver import pywraplp


def knapsack():
    """
    knapsack
    """
    values = [
        360,
        83,
        59,
        130,
        431,
        67,
        230,
        52,
        93,
        125,
        670,
        892,
        600,
        38,
        48,
        147,
        78,
        256,
        63,
        17,
        120,
        164,
        432,
        35,
        92,
        110,
        22,
        42,
        50,
        323,
        514,
        28,
        87,
        73,
        78,
        15,
        26,
        78,
        210,
        36,
        85,
        189,
        274,
        43,
        33,
        10,
        19,
        389,
        276,
        312,
    ]
    weights = [
        [
            7,
            0,
            30,
            22,
            80,
            94,
            11,
            81,
            70,
            64,
            59,
            18,
            0,
            36,
            3,
            8,
            15,
            42,
            9,
            0,
            42,
            47,
            52,
            32,
            26,
            48,
            55,
            6,
            29,
            84,
            2,
            4,
            18,
            56,
            7,
            29,
            93,
            44,
            71,
            3,
            86,
            66,
            31,
            65,
            0,
            79,
            20,
            65,
            52,
            13,
        ]
    ]
    capacity = [850]

    solver = pywrapknapsack_solver.KnapsackSolver(
        pywrapknapsack_solver.KnapsackSolver.KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER,
        "Knapsack",
    )
    solver.Init(values, weights, capacity)
    total_value = solver.Solve()

    total_weight = 0
    packed_items = []
    packed_weights = []

    for i in range(len(values)):
        if solver.BestSolutionContains(i):
            packed_items.append(i)
            packed_weights.append(weights[0][i])
            total_weight += weights[0][i]

    print("Total value: {}\n".format(total_value))
    print("Total weight: {}\n".format(total_weight))
    print("Packed items: {}\n".format(packed_items))
    print("Packed_weights: {}\n".format(packed_weights))


def maltiple_knapsacks():
    """
    maltiple_knapsacks
    """
    weights = [48, 30, 42, 36, 36, 48, 42, 42, 36, 24, 30, 30, 42, 36, 36]
    values = [10, 30, 25, 50, 35, 30, 15, 40, 30, 35, 45, 10, 20, 30, 25]
    capacities = [100, 100, 100, 100, 100]

    data = {}
    data["weights"] = weights
    data["values"] = values
    data["items"] = list(range(len(weights)))
    data["num_items"] = len(weights)
    data["bins"] = list(range(len(capacities)))
    data["capacities"] = capacities

    # Create the mip solver with the SCIP backend.
    solver = pywraplp.Solver.CreateSolver("SCIP")

    # Variables
    # variables[i, j] = 1 if item i is packed in bin j.
    variables = {}
    for i in data["items"]:
        for j in data["bins"]:
            variables[(i, j)] = solver.IntVar(0, 1, "{}_{}".format(i, j))

    # Constraints
    # Each item can be placed in at most one bin.
    # This constraint is set by requiring the sum of self.variables[i][j]
    # over all bins j to be less than or equal to 1.
    for i in data["items"]:
        solver.Add(sum(variables[i, j] for j in data["bins"]) <= 1)

    # The total weight packed in each bin can't exceed its capacity.
    # This constraint is set by requiring the sum of the weights of items
    # placed in bin j to be less than or equal to the capacity of the bin.
    for j in data["bins"]:
        solver.Add(
            sum(variables[(i, j)] * data["weights"][i] for i in data["items"])
            <= data["capacities"][j]
        )

    # Objective
    objective = solver.Objective()
    for i in data["items"]:
        for j in data["bins"]:
            objective.SetCoefficient(variables[(i, j)], data["values"][i])
    objective.SetMaximization()

    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print("Total packed value: {}".format(objective.Value()))
        total_weight = 0
        for j in data["bins"]:
            bin_weight = 0
            bin_value = 0
            print("Bin {}\n".format(j))
            for i in data["items"]:
                if variables[i, j].solution_value() > 0:
                    print(
                        "Item {} - weight: {} value: {}".format(
                            i, data["weights"][i], data["values"][i]
                        )
                    )
                    bin_weight += data["weights"][i]
                    bin_value += data["values"][i]
            print("Packed bin weight: {}".format(bin_weight))
            print("Packed bin value: {}".format(bin_value))
            total_weight += bin_weight
        print("Total packed weight: {}\n".format(total_weight))
    else:
        print("The problem does not have an optimal solution.\n")


def bin_packing():
    """
    bin_packing
    """
    weights = [48, 30, 19, 36, 36, 27, 42, 42, 36, 24, 30]

    data = {}
    data["weights"] = weights
    data["items"] = list(range(len(weights)))
    data["bins"] = data["items"]
    data["capacity"] = 100

    # Create the mip solver with the SCIP backend.
    solver = pywraplp.Solver.CreateSolver("SCIP")

    # Variables
    # var_x[i, j] = 1 if item i is packed in bin j.
    var_x = {}
    for i in data["items"]:
        for j in data["bins"]:
            var_x[(i, j)] = solver.IntVar(0, 1, "{}_{}".format(i, j))

    # var_y[j] = 1 if bin j is used.
    var_y = {}
    for j in data["bins"]:
        var_y[j] = solver.IntVar(0, 1, "y[{}]".format(j))

    # Constraints
    # Each item must be in exactly one bin.
    for i in data["items"]:
        solver.Add(sum(var_x[i, j] for j in data["bins"]) == 1)

    # The amount packed in each bin cannot exceed its capacity.
    for j in data["bins"]:
        solver.Add(
            sum(var_x[(i, j)] * data["weights"][i] for i in data["items"])
            <= var_y[j] * data["capacity"]
        )

    # Objective
    # Minimize the number of bins used.
    solver.Minimize(solver.Sum([var_y[j] for j in data["bins"]]))

    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        num_bins = 0
        for j in data["bins"]:
            if var_y[j].solution_value() == 1:
                bin_items = []
                bin_weight = 0
                for i in data["items"]:
                    if var_x[i, j].solution_value() > 0:
                        bin_items.append(i)
                        bin_weight += data["weights"][i]
                if bin_weight > 0:
                    num_bins += 1
                    print("Bin number {}".format(j))
                    print("  Items packed: {}".format(bin_items))
                    print("  Total weight: {}".format(bin_weight))
                    print("\n")
        print("Number of bins used: {}".format(num_bins))
        print("Time = {} milliseconds\n".format(solver.WallTime()))
    else:
        print("The problem does not have an optimal solution.\n")
