def seq_search(arr, ele):

    pos = 0
    found = False

    while pos < len(arr) and not found:
        if arr[pos] == ele:
            found = True
        else:
            pos += 1

    return found


def seq_search_2(arr, ele):

    for num in arr:
        if num == ele:
            return True

    return False


def ordered_seq_search(arr, ele):

    pos = 0
    found = False
    stopped = False

    while pos < len(arr) and not found and not stopped:
        if arr[pos] == ele:
            found = True
        else:
            if arr[pos] > ele:
                stopped = True
            else:
                pos += 1

    return found


def ordered_seq_search2(arr, ele):

    for num in arr:
        if num > ele:
            return False
        if num == ele:
            return True

    return False
