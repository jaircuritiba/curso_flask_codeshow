a = 0
b = 10

try:
    print(b // a)
except ZeroDivisionError:
    print("Não é possível dividir por zero")

try:
    b.Upper()
except Exception as e:
    print("Erro capturado -> ", e.args)