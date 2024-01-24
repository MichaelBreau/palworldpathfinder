"""Module for parsing the data required for breeding combination calculations"""

def parse_exceptions(path):
    """Function for parsing exceptions file for combinations that are 
    hardcoded by the palworld developers because they are mean"""

    exceptions_dictionary = {}
    with open(path, 'r') as file:
        for line in file:
            line = line.rstrip()
            pals = line.split("|")
            parents = [pals[0], pals[1]]
            parents.sort()
            parent_string = parents[0] + " " + parents[1]
            exceptions_dictionary[parent_string] = pals[2]
    
    return exceptions_dictionary

parse_exceptions('exceptions.txt')
