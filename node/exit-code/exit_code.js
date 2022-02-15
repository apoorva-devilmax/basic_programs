const express = require('express')

const app = express()

app.get('/', (req, res) => {
	setTimeout(_ => {
		console.log('timeout 1.........')
	}, 10000)
	setTimeout(_ => {
		res.send('Hi!')
		console.log('timeout 2.........')
	}, 5000)
})

const server = app.listen(3000, () => console.log('Server ready with process id ', process.pid))

process.on('SIGTERM', () => {
  server.close(() => {
    console.log('Process terminated')
  })
})

//process.kill(process.pid, 'SIGTERM') // to terminate the process gracefully so that all the pending tasks will complete its execution before scripts terminate
//process.kill(process.pid, 'SIGKILL') // to terminate the process immediately so any running tasks will be killed immediately