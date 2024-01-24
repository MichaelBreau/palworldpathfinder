"""Module for finding a path from an initial pal to a target pal"""
import fileparsers as parse


def breedingpathfinder(initial, target):
    """Function returns array of path from initial to target"""
    exceptdict = parse.parse_exceptions('exceptions.txt')
    valuesdict = parse.parse_values('palvalues.txt')

    parentvalueneeded = 2 * valuesdict[target] - valuesdict[initial]
    if (parentvalueneeded > 1500):
        parentvalueneeded = 1500
    elif (parentvalueneeded < 10):
        parentvalueneeded = 10

    parentneeded = min(valuesdict, key=lambda x: abs(valuesdict[x] - parentvalueneeded))
    
    currentbreedoutput = int((valuesdict[parentneeded] + valuesdict[initial])/2)
    breededpal = min(valuesdict, key=lambda x: abs(valuesdict[x] - currentbreedoutput))

    print(initial, "+" , parentneeded, "=" , breededpal)

    if (breededpal != target):
        return breedingpathfinder(breededpal, target)
    return breededpal

    


print(breedingpathfinder("Jetragon", "Lifmunk"))
