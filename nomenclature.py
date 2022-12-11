#naming basic organic molecules by IUPAC rules

def main():
    print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
    print("\nLet's Name a Molecule!")

    while True:
        ringorchain=input("\nDoes your molecule contain a ring (r) or a chain (c)? " ) # find how long the parent chain is
        if ringorchain== "c": #if the chain find the parentname
            while True:
                try:
                    chain = int(input("How many carbons long is the parent chain of your molecule?  " ))
                except ValueError:
                    print("Sorry, I can't perform this function. Please try again.")
                    continue
                else:
                    mainname=parentname(chain)
                    break
                    
            break
        elif ringorchain== "r": #if it's a ring find the size of the ring
            while True:
                try:
                    ring = int(input("How many carbons long is the ring in your molecule?: " ))
                except ValueError:
                    print("Sorry, I can't perform this function. Please try again.")
                    continue
                else:
                    mainname=("cyclo"+parentname(ring)) #if it's a ring the cyclo goes beforehand
                    break
                
            break
        else:
            print("That's not a valid option. Please try again.")
            continue

    while True:
        dbbonds=input("\nAre there any double bonds on the molecule? (y/n): ") #ask if there's double bonds
        if dbbonds == "y":
            while True:
                try:
                    dbhowmany=int(input("How many double bonds? "))+1
                except ValueError:
                    print("That's not a valid option. Please try again.")
                    continue
                else:
                    if dbhowmany>1:
                        prefixes_dbwhere = ''  # initialize the string for double bond locations
                        for i in range(1,dbhowmany):
                            dbwhere=input("What carbon is double bond {} located on? ".format(i))
                            prefixes_dbwhere += dbwhere+','  
                        db=('-'+prefixes_dbwhere+'-en')
                        mainname=(mainname+db)
                    else:
                        dbwhere=input("What carbon is the double bond located on? ")
                        db=("-"+dbwhere+"-en")
                        mainname=(mainname+db)
                    break
            break
        elif dbbonds == 'n':
            break
        else:
            print("That's not a valid option. Please try again.")
            continue

    while True:    
        tpbonds=input("\nAre there any triple bonds on the molecule? (y/n): ") #ask if there's triple bond
        if tpbonds == "y":
            while True:
                try:
                    tphowmany=int(input("How many triple bonds? "))+1
                except ValueError:
                    print("That's not a valid option. Please try again.")
                    continue
                else:
                    if tphowmany>1:
                        prefixes_tpwhere = '' #initialize the string for triple bond locations
                        for i in range(1,tphowmany):
                            tpwhere=input("What carbon is triple bond {} located on? ".format(i))
                            prefixes_tpwhere=(tpwhere+',') 
                        tp=('-'+prefixes_tpwhere+'-yl')
                        mainname=(mainname+tp)
                    else:
                        tpwhere=input("What carbon is the triple bond located on? ")
                        tp=("-"+tpwhere+"-yl")
                        mainname=(mainname+tp)
                    break
            break
        elif tpbonds == 'n':
            break
        else:
            print("That's not a valid option. Please try again.")
            continue


    #keep potential parts of the name as empty strings to add together later 
    prefixes=('') 
    count_Hsubs={}
    count_subs={}
    substit=("")
    subname=''
    carbon_prefix=('')
    halide_subname=("")
    halide_prefix=('')
    alcohol_suffix=('')
    is_there_an_alc=''

    while True:
        aretheresub=input("\nAre there substituents? (y/n): " ) 
        if aretheresub == "y":
            listofsubnames=[]
            while True:
                try:  
                    # listofsubnames=[]
                    howmanysub=int(input("How many substituents?: "))+1
                except ValueError:
                    print("That's not a valid option. Please try again.")
                    continue
                else:
                    for i in range(1,howmanysub):  #loop through and ask about each substituent
                        while True:
                            isitcarbon=input("\nIs substituent {} consistented of carbons? (y/n): ".format(i))
                            if isitcarbon[0]== "y": #if its a carbon substituent
                                howmanycarbons=int(input("How many carbons make up the substituent?: "))
                                subname= substituentname(howmanycarbons)
                                print("This is a {} group!".format(subname))
                                
                                listofsubnames.append(subname) #make a list of all of the substituents 

                                count_subs={}
                                #initialize a dictionary for amount
                                for i in listofsubnames: #count how many of each substituent 
                                    if not i in count_subs:
                                        count_subs[i]=1
                                    
                                    else:
                                        count_subs[i] +=1
                                break
                            elif isitcarbon[0]=="n":
                                halidelistofsubnames=[]
                                while True:
                                    is_there_a_halide=input("\nDoes substituent {} contain a halide? (y/n) ".format(i))
                                    if is_there_a_halide=="y": #if its a halide substituent
                                        whichhalide=input("Select which one: Fluorine (F), Chlorine (Cl), Bromine (Br), Iodine (I) ")
                                        if whichhalide=="F":
                                            halide_subname = "fluoro"
                                        if whichhalide=="Cl":
                                            halide_subname = "chloro"
                                        if whichhalide=="Br":
                                            halide_subname = "bromo"
                                        if whichhalide=="I":
                                            halide_subname = "iodo"

                                        halidelistofsubnames.append(halide_subname)

                                        count_Hsubs={}
                                        #initialize a dictionary for amount
                                        for i in halidelistofsubnames: #count how many of each substituent 
                                            if not i in count_Hsubs:
                                                count_Hsubs[i]=1
                                            
                                            else:
                                                count_Hsubs[i] +=1
                                    
                                        break
                                    elif is_there_a_halide=="n":
                                        while True:
                                            is_there_an_alc=input("\nDoes substituent {} contain an OH group? (y/n) ".format(i)) #if its an alcohol substituent 
                                            if is_there_an_alc=="y":
                                                whereonthechain=(input("What number carbon of the parent chain is the OH group located on?: "))
                                                alcohol_suffix = ("-"+whereonthechain+"-ol")
                                                mainname=mainname+alcohol_suffix
                                                break
                                            elif is_there_an_alc=='n':
                                                print("Sorry, this molecule will have to be named without this substituent for now.")
                                                break
                                            else:
                                                print("That's not a valid option. Please try again.")
                                                continue
                                        break
                                    else:
                                        print("That's not a valid option. Please try again.")
                                        continue
                                break    
                            else:
                                print("That's not a valid option. Please try again.")
                                continue   
                    break
        elif aretheresub=='n':
            break
        else:
            print("That's not a valid option. Please try again.")
            continue                                    
        break
    if count_subs:
        for key, value in count_subs.items():
            if value==1:
                prefixes=''
                substit=''
                substit +=key
                whereonthechain=(input("\nWhat number carbon of the parent chain is the {} group located on?: ".format(key)))
                prefixes+= (whereonthechain)
                carbon_prefix+=('-'+prefixes+'-'+substit)
            if value ==2:
                prefixes=''
                substit=''
                substit += "di"+key
                whereonthechain=(input("\nWhat number carbons of the parent chain are the {} groups located on? (separate by comma): ".format(key)))
                prefixes+= (whereonthechain)
                carbon_prefix+=('-'+prefixes+'-'+substit)
            if value==3:
                prefixes=''
                substit=''
                substit +="tri"+key
                whereonthechain=(input("\nWhat number carbons of the parent chain are the {} groups located on? (separate by comma): ".format(key)))
                prefixes+= (whereonthechain)
                carbon_prefix+=('-'+prefixes+'-'+substit)
            

    if count_Hsubs:
        
        for key, value in count_Hsubs.items():
            if value==1:
                prefixes=''
                substit=''
                substit +=key
                whereonthechain=(input("\nWhat number carbon of the parent chain is the {} group located on?: ".format(key)))
                prefixes+= (whereonthechain)
                halide_prefix+=('-'+prefixes+'-'+substit)
            if value ==2:
                prefixes=''
                substit=''
                substit += "di"+key
                whereonthechain=(input("\nWhat number carbons of the parent chain are the {} groups located on? (separate by comma): ".format(key)))
                prefixes+= (whereonthechain)
                halide_prefix+=(prefixes+'-'+substit)
            if value==3:
                prefixes=''
                substit=''
                substit +="tri"+key
                whereonthechain=(input("\nWhat number carbons of the parent chain are the {} groups located on? (separate by comma): ".format(key)))
                prefixes+= (whereonthechain)
                halide_prefix+=(prefixes+'-'+substit)
            
    if tpbonds and dbbonds != "y":
        sb="an"
        mainname=(mainname+sb)
        if is_there_an_alc != "y": #if it's just single bonds
            sbe="e"
            mainname=(mainname+sbe)     
           

    print("\nThe name of the molecule is...")
    print(carbon_prefix[1:],halide_prefix,mainname,sep="")
    
