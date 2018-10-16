
def insertion_sort(items):
    length =len(items)
    for i in range(length, 0, -1):
        for j in range(1,length):
            if items[j] < items[j-1]:
                items[j],items[j-1]=items[j-1],items[j]

    return items


if __name__ == 'main':

unsorted_list = [ 5,4,6,7,8,4,3,2,3,4,5,6]
print(insertion_sort(unsorted_list))

