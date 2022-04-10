# Last updated: April 10 2022
# version 1
import numpy as np
import time

start = time.time()

# function: begin
def begin():
    print ("begin")

# function: end
def end():
    print ("end")

def main():
    # main start
    begin()

    # input
    #lst = [3,0,1]
    #lst = [0,1]
    lst = [9,6,4,2,3,5,7,0,1]

    print("Original: " + str(lst))
    print("Table length: " + str(len(lst)))

    # liner sorting
    for i in range(0, len(lst)):
        #print("i: " + str(i))
        for j in range(i+1, len(lst)):
            if lst[i] > lst[j]:
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
                #print(lst)
            #print("j: " + str(j))
    print("Sorted: " + str(lst))

    #
    check = max(lst) # after sorting
    if check == (np.int64(len(lst))-1):
        print("You are missing: " + str(check+1))
    else:
        counter = 0
        check = min(lst)
        while counter < len(lst):
            if check == lst[counter]:
                check += 1
                counter += 1
            elif check != lst[counter]:
                print("You are missing: " + str(counter))
                break
    end()

    # time display
    elapsed_time = time.time()-start
    print("elapsed_time:{:.2f}".format(elapsed_time) + "[sec]")

if __name__ == '__main__':
    main()
