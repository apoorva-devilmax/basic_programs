const myPromise = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve('foo');
  }, 300);
});

myPromise
.then(data => {
	console.log('successs..1..', data)
	return 'bar'
})
.then(data => {
	console.log('successs..2..', data)
	return 'foobar'
})
.then(data => {
	console.log('successs..3..', data)
	throw new Error('my error')
})
.then(data => {
	console.log('successs..4..', data)
})
.catch(err => {
	console.log('error....', err)
})