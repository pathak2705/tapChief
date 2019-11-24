def search(labelselect,data,inverted_index):
    # len(dict)
    # len(inverted_index)
    # inverted_index
    # data
    query = labelselect
    res = inverted_index[inverted_index["words"] == query]["doc_id,freq"].values
    res[0]

    # k=[[[1,2],[3,4]]]
    # if(k[0][0][1]>k[0][1][1]):
    #     k[0][0],k[0][1]=k[0][1],k[0][0]
    # k
    c = 0
    for i in range(len(res[0])):
        if (c == 10):
            break
        for j in range(0, len(res[0]) - i - 1):
            if (res[0][j][1] > res[0][j + 1][1]):
                res[0][j], res[0][j + 1] = res[0][j + 1], res[0][j]
        c += 1
    data
    if (len(res[0]) >= 10):
        res = res[0][-1:-11:-1]
    else:
        res=res[0]

    l=[]
    for i, j in res:
        l.append(data[data["index"] == i]["question"].values[0])

    return l