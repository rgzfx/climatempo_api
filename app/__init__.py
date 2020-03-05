from flask import Flask, request, render_template
import requests
from app.methods import consulta_id, get_clima, historico_clima, insert, get_id
import sqlite3


app = Flask(__name__)


@app.route('/historico/<nome_cidade>')
def historico(nome_cidade):
    
    consulta1 = historico_clima(nome_cidade)
    
    return consulta1


@app.route('/weather/<nome_cidade>')
def weather(nome_cidade):
    
    id_cidade = consulta_id(nome_cidade)
        
    data = get_clima(id_cidade)    
    response = insert(data)

    return data


