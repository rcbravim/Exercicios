
from datetime import datetime, date
from flask import json, jsonify, request
from flask.helpers import send_file
from flask.wrappers import Response
from database.users import Users

# For tests
j = {
    "user": {
        "name": "Raphael Costa Bravim",
        "birth": "1986/02/08",
        "gender": "M"
    },
    "document": {
        "document": "103.333.333-33",
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

users = Users()

class Validate:
    def __init__(self):
        pass

    def pre_check(self, doc):

        users = Users()

        if not doc:
            doc = self.get('document').get('document').replace('.','').replace('-','')
        
        #Search database for document number
        if users.get_id_from_doc(i=doc):
            return True

        return False

    def check_raw(self):

        check_user = self['user']
        check_document = self['document']
        check_address = self['address']

        # Validate Variable Name
        if check_user.get('name'):
            if type(check_user.get('name')) == str:
                if check_user.get('name').replace(' ','').isalpha():
                    pass
                else: return False, 'Variable "Name" got an unexpected character!'
            else: return False, 'Variable "Name" must be a string type!'
        else: return False, 'Variable "Name" is empty!'

        # Validate Variable Birth
        if check_user.get('birth'):
            if type(check_user.get('birth')) == str:
                try:
                    aux = check_user.get('birth').split('/')
                    datetime(year=int(aux[0]),month=int(aux[1]),day=int(aux[2]))
                    pass
                except: return False, 'Variable "Birth" got an unexpected date!'
            else: return False, 'Variable "Birth" must be a string type!'
        else: return False, 'Variable "Birth" is empty!'

        # Validate Variable Gender
        if check_user.get('gender'):
            if type(check_user.get('gender')) == str:
                val_gender = Users().one_gender(i=check_user['gender']) # Search query for gender in database
                if check_user.get('gender') == val_gender.get('gen_description'):
                    pass
                else: return False, 'Variable "Gender" got an unexpected character!'
            else: return False, 'Variable "Gender" must be a string type!'
        pass

        # Validate Variable Document
        if check_document.get('document'):
            if type(check_document.get('document')) == str:
                try:
                    int((check_document.get('document').replace('.','').replace('-','')))
                    pass
                except: return False, 'Variable "Document" got character type other than a number!'
            else: return False, 'Variable "Document" must be a string type!'
        else: return False, 'Variable "Document" is empty!'

        # Validate Variable Nationality
        if check_document.get('nationality'):
            if type(check_document.get('nationality')) == str:
                if len(check_document.get('nationality')) == 3:
                    pass
                else: return False, 'Variable "Nationality" got more or less than 3 characters!'
            else: return False, 'Variable "Nationality" must be a string type!'
        else: return False, 'Variable "Nationality" is empty!'

        # Validate Variable Address/Zipcode
        if check_address.get('zipcode'):
            if type(check_address.get('zipcode')) == str:
                pass
            else: return False, 'Variable "Address/Zipcode" must be a string type!'
        else: return False, 'Variable "Address/Zipcode" is empty!'

        # Validate Variable Address/Street
        if check_address.get('street'):
            if type(check_address.get('street')) == str:
                pass
            else: return False, 'Variable "Address/Street" must be a string type!'
        else: return False, 'Variable "Address/Street" is empty!'

        # Validate Variable Address/Number
        if check_address.get('number'):
            if type(check_address.get('number')) == str:
                pass
            else: return False, 'Variable "Address/Number" must be a string type!'
        else: return False, 'Variable "Address/Number" is empty!'

        # Validate Variable Address/City
        if check_address.get('city'):
            if type(check_address.get('city')) == str:
                pass
            else: return False, 'Variable "Address/City" must be a string type!'
        else: return False, 'Variable "Address/City" is empty!'

        # Validate Variable Address/State
        if check_address.get('state'):
            if type(check_address.get('state')) == str:
                pass
            else: return False, 'Variable "Address/State" must be a string type!'
        else: return False, 'Variable "Address/State" is empty!'

        # Validate Variable Address/Country
        if check_address.get('country'):
            if type(check_address.get('country')) == str:
                pass
            else: return False, 'Variable "Address/Country" must be a string type!'
        else: return False, 'Variable "Address/Country" is empty!'

        return True, None

    def check_raw_update(self):

        check_user = check_document = check_address = dict()

        if self.get('user'): check_user = self.get('user')
        if self.get('document'): check_document = self.get('document')
        if self.get('address'): check_address = self.get('address')

        # Validate Variable Name
        _aux = check_user.get('user')
        if _aux:
            if type(_aux) == str:
                if _aux.replace(' ','').isalpha():
                    pass
                else: return False, 'Variable "Name" got an unexpected character!'
            else: return False, 'Variable "Name" must be a string type!'
        else: pass

        # Validate Variable Birth
        _aux = check_user.get('birth')
        if _aux:
            if type(_aux) == str:
                try:
                    aux = _aux.split('/')
                    datetime(year=int(aux[0]),month=int(aux[1]),day=int(aux[2]))
                    pass
                except: return False, 'Variable "Birth" got an unexpected date!'
            else: return False, 'Variable "Birth" must be a string type!'
        else: pass

        # Validate Variable Gender
        _aux = check_user.get('gender')
        if _aux:
            if type(_aux) == str:
                val_gender = Users().one_gender(i=_aux) # Search query for gender in database
                if _aux == val_gender.get('gen_description'):
                    pass
                else: return False, 'Variable "Gender" got an unexpected character!'
            else: pass
        pass

        # Validate Variable Document
        _aux = check_document.get('document')
        if _aux:
            if type(_aux) == str:
                try:
                    int((_aux.replace('.','').replace('-','')))
                    pass
                except: return False, 'Variable "Document" got character type other than a number!'
            else: return False, 'Variable "Document" must be a string type!'
        else: pass

        # Validate Variable Nationality
        _aux = check_document.get('nationality')
        if _aux:
            if type(_aux) == str:
                if len(_aux) == 3:
                    pass
                else: return False, 'Variable "Nationality" got more or less than 3 characters!'
            else: return False, 'Variable "Nationality" must be a string type!'
        else: pass

        # Validate Variable Address/Zipcode
        _aux = check_address.get('zipcode')
        if _aux:
            if type(_aux) == str:
                pass
            else: return False, 'Variable "Address/Zipcode" must be a string type!'
        else: pass

        # Validate Variable Address/Street
        _aux = check_address.get('street')
        if _aux:
            if type(_aux) == str:
                pass
            else: return False, 'Variable "Address/Street" must be a string type!'
        else: pass

        # Validate Variable Address/Number
        _aux = check_address.get('number')
        if _aux:
            if type(_aux) == str:
                pass
            else: return False, 'Variable "Address/Number" must be a string type!'
        else: pass

        # Validate Variable Address/City
        _aux = check_address.get('city')
        if _aux:
            if type(_aux) == str:
                pass
            else: return False, 'Variable "Address/City" must be a string type!'
        else: pass

        # Validate Variable Address/State
        _aux = check_address.get('state')
        if _aux:
            if type(_aux) == str:
                pass
            else: return False, 'Variable "Address/State" must be a string type!'
        else: pass

        # Validate Variable Address/Country
        _aux = check_address.get('country')
        if _aux:
            if type(_aux) == str:
                pass
            else: return False, 'Variable "Address/Country" must be a string type!'
        else: pass

        return True, None
