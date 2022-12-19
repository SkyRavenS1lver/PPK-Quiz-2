def factorOf(N):
    dictionary = {}
    if N > 1:
        for i in range(2,N+1):
            if N % i == 0:
                dictionary = factorOf(N//i)
                try:
                    dictionary[i] += 1
                except:
                    dictionary[i] = 1
                return dictionary
    return dictionary
def function(N):
    dictionary = factorOf(N)
    temp = dictionary.keys()
    hasil = 0
    for i in temp:
        hasil += dictionary[i] * i
    return hasil
soal = list(map(int, input().split()))
jawaban = 0
for i in soal:
    jawaban+=function(i)
print(jawaban)
# print(function(441))
