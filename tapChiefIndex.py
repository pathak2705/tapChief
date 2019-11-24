def indexing(data,dict):
    import pandas as pd
    from collections import defaultdict

    inverted_index = pd.DataFrame({"words": [], "doc_id,freq": []})
    for w in dict:
        for each in data["question"]:
            if w in each:
                if w in list(inverted_index["words"]):
                    inverted_index.loc[inverted_index[inverted_index["words"] == w].index.values[0]][
                        "doc_id,freq"].append([data[data["question"] == each]["index"].values[0], each.count(w)])
                else:
                    d = defaultdict()
                    d["words"] = w
                    d["doc_id,freq"] = [[data[data["question"] == each]["index"].values[0], each.count(w)]]
                    inverted_index = inverted_index.append(d, ignore_index=True)
    return inverted_index
