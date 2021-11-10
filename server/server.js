const express = require('express');
const mysql      = require('mysql');


const routes = require('./routes')
const config = require('./config.json')

const app = express();

// Route 1 - home page
app.get('/home', routes.home)

// Route 2 - head2head teams page
app.get('/teams/head2head', routes.teamshead2head)

// Route 3 - head2head players page
app.get('/players/head2head', routes.playershead2head)

// Route 4 - teams page
app.get('/teams', routes.teams)

// Route 5 - players page 
app.get('/players', routes.players)

// Route 6 - coments page
app.get('/comments', routes.comments)

app.listen(config.server_port, () => {
    console.log(`Server running at http://${config.server_host}:${config.server_port}/`);
});

module.exports = app;
