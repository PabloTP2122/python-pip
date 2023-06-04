import requests as req


def get_categories():
    path = 'https://api.escuelajs.co/api/v1'
    r = req.get(f'{path}/categories')
    print(r.status_code)
    print(r.text)
    print(type(r.text))
    
    # Transformando la respuesta para poder utilizarlo con python
    categories = r.json()
    print(type(categories))
    print(type(categories[0]))
    for property_prod in categories[0]:
        print(property_prod)
    for category in categories:
        print(category['name'])