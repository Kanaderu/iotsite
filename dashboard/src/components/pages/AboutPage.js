import React, { Component } from 'react';
import { Grid } from '@material-ui/core';
import { createMuiTheme, withStyles } from '@material-ui/core/styles';
import { ThemeProvider } from '@material-ui/styles';

import Paper from '@material-ui/core/Paper';
import Card from '@material-ui/core/Card';
import CardMedia from '@material-ui/core/CardMedia';
import CardContent from '@material-ui/core/CardContent';
import Typography from '@material-ui/core/Typography';
import { red } from '@material-ui/core/colors';

import GenericChart from './sections/GenericChart';

const styles = theme => ({
    root: {
        flexGrow: 1,
    },
    card: {
        maxWidth: 345,
    },
    media: {
        height: 0,
        paddingTop: '56.25%', // 16:9
    },
    expand: {
        transform: 'rotate(0deg)',
        marginLeft: 'auto',
        transition: theme.transitions.create('transform', {
            duration: theme.transitions.duration.shortest,
        }),
    },
    expandOpen: {
        transform: 'rotate(180deg)',
    },
    avatar: {
        backgroundColor: red[500],
    },
    paper: {
        //height: 200,
    },
});

class AboutPage extends Component {
    state = {
        expanded: false
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

    componentDidMount() {
    }

    render() {
        const { classes } = this.props;

        // snapshot of state
        const data = this.state;

        const handleExpandClick = () => {
            this.setState({expanded: !this.state.expanded});
        };

        return (
            <div classes={classes.root}>
                <ThemeProvider theme={this.theme}>
                <Grid container spacing={2}>
                    <Grid item xs={12} sm={12}>
                        <Paper className={classes.paper}>

                            <Card className={classes.card}>
                                <CardMedia
                                    className={classes.media}
                                    image="https://cdn.mos.cms.futurecdn.net/otjbibjaAbiifyN9uVaZyL-320-80.jpg"
                                    title="David Fan"
                                />
                                <CardContent>
                                    <Typography variant="body2" color="textSecondary" component="p">
                                    It a cat.
                                    </Typography>
                                </CardContent>
                            </Card>

                        </Paper>
                    </Grid>
                    <Grid item xs={12} sm={12}>
                        <Paper className={classes.paper}>

                        </Paper>
                    </Grid>
                </Grid>
                </ThemeProvider>
            </div>
        )
    }
}

export default withStyles(styles)(AboutPage);
