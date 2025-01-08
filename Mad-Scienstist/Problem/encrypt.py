def base_pair(DNA):
    new_base = ''
    for base in DNA:
        if base == 'T':
            new_base = new_base + 'A'
        elif base == 'G':
            new_base = new_base + 'C'
        elif base == 'C':
            new_base = new_base + 'G'
        elif base == 'A':
            new_base = new_base + 'T'
        else:
            return 'Invalid input'
    return new_base

def base(data):
    if data == 0:
        return 'A'
    elif data == 1:
        return 'C'
    elif data == 2:
        return 'G'
    elif data == 3:
        return 'T'
    else:
        return 'Invalid input'

def transfer_data(data):
    lagging_strand = ""
    while(data > 0):
        duplicate_data = data%4
        data //= 4
        lagging_strand = base(duplicate_data) + lagging_strand
    while(len(lagging_strand) < 4):
        lagging_strand = 'A' + lagging_strand
    return lagging_strand

def encrypt(virus):
    duplicate_virus = ""
    for data in virus:
        duplicate_virus = duplicate_virus + transfer_data(ord(data))
    return duplicate_virus

virus = input("Input Virus: ")
lagging_strand = encrypt(virus)
leading_strand = base_pair(lagging_strand)
print(leading_strand)