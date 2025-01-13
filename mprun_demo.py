def sum_of_list(N) :
    total =0 
    for i in range(5) : 
        L = [j^ (j >> 1) for j in range (N)] 
        total += sum(L)
        del L ##Remove Ref to L
    return total    