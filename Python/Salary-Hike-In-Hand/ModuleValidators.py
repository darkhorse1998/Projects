def classValidator(func):
    def wrapper(*args):
        name = args[0]
        regime = args[1]
        income = args[2]

        if(type(name) is not str):
            raise TypeError("Name should be string")
        if(type(regime) is not str):
            raise TypeError("Regime should be string")
        
        if(type(income) is int):
            pass
        else:
            raise TypeError("Income should be integer")
        
        if(income < 0):
            raise Exception(f"Expected income greater than 0. Received: {income}")
        
        if(regime.lower() == "old" or regime.lower() == "new"):
            pass
        else:
            raise Exception(f"Expected 'new' or 'old' for regime. Received: {regime}")
        return func(*args)
    
    return wrapper