l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
lnew = []
def flatten(liste):
    for i in liste:
        if isinstance(i, list): #Check if i in liste is a list or not
            flatten(i) #If true, run i in function again
        else:
            lnew.append(i) #If false, append i in l.new as was flatten
    return lnew

flatten(l)