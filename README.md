# INE5622 - Analisador Léxico em Python

Este projeto contém um analisador léxico e um analisador sintático implementado em Python para a disciplina INE5622 - Introdução a Compiladores, da Universidade Federal de Santa Catarina. O analisador léxico processa uma string de entrada e a divide em tokens que serão verificados pelo analisador sintático para verificar se esses tokens estão de acordo com as regras gramaticais da linguagem LSI-2024-1

## Estrutura do Projeto

```
src/
/── main.py
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
/── analyzers/
    ├── lexical.py
    └── syntax.py
/── utils/
    ├── parsing_stack.py
    ├── parsing_table.py
    └── token_component.py
/── tests/
    ├── test1.lsi
    ├── test2.lsi
    ├── test3.lsi
    ├── test4.lsi
    ├── test5.lsi
    ├── test6.lsi
    └── test7.lsi
```


### Arquivos e Pastas

- **main.py**: Contém o arquivo que inicia a execução do programa. É nesse arquivo que os analisadores são instanciados.
- **automatons/**: Contém as classes dos autômatos finitos para diferentes tipos de tokens. Cada arquivo implementa um autômato específico:
  - **arithmetic.py**: Autômato para operadores aritméticos.
  - **assign.py**: Autômato para operadores de atribuição.
  - **automaton.py**: Classe base para todos os autômatos.
  - **bracket.py**: Autômato para parênteses e chaves.
  - **identifier.py**: Autômato para identificadores.
  - **keyword.py**: Autômato para palavras-chave.
  - **number.py**: Autômato para números inteiros.
  - **punctuation.py**: Autômato para pontuações.
  - **relop.py**: Autômato para operadores relacionais.
- **analyzers/**: Contém as classes dos analisadores. Cada arquivo implementa um analisador específico:
  - **lexical.py**: Analisador léxico.
  - **syntax.py**: Analisador sintático.
- **utils/**: Contém classes que dão suporte aos analisadores.
  - **parsing_stack**: Implementa uma pilha para dar suporte a analise sintática
  - **parsing_table**: Contém a tabela de reconhecimento sintático. Como a gramatica não é LL(1), existe ambiguidades que são resolvidas também nessa classe.
  - **token_component.py**: Define a classe `Token`, que representa um token reconhecido pelo léxico.
- **tests/**: Contém arquivos escritos na linguagem LSI-2024-1 para fins de teste dos analisadores.
  - **test1.lsi**: Teste sem erros sintáticos e léxicos
  - **test2.lsi**: Teste com erro léxico. Token % não é reconhecido pela linguagem.
  - **test3.lsi**: Teste com erro léxico. Token / não é reconhecido pela linguagem.
  - **test4.lsi**: Teste com erro léxico. Número float não é reconhecido pela linguagem.
  - **test5.lsi**: Teste com erro sintático. Print com expressão relacional.
  - **test6.lsi**: Teste com erro sintático. Elses consecutivos
  - **test7.lsi**: Teste com erro sintático. Return sem ;

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
O arquivo main.py na linha 5 contém uma string com o caminho dos arquivos de teste. Basta modificar o número no fim para mudar o arquivo de teste

