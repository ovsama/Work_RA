


def FCFA_calculator(Euro) :
    
    "This function converts Euros to FCFA"
    FCFA1 = 655.957*Euro
    FCFA2 = round(FCFA1,2)
    
    return print(FCFA2,"Francs CFA")

FCFA_calculator(28)
