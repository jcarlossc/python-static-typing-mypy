from typing import Union, Optional, List, Tuple, Dict, TypeVar, Any

class TipagemEstatica():
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