itemLists = [[2,3,4,5],[1,4,7],[1,3,4,6]]

for each in itemLists:
    list_a = itemLists[each]
    list_b = itemLists[each+1]
    i=0
    unmatched = True
    while unmatched:
        if list_a[each+i] < list_b[each]:
            i+=1
        else:
            list_a[each+i].append(list_b[each])
            unmatched = False


