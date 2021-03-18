
#from typing import Counter
from flask import Flask, json, jsonify, request
from flask.views import MethodView
from library.validation import Validate
from library.treatment import Treat, get_ratio
from database.users import Users


app = Flask(__name__)

class ExCRUD(MethodView):

    def post(self): # Create a new user
        
        users = Users()

        try:
            # /\/\/\/\/ receiving data
            if json.loads(request.get_data()):
                raw_data = json.loads(request.get_data())
            else: return jsonify(status='Bad Request', error='Missing codes package!'), 400

            # /\/\/\/\/ checking for document and active status in database
            if Validate.pre_check(raw_data, doc=None):
                return jsonify(status='Conflit Error', error='Document number is already registered in database'), 409

            # /\/\/\/\/ validate data \/\/\/\/\ treat data
            val_bool = Validate.check_raw(raw_data)[0]
            val_err = Validate.check_raw(raw_data)[1]
            
            if val_bool: fine_data = Treat.new_user(raw_data)
            else: return jsonify(status='Unprocessable Entity',error='Unable to process package!'), 422, '> Error:', val_err
           
            # /\/\/\/\/ insert data
            # insert user data
            aux_user_id = users.add_user(d=fine_data.get('users')) 

            # get and fill user_id's
            fine_data['documents']['user_id'] = fine_data['address']['user_id'] = aux_user_id

            # insert document data
            if not users.add_document(d=fine_data.get('documents')): 
                return jsonify(status='Bad Request', error='Document data could not be save!'), 500
            # insert address data
            if not users.add_address(d=fine_data.get('address')):
                return jsonify(status='Bad Request', error='Address data could not be save!'), 500

            return jsonify(status='Created'), 201

        except Exception as err:
            return print(err) 

    def get(self, choice): # resume ratios, choices (1-4)
        
        choices = (
            'gender_ratio', # 1 resume % of user by gender 
            'country_zone_ratio', # 2 resume % of user by country zone 
            'state_ratio', # 3 resume % of user by state country
            'age_range_ratio' # 4 resume % of user by age (in predenfined range)
        )

        if choice in choices:
            try: 
                response = get_ratio(choices.index(choice)+1)    
                return jsonify(response)
            except Exception as err:
                return print(err)
        else: return jsonify(status='Unprocessable Entity', error='Unable to process package!'), 422

    def put(self, document): # update a single user
        
        users = Users()

        try:

            # /\/\/\/\/ checking for document and active status in database
            if not Validate.pre_check(self=None, doc=document):
                return jsonify(status='User Not Found', error='Document number is not in database'), 404
            else:
                user_id = users.get_id_from_doc(i=document).get('user_id')
                status = users.one_data_by_id(t='users', i=user_id).get('use_status')
                if not status == 1:
                    return jsonify(status='User Not Found', error='Document number is not in database'), 404

            # /\/\/\/\/ receiving data
            if json.loads(request.get_data()): raw_data = json.loads(request.get_data())
            else: return jsonify(status='Bad Request', error='Missing codes package!'), 400

            # /\/\/\/\/ validate data \/\/\/\/\ treat data
            val_bool = Validate.check_raw_update(raw_data)[0]
            val_err = Validate.check_raw_update(raw_data)[1]

            if val_bool: fine_data = Treat.update_user(raw_data)
            else: return jsonify(status='Unprocessable Entity',error='Unable to process package!'), 422, '> Error:', val_err

            # alter user data
            if users.alt_user(i=user_id, d=fine_data.get('users')): users.alt_user(i=user_id, d=fine_data.get('users'))
            # alter documents data
            if users.alt_document(i=user_id, d=fine_data.get('documents')): users.alt_document(i=user_id, d=fine_data.get('documents'))
            # alter address data
            if users.alt_address(i=user_id, d=fine_data.get('address')): users.alt_document(i=user_id, d=fine_data.get('documents'))

            return jsonify(status='Updated Successfully'), 200

        except Exception as err:
            return print(err) 
        
    def delete(self, document):

        users = Users()

        try:
            # /\/\/\/\/ checking for document and active status in database
            if not Validate.pre_check(raw_data=None, doc=document):
                return jsonify(status='User Not Found', error='Document number is not in database'), 404
            else:
                user_id = users.get_id_from_doc(i=document).get('user_id')
                status = users.one_data_by_id(t='users', i=user_id).get('use_status')
                if not status == 1:
                    return jsonify(status='User Not Found', error='Document number is not in database'), 404
            
            # /\/\/\/\/ checking for document in database
            user_id = users.get_id_from_doc(i=document).get('user_id')
            if not user_id: return jsonify(status='User Not Found', error='Document number is not in database'), 404

            fine_data = {'users': {'use_status': 0}}

            # "delete" a single user (actually use_status = 0)
            if users.alt_user(i=user_id, d=fine_data.get('users')):
                users.alt_user(i=user_id, d=fine_data.get('users'))

            return jsonify(status='Deleted Successfully'), 200
        
        except Exception as err:
            return print(err)

ex_crud = ExCRUD.as_view('CRUD_Example')
app.add_url_rule('/', view_func = ex_crud, methods=['POST'])
app.add_url_rule('/get/<choice>', view_func = ex_crud, methods=['GET'])
app.add_url_rule('/update/<document>', view_func = ex_crud, methods=['PUT'])
app.add_url_rule('/delete/<document>', view_func = ex_crud, methods=['DELETE'])

if __name__ == '__main__':
    app.run()