# SOLID-ENG.SOFT-29-04-2024

O código do ex1.py, tem como o objetivo somar um número e retornar o resultado, entretanto ele fere o princípio de responsabilidade única do SOLID, pois além de calcular o valor também o imprime.

O código do solu1.py resolve os problemas encontrados no ex1.py, pois agora a classe apenas realiza a soma e retorna seu valor.

O código do ex2.py tem como o objetivo mudar o nome de um time, porém fere o princípio de Demeter, pois usamos da classe user para chegar na classe team e alterar o nome.

O código do solu2.py resolve essa quebra do princípio recebendo diretamente o time que terá seu nome alterado.

O código do ex3.py tem como função servir como uma calculadora, porém fere o princípio aberto-fechado, pois se quisermos adicionar uma nova operação, como multiplicação ou divisão, teríamos que modificar a classe.

O código do solu3.py resolve essa quebra do princípio, usando da Interface “Operacao” e tendo as classes "Soma", "Subtracao", que implementam esta Interface, de forma que caso queiramos, por exemplo, adicionar a capacidade de multiplicação a calculadora, poderemos apenas criar mais uma classe que implemente tal operação.

 O código do ex4.py se trata da abstração de um animal, nele ferimos a preferência por composição sobre herança, ao criarmos a classe Cachorro herdando a classe Animal.

 O código do solu4.py resolve esse problema, ao usar da composição, com a Classe Cachorro carregando uma instância da classe Animal ao invés de herdá-la.

