#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from database.data import Database

class Users(Database):
    # -*- Codes related -*-
    def add_code(self, d):
        return self.insert('codes_documents', d)

    def one_data_by_id(self, t, i):
        q = 'select * from %s where id = "%s"' % (t, i)
        return self.one(q=q)

    def one_data_by_user_id(self, t, i):
        q = 'select * from %s where user_id = "%s"' % (t, i)
        return self.one(q=q)

    def one_code(self, t, i):
        q = 'select * from codes_%s where id = %s' \
            % (t, i)
        return self.one(q=q)

    def one_gender(self, i):
        q = 'select * from genders where gen_description = "%s"' \
            % (i)
        return self.one(q=q)

    def one_region(self, i):
        q = 'select * from regions where reg_initials = "%s"' \
            % (i)
        return self.one(q=q)
    
    # -*- Users related -*-
    def add_user(self, d):
        return self.insert('users', d)

    def alt_user(self, i: int, d) -> bool:
        return self.update_from_id('users', i, d)

    # -*- Documents related -*-
    def add_document(self, d):
        return self.insert('documents', d)

    def alt_document(self, i: int, d) -> bool:
        return self.update_from_user_id('documents', i, d)

    # -*- Address related -*-
    def add_address(self, d):
        return self.insert('address', d)

    def alt_address(self, i: int, d) -> bool:
        return self.update_from_user_id('address', i, d)


    # Get for /\/\/\/\/

    # -*- Gender distribution -*-
    def get_id_from_doc(self, i):
        q = 'select user_id from documents where doc_document = "%s"' \
            % (i)
        return self.one(q=q)

    # -*- Gender distribution -*-
    def gender_ratio(self, i):
        q = 'select * from users where gender_id = "%s" and use_status = 1' \
            % (i)
        return self.fetch(q=q)
    
    # -*- Country zone distribution -*-
    def country_zone_ratio(self, i):
        q = 'select * from address where add_region = "%s" and add_status = 1' \
        % (i)
        return self.fetch(q=q)

    # -*- State distribution -*-
    def state_ratio(self, i):
        q = 'select * from address where add_state = "%s" and add_status = 1' \
        % (i)
        return self.fetch(q=q)

    # -*- Range distribution -*-
    def age_ratio(self, i):
        q = 'select * from users where use_birth = "%s" and use_status = 1' \
        % (i)
        return self.fetch(q=q)

    # -*- All data -*-
    def all_data(self, t):
        q = 'select * from %s where use_status = 1' % (t)
        return self.fetch(q=q)

    def all_data_address(self, t):
        q = 'select * from %s where add_status = 1' % (t)
        return self.fetch(q=q)

    def all_data_regions(self, t): 
        q = 'select * from %s where reg_status = 1' % (t)
        return self.fetch(q=q)

    def all_data_by_id(self, t, i):
        q = 'select * from %s where id = "%s"' % (t, i)
        return self.fetch(q=q)

    def all_data_by_user_id(self, t, i):
        q = 'select * from %s where user_id = "%s"' % (t, i)
        return self.fetch(q=q)