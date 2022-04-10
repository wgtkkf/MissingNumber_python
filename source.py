# Last updated: April 10 2022
# version 2
import numpy as np
import time

start = time.time()

# function: begin
def begin():
    print ("begin")
    return 0

# function: end
def end():
    print ("end")
    return 0

# list information
def list_information(arg_lst):
    print("Original: " + str(arg_lst))
    print("Table length: " + str(len(arg_lst)))
    return 0

# liner sort
def lsort(arg_lst):
    for i in range(0, len(arg_lst)):
        for j in range(i+1, len(arg_lst)):
            if arg_lst[i] > arg_lst[j]:
                temp = arg_lst[i]
                arg_lst[i] = arg_lst[j]
                arg_lst[j] = temp

    print("Sorted: " + str(arg_lst))

    return arg_lst

# check missing number
def mcheck(arg_lst):
    check = max(arg_lst) # after sorting

    if check == (np.int64(len(arg_lst))-1):
        print("You are missing: " + str(check+1))
    else:
        counter = 0
        check = min(arg_lst)
        while counter < len(arg_lst):
            if check == arg_lst[counter]:
                check += 1
                counter += 1
            elif check != arg_lst[counter]:
                print("Missing number is: " + str(counter))
                break
    return 0

def main():
    # main start
    begin()

    # input
    #lst = [3,0,1]
    #lst = [0,1]
    lst = [9,6,4,2,3,5,7,0,1]

    # display information
    list_information(lst)

    # liner sorting
    sorted = lsort(lst) # sorted is a sortd list of "lst" above

    # check missing number
    mcheck(sorted)

    # main end
    end()

    # time display
    elapsed_time = time.time()-start
    print("elapsed_time:{:.2f}".format(elapsed_time) + "[sec]")

if __name__ == '__main__':
    main()
