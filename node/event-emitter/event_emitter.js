const EventEmitter = require('events');

class MyEmitter extends EventEmitter {}

const myEmitter1 = new MyEmitter();
const myEmitter2 = new MyEmitter();

myEmitter1.on('event', function(a, b) {
  console.log(a, b, this, this === myEmitter1);
  // Prints:
  //   a b MyEmitter {
  //     domain: null,
  //     _events: { event: [Function] },
  //     _eventsCount: 1,
  //     _maxListeners: undefined } true
});
myEmitter2.on('event', (a, b) => {
  console.log(a, b, this, this === myEmitter2);
  // Prints:
  //   a b {} false
});
myEmitter1.emit('event', 'a', 'b');
myEmitter2.emit('event', 'a', 'b');