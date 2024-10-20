const express = require("express")
const router = express.Router()
const bcrypt = require("bcryptjs")
const jwt = require('jsonwebtoken')
const config = require('config')
const User = require('../models/User')
const { check, validationResult } = require("express-validator");


/* ------------------------------ Signup Route ------------------------------ */

//* @route   POST /api/auth/signup
//* @desc    This is the signup page
//* @access  PUBLIC

router.post(
    '/signup',
    [
      check('name', 'Name is required').not().isEmpty(),
      check('email', 'Please include a valid email').isEmail(),
      check('password','Please enter a password with 6 or more characters').isLength({ min: 6 }),
    ],
    async (req, res) => {
      const errors = validationResult(req);
      if (!errors.isEmpty()) {
        return res.status(400).json({ errors: errors.array() });
      }
      const { name, email, password } = req.body;
        try {
            const hash = await bcrypt.hashSync(password, 10);
            let user_duplicate = await User.findOne({email})
            
            if(user_duplicate){
                return res.status(400).json({msg:"User already exists"})
            }else{
                const user = new User({
                    name,
                    email,
                    password:hash,
                })
                await user.save()
                const payload = {
                    user:{
                        id:user.id
                    }
                }
                jwt.sign(payload,
                    config.get('jwtSecret'),
                    {expiresIn:360000},
                    (err,token)=> {
                        if(err) throw err;
                        res.json({token})
                        
                    } 
                )
            }

        } catch (err) {
            console.log(err.message)   
            res.status(500).send("Server Error")
        }
})

/* ------------------------------- Login route ------------------------------ */

//* @route   POST /api/auth/login
//* @desc    This is the login endpoint
//* @access  PUBLIC


router.post('/login',[
    check("email","Email is required").not().isEmpty(),
    check("password","Password is required").exists()
],async (req, res) => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      return res.status(400).json({ errors: errors.array() });
    }
    const { email, password } = req.body;
    try {
			let user = await User.findOne({ email });
			
			if(!user){
				return res.status(400).send({'errors':[{'msg':'Invlid credentials'}]})
            }
            const isMatch = await bcrypt.compare(password,user.password)

            if(!isMatch){
                return res.status(400).send({'errors':[{'msg':'Invlid credentials'}]})
            }
            
			const payload = {
				user:{
					id:user.id,
				}
			}
		
			jwt.sign(payload,
				config.get('jwtSecret'),
				{expiresIn:360000},
				(err,token)=> {
					if(err) throw err;
					res.json({token})
					
				} 
				)
    } catch (error) {
      console.log(error.message);
      res.status(500).send('Server Error');
    }
  })


module.exports = router
