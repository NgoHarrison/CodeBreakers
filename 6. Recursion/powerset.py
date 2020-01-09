def powerset(array):
    powerset = [[]]
    for elem in array:
        for i in range(len(array)):
            sub = powerset[i]
            powerset.append(sub+[elem])
    return powerset

                   
