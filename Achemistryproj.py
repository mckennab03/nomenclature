#naming basic organic molecules by IUPAC rules
# Hi, McKenna! It's Dr. Eicholtz. :)
def main():
    #add a title/intro or something 

    ringorchain=input("Does your molecule contain a ring (r) or a chain (c)?" ) # find how long the parent chain is
    if ringorchain== "c": #if the chain find the parentname
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
    elif ringorchain== "r": #if it's a ring find the size of the ring
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
        mainname=("cyclo"+parentname) #if it's a ring the cyclo goes beforehand

        
#keep potential parts of the name as empty strings to add together later 
    prefixes=('') 
    sub=("")
    suffix=("")
    carbon_prefix=('')
    halide_subname=("")
    halide_prefix=('')
    alcohol_suffix=('')
    aretheresub=input("are there substituents? (y/n): " ) 
    if aretheresub == "y":  
        howmanysub=int(input("How many substituents?: "))
        for i in range(howmanysub):  #loop through and ask about each substituent
            whereonthechain=(input("What number carbon (of the parent chain) is this substituent located on?: "))
            isitcarbon=input("Is this substituent consistented of carbons? (y/n): ")
            if isitcarbon[0]== "y": #if its a carbon substituent
                howmanycarbons=int(input("How many carbons are a part of substituent?: "))
                if howmanycarbons == 1:
                    subname= "methyl"
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

                if howmanysub>1:
                    prefixes+= (whereonthechain +',')
                    #okay so prefixes here work by making the comma separated list 
                    #i still  need to make it so it says something like (1,2-methyl-3-ethyl)
                    #instead of (1,2,3-methylethyl)
                    sub+=subname
                    carbon_prefix=(prefixes+'-'+sub)


            elif isitcarbon[0]=="n":
                is_there_a_halide=input("Does the substituent contain a halide? (y/n) ")
                if is_there_a_halide=="y": #if its a halide substituent
                    whichhalide=input("Select which one: Fluorine (F), Chlorine (Cl), Bromine (Br), Iodine (I)")
                    if whichhalide=="F":
                        halide_subname = "fluoro"
                    if whichhalide=="Cl":
                        halide_subname = "chloro"
                    if whichhalide=="Br":
                        halide_subname = "bromo"
                    if whichhalide=="I":
                        halide_subname = "iodo"
                    halide_prefix=(whereonthechain+"-"+halide_subname+"-")
                    # if howmanysub>1:
                    #     halide_prefix+=(halide_prefix+"-")
                    #needed to do something similar as to earlier but might just need to figure out a new order for coding all of this


                elif is_there_a_halide=="n":
                    is_there_an_alc=input("Does the substituent contain an OH group? (y/n) ") #if its an alcohol substituent 
                    if is_there_an_alc=="y":
                        alcohol_suffix = ("-"+whereonthechain+"-ol")

                
                 


    
    dbbonds=input("are there any double bonds on the molecule? (y/n): ") #ask if there's double bonds
    tpbonds=input("are there any triple bonds on the molecule? (y/n): ") #ask if there's triple bond
    if dbbonds == "y":
        dbhowmany=int(input("How many double bonds?"))
        if dbhowmany>1:
            prefixes_dbwhere = ''  # initialize the string for double bond locations
            for i in range(dbhowmany):
                dbwhere=input("What carbon is this double bond located on?")
                prefixes_dbwhere += dbwhere + ',' #okay so this doesnt work 
            db=('-'+prefixes_dbwhere+'-ene')
            mainname=(mainname+db)
        else:
            db=("-"+dbwhere+"-ene")
            mainname=(mainname+db)
     #need to ask where
    if tpbonds == "y":
        tphowmany=int(input("how many triple bonds?"))
        if tphowmany>1:
            for i in range(tphowmany):
                tpwhere=input("What carbon is the triple bond located on?")
                prefixes_tpwhere=(tpwhere+',') #this also doesnt work
            tp=('-'+prefixes_tpwhere+'-yl')
            mainname=(mainname+tp)
        else:
            tp=("-"+tpwhere+"-yl")
            mainname=(mainname+tp)

    else: #if it's just single bonds
        sb="ane"
        mainname=(mainname+sb)

    print(halide_prefix,carbon_prefix,mainname,alcohol_suffix, sep="")
                
                
if __name__ == "__main__":
    main()