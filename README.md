# climatempo_api

Uma simples aplicação REST em Python utilizando o framework Flask e banco de dados SQLite
A aplicação possui rota/url básicas:

<p><b>/weather/<nome_cidade></p></b>

Url responsável por gerenciar a requisição entre esta api e a api de serviço metereológico, e persistir os dados no banco.
O campo <nome_cidade> deve ser substituido pelas seguintes opções:

<p><b>São Paulo</b></p> 
<p><b>São Carlos</b></p>
<p><b>Santos</b></p>
<p><b>Rio do Janeiro</b></p>
<p><b>Salvador</b></p>
<p><b>Maceió</b></p>

<p><p>Url responsável por recuperar o id na base local e consultar na api o tempo no momento.</p></p>

para iniciar a aplicação é necessário instalar as <p>requirements</b> (/requirements.txt) e executar o comando

<p><b>python3 run.py</p></b>

Após a inicialização o serviço estará disponível no seu ip local, utilizando a porta 3000

<p><b>127.0.0.1:3000</p></b>

O banco de dados (/banco.db) persiste o histórico de consultas climáticas e id's para consulta na api
