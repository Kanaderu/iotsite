import React, { Component } from 'react';
import { withStyles } from '@material-ui/core/styles';
import { Grid } from '@material-ui/core';
import { createMuiTheme } from '@material-ui/core/styles';
import { ThemeProvider } from '@material-ui/styles';
import { MDBRow } from 'mdbreact';

import Button from '@material-ui/core/Button';
import Paper from '@material-ui/core/Paper';

import DarkSkyCard from './sections/DarkSkyCard';
import ChartSection4 from './sections/ChartSection4';
import ChartSection5 from './sections/ChartSection5';
import ChartSection6 from './sections/ChartSection6';
import MapSection from './sections/MapSection';
import MapVectorSection from './sections/MapVectorSection';
import LoRaGatewayChart from './sections/LoRaGatewayChart';
import GenericChart from './sections/GenericChart';
//import Test from './Test';

const styles = theme => ({
    root: {
        flexGrow: 1,
    },
    paper: {
        //height: 200,
    },
});

class DashboardPage extends Component {
    state = {
        latitude: undefined,
        longitude: undefined,
        timezone: undefined,
        offset: undefined,
        currently: {
            data: []
        },
        hourly: {
            data: []
        },
        daily: {
            data: []
        },
        minutely: {
            data: []
        },
        flags: {}
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


    fetchDarkSkyData() {
        fetch('https://udsensors.tk/ws/darksky/')
            .then(response => response.json())
            .then((data) => {
                this.setState({
                    latitude: data.latitude,
                    longitude: data.longitude,
                    timezone: data.timezone,
                    offset: data.offset,
                    currently: data.currently,
                    hourly: data.hourly,
                    daily: data.daily,
                    minutely: data.minutely,
                    flags: data.flags
                });
            })
            .catch((error) => {
                console.log(error);
            })
    }

    componentDidMount() {
        this.fetchDarkSkyData()
    }

    render() {
        const { classes } = this.props;

        const data = this.state;
        //// darksky data
        // current
        const darksky_current_labels = data.hourly.data.map((data) => {
            const date = new Date(data.time*1000);
            return date.getHours();
        });
        const darksky_current_data = [
            {
                data: data.hourly.data.map((data) => (data.temperature)),
                label: 'Temperature',
                backgroundColor: 'rgba(75,192,192,0.4)',
                borderColor: 'rgba(75,192,192,1)',
                pointBorderColor: 'rgba(75,192,192,1)',
                pointBackgroundColor: '#fff',
                pointHoverBackgroundColor: 'rgba(75,192,192,1)',
                pointHoverBorderColor: 'rgba(220,220,220,1)',
            },
            {
                data: data.hourly.data.map((data) => (data.apparentTemperature)),
                label: 'Apparent Temperature',
                backgroundColor: 'rgba(255,100,100,0.4)',
                pointBorderColor: 'rgba(255,192,192,1)',
                borderColor: 'rgba(255,100,100,1)',
                pointBorderColor: 'rgba(255,100,100,1)',
                pointBackgroundColor: '#fff',
                pointHoverBackgroundColor: 'rgba(255,100,100,1)',
                pointHoverBorderColor: 'rgba(220,220,220,1)',
            }
        ];
        // daily temp
        const weekday = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
        const darksky_daily_labels = data.daily.data.map((data) => {
            const date = new Date(data.time*1000);
            return weekday[date.getDay()];
        });
        const darksky_daily_temp_data = [
            {
                data: data.daily.data.map((data) => (data.temperatureHigh)),
                label: 'Temperature High',
                backgroundColor: 'rgba(255,51,51,0.4)',
                borderColor: 'rgba(255,51,51,1)',
                pointBorderColor: 'rgba(255,51,51,1)',
                pointBackgroundColor: '#fff',
                pointHoverBackgroundColor: 'rgba(255,51,51,1)',
                pointHoverBorderColor: 'rgba(220,220,220,1)',
            },
            {
                data: data.daily.data.map((data) => (data.temperatureLow)),
                label: 'Temperature Low',
                backgroundColor: 'rgba(75,192,192,0.4)',
                pointBorderColor: 'rgba(75,192,192,1)',
                borderColor: 'rgba(75,192,192,1)',
                pointBorderColor: 'rgba(75,192,192,1)',
                pointBackgroundColor: '#fff',
                pointHoverBackgroundColor: 'rgba(75,192,192,1)',
                pointHoverBorderColor: 'rgba(220,220,220,1)',
            }
        ];
        // daily precip
        const darksky_daily_precip_data = [
            {
                data: data.daily.data.map((data) => (data.precipProbability * 100)),
                label: 'Precipitation',
                backgroundColor: 'rgba(0,255,154,0.4)',
                borderColor: 'rgba(0,255,154,1)',
                pointBorderColor: 'rgba(0,255,154,1)',
                pointBackgroundColor: '#fff',
                pointHoverBackgroundColor: 'rgba(0,255,154,1)',
                pointHoverBorderColor: 'rgba(220,220,220,1)',
            },
            {
                data: data.daily.data.map((data) => (data.cloudCover * 100)),
                label: 'Cloud Coverage',
                backgroundColor: 'rgba(0,102,204,0.4)',
                pointBorderColor: 'rgba(0,102,204,1)',
                borderColor: 'rgba(0,102,204,1)',
                pointBorderColor: 'rgba(0,102,204,1)',
                pointBackgroundColor: '#fff',
                pointHoverBackgroundColor: 'rgba(0,102,204,1)',
                pointHoverBorderColor: 'rgba(220,220,220,1)',
            },
            {
                data: data.daily.data.map((data) => (data.humidity * 100)),
                label: 'Humidity',
                backgroundColor: 'rgba(64,64,64,0.4)',
                pointBorderColor: 'rgba(64,64,64,1)',
                borderColor: 'rgba(64,64,64,1)',
                pointBorderColor: 'rgba(64,64,64,1)',
                pointBackgroundColor: '#fff',
                pointHoverBackgroundColor: 'rgba(64,64,64,1)',
                pointHoverBorderColor: 'rgba(220,220,220,1)',
            }
        ];
        return (
            <div classes={classes.root}>
                {/*
                <MDBRow className="mb-4">
                    <DarkSkyCard data={data} />
                    <LoRaGatewayChart />
                </MDBRow>
                <MDBRow className="mb-4">
                    <ChartSection4 data={data} />
                    <ChartSection5 data={data} />
                    <ChartSection6 data={data} />
                </MDBRow>
                <MDBRow className="mb-6">
                    <MapSection />
                    <MapVectorSection />
                </MDBRow>
                <Test />
                */}
                <ThemeProvider theme={this.theme}>
                <Grid container spacing={2}>
                    <Grid item xs={12} sm={4}>
                        <Paper className={classes.paper}>
                            <GenericChart
                                title="Current Temperature"
                                labels={darksky_current_labels}
                                data={darksky_current_data}
                            />
                        </Paper>
                    </Grid>
                    <Grid item xs={12} sm={4}>
                        <Paper className={classes.paper}>
                            <GenericChart
                                title="Daily Temperature High/Low"
                                labels={darksky_daily_labels}
                                data={darksky_daily_temp_data}
                            />
                        </Paper>
                    </Grid>
                    <Grid item xs={12} sm={4}>
                        <Paper className={classes.paper}>
                            <GenericChart
                                title="Percentages"
                                labels={darksky_daily_labels}
                                data={darksky_daily_precip_data}
                            />
                        </Paper>
                    </Grid>
                    <Grid item xs={12} sm={6}>
                        <Paper className={classes.paper}>
                            <GenericChart
                                title="Current Temperature"
                                labels={darksky_current_labels}
                                data={darksky_current_data}
                            />
                        </Paper>
                    </Grid>
                    <Grid item xs={12} sm={6}>
                        <Paper className={classes.paper}>
                            <GenericChart
                                title="Daily Temperature High/Low"
                                labels={darksky_daily_labels}
                                data={darksky_daily_temp_data}
                            />
                        </Paper>
                    </Grid>
                    {/*
                    <Grid item xs={12} sm={4}>
                        <Paper className={classes.paper}>
                            <GenericChart
                                title="Percentages"
                                labels={darksky_daily_labels}
                                data={darksky_daily_precip_data}
                            />
                        </Paper>
                    </Grid>
                    */}
                </Grid>
                </ThemeProvider>
            </div>
        )
    }
}

export default withStyles(styles)(DashboardPage);
