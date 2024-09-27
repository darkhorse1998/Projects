def classValidator(func):
    def wrapper(*args):
        name = args[1]
        regime = args[2]
        if(type(name) is not str):
            raise TypeError("Name should be string")
        if(type(regime) is not str):
            raise TypeError("Regime should be string")
        
        if(regime.lower() == "old" or regime.lower() == "new"):
            pass
        else:
            raise Exception("Regime can either be 'new' or 'old'")
        return func(*args)
    return wrapper