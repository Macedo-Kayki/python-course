from collections import Counter

def calc_notas(dic):
    conta = Counter(dic).most_common(1)
    return print(conta) 

if __name__ == "__main__":
    dic = [
        "kayki", 10,
        "carlos", 9.5,
        "nicolas", 5,
        "rafael", 10,
        "enzo", 9.5,
        "mateus", 10
    ]
    calc_notas(dic)