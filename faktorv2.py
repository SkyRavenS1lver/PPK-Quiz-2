def factorOf(N):
    dictionary = []
    if N > 1:
        for i in range(2,N+1):
            if N % i == 0:
                dictionary = factorOf(N//i)
                dictionary.append(i)
                return dictionary
    return dictionary
def function(N):
    dictionary = factorOf(N)
    return sum(dictionary)
soal = list(map(int, input().split()))
jawaban = 0
for i in soal:
    jawaban+=function(i)
print(jawaban)