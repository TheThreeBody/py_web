import socketio

sio = socketio.Client(logger=True, engineio_logger=True)

@sio.event
def connect():
    print('connected func')
    # defaultGroup = sio.call('guest',
    #          {'os': 'falseOs', 'browser': 'Async', 'environment': 'None', })
    #                   # callback=print('guest'))
    # SEAL_TEXT = sio.call('seal', {sid})
    # print(SEAL_TEXT)

    # result = sio.call('loginByToken', data={
    #     'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiNjI0YzQ4YWFkYWJiYmI3ZDY3NTYzZTBjIiwiZW52aXJvbm1lbnQiOiJDaHJvbWUgODMuMC40MTAzLjExNiBvbiBPUyBYIDEwLjE0LjYgNjQtYml0IiwiZXhwaXJlcyI6MTY1MTc1ODUwNzAwN30.XP-4rrJoI9y-ZP4FQCP3QVMfAF1dBg8nD8N9b7-OJF8',
    #     'os': 'falseOs', 'browser': 'Async',
    #     'environment': 'Chrome 83.0.4103.116 on OS X 10.14.6 64-bit'})
    # sts = sio.emit('getSTS')
    result = sio.call({'username':'py','password':'py',
                       'os': 'OS X', 'browser': 'Chrome',
        'environment': 'Chrome 83.0.4103.116 on OS X 10.14.6 64-bit'})
    # print(sts)
    print(result)


@sio.event
def connection_error(e):
    print(e)

# @sio.event
# def guest():
#     print('guest')
#     # sio.emit('my message', {'foo': 'bar'})

# @sio.event
# def login():
#     print('l')
#     # sio.guest()
#     sio.emit('login',{'username': 'qwe', 'password': 'qwe', 'os': 'OS', 'browser': 'A','environment': 'F', }, callback=print('login'))
#
# @sio.event
# def guest(sid,data):
#     result = sio.call('guest', {'os': 'OS', 'browser': 'A', 'environment': 'F', },
#              callback=print('guest'))
#     print(result)
    # return sid, data

@sio.event
def disconnect():
    print('disconnect func')

# def call(data):
#     print(data)

sio.connect('http://localhost:8888')
# sio.connect('ws://localhost:8888')
print('my sid is: ', sio.sid)
sio.wait()
# sio.guest()
# defaultG = sio.emit('guest', { 'os':'OS', 'browser':'A', 'environment':'F', },callback=print('call'))
# print(defaultG)
# sio.emit('guest', { 'os':'OS', 'browser':'A', 'environment':'F', }, callback=print('guest'))
# sio.sleep(10)
# sio.disconnect()