console.log('before')
setImmediate(_ => {
    console.log('set immediate called!')
})
process.nextTick(_ => {
    console.log('next tick called!')
})
setTimeout(_ => {
    console.log('set timeout called!')
}, 0)
console.log('after')