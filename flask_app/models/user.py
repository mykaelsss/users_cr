
from flask_app.config.mysqlconnection import connectToMySQL

class Users:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL('users_schema').query_db(query)

        users = []
        for user in results:
            users.append( cls(user) )
        return users


    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users(first_name, last_name, email, created_at, updated_at)"
        query += "VALUES(%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW() )"
        new_user_id = connectToMySQL('users_schema').query_db(query,data)
        return new_user_id

    @classmethod
    def show_user(cls, data):
        query = " SELECT * FROM users WHERE id = %(id)s";
        result = connectToMySQL('users_schema').query_db(query,data)
        return cls(result[0])

    @classmethod
    def update(cls,data):
        print(data)
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, updated_at =NOW() WHERE id = %(id)s"
        return connectToMySQL('users_schema').query_db(query,data)

    @classmethod
    def delete_user(cls,data ):
        query = " DELETE FROM users WHERE id = %(id)s"
        return connectToMySQL('users_schema').query_db(query,data)
