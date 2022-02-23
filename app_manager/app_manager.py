import docker
from flask import Flask
from flask_restful import Api, Resource, reqparse
from docker import APIClient, errors
from os import environ
import requests


app = Flask(__name__)
api = Api(app)

client = docker.APIClient(base_url='unix://var/run/docker.sock')
client.version()

# AM_INIT_PORT = environ.get('AM_INIT_PORT')
# AM_HOSTNAME = environ.get('AM_HOSTNAME')
# DOCKER_API_URL = environ.get('DOCKER_API_URL')
# DOCKER_API_PORT = environ.get('DOCKER_API_PORT')

# client = APIClient(f'{DOCKER_API_URL}:{DOCKER_API_PORT}')
# network_data = client.inspect_container(
#     "app-manager")['NetworkSettings']['Networks']
# network_default = network_data[next(iter(network_data))]['NetworkID']


applications = []

# appFields = {
#     "id": fields.Integer,
#     "user_id": fields.Integer,
#     "port": fields.Integer,
#     "name": fields.String,
# }

# application_put_args = reqparse.RequestParser()
# application_put_args.add_argument(
#     "user_id", type=int, help="Id of user does not specified", required=False)
# application_put_args.add_argument(
#     "port", type=int, help="Port does not specified", required=False)
# application_put_args.add_argument("name", type=str, help="Name of app", required=False)

ports_in_use = []
users_with_app = []

class Manage(Resource):

    def __init__(self):
        
        all_containers = client.containers(all=True)

        for i in all_containers:
            container_name = i['Names'][0][1:]
            if container_name.find('app_') != (-1):
                id_port=container_name.replace('app_','').split('_')     #removesuffix('app_').split('_')
                users_with_app.append(int(id_port[0]))
                ports_in_use.append(int(id_port[1]))
        app_manager = 'app_manager'


    def list(self):
        all_containers = client.containers(all=True)

        apps = []
        for i in all_containers:
            container_name = i['Names'][0][1:] #all applications have structure of name "app_" + {name/id of app} 
            if container_name.find('app_') != (-1):
                apps.append(container_name)
                print(container_name, flush=True)
        
        return str(apps), 200


    def add(self,usr_id,port):
        # args = application_put_args.parse_args()

        if usr_id in users_with_app:
            return "User already has app", 400
        if port in ports_in_use:
            return "This port is in use", 400
        
        application = {
            "id": applications[-1]['id'] + 1 if len(applications) > 0 else 1,
            "user_id": usr_id,
            "port": port,
            "name": "app_" + str(usr_id) + '_' + str(port),
        }
        
        container_name = str(application['name'])
        container_id = client.create_container(
            'base-app', ports=[port,port],  hostname=container_name, name=container_name,  stdin_open=True, tty=True,
            host_config=client.create_host_config(
                port_bindings={ port:port },
            )
        )

        client.start(container_id)
        # client.connect_container_to_network(container_id, network_default)
        
        applications.append(application)
        users_with_app.append(usr_id)
        ports_in_use.append(port)

        return str(application), 200


    def delete(self,usr_id):
        all_containers = client.containers(all=True)
        container_to_delete = "app_" + str(usr_id)            #all applications have structure of name "app_" + {name/id of app} 
        for i in all_containers:
            container_name = i['Names'][0][1:]  #containers starting with '/'
            if container_to_delete in container_name:
                client.stop(container_name, timeout=None)
                client.remove_container(container_name, v=False, link=False, force=False)
                users_with_app.remove(usr_id)
                port = int(container_name.replace('app_','').split('_')[1])#removesuffix(container_name + '_'))
                ports_in_use.remove(port)
                return "Container deleted successfully", 200
                
        return "The container does not exist. Make sure you've entered the correct id", 404

        
manager = Manage()

app.add_url_rule('/app-manager/list', view_func=manager.list, methods=['GET'])
app.add_url_rule('/app-manager/add/<int:usr_id>/<int:port>', view_func=manager.add, methods=['POST'])
app.add_url_rule('/app-manager/delete/<int:usr_id>', view_func=manager.delete, methods=["DELETE"])


app.run(debug=True, port=5005, host='0.0.0.0')
