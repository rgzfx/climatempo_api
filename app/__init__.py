from flask import Flask, request, render_template
import requests
from app.methods import consulta_id, get_clima, insert
import sqlite3


app = Flask(__name__)


@app.route('/weather/<nome_cidade>')
def weather(nome_cidade):
    
    id_cidade = consulta_id(nome_cidade)
        
    data = get_clima(id_cidade)    
    response = insert(data)

    return data



