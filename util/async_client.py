# https://github.com/miguelgrinberg/quick-socketio-tutorial/blob/master/async_client.py

import asyncio
import socketio

sio = socketio.AsyncClient()

@sio.event
async def connect():
    print('connected func')
    defaultGroup = await sio.call('guest',
                      {'os': 'falseOS', 'browser': 'Async', 'environment': 'None', })
                      # callback=print('guest'))
    print(defaultGroup)

@sio.event
async def disconnect():
    print('disconnect func')



async def main():
    await sio.connect('http://localhost:8888')
    print('my sid is: ', sio.sid)
    await sio.wait()

asyncio.run(main())