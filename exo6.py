##Exo 6
def Res (r1,r2, u1, u2):

    if not isinstance(r1, int):
        raise ValueError("r1 doit être un entier")
    if not isinstance(r2, int):
       raise ValueError("r2 doit être un entier")
    if not isinstance(u1, str):
        raise ValueError("u1 doit être une chaine de caractére")
    if not isinstance(u2, str):
        raise ValueError("u2 doit être une chane de caractére")
    conversion={"m\u2126":1e-3, "\u2126":1, "k\u2126":1e3}
    if u1!="k\u2126":
        r1=r1*conversion[u1]
    if u2!="k\u2126":
        r2=r2*conversion[u2]
    Reserie=r1 + r2
    Reparallele=1/(1/r1 + 1/r2)
    Resultat={"Reserie":Reserie, "Reparallele":Reparallele}
    return Resultat

P=Res(14,20, "k\u2126", "m\u2126")
print(P)

    
    




