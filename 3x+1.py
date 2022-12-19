def collatz(N):
    temp = [N]
    if N == 1:
        return temp
    if N %2 == 1:
        temp += collatz(3*N+1)
    if N %2 == 0:
        temp = [temp]
        temp[0]+=collatz(N//2)
    return temp
def hitung(arrays):
    hasilHitung = 0
    for i in range(len(arrays)):
        if arrays[i] == 1:
            return hasilHitung+1
        if isinstance(arrays[i], list):
            if i == 0:
                hasilHitung = 1
            hasilHitung *= hitung(arrays[i])
        else:
            hasilHitung += arrays[i]
    return hasilHitung
def hasil(N):
    hasil = collatz(N)
    print(hasil)
    print(hitung(hasil))
hasil(int(input()))
