import React, { Component } from 'react';
import { lighten, withStyles } from '@material-ui/core/styles';
import LinearProgress from '@material-ui/core/LinearProgress';
import { Grid, Card, CardContent, CardHeader, Paper } from '@material-ui/core';
import CardMedia from '@material-ui/core/CardMedia';
import Typography from '@material-ui/core/Typography';
import { MDBIcon } from 'mdbreact';
import dayton_img from '../../../assets/dayton.jpeg'

const styles = theme => ({
    card: {
        //height: 400
    },
    media: {
        height: 140,
    },
});

const BorderLinearProgress = withStyles({
    root: {
        height: 10,
        backgroundColor: lighten('#5cff6c', 0.5),
        borderRadius: 20,
    },
    bar: {
        borderRadius: 20,
        backgroundColor: '#5cff6c',
    },
})(LinearProgress);

class DarkSkyCard extends Component {

    renderWeatherIcon(icon) {
        switch(icon) {
            case 'clear-day':
                return <MDBIcon icon="sun" size="5x" className="amber-text" />;
            case 'clear-night':
                return <MDBIcon icon="moon" size="5x" className="blue-text" />;
            case 'rain':
                return <MDBIcon icon="cloud-rain" size="5x" className="indigo-text" />;
            case 'snow':
                return <MDBIcon icon="snowflake" size="5x" className="blue-grey-text" />;
            case 'sleet':
                return <MDBIcon icon="snowflake" size="5x" className="light-blue-text" />;
            case 'wind':
                return <MDBIcon icon="wind" size="5x" className="blue-grey-text" />;
            case 'fog':
                return <MDBIcon icon="cloud" size="5x" className="grey-text" />;
            case 'cloudy':
                return <MDBIcon icon="cloud" size="5x" className="blue-grey-text" />;
            case 'partly-cloudy-day':
                return <MDBIcon icon="cloud-sun" size="5x" className="orange-text" />;
            case 'partly-cloudy-night':
                return <MDBIcon icon="cloud-moon" size="5x" className="deep-purple-text" />;
            default:
                return <MDBIcon icon="poo-storm" size="5x" className="brown-text" />;
        }
    }

    render() {
        const { classes } = this.props;

        const currentDay = new Date(this.props.data.time * 1000).toDateString();
        const currentTime = new Date();
        const percentTime = 100*(currentTime.getHours()*60.0 + currentTime.getMinutes()) / 1440.0;
        return (
            <Card className={classes.card}>
                <CardMedia
                    className={classes.media}
                    image={dayton_img}
                    title="Dayton"
                />
                <CardHeader
                    title={this.props.title}
                    titleTypographyProps={{variant: 'h6'}}
                />
                <CardContent>
                    <Grid
                        container
                        spacing={2}
                    >
                        <Grid item xs={12}>
                            <Typography variant="h4" color="textSecondary" component="p">
                                Dayton
                            </Typography>
                            <Typography variant="h4" color="textSecondary" component="p">
                                { currentDay }
                            </Typography>
                            <hr />
                        </Grid>
                    </Grid>
                    <Grid
                        justify="space-between"
                        container
                        spacing={6}
                    >
                        <Grid item>
                            <Typography variant="h2" display="inline" align="left" component="p">
                                    { this.props.data.apparentTemperature } °F
                            </Typography>
                        </Grid>
                        <Grid item>
                            <Typography variant="body2" display="inline" align="right" component="p">
                                    { this.renderWeatherIcon(this.props.data.icon) }
                            </Typography>
                            <Typography variant="body2" color="textSecondary" component="p">
                                {this.props.data.summary}
                            </Typography>
                        </Grid>
                    </Grid>
                    <Grid
                        justify="space-between"
                        container
                        spacing={2}
                    >
                        <Grid item>
                            <Typography variant="body2" color="textSecondary" component="p">
                                <MDBIcon icon="tint" size="lg" className="cyan-text pr-2"/>{ this.props.data.precipProbability * 100.0}% Precipitation
                            </Typography>
                        </Grid>
                        <Grid item>
                            <Typography variant="body2" color="textSecondary" component="p">
                                <MDBIcon icon="leaf" size="lg" className="grey-text pr-2"/>{ this.props.data.windSpeed } mi/h Winds
                            </Typography>
                        </Grid>
                        <Grid item>
                            <Typography variant="body2" color="textSecondary" component="p">
                                <MDBIcon icon="water" size="lg" className="blue-text pr-2" />{ this.props.data.humidity * 100.0}% Humidity
                            </Typography>
                        </Grid>
                        <Grid item xs={12}>
                                <BorderLinearProgress
                                    className={classes.margin}
                                    variant="determinate"
                                    color="secondary"
                                    value={percentTime}
                                />
                                <ul className="list-unstyled d-flex justify-content-between font-small text-muted mb-4">
                                    <li className="pl-4">3AM</li>
                                    <li>7AM</li>
                                    <li>11PM</li>
                                    <li>3PM</li>
                                    <li className="pr-4">7PM</li>
                                </ul>
                        </Grid>
                    </Grid>
                </CardContent>
            </Card>
        )
    }
}

export default withStyles(styles)(DarkSkyCard);
