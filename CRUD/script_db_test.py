#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import http.client, json
import random
from datetime import datetime, timedelta

class Filler:
    def _client(self):
        storage = list()
        
        name = ['Julio', 'Julia', 'Gabriele', 'Gabriel', 'Jonathan', 'Natan', 'Wagner', 'Adalgiza', 'João', 'Lucas', \
                'Mayara', 'Mariana', 'Aline', 'Alice', 'Renata', 'Marisbela', 'Rafael', 'Claudia', 'Vitória', 'Jorge', \
                'Gean', 'Abelardo', 'Rodrigo', 'Benedito', 'Daniela', 'Daniel', 'Priscila', 'Patrícia', 'Jefferson']
        surname = ['Silva', 'Checon', 'Lanza', 'Maltese', 'Isaac', 'Schum', 'Fankhauser', 'Grim', 'Lynch', 'França', \
                   'dos Santos', 'Zamborlini', 'Nunes', 'Machado', 'de Souza', 'Fontineli', 'Tinelli', 'Soares', 'Alves', \
                   'Pereira', 'Veloso', 'Ribeiro', 'Behrend', 'Falqueto', 'Sodré', 'Mota', 'Nascimento', 'Escobar', 'Gobbi', \
                   'Mesquita', 'Campos', 'Grecco', 'Miranda', 'Jaccoud', 'Melo', 'Dias', 'Cipriano', 'Camargo']
        state = ['AM','PA','RR','AP','RO','AC','TO','PI','MA','PE','RN','PB','CE','BA','AL','SE','MT','MS','GO','DF','SP','RJ','ES','MG','RS','SC','PN']  
        city = ['Laranja','Maçã','Pêra','Morango','Uva','Banana','Manga','Jabuticaba','Pêssego','Limão','Caqui','Amora']

        interval = 1000
        print(interval, datetime.now())

        for i in range(interval):
            client_information = dict()
            resp_amount = random.randint(1, 3)
            responsible = dict()

            for i in range(resp_amount):
                _name = random.choice(name)
                _surname = random.choice(surname)
                _city = random.choice(city)
                _state = random.choice(state)
                _birth = random_datetime(datetime(1900, 1, 1), datetime(2005, 12, 31))
                _doc = '{:03d}.{:03d}.{:03d}-{:02d}'.format(random.randint(0, 999), random.randint(0, 999), random.randint(0, 999), random.randint(0, 99))
                responsible.clear()
                responsible = {
                    'user': {
                        'name': f'{_name} {_surname}',
                        'birth': _birth,
                        'gender': random.choice(['M','M','M','M','F','F','F','F',''])                     
                    },
                    'document': {
                        'document': _doc,
                        'type': 'CPF',
                        'nationality': 'BRA'
                    },          
                    'address': {
                        "zipcode": '{:05d}-{:03d}'.format(random.randint(0, 99999), random.randint(0, 999)),
                        "street": f'Rua {random.choice(name)} de {random.choice(surname)}',
                        "number": f'{random.randint(0, 9999)}',
                        "city": _city,
                        "state": _state,
                        "country": "BRA"
                    }
                }

            client_information.update(responsible)
            storage.append(client_information.copy())
            client_information.clear()

        print('1st stage done - ', datetime.now())

        self._client_send(storage=storage)

    def _client_send(self, storage):
        try:
            url = '127.0.0.1:5000'
            for payload in storage:
                conn = http.client.HTTPConnection(url)
                headers = {
                    'Content-Type': 'application/json'
                }
                conn.request('POST', '/', json.dumps(payload), headers)
                data = json.loads(conn.getresponse().read().decode('utf-8'))
                
                if data.get('error'):
                    print(json.dumps(payload))
                    print(data)
            print('2nd stage done - ', datetime.now())

        except Exception as err:
            print(err)

def random_datetime(start, end): #https://stackoverflow.com/questions/553303/generate-a-random-date-between-two-other-dates
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return (start + timedelta(seconds=random_second)).strftime('%Y/%m/%d')

if __name__ == "__main__":             
    Filler()._client()
    #Helper().ddd_state()
