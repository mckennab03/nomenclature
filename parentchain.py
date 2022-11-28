#naming alkanes by parent chain (no sub)

def main():
    print("A parent chain is the longest chain of carbons in a molecule.")
    chain = int(input("How many carbons long is the parent chain of your molecule?" ))
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
    # name=(parentname+"ane")
    # print("The name is: ", name)
    
if __name__ == "__main__":
    main()