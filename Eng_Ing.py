import sys
for i in range(1,100):
    try:
        Verb = sys.argv[i]
    except IndexError:
        break
    if Verb[(len(Verb)-2):(len(Verb))] == "ie":
        NewVerb = Verb[0:len(Verb)-2] + "ying"
        print(NewVerb)
    elif Verb[(len(Verb)-1):(len(Verb))] == "e":
        NewVerb = Verb[0:len(Verb)-1] + "ing"
        print(NewVerb)
    else:
        NewVerb = Verb + "ing"
        print(NewVerb)
    