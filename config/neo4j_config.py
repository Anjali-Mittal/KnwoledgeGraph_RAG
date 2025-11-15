from py2neo import Graph

def get_graph():
    return Graph("neo4j://127.0.0.1:7687", auth=("neo4j", "astraloom123"))
