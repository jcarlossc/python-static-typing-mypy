# 📌 Estudo sobre tipagem estática e módulo mypy em linguagem Python.

[![Python](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/)
[![Poetry](https://img.shields.io/badge/poetry-managed-orange)](https://python-poetry.org/)
[![mypy](https://img.shields.io/badge/mypy-checked-success)](https://mypy.readthedocs.io/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

Este repositório apresenta um estudo prático de **tipagem estática em Python** utilizando:
- [mypy](https://mypy.readthedocs.io/) para verificação estática de tipos  
- [Poetry](https://python-poetry.org/) para gerenciamento de dependências e ambientes  
- `typing` para uso de **type hints**, **Union**, **Any** e **genéricos (TypeVar)**  

---

## 📌 Objetivo

O projeto **python-static-typing-mypy** foi desenvolvido para demonstrar:
1. Como aplicar **tipagem estática** em Python moderno.  
2. Uso de **genéricos** em funções.  
3. Como integrar `mypy` no fluxo de desenvolvimento.  
4. Estruturação de projeto com **Poetry**.  

---

## 📌 Modo de utilizar

```bash
git clone https://github.com/jcarlossc/python-static-typing-mypy.git
cd python-static-typing-mypy
```

---

## 📌 Instalar o Poetry (se ainda não tiver)

Se você não tiver o Poetry instalado:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

---

## 📌 Restaurar as dependências

```bash
poetry install
```

---

## 📌 Usar o projeto

Rodar a aplicação principal
Você pode executar o script principal com:
```bash
poetry run tipagem
```
---

## 📌 Verificação de tipos com mypy

Para checar estática de tipos:

```bash
# Executa arquivo específico
poetry run nomeDoArquivo.py
# Executa todos os arquivos
poetry run mypy .
```

---

## 📌 Executando os testes

Os testes estão localizados na pasta tests/. Para rodar:

```bash
poetry run pytest
```

---

## 📌 Benefícios da Tipagem Estática

📌 Identificação precoce de erros<br>
📌 Melhor legibilidade e documentação do código<br>
📌 Auxílio de IDEs/autocompletar<br>
📌 Segurança em projetos grandes<br>

---

## 📌 Contatos

📌Recife, PE - Brasil<br>
📌Telefone: +55 81 99712 9140<br>
📌Telegram: @jcarlossc<br>
📌Blogger linguagem R: https://informaticus77-r.blogspot.com/<br>
📌Blogger linguagem Python: https://informaticus77-python.blogspot.com/<br>
📌Email: jcarlossc1977@gmail.com<br>
📌Portfólio em construção: https://portfolio-carlos-costa.netlify.app/<br>
📌LinkedIn: https://www.linkedin.com/in/carlos-da-costa-669252149/<br>
📌GitHub: https://github.com/jcarlossc<br>
📌Kaggle: https://www.kaggle.com/jcarlossc/<br>
📌Twitter/X: https://x.com/jcarlossc1977<br>