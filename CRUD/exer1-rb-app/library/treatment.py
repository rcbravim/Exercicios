
from datetime import datetime, date
from flask import json, jsonify, request
from flask.helpers import send_file
from database.users import Users
from matplotlib import pyplot as plt

#from database import deploy

k = {
    "user": {
        "name": "Raphael Costa Bravim",
        "birth": "1986/02/08",
        "gender": "M"
    },
    "document": {
        "document": "103.645.687-04",
        "type": "CPF",
        "nationality": "BRA"
    },
    "address": {
        "zipcode": "29070-000",
        "street": "Rua Professora ...",
        "number": "405 ...",
        "city": "Vitória",
        "state": "ES",
        "country": "BRA"
    }
}

# Treatment for all values
class Treat:
    def __init__(self):
        pass
    
    # Specific treatment for new users data
    def new_user(self):

        fine_data = dict()
        fine_data['users'] = dict()
        fine_data['documents'] = dict()
        fine_data['address'] = dict()
        users = Users()
        
        """
        valid = users.one_gender(i=self['user']['gender'])
        if valid:
            fine_data['users']['gender_id'] = valid.get('id')
        else: "erro nao existe"
        """
        now = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
               
        """
        # >>> Pesquisar solução para estruturar com deploy
        # Please check deploy file
        for i in deploy.STRUCTURE['users']:
            for j in self['users']:
                fine_data['users'][i] = self['users'][j]
        return fine_data
        """

        #users_block
        if self['user']['name']: fine_data['users']['use_name'] = self['user']['name']
        fine_data['users']['use_name'] = self['user']['name']
        fine_data['users']['use_birth'] = self['user']['birth']
        fine_data['users']['gender_id'] = users.one_gender(i=self['user']['gender']).get('id')
        fine_data['users']['use_status'] = 1
        fine_data['users']['use_date_create'] = now
        fine_data['users']['use_date_update'] = now
        #fine_data['users']['use_date_delete'] = None # Dispensable, to keep standard
        #documents_block
        _aux = int((self['document']['document'].replace('.','').replace('-','')))
        fine_data['documents']['doc_document'] = _aux
        fine_data['documents']['doc_type'] = self['document']['type']
        fine_data['documents']['doc_nationality'] = self['document']['nationality']
        fine_data['documents']['doc_status'] = 1
        fine_data['documents']['doc_date_create'] = now
        fine_data['documents']['doc_date_update'] = now
        #fine_data['documents']['doc_date_delete'] = None # Dispensable, to keep standard
        #address_block
        fine_data['address']['add_zipcode'] = self['address']['zipcode']
        fine_data['address']['add_street'] = self['address']['street']
        fine_data['address']['add_number'] = self['address']['number']
        fine_data['address']['add_city'] = self['address']['city']
        fine_data['address']['add_state'] = self['address']['state']
        fine_data['address']['add_country'] = self['address']['country']
        fine_data['address']['add_region'] = users.one_region(i=self['address']['state']).get('reg_region')
        fine_data['address']['add_status'] = 1
        fine_data['address']['add_date_create'] = now
        fine_data['address']['add_date_update'] = now
        #fine_data['address']['add_date_delete'] = None # Dispensable, to keep standard

        return fine_data

    # Specific treatment for update a single user
    def update_user(self):
        
        users = Users()

        fine_data = dict()
        
        #users_block
        if self.get('user'):
            fine_data['users'] = dict()
            _a1 = 'user'
            if self.get(_a1).get('name'): fine_data['users']['use_name'] = self.get(_a1).get('name')
            if self.get(_a1).get('birth'): fine_data['users']['use_birth'] = self.get(_a1).get('birth')
            if self.get(_a1).get('gender'): fine_data['users']['use_gender'] = self.get(_a1).get('gender')

        #documents_block
        if self.get('document'):
            fine_data['documents'] = dict()
            _a1 = 'document'
            if self.get(_a1).get('document'): 
                fine_data['documents']['doc_document'] = int((self[_a1]['document'].replace('.','').replace('-','')))
            if self.get(_a1).get('type'): fine_data['documents']['doc_type'] = self[_a1]['type']
            if self.get(_a1).get('nationality'): fine_data['documents']['doc_nationality'] = self[_a1]['nationality']

        #address_block
        if self.get('address'):
            fine_data['address'] = dict()
            _a1 = 'address'
            if self.get(_a1).get('zipcode'): fine_data['address']['add_zipcode'] = self.get(_a1).get('zipcode')
            if self.get(_a1).get('street'): fine_data['address']['add_street'] = self.get(_a1).get('street')
            if self.get(_a1).get('number'): fine_data['address']['add_number'] = self.get(_a1).get('number')
            if self.get(_a1).get('city'): fine_data['address']['add_city'] = self.get(_a1).get('city')
            if self.get(_a1).get('state'):
                fine_data['address']['add_state'] = self.get(_a1).get('state')
                fine_data['address']['add_region'] = users.one_region(i=self.get(_a1).get('reg_region'))
            if self.get(_a1).get('country'): fine_data['address']['add_country'] = self.get(_a1).get('country')

        return fine_data

