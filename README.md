##COMO RODAR O CÓDIGO

Criei um ambiente virtual pra rodarmos o código e instalei o pygame nele.

Para rodar, use na pasta do repositório

source .venv/bin/activate
python main.py

para sair do ambiente virtual, basta rodar

deactivate

##Refatoracoes

vide comentários no código, comentei com ##, basta dar um ctrl+F e procurar ## pra ver o que eu comentei.

De maneira geral, acredito que o principal ponto pra gente melhorar a refatorar é quebrar o código em diferentes arquivos

Criar um arquivo para
-Background
-Player
-Main
-Detectar colisão
-Rodar a interface

## Lista Proposta
1 - Todos os nomes em portugues, nomeclatura padrao como mudar_x -> velocidade_x; h_passou -> obstaculos_passados; bateulateral -> colisao_lateral
2 - Separar a Classe Game em Eventos, Interface e Colisoes
3 - Corrigir Background.move() trocar 14 chamadas de screen.blit() por método auxiliar - FEITO
4 - Substituir hazard_1 ... hazard_muitos e série de if/else do draw_hazard() por lista e iterações
5 - Migração de atributos de classe -> atributo de instancia: colocar atributos de estado como image, x e y nas classes Background, Player, Hazard e Game. Manter no corpo só coisas realmente que são compartilhadas (ex: width e height da classe Game)
6 - Substituir recursão por máquina de estados
7 - Ajeitar colisão por métodos mais consolidados do pygame

## Outras Partes do Entregável
- Lista de Refatoração feita 
- Diagrama de classe do código refatorado
- Video???