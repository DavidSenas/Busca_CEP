from busca import buscando
def div():
    return print("=="*80)
div()

end = {}
while True:
    print('''Escolha a opção deseja
[1 ] Buscar um Endereço
[2 ] Encerrar o Programa''')
    op = int(input("=> "))
    if op == 2:
        print("Programa Encerrado")
        break
    if op == 1:
        try:
            end = buscando.busca_cep()
            div()
            print(f"{'Endereço Requerido':^50}")
            print()
            for k, v in end.items():
                print(f"{k} = {v}")
            div()
        except:
            print("\033[1;31mHouve um erro\033[0;0m")
            continue

    