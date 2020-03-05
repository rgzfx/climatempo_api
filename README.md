# climatempo_api

Uma simples aplicação REST em Python utilizando o framework Flask e banco de dados SQLite
A aplicação possui rota/url básicas:

<b> /weather/<nome_cidade> </b>

Url responsável por gerenciar a requisição entre esta api e a api de serviço metereológico (Clima Tempo), buscando o id da cidade na base e persistir os dados recebidos no banco.
O campo <nome_cidade> deve ser substituido pelas seguintes opções:

<p><b>São Paulo</b></p> 
<p><b>São Carlos</b></p>
<p><b>Santos</b></p>
<p><b>Rio do Janeiro</b></p>
<p><b>Salvador</b></p>
<p><b>Maceió</b></p>



Para iniciar a aplicação é necessário instalar os <b>requirements</b> (/requirements.txt) e executar o comando

<p><b>python3 run.py</p></b>

Após a inicialização o serviço estará disponível no seu ip local, utilizando a porta 3000

<p><b>127.0.0.1:3000</p></b>

O banco de dados (/banco.db) persiste o histórico de consultas climáticas e id's para consulta na api
