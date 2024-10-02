from behave import given, then
from utils.api_requests import ApiRequests

@given('que eu faço uma requisição para listar celulares')
def step_impl(context):
    context.response = ApiRequests.get_all_phones()

@then('a resposta deve conter uma lista de celulares')
def step_impl(context):
    assert context.response.status_code == 200
    assert isinstance(context.response.json(), list)

@given('que eu faço uma requisição para listar celulares com ids "{ids}"')
def step_impl(context, ids):
    context.response = ApiRequests.get_phones_by_ids(ids.split(','))

@then('a resposta deve conter os celulares com ids "{ids}"')
def step_impl(context, ids):
    expected_ids = set(ids.split(','))
    response_ids = {str(item['id']) for item in context.response.json()}
    assert expected_ids == response_ids

@given('que eu faço uma requisição para cadastrar um celular')
def step_impl(context):
    context.response = ApiRequests.create_phone({
        "brand": "TestBrand",
        "name": "TestName",
        "model": "TestModel",
        "price": 1234.56
    })


@then('o celular deve ser cadastrado com sucesso')
def step_impl(context):
    assert context.response.status_code == 200
    assert context.response.json()['name'] == "TestName"
    assert context.response.json()['createdAt'] != None
