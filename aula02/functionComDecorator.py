def pao(f):
    def wrapper():
        print("(Fatia superior de Pão)")
        f()
        print("(Fatia inferior de Pão)")
    return wrapper

@pao
def x_vegan():
    print("Hambúrguer Vegano")


x_vegan()