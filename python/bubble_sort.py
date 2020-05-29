
def bubble_sort(alist):
    for i in range(0,len(alist)-1):  # i表示每次迭代的最后一个用于比较的位置， 从0到句长-1
        for j in range(len(alist)-1, i, -1):  # j表示每次迭代中所有的比较位置，从最后一个元素开始
            if(alist[j]<alist[j-1]):
                tmp = alist[j]
                alist[j] = alist[j-1]
                alist[j-1] = tmp

if __name__ == "__main__":
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    bubble_sort(alist)
    print(alist)