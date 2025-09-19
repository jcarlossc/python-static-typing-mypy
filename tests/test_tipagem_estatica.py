import pytest
from python_static_typing_mypy.TipagemEstatica import TipagemEstatica


@pytest.fixture
def app() -> TipagemEstatica:
    """Cria uma instância da classe para os testes."""
    return TipagemEstatica()


def test_boas_vindas(app: TipagemEstatica) -> None:
    assert app.boas_vindas() == "Seja bem vindo(a) ao estudo de tipagem estática em Python!"


def test_somar(app: TipagemEstatica) -> None:
    assert app.somar(2, 3) == 5
    assert app.somar(-1, 1) == 0


def test_multiplicar(app: TipagemEstatica) -> None:
    assert app.multiplicar(2.0, 3.0) == 6.0
    assert app.multiplicar(0.5, 2.0) == 1.0


def test_dividir(app: TipagemEstatica) -> None:
    assert app.dividir(10, 2) == 5.0
    assert app.dividir(7, 2) == 3.5
    assert app.dividir(5, 0) == "Divisão por zero!"


def test_checar_idade(app: TipagemEstatica) -> None:
    assert app.checar_idade(18) is True
    assert app.checar_idade(10) is False


def test_digite_nome(app: TipagemEstatica) -> None:
    assert app.digite_nome("José") == "José"
    assert app.digite_nome() == "Sem nome!"


def test_media(app: TipagemEstatica) -> None:
    assert app.media([10, 20, 30]) == 20.0
    assert app.media([5, 5, 5, 5]) == 5.0


def test_idades(app: TipagemEstatica) -> None:
    resultado = app.idades()
    assert isinstance(resultado, tuple)
    assert resultado == (44, 77)


def test_frutas(app: TipagemEstatica) -> None:
    frutas = app.frutas()
    assert isinstance(frutas, dict)
    assert frutas["abacate"] == 10
    assert frutas["banana"] == 5


def test_identidade(app: TipagemEstatica) -> None:
    assert app.identidade(123) == 123
    assert app.identidade("texto") == "texto"
    assert app.identidade([1, 2, 3]) == [1, 2, 3]


def test_qualque_valor(app: TipagemEstatica) -> None:
    assert app.qualque_valor(3.14) == 3.14
    assert app.qualque_valor({"chave": "valor"}) == {"chave": "valor"}
