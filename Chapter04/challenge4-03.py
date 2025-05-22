def f(a,b,c,d = 6,e = 4):
    """
    3つの必須引数と2つのオプション引数がある関数を書いてみよう。
    """
    return a * b * (d - e + c)
result = f(3,4,5)
print(result)
