import React, { Component } from 'react';
import { Grid } from '@material-ui/core';
import { createMuiTheme, withStyles } from '@material-ui/core/styles';
import { ThemeProvider } from '@material-ui/styles';

import Paper from '@material-ui/core/Paper';

import DarkSkyCard from './sections/DarkSkyCard';
import MapSection from './sections/MapSection';
import MapVectorSection from './sections/MapVectorSection';
import GenericChart from './sections/GenericChart';

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
            time: null,
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
        flags: {},
        feather: [],
        lora: []
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

    fetchFeather() {
        fetch('https://udsensors.tk/ws/api/FeatherV2/')
            .then(response => response.json())
            .then(responses => {
                this.setState({
                    feather: responses.map(response => ({
                        dev_id: response.dev_id,
                        metadata: response.metadata,
                        data: response.data,
                    }))
                });
            })
            .catch((error) => {
                console.log(error);
            });
    }

    fetchLoRaGateway() {
        fetch('https://udsensors.tk/ws/api/LoRaGateway/')
            .then(response => response.json())
            .then(responses => {
                this.setState({
                    lora: responses.map(response => ({
                        app_id: response.app_id,
                        dev_id: response.dev_id,
                        hardware_serial: response.hardware_serial,
                        port: response.port,
                        counter: response.counter,
                        payload_raw: response.payload_raw,
                        payload_fields: response.payload_fields,
                        metadata: response.metadata,
                        downlink_url: response.downlink_url
                    }))
                });
            })
            .catch((error) => {
                console.log(error);
            });
    }

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
        this.fetchDarkSkyData();
        this.fetchLoRaGateway();
        this.fetchFeather();
    }

    render() {
        const { classes } = this.props;

        // snapshot of state
        const data = this.state;

        const months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                        "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"];
        // lora data
        const lora_labels = data.lora.map((data) => {
            const d = new Date(data.metadata.time);
            return months[d.getMonth()] + "-" + ('0' + d.getDate()).slice(-2) + " " + ('0' + d.getHours()).slice(-2) + ":" + ('0' + d.getMinutes()).slice(-2);
        });
        const lora_data = [
            {
                data: data.lora.map((data) => {
                    return parseFloat(data.payload_fields.t1).toFixed(2);
                }),
                label: 'T1',
                backgroundColor: 'rgba(75,192,192,0.4)',
                pointBorderColor: 'rgba(75,192,192,1)',
                borderColor: 'rgba(75,192,192,1)',
                pointBackgroundColor: '#fff',
                pointHoverBackgroundColor: 'rgba(75,192,192,1)',
                pointHoverBorderColor: 'rgba(220,220,220,1)',
            },
            {
                data: data.lora.map((data) => {
                    return parseFloat(data.payload_fields.t2).toFixed(2);
                }),
                label: 'T2',
                backgroundColor: 'rgba(255,100,100,0.4)',
                pointBorderColor: 'rgba(255,192,192,1)',
                borderColor: 'rgba(255,100,100,1)',
                pointBackgroundColor: '#fff',
                pointHoverBackgroundColor: 'rgba(255,100,100,1)',
                pointHoverBorderColor: 'rgba(220,220,220,1)',
            }
        ];

        // feather data
        const feather_labels = data.feather.map((data) => {
            const d = new Date(data.metadata.time);
            return months[d.getMonth()] + "-" + ('0' + d.getDate()).slice(-2) + " " + ('0' + d.getHours()).slice(-2) + ":" + ('0' + d.getMinutes()).slice(-2);
        });
        const feather_data = [
            {
                data: data.feather.map((data) => {
                    return parseFloat(data.data[0].sensor_data).toFixed(2);
                }),
                label: '1',
                backgroundColor: 'rgba(75,192,192,0.4)',
                pointBorderColor: 'rgba(75,192,192,1)',
                borderColor: 'rgba(75,192,192,1)',
                pointBackgroundColor: '#fff',
                pointHoverBackgroundColor: 'rgba(75,192,192,1)',
                pointHoverBorderColor: 'rgba(220,220,220,1)',
            },
            {
                data: data.feather.map((data) => {
                    return parseFloat(data.data[1].sensor_data).toFixed(2);
                }),
                label: '2',
                backgroundColor: 'rgba(255,100,100,0.4)',
                pointBorderColor: 'rgba(255,192,192,1)',
                borderColor: 'rgba(255,100,100,1)',
                pointBackgroundColor: '#fff',
                pointHoverBackgroundColor: 'rgba(255,100,100,1)',
                pointHoverBorderColor: 'rgba(220,220,220,1)',
            }
        ];

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
                pointBorderColor: 'rgba(75,192,192,1)',
                borderColor: 'rgba(75,192,192,1)',
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
                pointBorderColor: 'rgba(255,51,51,1)',
                borderColor: 'rgba(255,51,51,1)',
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
                pointBorderColor: 'rgba(0,255,154,1)',
                borderColor: 'rgba(0,255,154,1)',
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
                pointBackgroundColor: '#fff',
                pointHoverBackgroundColor: 'rgba(64,64,64,1)',
                pointHoverBorderColor: 'rgba(220,220,220,1)',
            }
        ];
        return (
            <div classes={classes.root}>
                <ThemeProvider theme={this.theme}>
                <Grid container spacing={2}>
                    <Grid item xs={12} sm={12}>
                        <Paper className={classes.paper}>
                            <DarkSkyCard
                                data={data.currently}
                                title="DarkSky"
                            />
                        </Paper>
                    </Grid>
                    <Grid item xs={12} sm={6}>
                        <Paper className={classes.paper}>
                            <GenericChart
                                title="LoRa Gateway Temperatures"
                                labels={lora_labels}
                                data={lora_data}
                                xlabel="Timestamp"
                                ylabel="Temperature (C)"
                            />
                        </Paper>
                    </Grid>
                    <Grid item xs={12} sm={6}>
                        <Paper className={classes.paper}>
                            <GenericChart
                                title="Feather Temperatures"
                                labels={feather_labels}
                                data={feather_data}
                                xlabel="Timestamp"
                                ylabel="Temperature (C)"
                            />
                        </Paper>
                    </Grid>
                    <Grid item xs={12} sm={4}>
                        <Paper className={classes.paper}>
                            <GenericChart
                                title="Current Temperature"
                                labels={darksky_current_labels}
                                data={darksky_current_data}
                                xlabel="Timestamp"
                                ylabel="Temperature"
                            />
                        </Paper>
                    </Grid>
                    <Grid item xs={12} sm={4}>
                        <Paper className={classes.paper}>
                            <GenericChart
                                title="Daily Temperature High/Low"
                                labels={darksky_daily_labels}
                                data={darksky_daily_temp_data}
                                xlabel="Day"
                                ylabel="Temperature"
                            />
                        </Paper>
                    </Grid>
                    <Grid item xs={12} sm={4}>
                        <Paper className={classes.paper}>
                            <GenericChart
                                title="Percentages"
                                labels={darksky_daily_labels}
                                data={darksky_daily_precip_data}
                                xlabel="Day"
                                ylabel="Percentage"
                            />
                        </Paper>
                    </Grid>
                    <Grid item xs={12} sm={6}>
                        <Paper className={classes.paper}>
                            <MapSection
                                title="ArcGIS Satellite Elevation Map"
                            />
                        </Paper>
                    </Grid>
                    <Grid item xs={12} sm={6}>
                        <Paper className={classes.paper}>
                            <MapVectorSection
                                title="ArcGIS Map Vector"
                            />
                        </Paper>
                    </Grid>
                </Grid>
                </ThemeProvider>
            </div>
        )
    }
}

export default withStyles(styles)(DashboardPage);
