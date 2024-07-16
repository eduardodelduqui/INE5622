# INE5622 - Analisador Léxico em Python

Este projeto é um analisador léxico implementado em Python para a disciplina INE5622 - Introduçaõ a Compiladores, da Universidade Federal de Santa Catarina. Ele processa uma string de entrada e a divide em tokens que podem ser usados nas etapas posteriores de um compilador.

## Estrutura do Projeto

```
src/
/── main.py
/── token_component.py
/── automatons/
    ├── arithmetic.py
    ├── assign.py
    ├── automaton.py
    ├── bracket.py
    ├── identifier.py
    ├── keyword.py
    ├── number.py
    ├── punctuation.py
    └── relop.py
```


### Arquivos e Pastas

- **main.py**: Contém a lógica principal do analisador léxico.
- **token_component.py**: Define a classe `Token`, que representa um token reconhecido pelo analisador.
- **automatons/**: Contém as classes dos autômatos finitos para diferentes tipos de tokens. Cada arquivo implementa um autômato específico:
  - **arithmetic.py**: Autômato para operadores aritméticos.
  - **assign.py**: Autômato para operadores de atribuição.
  - **automaton.py**: Classe base para todos os autômatos.
  - **bracket.py**: Autômato para parênteses e chaves.
  - **identifier.py**: Autômato para identificadores.
  - **keyword.py**: Autômato para palavras-chave.
  - **number.py**: Autômato para números.
  - **punctuation.py**: Autômato para pontuações.
  - **relop.py**: Autômato para operadores relacionais.

## Como Executar

### Pré-requisitos

Certifique-se de ter o Python instalado em sua máquina.

### Passos

1. Clone este repositório para sua máquina local.
2. Navegue até o diretório `src`.
3. Execute o script `main.py` usando o seguinte comando:

```bash
python main.py
```

### Exemplo de Uso
O arquivo main.py contém uma string de entrada que será analisada pelo analisador léxico. Aqui está um exemplo de como a entrada é definida e processada:

```python
input = """
def func1 ( int A , int B )
{
    int C = A + B ;
    int D = B * C ;
    return ;
}
def principal ()
{
    int C ;
    int D ;
    int R ;
    C = 4 ;
    D = 5 ;
    R = func1 ( C , D ) ;
    return ;
}
"""

```

### Saída Esperada
A saída será uma lista de tokens identificados na string de entrada. Cada token será representado pelo seu tipo e valor. Aqui está um exemplo de saída:
