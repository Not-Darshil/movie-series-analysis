const express = require('express');
const server = express();
const mysql = require('mysql2');
const bodyParser = require("body-parser");
const path = require('path');
const cors = require('cors');

server.use(cors({ origin: "http://127.0.0.1:5500" }));

server.set('viewengine', 'pug');



server.use(bodyParser.json());
const port = 3000;
server.use(express.static(path.join(__dirname, "public")));

server.use(express.static("views"));


server.use(express.json());
server.use(cors({ origin: "http://127.0.0.1:5500" }));

server.get("/", (req, res) => {
    res.send("Welcome to the API!");
});

server.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
  });