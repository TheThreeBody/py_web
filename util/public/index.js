const sio = io('http://localhost:8888');

sio.on('connect', () => {
  console.log('connected');
  sio.emit(
      // 'loginByToken',
      // {'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiNjI0YzQ4YWFkYWJiYmI3ZDY3NTYzZTBjIiwiZW52aXJvbm1lbnQiOiJDaHJvbWUgODMuMC40MTAzLjExNiBvbiBPUyBYIDEwLjE0LjYgNjQtYml0IiwiZXhwaXJlcyI6MTY1MTc1ODUwNzAwN30.XP-4rrJoI9y-ZP4FQCP3QVMfAF1dBg8nD8N9b7-OJF8',
      //                  'os': 'falseOs', 'browser': 'Async',
      //   'environment': 'Chrome 83.0.4103.116 on OS X 10.14.6 64-bit'},
      'login',
      {'username':'py','password':'py',
      'os' : '',
    'browser' : '',
    'environment' : '',},
      (result) => {
    console.log(result);
  });
});

sio.on('error', (e) => {
  console.log(e);
});

sio.on('disconnect', () => {
  console.log('disconnected');
});

sio.on('mult', (data, cb) => {
  const result = data.numbers[0] * data.numbers[1];
  cb(result);
});

sio.on('client_count', (count) => {
  console.log('There are ' + count + ' connected clients.');
});

sio.on('room_count', (count) => {
  console.log('There are ' + count + ' clients in my room.');
});

sio.on('user_joined', (username) => {
  console.log('User ' + username + ' has joined.');
});

sio.on('user_left', (username) => {
  console.log('User ' + username + ' has left.');
});