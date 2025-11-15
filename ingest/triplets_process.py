import pandas as pd
from py2neo import Node, Relationship
from ingest.utils import get_label_from_uri, is_numeric_value
from config.neo4j_config import get_graph

graph =get_graph()

def ingest_triplets(csv_path, dataset_name):
    df = pd.read_csv(csv_path)

    for _, row in df.iterrows():
        s_uri, predicate, o_value = row["subject"], row["predicate"], row["object"]
        
        # Labels
        s_label = get_label_from_uri(s_uri)

        # Nodes
        subj = Node(s_label, id=s_uri)
        graph.merge(subj, s_label, "id")

        # Handle Object (either URI or literal)
        if is_numeric_value(o_value):
            obj = Node("Literal", value=float(o_value))
            obj_id = f"{predicate}_val_{o_value}"
            obj["id"] = obj_id
            graph.merge(obj, "Literal", "id")
        elif isinstance(o_value, str) and "/" in o_value:
            o_label = get_label_from_uri(o_value)
            obj = Node(o_label, id=o_value)
            graph.merge(obj, o_label, "id")
        else:
            obj = Node("Literal", value=o_value)
            obj["id"] = f"{predicate}_val_{o_value}"
            graph.merge(obj, "Literal", "id")

        # Relationship
        rel = Relationship(subj, predicate.upper(), obj)
        graph.merge(rel)

        # Dataset tagging
        dataset_node = Node("Dataset", name=dataset_name)
        graph.merge(dataset_node, "Dataset", "name")
        contains_rel = Relationship(dataset_node, "CONTAINS", subj)
        graph.merge(contains_rel)
