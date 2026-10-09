
example = [1, 4, 5, 8, 12, 23, 34, 41, 42, 59, 60, 61, 62, 63, 65, 68, 70, 80, 90, 99]


# return True if x in the list l.
def linear_search(x,l):
    for y in l:
        if y == x:
            return True
    return False

def binary_search(x,l):
    if len(l) == 0:
        return False
    else:
        middle_index = len(l) // 2
        left_part = l[:middle_index]
        right_part = l[middle_index+1:]
        # print("search: ", x, l, "middle=",middle_index, "l[middle]=", l[middle_index])
        if l[middle_index] == x:
            return True
        elif l[middle_index] < x:
            return binary_search(x,right_part)
        else: # l[middle_index] > x
            return binary_search(x,left_part)

assert not binary_search(40,example)
assert binary_search(61,example)
assert not binary_search(100,example)
