const mongoose = require('mongoose')
const config = require('config')
const colors = require('colors')
const db = config.get('mongoURI')

const connectDB = async() => {
    try {
        await mongoose.connect(db , { useUnifiedTopology: true , useNewUrlParser: true , useCreateIndex:true, useFindAndModify:false})
        console.log(`MongoDB connected`.white.bgGreen.bold)
    } catch (error) {
        console.log(error.red)
        // * Exits process with failure
        process.exit(1)
    }
}


module.exports = connectDB;
