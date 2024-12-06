# open the file and read the lines
def read_numbers_from_file(list1, list2):
    with open("testinput.txt", "r") as file:
        for line in file:
            x, y = line.strip().split()
            list1.append(int(x))
            list2.append(int(y))

    list1.sort()
    list2.sort()


def main():
    list1 = []
    list2 = []
    read_numbers_from_file(list1, list2)
    # manipulate the list
    print(list1, list2)


if __name__ == "__main__":
    main()
