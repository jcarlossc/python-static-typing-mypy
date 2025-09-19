from typing import Union, Optional, List, Tuple, Dict, TypeVar, Any

class TipagemEstatica():
    """
    Classe TipagemEstatica demonstra o uso de tipagem estática em Python utilizando o módulo typing.
    
    Métodos:
        boas_vindas() -> str:
            Retorna uma mensagem de boas-vindas.
        
        somar(num1: int, num2: int) -> int:
            Soma dois números inteiros e retorna o resultado.
        
        multiplicar(num1: float, num2: float) -> float:
            Multiplica dois números de ponto flutuante e retorna o resultado.
        
        dividir(num1: float, num2: float) -> Union[float, str]:
            Divide dois números de ponto flutuante. Retorna o resultado ou uma mensagem de erro em caso de divisão por zero.
        
        checar_idade(idade: int) -> bool:
            Verifica se a idade é maior ou igual a 18 anos.
        
        digite_nome(nome: Optional[str] = None) -> str:
            Retorna o nome informado ou "Sem nome!" caso não seja fornecido.
        
        media(notas: List[int]) -> float:
            Calcula a média de uma lista de notas inteiras.
        
        idades() -> Tuple[int, int]:
            Retorna uma tupla de idades.
        
        frutas() -> Dict[str, int]:
            Retorna um dicionário com frutas e suas quantidades.
        
        identidade(valor: T) -> T:
            Retorna o valor informado, mantendo o tipo.
        
        qualque_valor(valor: Any) -> Any:
            Retorna qualquer valor informado, sem restrição de tipo.
    """
    def __init__(self) -> None:
        pass

    def boas_vindas(self) -> str:
        return "Seja bem vindo(a) ao estudo de tipagem estática em Python!"

    def somar(self, num1: int, num2: int) -> int:
        return num1 + num2  

    def multiplicar(self, num1: float, num2: float) -> float: 
        return num1 * num2   

    def dividir(self, num1: float, num2: float) -> Union[float, str]:
        if num2 == 0:
            return f"Divisão por zero!"
        else:    
            return num1 / num2

    def checar_idade(self, idade: int) -> bool:
        if idade >= 18:
            return True
        else:
            return False    

    def digite_nome(self, nome: Optional[str] = None) -> str:
        return nome or "Sem nome!"

    def media(self, notas: List[int]) -> float: 
        return sum(notas) / len(notas)  

    def idades(self) -> Tuple[int, int]:
        return (44, 77)     

    def frutas(self) -> Dict[str, int]:
        return {"abacate": 10, "banana": 5}  

    T = TypeVar("T")

    def identidade(self, valor: T) -> T:
        return valor

    def qualque_valor(self, valor: Any) -> Any:
        return valor    