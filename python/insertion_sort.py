
def insertion_sort(alist):
    for i in range(0, len(alist)-1):
        index = i
        min = alist[i]
        for j in range(i+1, len(alist)):
            if alist[j] < min:
                index = j
                min = alist[j]
        if index != i:
            tmp = alist[i]
            alist[i] = alist[index]
            alist[index] = tmp
        
if __name__ == "__main__":
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insertion_sort(alist)
    print(alist)