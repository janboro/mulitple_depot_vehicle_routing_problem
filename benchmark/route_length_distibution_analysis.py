import matplotlib.pyplot as plt

"""
This is the visualization of the Benchmarking results before using the Min Max algorithm and after, comparing the route length distributions.
The analysis was conducted on the Nearest Insertion Algorithm.
"""

initial_solution: dict[str, int] = {
    "depot_0": 3736,
    "depot_1": 2282,
    "depot_2": 1374,
    "depot_3": 3663,
    "depot_4": 6027,
    "depot_5": 3741,
    "depot_6": 2883,
    "depot_7": 1500,
    "depot_8": 1499,
    "depot_9": 3829,
}
final_solution: dict[str, int] = {
    "depot_0": 3736,
    "depot_1": 2282,
    "depot_2": 1374,
    "depot_3": 3663,
    "depot_4": 4554,
    "depot_5": 3741,
    "depot_6": 2883,
    "depot_7": 1500,
    "depot_8": 4555,
    "depot_9": 4529,
}

plt.figure()
plt.bar(x=range(len(initial_solution)), height=initial_solution.values())
plt.title("Nearest Insertion route lengths")
plt.ylim(0, 6100)

plt.figure()
plt.bar(x=range(len(final_solution)), height=final_solution.values())
plt.ylim(0, 6100)
plt.title("Nearest Insertion Min Max route lengths")
plt.show()
