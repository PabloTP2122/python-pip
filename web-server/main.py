import store
from fastapi import FastAPI
# Retornar HTML
from fastapi.responses import HTMLResponse


app = FastAPI()

# Título de la documentación de la API
app.title = 'API 1'
app.version = '0.0.1'

# Se añade un decorador
@app.get('/', tags=['list'])
def get_list():
    return [2,3,4,5,12,2]

@app.get('/contact', tags=['contact'])
def get_contact():
    return { 'name': 'EvilCorp' }

# Retorna HTML
@app.get("/patas/")
async def read_items():
    html_content = """
    <html>
        <head>
            <title>Título</title>
        </head>
        <body>
            <h1>Miradme soy un HTML</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

def run():
    store.get_categories()


if __name__ == '__main__':
    run()