
import mysql.connector
from database import deploy

class Database():

    def __init__(self):
        try:
            self.cnx = mysql.connector.connect(
                host=deploy.DB['host'],
                user=deploy.DB['user'],
                password=deploy.DB['pwd'],
                database=deploy.DB['database'],
                port=deploy.DB['port'])
            self.cursor = self.cnx.cursor(dictionary=True)
        except Exception as err:
            print(err)
            return None

    def insert(self, t, d):
        try:
            p = ', '.join(['%s'] * len(d))
            c = ', '.join(d.keys())
            q = "INSERT INTO %s ( %s ) VALUES ( %s )" % (t, c, p) #INSERT INTO users (',' chaves dicionarios) VALUES (', ')
            self.cursor.execute(q, list(d.values()))
            self.cnx.commit()
            return self.cursor.lastrowid
        except Exception as err:
            print(err)
            return None

    def update_from_user_id(self, t, i, d):
        try:
            s = ', '.join('{}=%s'.format(k) for k in d)
            sql = "UPDATE %s SET %s WHERE user_id = %s " % (t, s, i)
            print(sql)
            self.cursor.execute(sql, list(d.values()))
            self.cnx.commit()
            return True
        except Exception as err:
            print(err)
            return None

    def update_from_id(self, t, i, d):
        try:
            s = ', '.join('{}=%s'.format(k) for k in d)
            sql = "UPDATE %s SET %s WHERE id = %s " % (t, s, i)
            self.cursor.execute(sql, list(d.values()))
            self.cnx.commit()
            return True
        except Exception as err:
            print(err)
            return None
    
    def delete(self, t, f, d):
        try:
            q = "DELETE FROM %s where %s=%s" % (t, f, d)
            self.cursor.execute(q)
            self.cnx.commit()
            return True
        except Exception as err:
            print(err)
            return None

    def one(self, q):
        try:
            self.cursor.execute(q)
            return self.cursor.fetchone()
        except Exception as err:
            print(err)
            return None

    def fetch(self, q):
        try:
            self.cursor.execute(q)
            return self.cursor.fetchall()
        except Exception as err:
            print(err)
            return None
