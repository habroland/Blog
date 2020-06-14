def equivSingleLens_2lenses(f1,d12,f2):
    """ Calculates the equivalent single-lens system for an array of two lenses
    
    Arguments:
    f1: Focal length of the first lens
    d12: Distance between the lenses
    f2: Focal length of second lens
    
    Returns:
    df: Front distance (towards f1)
    feff: Effective focal length
    db: Back distance (towards f2)
    
    """
    df = (d12*f1)/(f1+f2-d12)
    feff = (f2*f1)/(f1+f2-d12)
    db = (d12*f2)/(f1+f2-d12)
    
    return df, feff, db

def equivSingleLens(fls,ds):
    """ Calculates the equivalent single-lens system for an array of lenses
    
    Arguments:
    fls: List of N focal lengths
    ds: List of N-1 distances, each one between lenses fi and fi+1
    
    Returns: Dictionary
    df: Front distance (towards f1)
    feff: Effective focal length
    db: Back distance (towards f2)
    
    """
    assert(len(fls) == len(ds)+1)
    
    df = 0
    feff = fls[0]
    db = 0
    for i in range(len(ds)):
        df_temp, feff, db = equivSingleLens_2lenses(feff,db+ds[i],fls[i+1])
        print(feff)
        df+=df_temp
    
    return {"df":df, "feff":feff,"db":db}