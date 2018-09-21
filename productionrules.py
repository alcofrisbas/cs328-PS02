"""
Homework 2 problem 2
Forward Production

Ben Green and Quinn Schiller

Anna Rafferty CS328 -- 21 September 2018
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
    # told to be non-destructive, so shallow copy is made
    beliefs = beliefs.copy()
    b = get_triggered_rule(beliefs, rules)
    if b:
        beliefs.add(b[1])
    if len(beliefs) > origSize:
        return forward_chain(beliefs, rules)
    else:
        return (beliefs, rules)

def backward_chain(beliefs, rules, goal):
    """
    beliefs: a SET of strings
    rules: a list of string 2ples
    goal: a string

    return whether or not the goal can be proven given the
    set of beliefs and rules
    """

    """
    look at goal. Find a set of rules that have the goal as the consequent
    are those in beliefs? if yes return return true
    else: evaluate the rules with consequents as goals, using their
    antecedents as new goals...
    
    """
    if goal in beliefs:
        return True
    l = []
    b = beliefs.copy()
    for rule in rules:
        if rule[1] == goal:
            return backward_chain(b, rules, rule[0])
    return False


