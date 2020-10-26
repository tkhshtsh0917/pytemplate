"""
route_search
"""
import networkx as nx


def dijkstra_search():
    """
    dijkstra_search
    """

    graph = nx.Graph()

    graph.add_nodes_from(
        ["a1", "a2", "a3", "a4", "a5", "b1", "b2", "b3", "b4", "b5", "gw"]
    )
    nx.add_cycle(graph, ["a1", "a2", "a3", "a4", "a5"])
    nx.add_cycle(graph, ["b1", "b2", "b3", "b4", "b5"])
    nx.add_star(graph, ["gw", "a1", "a2", "a3", "a4", "a5"])
    nx.add_star(graph, ["gw", "b1", "b2", "b3", "b4", "b5"])

    print("graph.nodes: {}\n".format(list(graph.nodes)))
    print("graph.edges: {}\n".format(list(graph.edges)))

    # Dijkstra theory search for the shortest path from source (from "a1" node)
    pred, dist = nx.dijkstra_predecessor_and_distance(graph, "a1")

    print("route: {}\n".format(sorted(pred.items())))
    print("distance: {}\n".format(sorted(dist.items())))
