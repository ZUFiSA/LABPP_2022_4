n = int(input())
def nilai_faktorial(n):
    if n > 1:
        return n*nilai_faktorial(n-1)
    elif n < 0:
        return 'tidak terdefinisi'
    return 1
print(nilai_faktorial(n))