def parentname(x): #function for naming parent
    if x == 1:
        parentname= "Meth"
    if x == 2:
        parentname="eth"
    if x == 3:
        parentname="prop"
    if x == 4:
        parentname="but" 
    if x == 5:
        parentname="pent" 
    if x == 6:
        parentname="hex" 
    if x == 7:
        parentname="hept" 
    if x == 8:
        parentname="oct" 
    if x == 9:
        parentname="non" 
    if x==10:
        parentname="dec" 
    if x==11:
        parentname="undec" 
    if x==12:
        parentname="dodec" 
    if x==13:
        parentname="tridec"
    if x==14:
        parentname="tetradec"
    if x==15:
        parentname="pentadec"
    if x==16:
        parentname="hexadec"
    if x==17:
        parentname="heptadec"
    if x==18:
        parentname="octadec"
    if x==19:
        parentname="nonadec"
    if x==20:
        parentname="icos"
    return parentname 

def substituentname(x): #function for naming substit
    if x == 1:
        subname= "Methyl"
    if x == 2:
        subname="ethyl"
    if x == 3:
        subname="propyl"
    if x == 4:
        subname="butyl" 
    if x == 5:
        subname="pentyl" 
    if x == 6:
        subname="hexyl" 
    if x == 7:
        subname="heptyl" 
    if x == 8:
        subname="octyl" 
    if x == 9:
        subname="nonyl" 
    if x==10:
        subname="decyl" 
    if x==11:
        subname="undecyl" 
    if x==12:
        subname="dodecyl" 
    if x==13:
        subname="tridecyl"
    if x==14:
        subname="tetradecyl"
    if x==15:
        subname="pentadecyl"
    if x==16:
        subname="hexadecyl"
    if x==17:
        subname="heptadecyl"
    if x==18:
        subname="octadecyl"
    if x==19:
        subname="nonadecyl"
    if x==20:
        subname="icosyl"
    return subname 




if __name__ == "__main__":
    main()