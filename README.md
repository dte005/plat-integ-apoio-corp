Plataforma IAC - Meu projeto pessoal de gestão de ordens de serviço.
Para utilizar este projeto acesse: https://platintegapoiocorp.herokuapp.com

O que é o projeto?
O projeto foi idealizado para ser um trabalho de TCC.
Ao final da apresentação o mesmo foi implementado com a finalidade de gerênciar
ordens de serviço, voltado para área industrial, e recursos que são partes impor-
tantes para o desenvolvimento das tarefas.
O projeto se inicia através do Login do funcionário que possue conta de "super
usuário", para que assim, tenha acesso a todas as ferramentas da paltaforma.
O processo se inica através do cadastro de umanova oportunidade dentro do ADMIN
do django que vira uma oportunidade na tela de listagem. Após esta criação o
usuário terá como possibilidade a criação da ordem de serviço, onde a mesma rece-
berá um numeração única. Em seguida a plataforma dará a possibilidade de gerência-
mento do processo através das FLAGS da listagem de ordem de serviço.

o projeto conta com telas de:
  1 - LOGIN / LOGOUT
  2 - LISTAGEM DE OPORTUNIDADES
  3 - LISTAGEM DE ORDENS DE SERVIÇO
  4 - CADASTRO DE ORDENS DE SERVIÇO
  5 - LISTAGEM DE FUNCIONÁRIOS (RECURSOS)
  6 - CADASTRO DE FUNCIONÁRIOS
  7 - LISTAGEM DE SUPER USUÁRIOS

Para executa-lo:
Para executar é necessário executar o servidor local no computador através do
comando:
python manage.py runserver

dentro do arquivo settings.py já está configurado o host local.

Diário de bordo:
Dia 1 - 01/12/2018
  - Foi realizada a criação do projeto e a criação do APP no django.
  - Foi realizada a configuração básica do settings.
  - Foi realizada a configuração básica do models.

Dia 2 - 02/12/2018
  - Foi realizada a configuração do ADMIN.
  - Foi realizada o CRUD do projeto principal.
  - Foi realizado o CRUD do projeto do PB.

Dia 3 - 03/12/2018
  - Foi realizada a programação básica do html.
  - Foi configurado o arquivo gitignore.
  - Foi programado as funcionalidade de pesquisa.

Dia 10 - 10/12/2018
  - Foram realizados testes da aplicação

Principais dificuldade:
  1 - Relização da estilização do HTML(frontend).
  2 - Programação e instanciamento de uma query no formulário criado.
