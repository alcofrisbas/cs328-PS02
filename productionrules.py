"""

"""

def get_triggered_rule(beliefs, rules):
    """
    beliefs: a SET of strings
    rules: a list of 2ples.

    return: first rule where there a belief in
    a -> b && a in beliefs && not b in beliefs
    """
    finals = []
    for rule in rules:
        if rule[0] in beliefs and rule[1] in beliefs:
            continue
        elif rule[0] in beliefs:
            return rule
    return None

def forward_chain(beliefs, rules):
    """
    beliefs: a SET of strings
    rules: a list of 2ples

    return: a 2ple of new beliefs and rules
    """
    origSize = len(beliefs)
    # told to be non-destructive
    beliefs = beliefs.copy()
    b = get_triggered_rule(beliefs, rules)
    if b:
        beliefs.add(b[1])
    if len(beliefs) > origSize:
        return forward_chain(beliefs, rules)
    else:
        return (beliefs, rules)
