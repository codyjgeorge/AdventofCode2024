# open the file and read the lines
def read_numbers_from_file(list1, list2):
    with open("input.txt", "r") as file:
        for line in file:
            x, y = line.strip().split()
            list1.append(int(x))
            list2.append(int(y))
    # sort each list in ascending order
    list1.sort()
    list2.sort()

# define main function
def main():
    total = 0 
    list1 = []
    list2 = []
    read_numbers_from_file(list1, list2)

    # manipulate the list
    for i, j in zip(list1, list2):
       difference = i - j
       absval = abs(difference)
       total += absval
    else:
        print(total)

# call main function
main()
