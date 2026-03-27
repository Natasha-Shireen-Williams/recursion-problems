def permutations(n):
    
    if len(n) == 0:
        return ['']
    hey = permutations(n[1:])
    result =[]
    for i in hey:
        for p in range(len(i)+1):
            perm = i[:p] +n[0] + i[p:]
            print(perm)
            result.append(perm)
        
    return result   

#print(permutations('abc'))  
