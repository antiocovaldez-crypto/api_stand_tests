import requests
import configuration
import data

def post_new_user(body):
    # Envía solicitud POST para crear usuario
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

def get_users_table():
    # Obtiene la tabla de usuarios
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)