process.on('message', (msg) => {
    console.log('Message from parent:', msg);
});

let counter = 0;

let timeInterval = setInterval(() => {
    process.send({ counter: counter++ });
}, 1000);

process.on('disconnect', _ => {
    clearInterval(timeInterval)
    console.log('child killed by parent!')
})