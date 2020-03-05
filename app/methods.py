import flask
import requests
import sqlite3
import json





def get_id():
    
                
        get_info = requests.get('http://apiadvisor.climatempo.com.br/api/v1/locale/city?name=rio+de+janeiro&state=RJ&token=b22460a8b91ac5f1d48f5b7029891b53').json()

                       
        city = {'id' : get_info['id'], 'name' : get_info['name'], 'state' : get_info['state'], 'country' : ['country']}
                
                
                
        sql = """INSERT INTO cidades ( id, name, state, country ) VALUES ( {}, '{}', '{}', '{}' ) """.format(city['id'], city['name'], city['state'], city['country'])
        
        result = query(sql)        
                
               
        return str (get_info)




def consulta_id(nome_cidade):
    
        result = query (""" SELECT id FROM cidades WHERE name = '{}' """.format(nome_cidade))    

        return result[0][0]
    
            
        

def get_clima(id_cidade):
        
              
        result = requests.get('http://apiadvisor.climatempo.com.br/api/v1/weather/locale/{}/current?token=b22460a8b91ac5f1d48f5b7029891b53'.format(id_cidade)).json()
        
        return result




def query(sql):
        
        
        conn = sqlite3.connect('banco.db')
        c = conn.cursor()
        
        c.execute(sql)
        
        result = c.fetchall()
        
        conn.commit()
        
        c.close()
        
        return result


def insert(data):  
        
        print('entrou no insert')
        
        weather = { 'id' : int(data ['id']), 'name' : data ['name'], 'state' : data ['state'],
                    'country' : data ['country'], 'temperature' : float(data['data']['temperature']), 
                    'wind_direction' :data['data']['wind_direction'], 'wind_velocity' : float(data['data']['wind_velocity']),
                    'humidity' : float(data['data']['humidity']), 'condition' : data['data']['condition'], 'pressure' : float(data['data']['pressure']),
                    'sensation' : float(data['data']['sensation']), 'date' : data['data']['date']}
        
        
        sql = ( """INSERT INTO previsao ( id_cidade, name, state, country, temperature, wind_direction, wind_velocity, humidity, 
                condition, pressure, sensation, date ) VALUES ( {}, '{}', '{}', '{}', {}, '{}', {}, {}, '{}', {}, {}, '{}' ) """.format(weather['id'], weather['name'], weather['state'], 
                weather['country'], weather['temperature'], weather['wind_direction'], weather['wind_velocity'], weather['humidity'], weather['condition'], weather['pressure'],
                weather['sensation'], weather['date']))
        
        result = query(sql)
        
        return True

