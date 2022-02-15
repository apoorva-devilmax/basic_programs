function getSuccessResponse() {
	return new Promise((resolve, reject) => {
		console.log('in getSuccessResponse')
		setTimeout(_ => {
			console.log('in getSuccessResponse timeout')
			resolve('response from 1st API')
		}, 5000)
	})
}

function getAnotherSuccessResponse() {
	return new Promise((resolve, reject) => {
		console.log('in getAnotherSuccessResponse')
		setTimeout(_ => {
			console.log('in getAnotherSuccessResponse timeout')
			resolve('response from 2nd API')
		}, 10000)
	})
}

function getErrorResponse() {
	return new Promise((resolve, reject) => {
		console.log('in getErrorResponse')
		setTimeout(_ => {
			console.log('in getErrorResponse timeout')
			reject('error response from 1st API')
		}, 15000)
	})
}


function getAnotherErrorResponse() {
	console.log('in getAnotherErrorResponse')
	return new Promise((resolve, reject) => {
		setTimeout(_ => {
			console.log('in getAnotherErrorResponse timeout')
			reject('error response from 2nd API')
		}, 20000)
	})
}


let p1 = getSuccessResponse()
let p2 = getAnotherSuccessResponse()
let p3 = getErrorResponse()
let p4 = getAnotherErrorResponse()

//success only (10sec)
Promise.allSettled([p1, p2])
.then(data => {
	console.log('successss1 ', data)
})
.catch(err => {
	console.log('errorrrrrrrrr1 ', err)
})

// mixed (20sec)
Promise.allSettled([p1, p2, p3, p4])
.then(data => {
	console.log('successss2 ', data)
})
.catch(err => {
	console.log('errorrrrrrrrr2 ', err)
})

//error only (20sec)
Promise.allSettled([p3, p4])
.then(data => {
	console.log('successss3 ', data)
})
.catch(err => {
	console.log('errorrrrrrrrr3 ', err)
})

console.log('endedd')

/**
output:

in getSuccessResponse
in getAnotherSuccessResponse
in getErrorResponse
in getAnotherErrorResponse
endedd
in getSuccessResponse timeout
in getAnotherSuccessResponse timeout
successss1  [
  { status: 'fulfilled', value: 'response from 1st API' },
  { status: 'fulfilled', value: 'response from 2nd API' }
]
in getErrorResponse timeout
in getAnotherErrorResponse timeout
successss2  [
  { status: 'fulfilled', value: 'response from 1st API' },
  { status: 'fulfilled', value: 'response from 2nd API' },
  { status: 'rejected', reason: 'error response from 1st API' },
  { status: 'rejected', reason: 'error response from 2nd API' }
]
successss3  [
  { status: 'rejected', reason: 'error response from 1st API' },
  { status: 'rejected', reason: 'error response from 2nd API' }
]

Exit after 20sec

*/