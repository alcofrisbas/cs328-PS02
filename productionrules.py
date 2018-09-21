"""

"""

def get_triggered_rule(beliefs, rules):
    """
    beliefs: a SET of strings
    rules: a list of 2ples.

    return: first rule where there a belief in
    a -> b && a in beliefs && not b in beliefs
