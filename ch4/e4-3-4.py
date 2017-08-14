#e4-3-4
numHeads = 35 
numLegs = 94
for  numChickens in  range ( 0,numHeads + 1)  :
    numRabbits = numHeads - numChickens
    if 2 * numChickens + 4 * numRabbits ==  numLegs: 
        print ( " numChickens : " ,numChickens) 
        print( " numRabbits: " ,numRabbits)
