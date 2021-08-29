import uvicorn
from starlette.responses import PlainTextResponse


async def app(scope, receive, send):
    assert scope['type'] == 'http'
    response = PlainTextResponse('Hello, world!')
    await response(scope, receive, send)


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
