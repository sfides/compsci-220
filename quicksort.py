import random
import time
random.seed(67)
def partition1(a_list):#####pivot is first element
    pivot = a_list[0]
    smaller, larger = [], []
    for x in a_list[1:]:
        if x < pivot:
            smaller.append(x)
        else:
            larger.append(x)
    return smaller, [pivot], larger

def partition2(a_list):#####pivot is random element
    rand_num = random.randint(0,len(a_list)-1)
    pivot = a_list[rand_num]
    smaller, larger = [], []
    for x in a_list[1:]:
        if x < pivot:
            smaller.append(x)
        else:
            larger.append(x)
    return smaller, [pivot], larger


def partition3(a_list):#####pivot is median of 3 random elements from the input a_list
    find_median1 = []
    for i in range(3):
        find_median1.append(a_list[random.randint(0,len(a_list)-1)])
    find_median1.sort()
    pivot = find_median1[1]
    smaller, larger = [], []
    for x in a_list[1:]:
        if x < pivot:
            smaller.append(x)
        else:
            larger.append(x)
    return smaller, [pivot], larger

def partition4(a_list):#####pivot is median of 5 random elements from the input a_list
    find_median2 = []
    for i in range(5):
        find_median2.append(a_list[random.randint(0,len(a_list)-1)])
    find_median2.sort()
    pivot = find_median2[2]
    smaller, larger = [], []
    for x in a_list[1:]:
        if x < pivot:
            smaller.append(x)
        else:
            larger.append(x)
    return smaller, [pivot], larger

def partition5(a_list):#####pivot is median of 7 random elements from the input a_list
    find_median3 = []
    for i in range(7):
        find_median3.append(a_list[random.randint(0,len(a_list)-1)])
    find_median3.sort()
    pivot = find_median3[3]
    smaller, larger = [], []
    for x in a_list[1:]:
        if x < pivot:
            smaller.append(x)
        else:
            larger.append(x)
    return smaller, [pivot], larger

def quicksort(a_list):
    if len(a_list) <= 1: return a_list
    smaller, equal, larger = partition5(a_list)
    smaller = quicksort(smaller)
    larger = quicksort(larger)
    return smaller + equal + larger

###ordered elements from 0 - 5527092
def ordered_list(ID):
    a_list = [j for j in range(0,ID)]
    return quicksort(a_list)
###random elements from 0 - 5527092
def rand_list(ID):
    n = ID - 1
    a_list = []
    for k in range(0, ID):
        a_list.append(random.randint(0,n))
    return quicksort(a_list)

ID = 5527093
start_time = time.perf_counter()
print(rand_list(ID))
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Execuion time: {elapsed_time:.4f} seconds")
