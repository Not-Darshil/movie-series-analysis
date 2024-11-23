// is file me admin routes like admin signin/signup/chagne password / add a movie / dashboard jaise lofic likhne h

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