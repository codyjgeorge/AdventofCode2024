def read_numbers_from_file(matrix):
    with open("testinput.txt", "r") as file:
        for line in file:
            report = line.strip().split()
            matrix.append(report)
            

def main():
    matrix = []
    issafe = True
    read_numbers_from_file(matrix)

    for line in matrix:
        report = line
        report = [int(i) for i in report]   
        print(report)
        for i in report:
            if report[i] < report[i+1]:
                print("increasing")
            else:
                print("unsafe")
        report = []
main()
