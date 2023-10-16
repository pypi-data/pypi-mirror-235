def Unique(a):
    li = []
    for i in a:
        if i not in li:
            li.append(i)
    return li