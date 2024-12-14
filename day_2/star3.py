def read_numbers_from_file(matrix):
    with open("input.txt", "r") as file:
        for line in file:
            report = line.strip().split()
            matrix.append(report)
            

def main():
    matrix = []
    is_Safe = False
    unsafe = 0
    safe = 0
    read_numbers_from_file(matrix)

    for line in matrix:
        report = line
        report = [int(i) for i in report] # changes each string number in report to int

        # checks if list is ascending or descneding
        if sorted(report) == report or sorted(report, reverse = True) == report:
            is_Safe = True
            while is_Safe == True:
                # search if sorted(safe) list is still safe by step
                for i in range(len(report) - 1):
                    difference = report[i] - report[i +1]
                    step = abs(difference) # finds step interval to adjacent number
                    if step < 1 or step > 3:
                        is_Safe = False
                        unsafe += 1
                        
                if is_Safe == True:
                    safe += 1
                    is_Safe = False

        else:
            unsafe += 1
        report = []

    print("Safe: ", safe)
    print("Unsafe: ", unsafe)
main()
