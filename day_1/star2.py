# read and open file
def read_numbers_from_file(list1, list2):
    with open("testinput.txt", "r") as file:
        for line in file:
            x, y = line.strip().split()
            list1.append(int(x))
            list2.append(int(y))
        
        # sort in ascending order
        list1.sort()
        list2.sort()

def main():
    list1 = []
    list2 = []
    read_numbers_from_file(list1, list2)
    print(list1, list2)
        
    similarity = 0

    for i in list1:
        for j in list2:
            if i == j:
                similarity += 1
    
    print(similarity)

main()

