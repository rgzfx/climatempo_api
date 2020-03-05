# climatempo_api

Uma simples aplicação REST em Python utilizando o framework Flask e banco de dados SQLite
A aplicação possui rota/url básicas:

/weather/<nome_cidade>

Url responsável por gerenciar a requisição entre esta api e a api de serviço metereológico, e persistir os dados no banco.
O campo <nome_cidade> deve ser substituido pelas seguintes opções:

<p>São Paulo,</p> 
São Carlos, 
Santos, 
Rio do Janeiro, 
Salvador, 
Maceió, 

Url responsável por recuperar o id na base local e consultar na api o tempo no momento.

para iniciar a aplicação é necessário instalar as requirements (/requirements.txt) e executar o comando

python3 run.py

Após a inicialização o serviço estará disponível no seu ip local, utilizando a porta 3000

127.0.0.1:3000

O banco de dados (banco.db) persiste o histórico de consultas climáticas e id's para consulta na api
