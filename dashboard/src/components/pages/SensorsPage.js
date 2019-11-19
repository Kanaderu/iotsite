import React, { Component } from 'react';
import { Grid } from '@material-ui/core';
import { createMuiTheme, withStyles } from '@material-ui/core/styles';
import { ThemeProvider } from '@material-ui/styles';

import Paper from '@material-ui/core/Paper';

import GenericChart from './sections/GenericChart';

const styles = theme => ({
    root: {
        flexGrow: 1,
    },
    paper: {
        //height: 200,
    },
});

class SensorsPage extends Component {
    state = {
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

    checkStatus(response) {
        if (response.status >= 200 && response.status < 300) {
            return response
        } else {
            var error = new Error(response.statusText)
            error.response = response
            throw error
        }
    }

    fetchFeather(url) {
        fetch(url)
            .then(this.checkStatus)
            .then(response => response.json())
            .then(responses => {
                this.setState({
                    feather: responses.results.reverse().map(response => ({
                        sensor_id: response.sensor_id,
                        sensor: response.sensor,
                        metadata: response.metadata,
                        data: response.data
                    }))
                });
            })
            .catch((error) => {
                console.log(error);
            });
    }

    fetchLoRaGateway(url) {
        fetch(url)
            .then(this.checkStatus)
            .then(response => response.json())
            .then(responses => {
                this.setState({
                    lora: responses.results.reverse().map(response => ({
                        sensor_id: response.sensor_id,
                        sensor: response.sensor,
                        metadata: response.metadata,
                        data: response.data
                    }))
                });
            })
            .catch((error) => {
                console.log(error);
            });
    }

    componentDidMount() {
        this.fetchLoRaGateway('/ws/api/sensors/?sensor=LG');
        this.fetchFeather('/ws/api/sensors/?sensor=F');
    }

    render() {
        const { classes } = this.props;

        // snapshot of state
        const data = this.state;

        const months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                        "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"];
        // lora data
        const lora_labels = data.lora.map((data) => {
            const d = new Date(data.metadata.timestamp);
            return months[d.getMonth()] + "-" + ('0' + d.getDate()).slice(-2) + " " + ('0' + d.getHours()).slice(-2) + ":" + ('0' + d.getMinutes()).slice(-2);
        });
        const lora_data = [
            {
                data: data.lora.map((data) => {
                    return parseFloat(data.data[5].data).toFixed(2);
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
                    return parseFloat(data.data[6].data).toFixed(2);
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
            const d = new Date(data.metadata.timestamp);
            return months[d.getMonth()] + "-" + ('0' + d.getDate()).slice(-2) + " " + ('0' + d.getHours()).slice(-2) + ":" + ('0' + d.getMinutes()).slice(-2);
        });
        const feather_data = [
            {
                data: data.feather.map((data) => {
                    return parseFloat(data.data[0].data).toFixed(2);
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
                    return parseFloat(data.data[1].data).toFixed(2);
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

        return (
            <div classes={classes.root}>
                <ThemeProvider theme={this.theme}>
                <Grid container spacing={2}>
                    <Grid item xs={12} sm={12}>
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
                    <Grid item xs={12} sm={12}>
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
                </Grid>
                </ThemeProvider>
            </div>
        )
    }
}

export default withStyles(styles)(SensorsPage);
