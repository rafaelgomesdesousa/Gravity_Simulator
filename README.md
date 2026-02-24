# Gravity Simulator in Python

## Sobre o projeto
Simples projeto desenvolvido em python que simula corpos no espaço utilizando as fórmulas da mecânica clássica de Newton, mais especificamente e equação da gravitação universal.

O programa permite que o usuário ao clicar e segurar na tela, crie uma esfera que simula um corpo celeste com massa. O Usuário tambem pode movimentar o mouse enquanto segura o botão esquerdo
para direcionar o sentido e a velocidade com que a esfera vai vagar pelo espaço.
Ao criar duas esferas, é possível visualizar a gravidade funcionando.

## Como jogar
- Criar Corpos: Clique e segure o botão esquerdo em qualquer lugar da tela.
- Definir Trajetória: Enquanto segura, arraste o mouse para definir a direção e a velocidade inicial do corpo.
- Lançar: Solte o botão para criar a esfera e vê-la interagir com os outros corpos.

## Correção da colisão das esferas
Inicialmente, um grande problema estava acontecendo, quando duas esferas se aproximavam demais, como a distância entre elas se aproximava de zero, a aceleração de ambas as esferas tendia 
para o infinito e elas saíam da tela em uma velocidade absurda.
Entretanto, pra corrigir esse bug, eu implementei duas soluções: 
1. Parâmetro de suavização: Eu adicionei um valor epsilon pra somar r (A distância entre os corpos)
2. Transferência de Massa e Fusão: Quando duas esferas se aproximam muito uma da outra, de modo que, a soma de seus raios seja maior do que a distância entre as duas (Quando elas colidem), a massa da esfera "menor" (Com menos massa) vai gradualmente 
sendo transferida pra massa da esfera de massa maior, consequentemente, também os seu raio/tamanho.

## Mecânica secreta
Tentando fazer alguns testes de corpos com massa absurdamente grande, eu tive a ideia de implementar um objeto especial, um "buraco negro". 
Sempre que a massa de um objeto fica consideravelmente "grande", o objeto adquire uma massa absurda e fixa e se transforma em uma esfera negra com bordas brancas (Que provavelmente vai sugar 
todos os objetos que foram criados anteriormente)

## Como rodar
1. Certifique-se de ter o python instalado
2. Instale a biblioteca pygame: bash pip install pygame
3. Execute o arquivo principal (main.py)
