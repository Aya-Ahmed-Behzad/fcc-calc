import numpy as np
import ast

def calculate(list):
    
    Input= list
    
    try:
        z = np.array(Input)
        z= z.reshape(3,3)
        strmean= f"[{(z.mean(axis=0)).tolist()}, {(z.mean(axis=1)).tolist()}, {z.mean()}]"
        strvar= f"[{(z.var(axis=0)).tolist()}, {(z.var(axis=1)).tolist()}, {z.var()}]"
        strstd= f"[{(z.std(axis=0)).tolist()}, {(z.std(axis=1)).tolist()}, {z.std()}]"
        strmax= f"[{(z.max(axis=0)).tolist()}, {(z.max(axis=1)).tolist()}, {z.max()}]"
        strmin= f"[{(z.min(axis=0)).tolist()}, {(z.min(axis=1)).tolist()}, {z.min()}]"
        strsum= f"[{(z.sum(axis=0)).tolist()}, {(z.sum(axis=1)).tolist()}, {z.sum()}]"
    
        meanlist = ast.literal_eval(strmean)
        varlist = ast.literal_eval(strvar)
        maxlist = ast.literal_eval(strmax)
        minlist = ast.literal_eval(strmin)
        stdlist = ast.literal_eval(strstd)
        sumlist = ast.literal_eval(strsum)
        calculations={
                      'mean': meanlist,
                      'variance': varlist,
                      'standard deviation': stdlist,
                      'max': maxlist,
                      'min': minlist,
                      'sum': sumlist
                       }
                                  
    except:
        raise ValueError("List must contain nine numbers.")
    

    return calculations