def get_ratio(choice):
    users = Users()

    if choice == 1: # 1 resume % of user by gender 
        aux_m = users.gender_ratio(i=1) #male
        aux_f = users.gender_ratio(i=2) #female
        aux_u = users.gender_ratio(i=3) #unidentified
        aux_a = users.all_data(t='users') #all

        ratio_m = 100*len(aux_m)/len(aux_a)
        ratio_f = 100*len(aux_f)/len(aux_a)
        ratio_u = 100*len(aux_u)/len(aux_a)

        response = {
            'male':f'{ratio_m:.2f}%',
            'female':f'{ratio_f:.2f}%',
            'unidentified':f'{ratio_u:.2f}%'
        }

        return response

    elif choice == 2: # 2 resume % of user by country zone

        aux_a = len(users.all_data_address(t='address'))

        aux_n = 100*len(users.country_zone_ratio(i='norte'))/aux_a
        aux_ne = 100*len(users.country_zone_ratio(i='nordeste'))/aux_a
        aux_s = 100*len(users.country_zone_ratio(i='sul'))/aux_a
        aux_se = 100*len(users.country_zone_ratio(i='sudeste'))/aux_a
        aux_co = 100*len(users.country_zone_ratio(i='centro oeste'))/aux_a

        response = {    
            'Norte':f'{aux_n:.2f}%',
            'Nordeste':f'{aux_ne:.2f}%',
            'Sul':f'{aux_s:.2f}%',
            'Sudeste':f'{aux_se:.2f}%',
            'Centro Oeste':f'{aux_co:.2f}%'
        }

        return response

    elif choice == 3: # 3 resume % of user by state country
        
        aux_all_state = users.all_data_regions(t='regions') #retorna lista com dicts dentro
        aux_all_data = users.all_data_address(t='address') #retorna lista com dicts dentro
        
        list_state = list()
        response = dict()

        for i in aux_all_state: #cria lista com todos ESTADOS
            list_state.append(i['reg_initials']) #i == aux_all_state[0]

        for j in list_state:
            aux_value = 100*len(users.state_ratio(i=j))/len(aux_all_data)
            response[j] = f'{aux_value:.2f}%'

        return response

    elif choice == 4: # 4 resume % of user by age (in predenfined range)
        
        def calculate_age(birth): #https://qastack.com.br/programming/2217488/age-from-birthdate-in-python
            birth = datetime.strptime(birth, '%Y-%m-%d')
            today = date.today()
            return today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))

        aux_all = users.all_data(t='users')

        list_ages = list()
        list_range = [13, 18, 25, 35, 45, 55, 65]
        response = dict()
        
        #list_ages = list with ages of each user
        for i in aux_all:
            aux = i['use_birth'].strftime('%Y-%m-%d')
            aux = calculate_age(aux)
            list_ages.append(aux)
        
        #response = dictionary with predefined range and respective value
        for i in list_range:
            range_start = i

            if range_start == list_range[-1]:
                range_end = i+1
                response_key = f'{range_end-1}'
            else:
                range_end = list_range[list_range.index(i)+1]#-1
                response_key = f'{range_start}-{range_end-1}'
            
            aux_ratio = 0
            
            for j in range(range_start, range_end):
                aux_ratio = aux_ratio + 100*list_ages.count(j)/len(aux_all)

            response[response_key] = f'{aux_ratio:.2f}%'

        return response
    
    else: return 'Option not avaliable!'