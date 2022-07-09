a = [21, -13, 45, 3, 15, -0.73]
b = [1, 92, 34, 48, 17, -3, 15, 59, 46, 78, 0, 11]
c = [3, 21, 21, 45, 3, 45, 3, 10, 3, 10, 174, 38]


def sorting(list_to_sort):
    """
 Function to sort the list using bubbleSort method
 """
    for i in range(0, len(list_to_sort) - 1, 1):
        for j in range(0, len(list_to_sort) - i - 1, 1):
            if list_to_sort[j] > list_to_sort[j + 1]:
                list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j + 1], list_to_sort[j]
    return list_to_sort


def search(list_to_search, element, i=0):
    """
 Function to find the element by its value in the list.
 """
    list_to_search.append(element)
    while list_to_search[i] != element:
        i = i + 1
    if i == len(list_to_search) - 1:
        print('There is no such element -', element, 'in the list')
        list_to_search.pop()
    else:
        print('Index of element', element, 'is', i)


def seq_search(list_to_search, *args):
    """
 Function to find the sequence of elements in the list
 """
    for j in range(0, len(args), 1):
        search(list_to_search, list(args)[j], 0)


def min_five(list_to_search):
    """
 Function to find first five minimal elements in the list.
 If length of the list is less than five, n-1 elements will be returned.
 """
    if len(list_to_search) < 5:
        print('Size of list is less than five\n'
              'n-1 min elements will be searched')
        sorting(list_to_search)
        return list_to_search[:len(list_to_search) - 1]
    else:
        sorting(list_to_search)
        return list_to_search[:5]


def max_five(list_to_search):
    """
 Function to find first five maximal elements in the list.
 If length of the list is less than five, n-1 elements will be returned.
 """
    if len(list_to_search) < 5:
        print('Size of list is less than five\n'
              'n-1 max elements will be searched')
        sorting(list_to_search)
        return list_to_search[len(list_to_search) - 1:0:-1]
    elif len(list_to_search) == 5:
        sorting(list_to_search).reverse()
        return list_to_search
    else:
        sorting(list_to_search)
        return list_to_search[len(list_to_search):len(list_to_search) - 6:-1]


def ar_mean(*args):
    """
 Function to find the arithmetical mean of values.
 """
    return sum(list(args)) / len(list(args))


def remove_same(list1):
    """
 Function to remove the duplicates from the list.
 """
    list1 = list(set(list1))
    return list1


def welcome():
    name = input('Enter your name: ')
    print('Hello,', name)


if __name__ == '__main__':
    print('Initial list:', a)
    print('Sorted list:', sorting(a))
    print('\nNext list to be searched in:', b)
    search(b, 17)
    seq_search(b, 32, 11, 192, 0)
    print('\nNext list to search 5 min and 5 max elements in:', c)
    print(min_five(c))
    print(max_five(c))
    print('\nArithmetical mean of elements entered:', ar_mean(132, 39, 218, 2911))
    print('List to remove duplicates in: ', c)
    print('List with no same elements:', remove_same(c))
