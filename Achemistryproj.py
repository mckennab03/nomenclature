#naming alkanes by parent chain (no sub)

def main():
    name=[]
    # print("A parent chain is the longest chain of carbons in a molecule.")
    ringorchain=input("Does your molecule contain a ring (r) or a parent chain (c)?")
    if ringorchain== "c":
        chain = int(input("How many carbons long is the parent chain of your molecule?  " ))
        if chain == 1:
            parentname= "Meth"
        if chain == 2:
            parentname="eth"
        if chain == 3:
            parentname="prop"
        if chain == 4:
            parentname="but" 
        if chain == 5:
            parentname="pent" 
        if chain == 6:
            parentname="hex" 
        if chain == 7:
            parentname="hept" 
        if chain == 8:
            parentname="oct" 
        if chain == 9:
            parentname="non" 
        if chain==10:
            parentname="dec" 
        if chain==11:
            parentname="undec" 
        if chain==12:
            parentname="dodec" 
        if chain==13:
            parentname="tridec"
        if chain==14:
            parentname="tetradec"
        if chain==15:
            parentname="pentadec"
        if chain==16:
            parentname="hexadec"
        if chain==17:
            parentname="heptadec"
        if chain==18:
            parentname="octadec"
        if chain==19:
            parentname="nonadec"
        if chain==20:
            parentname="icos"
        mainname=(parentname)
    elif ringorchain== "r":
        ring = int(input("How many carbons long is the ring in your molecule?:  " ))
        if ring == 1:
            parentname= "Meth"
        if ring == 2:
            parentname="eth"
        if ring == 3:
            parentname="prop"
        if ring == 4:
            parentname="but" 
        if ring == 5:
            parentname="pent" 
        if ring == 6:
            parentname="hex" 
        if ring == 7:
            parentname="hept" 
        if ring == 8:
            parentname="oct" 
        if ring == 9:
            parentname="non" 
        if ring==10:
            parentname="dec" 
        if ring==11:
            parentname="undec" 
        if ring==12:
            parentname="dodec" 
        if ring==13:
            parentname="tridec"
        if ring==14:
            parentname="tetradec"
        if ring==15:
            parentname="pentadec"
        if ring==16:
            parentname="hexadec"
        if ring==17:
            parentname="heptadec"
        if ring==18:
            parentname="octadec"
        if ring==19:
            parentname="nonadec"
        if ring==20:
            parentname="icos"
        mainname=("cyclo"+parentname)
    # name=(parentname+"ane")
    # print("the name is: ", name)
        
# #name with substituents
    sub=("")
    aretheresub=input("are there substituents? (y/n): " )
    if aretheresub == "y":  
        howmanysub=int(input("How many substituents?: "))
        for i in range(howmanysub): 

#figure out how to update the substituents to make multiple 


            whereonthechain=(input("What number carbon (of the parent chain) is this substituent located on?: "))
            isitcarbon=input("Is this substituent consistented of only carbons? (y/n): ")
            if isitcarbon[0]== "y":
                howmanycarbons=int(input("How many carbons are a part of substituent?: "))
                if howmanycarbons == 1:
                    subname= "Methyl"
                if howmanycarbons == 2:
                    subname="ethyl"
                if howmanycarbons == 3:
                    subname="propyl"
                if howmanycarbons == 4:
                    subname="butyl" 
                if howmanycarbons == 5:
                    subname="pentyl" 
                if howmanycarbons == 6:
                    subname="hexyl" 
                if howmanycarbons == 7:
                    subname="heptyl" 
                if howmanycarbons == 8:
                    subname="octyl" 
                if howmanycarbons == 9:
                    subname="nonyl" 
                if howmanycarbons==10:
                    subname="decyl" 
                # if howmanycarbons==11:
                #     subname="undec" 
                # if howmanycarbons==12:
                #     subname="dodec" 
                # if howmanycarbons==13:
                #     subname="tridec"
                # if howmanycarbons==14:
                #     subname="tetradec"
                # if howmanycarbons==15:
                #     subname="pentadec"
                # if howmanycarbons==16:
                #     subname="hexadec"
                # if howmanycarbons==17:
                #     subname="heptadec"
                # if howmanycarbons==18:
                #     subname="octadec"
                # if howmanycarbons==19:
                #     subname="nonadec"
                # if howmanycarbons==20:
                #     subname="icos"
                # strwhere=str(whereonthechain)
                # subs=[strwhere+"-"+subname]
                # totalsub=[subs]
                # name=[totalsub+parentname+"ane"]
                sub=(whereonthechain+"-"+subname)
    
    dbbonds=input("are there any double bonds on the molecule? (y/n): ") #need to ask where
    tpbonds=input("are there any triple bonds on the molecule? (y/n): ")
    if dbbonds == "y":
        dbwhere=input("What carbon is the double bond located on?")
        db=(dbwhere+"-ene")
        mainname=(mainname+db)
     #need to ask where
    elif tpbonds == "y":
        tpwhere=input("What carbon is the triple bond located on?")
        tp=(tpwhere+"-yl")
        mainname=(mainname+tp)
    else:
        sb="ane"
        mainname=(mainname+sb)

    print(sub,mainname, sep="")
                
                
if __name__ == "__main__":
    main()