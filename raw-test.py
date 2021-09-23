import mysql.connector
import http.client, mimetypes, json
import random
from datetime import datetime, timedelta

name = ['Julio', 'Julia', 'Gabriele', 'Gabriel', 'Jonathan', 'Natan', 'Wagner', 'Adalgiza', 'João', 'Lucas', \
        'Mayara', 'Mariana', 'Aline', 'Alice', 'Renata', 'Marisbela', 'Rafael', 'Claudia', 'Vitória', 'Jorge', \
        'Gean', 'Abelardo', 'Rodrigo', 'Benedito', 'Daniela', 'Daniel', 'Priscila', 'Patrícia', 'Jefferson']
surname = ['Silva', 'Checon', 'Lanza', 'Maltese', 'Isaac', 'Schum', 'Fankhauser', 'Grim', 'Lynch', 'França', \
            'dos Santos', 'Zamborlini', 'Nunes', 'Machado', 'de Souza', 'Fontineli', 'Tinelli', 'Soares', 'Alves', \
            'Pereira', 'Veloso', 'Ribeiro', 'Behrend', 'Falqueto', 'Sodré', 'Mota', 'Nascimento', 'Escobar', 'Gobbi', \
            'Mesquita', 'Campos', 'Grecco', 'Miranda', 'Jaccoud', 'Melo', 'Dias', 'Cipriano', 'Camargo']

state = ['AM','PA','RR','AP','RO',
            'AC','TO','PI','MA','PE','RN','PB',
            'CE','BA','AL','SE','MT','MS','GO',
            'DF','SP','RJ','ES','MG'
            ]

z = random.choice(['m','f',''])  

print(z)
'''
def random_datetime(start, end):
    random_seconds = (end - start).total_seconds()
    return datetime.fromtimestamp(random.randrange(random_seconds)).strftime('%Y/%m/%d')
'''

def random_datetime(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return (start + timedelta(seconds=random_second)).strftime('%Y/%m/%d')

_birth = random_datetime(datetime(1970, 1, 1), datetime(2000, 1, 1))
print(_birth)
