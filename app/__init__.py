from flask import Flask, request, render_template
import requests
from app.methods import consulta_id, get_clima, insert, conulta_historico
import sqlite3
import json


app = Flask(__name__)


@app.route('/weather/<nome_cidade>')
def weather(nome_cidade):
    
    id_cidade = consulta_id(nome_cidade)
        
    data = get_clima(id_cidade)    
    response = insert(data)
    
    return render_template('previsao_momento.html', foobar=response)


@app.route('/historico/<nome_cidade>')
def historico(nome_cidade):
    
    result = conulta_historico(nome_cidade)


    return render_template('historico.html', foobar=result)