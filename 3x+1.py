
# N = int(input())

def collatz(N):
    temp = [N]
    if N == 1:
        return temp
    if N %2 == 1:
        temp += collatz(3*N+1)
    if N %2 == 0:
        temporary = []
        temporary.append(temp)
        temporary[0]+=collatz(N//2)
        return temporary
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

# print(collatz(4))
# print([5]+[6])
hasil(int(input()))