import React, { Component } from 'react';
import { lighten, withStyles } from '@material-ui/core/styles';
import LinearProgress from '@material-ui/core/LinearProgress';
import { Grid, Card, CardContent, CardHeader } from '@material-ui/core';
import CardMedia from '@material-ui/core/CardMedia';
import Typography from '@material-ui/core/Typography';
import { IconContext } from "react-icons";
import { WiDaySunny, WiMoonWaxingCrescent4, WiRain, WiSnowflakeCold, WiSleet, WiStrongWind, WiFog, WiCloudy, WiDayCloudy, WiNightAltCloudy, WiWindDeg, WiRaindrop, WiHumidity } from "react-icons/wi";

import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import ListItemAvatar from '@material-ui/core/ListItemAvatar';
import Avatar from '@material-ui/core/Avatar';

import dayton_img from '../../../assets/dayton.jpeg'

const styles = theme => ({
    card: {
        //height: 400
    },
    media: {
        height: 140,
    },
    list: {
        width: '100%',
        backgroundColor: theme.palette.background.paper,
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
                return <WiDaySunny />;
            case 'clear-night':
                return <WiMoonWaxingCrescent4 />;
            case 'rain':
                return <WiRain />;
            case 'snow':
                return <WiSnowflakeCold />;
            case 'sleet':
                return <WiSleet />;
            case 'wind':
                return <WiStrongWind />;
            case 'fog':
                return <WiFog />;
            case 'cloudy':
                return <WiCloudy />;
            case 'partly-cloudy-day':
                return <WiDayCloudy />;
            case 'partly-cloudy-night':
                return <WiNightAltCloudy />;
            default:
                return <WiWindDeg />;
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
                                <IconContext.Provider value={{ color: "blue", className: "global-class-name", size: 60 }}>
                                    { this.renderWeatherIcon(this.props.data.icon) }
                                </IconContext.Provider>
                            </Typography>
                            <Typography variant="body2" color="textSecondary" component="p">
                                {this.props.data.summary}
                            </Typography>
                        </Grid>
                    </Grid>
                    <List className={classes.list}>
                        <ListItem>
                            <ListItemAvatar>
                                <Avatar>
                                    <IconContext.Provider value={{ color: "blue", size: 50 }}>
                                        <WiRaindrop />
                                    </IconContext.Provider>
                                </Avatar>
                            </ListItemAvatar>
                            <ListItemText primary="Precipitation Probability" secondary={ parseFloat(this.props.data.precipProbability * 100.0).toFixed(2) + '%' } />
                            <ListItemAvatar>
                                <Avatar>
                                    <IconContext.Provider value={{ color: "white", size: 50 }}>
                                        <WiStrongWind />
                                    </IconContext.Provider>
                                </Avatar>
                            </ListItemAvatar>
                            <ListItemText primary="Wind Speed" secondary={ parseFloat(this.props.data.windSpeed).toFixed(2) + 'mi/h' } />
                            <ListItemAvatar>
                                <Avatar>
                                    <IconContext.Provider value={{ color: "green", size: 50 }}>
                                        <WiHumidity />
                                    </IconContext.Provider>
                                </Avatar>
                            </ListItemAvatar>
                            <ListItemText primary="Humidity" secondary={ parseFloat(this.props.data.humidity * 100.0).toFixed(2) + '%' } />
                        </ListItem>
                    </List>
                    <Grid
                        justify="space-between"
                        container
                        spacing={2}
                    >
                        <Grid item xs={12}>
                                <BorderLinearProgress
                                    className={classes.margin}
                                    variant="determinate"
                                    color="secondary"
                                    value={percentTime}
                                />
                        </Grid>
                        <Grid item xs={2}>
                            <Typography>
                                12AM
                            </Typography>
                        </Grid>
                        <Grid item xs={2}>
                            <Typography>
                                4AM
                            </Typography>
                        </Grid>
                        <Grid item xs={2}>
                            <Typography>
                                8AM
                            </Typography>
                        </Grid>
                        <Grid item xs={2}>
                            <Typography>
                                12PM
                            </Typography>
                        </Grid>
                        <Grid item xs={2}>
                            <Typography>
                                4PM
                            </Typography>
                        </Grid>
                        <Grid item xs={1}>
                            <Typography>
                                8PM
                            </Typography>
                        </Grid>
                        <Grid item xs={1}>
                            <Typography align='right'>
                                12AM
                            </Typography>
                        </Grid>
                    </Grid>
                </CardContent>
            </Card>
        )
    }
}

export default withStyles(styles)(DarkSkyCard);
