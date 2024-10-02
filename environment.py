import requests

def before_scenario(context, scenario):
    # Configurações antes de cada cenário
    context.base_url = "https://api.restful-api.dev/objects"
    context.headers = {"Content-Type": "application/json"}
    context.response = None
    context.created_objects = []

def after_scenario(context, scenario):
    # Limpeza após cada cenário
    for obj_id in context.created_objects:
        response = requests.delete(f"{context.base_url}/{obj_id}")
        if response.status_code == 200:
            print(f"Deleted object with id: {obj_id}")
        else:
            print(f"Failed to delete object with id: {obj_id}")

def after_all(context):
    # Código de limpeza geral ao final de todos os testes
    pass
