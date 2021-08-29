from starlette.applications import Starlette
import uvicorn
from starlette.routing import Route
from starlette.responses import PlainTextResponse


async def homepage(request):
    return PlainTextResponse('Hello, world!')


def startup():
    print('Ready to go')


routes = [
    Route('/', homepage),
]

app = Starlette(debug=True, routes=routes, on_startup=[startup])

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
