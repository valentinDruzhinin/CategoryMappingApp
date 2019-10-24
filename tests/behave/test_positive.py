import json
from app import Category


def test_user_behaviour(client):
    mock_category = Category(name='Men', mapping='Men clothes')

    # categories endpoint
    categories_url = '/categories'

    response = client.get(categories_url)
    assert '200 OK' == response.status
    assert [] == response.json

    response = client.post(
        categories_url,
        data=json.dumps({
            'name': mock_category.name,
            'mapping': mock_category.mapping
        }),
        content_type='application/json'
    )
    assert '200 OK' == response.status
    assert 'id' in response.json

    # category endpoint
    category_url = f'{categories_url}/{response.json["id"]}'

    response = client.get(category_url)
    assert '200 OK' == response.status
    assert mock_category.name == response.json['name']
    assert mock_category.mapping == response.json['mapping']

    response = client.put(
        category_url,
        data=json.dumps({
            'name': 'test_name',
            'mapping': 'test_mapping'
        }),
        content_type='application/json'
    )
    assert '204 NO CONTENT' == response.status

    response = client.get(category_url)
    assert '200 OK' == response.status
    assert 'test_name' == response.json['name']
    assert 'test_mapping' == response.json['mapping']

    response = client.delete(category_url)
    assert '204 NO CONTENT' == response.status

    response = client.get(categories_url)
    assert '200 OK' == response.status
    assert [] == response.json

    # batch processing
    response = client.post(
        categories_url,
        data=json.dumps([
            {
                'name': 'Name1',
                'mapping': 'Mapping1'
            },
            {
                'name': 'Name2',
                'mapping': 'Mapping2'
            },
            {
                'name': 'Name3',
                'mapping': 'Mapping3'
            }
        ]),
        content_type='application/json'
    )
    assert '202 ACCEPTED' == response.status
    assert 'process_id' in response.json

    response = client.get(f'/processes/{response.json["process_id"]}')
    assert '200 OK' == response.status
    assert 'state' in response.json
