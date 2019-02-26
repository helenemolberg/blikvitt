import numpy as np


def createObjList(adrList, coords, types):
        t = len(coords)
        matrix = [[0 for x in range(4)] for y in range(t)]
        np.array(matrix)
        #fyller inn i matrisen
        for i in range (t):
            matrix[i][0] = i +1 #id
            matrix[i][1] = coords[i]
            matrix[i][2] = adrList[i]
            matrix[i][3] = types[i]

        #print(matrix)
        return matrix


def filterRecycle(matrix, type):
    t = len(matrix)
    filtered = []
    for i in range(t):
        if matrix[i][3] == type:
            filtered.append(matrix[i][1])   # <-- koordinatene for riktig type
    print (filtered)
    return filtered


def main():
    adr =["Midtbypunkt, Abelsborgs gate, v/Kleists gate",
          "Midtbypunkt, Abelsborgs gate, v/Kleists gate",
          "Midtbypunkt, Anton Kalvaasgate, v/A.Buens gate",
          "Midtbypunkt, Anton Kalvaasgate, v/A.Buens gate",
          "Midtbypunkt, Anton Kalvaasgate, v/Biskop Sigurdsgt"]

    coords =[(63.42983445294848, 10.368214199539029),
            (63.42983445294848, 10.368214199539029),
            (63.439024006030465, 10.42835219928823),
            (63.439024006030465, 10.42835219928823),
            (63.437900534389016, 10.42435702576183)]

    types=  ["Papir",
             "Plastemballasje",
             "Papir",
             "Plastemballasje",
             "Glass- og metallemballasje"]

    m = createObjList(adr, coords, types)
    a = filterRecycle(m, "Papir")


    print(a)




main();
