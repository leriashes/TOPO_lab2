
def SortAsc(params, seq, param_number):

    seq = seq.copy()

    n = len(seq)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if params[seq[j]][param_number] > params[seq[j + 1]][param_number]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]
    
    return seq

def SortDesc(params, seq, param_number):

    seq = seq.copy()

    n = len(seq)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if params[seq[j]][param_number] < params[seq[j + 1]][param_number]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]
    
    return seq


