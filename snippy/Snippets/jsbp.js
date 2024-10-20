const express = require('express')
const app = express()
const colors = require('colors')
const PORT = process.env.PORT || 5000
const db = require('./config/db')


// * Init MiddleWare
app.use(express.json({extended:false}))

// * Connected MongoDB
db()

app.get('/' ,(req,res) => res.send('Home'))
app.listen(PORT, () => console.log(`Server running on port ${PORT}`.white.bgBlue.bold))

