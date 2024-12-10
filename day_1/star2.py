# open and read file, append data from file into 2 lists
def read_numbers_from_file(list1, list2):
    with open("input.txt", "r") as file:
        for line in file:
            x, y = line.strip().split()
            list1.append(int(x))
            list2.append(int(y))

def main():
    list1 = []
    list2 = []
    simlist = []
    scorelist = []
    similarity = 0
    totalsim = 0
    read_numbers_from_file(list1, list2)

    for i in list1: #iterate through each row in list1
        for j in list2: # iterate through list 2 per row
            if i == j: # compare list1 to list2
                similarity += 1 # add 1 to similarity per match
        simlist.append(similarity) # appends similarity to simlist
        similarity = 0 # reset similarity for next iteration of list1
    
    for x,y in zip(list1, simlist): # iterate through both lists
        scorelist.append(x*y) # append product of each comparison

    for i in scorelist: # iterate through scorelist
        totalsim += i #calulate sum of list (total similarity score)

    print("The similarity score is: ", totalsim)

main()

