def read(filename, className):
    itemList = {}
    with open(filename) as f:
        f.readline() # skip first line
        line = f.readline()
        while line:
            values = line.split(',')
            item = className(values)
            itemList[int(values[0])] = item
            line = f.readline()
    f.close()

    return itemList
