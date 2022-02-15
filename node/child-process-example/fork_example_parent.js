const { fork } = require('child_process');

const forked = fork('fork_example_child.js');

forked.on('message', (msg) => {
  console.log('Message from child', msg);
});

forked.send({ hello: 'world' });

setTimeout(() => {
  forked.disconnect()
}, 10000);