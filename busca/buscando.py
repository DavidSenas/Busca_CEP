def busca_cep(*num):
    import requests as RQ
    num = str(input("Digite o CEP: "))
    cep = RQ.get(f'http://viacep.com.br/ws/{num}/json/')
    mostra = cep.json()
    return mostra
