import React, { Component } from 'react';
import { Grid } from '@material-ui/core';
import { createMuiTheme, withStyles } from '@material-ui/core/styles';
import { ThemeProvider } from '@material-ui/styles';

import TableCard from './sections/TableCard';

import Paper from '@material-ui/core/Paper';
import Card from '@material-ui/core/Card';
import CardMedia from '@material-ui/core/CardMedia';
import CardContent from '@material-ui/core/CardContent';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import { red } from '@material-ui/core/colors';

import { auth } from '../actions';

import GenericChart from './sections/GenericChart';

const styles = theme => ({
    root: {
        flexGrow: 1,
    },
    card: {
        maxWidth: 345,
    },
    paper: {
        //height: 200,
    },
});

class TokenPage extends Component {
    state = {
        expanded: false,
        token: null
    }

    theme = createMuiTheme({
        palette: {
            primary: {
                main: '#0091EA'
            },
            secondary: {
                main: '#64dd17'
            }
        }
    });

    checkStatus(response) {
        if (response.status >= 200 && response.status < 300) {
            return response
        } else {
            var error = new Error(response.statusText);
            error.response = response;
            throw error
        }
    }

    generateToken = () => {
        const access = localStorage.access;
        fetch('/api/token/', {
            method: 'GET',
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${ access }`
            }
        })
            .then(this.checkStatus)
            .then(response => response.json())
            .then(response => {
                this.setState({
                    token: response.token
                });
            })
            .catch((error) => {
                console.log(error);
            });
    };

    render() {
        const { classes } = this.props;

        // snapshot of state
        const data = this.state;

        return (
            <div classes={classes.root}>
                <ThemeProvider theme={this.theme}>
                <Grid
                    container
                    spacing={2}
                    direction="column"
                    alignItems="center"
                    justify="center"
                    style={{ minHeight: '50vh' }}
                >
                    <Grid item xs={3}>
                        <Paper className={classes.paper}>
                            <Card className={classes.card}>
                                <CardContent>
                                    <Button variant="contained" color="primary" onClick={this.generateToken}>
                                        Generate Token
                                    </Button>
                                </CardContent>
                            </Card>
                        </Paper>
                    </Grid>
                    <Grid item xs={9} sm={9}>
                        <Paper className={classes.paper}>
                            <Card style={{maxWidth:1000, maxHeight:300}}>
                                <CardContent style={{maxWidth:1000, maxHeight:300}}>
                                    <Typography style={{maxWidth:1000, maxHeight:300, wordWrap: "break-word"}} variant="body2">
                                        Token: <br /><br />
                                        {this.state.token}
                                    </Typography>
                                </CardContent>
                            </Card>
                        </Paper>
                    </Grid>
                </Grid>
                <Grid container spacing={2}>
                    <Grid item xs={12} sm={12}>
                        <Paper className={classes.paper}>
                            {/*<TableCard />*/}
                        </Paper>
                    </Grid>
                </Grid>
                </ThemeProvider>
            </div>
        )
    }
}

export default withStyles(styles)(TokenPage);
