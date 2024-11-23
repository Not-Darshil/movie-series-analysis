// is movie me sare movies roites like fetch movies from db / fetch new comming / fetch reveiws from db of a movie / movie details wale logic likhne h

const express = require("express");
const db = require("../config/db");
const router = express.Router();
require("dotenv").config();
const authenticateToken = require("../middleware/authenticateToken");

const otpTemplate = require("../templates/otpEmailTemplate");
const otp_forgot_password_template = require("../templates/otpForgotPass");


router.get("/sheeeeer", (req, res) => {
    return null;
});

module.exports = router;