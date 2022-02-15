const URL = [
    'https://jsonplaceholder.typicode.com/posts',
    'https://jsonplaceholder.typicode.com/albums',
    'https://jsonplaceholder.typicode.com/todos',
    'https://jsonplaceholder.typicode.com/users',
]

const fetchAll = (logger) => {
    return new Promise((resolve, reject) => {
        fetch(URL[0]).then(posts => {
            resolve(posts)
        })
        .catch(err => console.log('ErrI', err, ' logger-name: ', logger.name))
        .finally(() => console.log('IFinally', ' logger-name: ', logger.name))
    })
    .catch(err => console.log('ErrO', err, ' logger-name: ', logger.name))
    .finally(() => console.log('OFinally', ' logger-name: ', logger.name))
}

let myLogger = {'name': 'this is my custom logger'}

let res = fetchAll(myLogger)
console.log(res)