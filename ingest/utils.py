# utils.py

def get_label_from_uri(uri):
    """
    Extracts the label from a URI-like string.
    For example, 'mission/Chandrayaan-2' → 'Mission'.
    """
    if isinstance(uri, str) and "/" in uri:
        return uri.split("/")[0].capitalize()
    return "Literal"


def is_numeric_value(value):
    """
    Checks if a value is numeric (int or float).
    Useful for determining how to store it in the graph.
    """
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False

    


