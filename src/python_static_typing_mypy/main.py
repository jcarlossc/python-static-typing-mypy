from python_static_typing_mypy.TipagemEstatica import TipagemEstatica


def main() -> None:
    """Função principal do projeto"""
    app = TipagemEstatica()
    print(app.boas_vindas())
    print(f"Valor da soma: {app.somar(2, 5)}")
    print(f"Valor da multiplicação: {app.multiplicar(2, 5)}")
    print(f"Valor da divisão: {app.dividir(5, 2)}")
    print(f"Valor da divisão: {app.dividir(5, 0)}")
    print(f"Maioridade?: {app.checar_idade(17)}")
    print(f"Maioridade?: {app.checar_idade(48)}")
    print(f"Digite um nome: {app.digite_nome("Carlos")}")
    print(f"Digite um nome: {app.digite_nome()}")


if __name__ == "__main__":
    main()
