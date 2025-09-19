from python_static_typing_mypy.TipagemEstatica import TipagemEstatica

def main() -> None:
    """Função principal do projeto"""
    app = TipagemEstatica()

    # Tipos primitivos.
    print(app.boas_vindas())
    print(f"Valor da soma: {app.somar(2, 5)}")
    print(f"Valor da multiplicação: {app.multiplicar(2, 5)}")
    print(f"Maioridade?: {app.checar_idade(17)}")  
    print(f"Maioridade?: {app.checar_idade(48)}")  

    # Tipos Union.
    print(f"Valor da divisão: {app.dividir(5, 2)}")
    print(f"Valor da divisão: {app.dividir(5, 0)}")

    # Tipo Optional.
    print(f"Digite um nome: {app.digite_nome('Carlos')}")
    print(f"Digite um nome: {app.digite_nome()}")

    # Tipo List, Tuple e Dict.
    print(f"Média: {app.media([18, 48, 38, 44])}")
    print(f"Idades: {app.idades()}")
    print(f"Frutas: {app.frutas()}")

    # Tipo Generics.
    print(f"Entrada de valor inteiro: {app.identidade(1)} - {type(app.identidade(1))}")
    print(f"Entrada de valor de ponto flutuante: {app.identidade(2.5)} - {type(app.identidade(2.5))}")
    print(f"Entrada de valor string: {app.identidade("Carlos")} - {type(app.identidade("Carlos"))}")

    # Tipo Any.
    print(f"Entrada de valor inteiro: {app.qualque_valor(1)} - {type(app.qualque_valor(1))}")
    print(f"Entrada de valor de ponto flutuante: {app.qualque_valor(2.6)} - {type(app.qualque_valor(2.6))}")
    print(f"Entrada de valor string: {app.qualque_valor("Carlos")} - {type(app.qualque_valor("Carlos"))}")
    print(f"Entrada de valor lista: {app.qualque_valor([1,2,3])} - {type(app.qualque_valor([1,2,3]))}")

if __name__ == "__main__":
    main()
