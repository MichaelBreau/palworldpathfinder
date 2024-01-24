"""Module for parsing the data required for breeding combination calculations"""

def parse_exceptions(path):
    """Function for parsing exceptions file for combinations that are 
    hardcoded by the palworld developers because they are mean"""

    exceptions_dictionary = {}
    with open(path, 'r') as file:
        for line in file:
            pals = line.split("|")
            exceptions_dictionary[{pals[0], pals[1]}] = pals[2]
    
    print(exceptions_dictionary[{"Incineram", "Maraith"}])

parse_exceptions('exceptions.txt')
