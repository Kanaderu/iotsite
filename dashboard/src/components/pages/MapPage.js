import React, { Component } from 'react';
import { Grid } from '@material-ui/core';
import { createMuiTheme, withStyles } from '@material-ui/core/styles';
import { ThemeProvider } from '@material-ui/styles';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import Paper from '@material-ui/core/Paper';

import { w3cwebsocket as W3CWebSocket } from 'websocket';
import WebMapView from '../map/Map';
import { loadModules } from 'esri-loader';

const styles = theme => ({
    root: {
        flexGrow: 1,
    },
    paper: {
        padding: theme.spacing(3, 2),
        //height: 200,
    },
});

const protocol = window.location.protocol;
const host = window.location.host;

const wsStart = protocol == "https:" ? "wss://" : "ws://";

class MapPage extends Component {
    constructor(props) {
        super(props);
        this.state = {
            locations: {},
            roomName: null,
            validRoomName: false,
            geojsonLayer: null,
            initialized: false,
        };
        this.client = null;
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

    onSubmit = e => {
        e.preventDefault();

        const address = wsStart + host + '/live/' + this.state.roomName + '/';
        this.client = new W3CWebSocket(address);

        this.client.onopen = () => {
            console.log('Websocket Client Connected');
        };

        this.client.onclose = () => {
            console.log('Websocket closed unexpectedly');
            this.setState({validRoomName: false})
        };

        this.client.onmessage = (message) => {
            const data = JSON.parse(message.data);

            switch(data.type) {
              case 'sensor_initialize':
                break;
              case 'sensor_message':
                loadModules(['esri/Graphic']).then(([Graphic]) => {
                    const point = {
                        type: "point", // autocasts as new Point()
                        x: data.lon,
                        y: data.lat,
                    };

                    // Add the geometry and symbol to a new graphic
                    const graphic = Graphic({
                        geometry: point,
                        //symbol: fillSymbol
                        attributes: {
                          Name: data.message
                        },
                        popupTemplate: {
                          title: "{Name}",
                          content: [{
                            type: "fields",
                            fieldInfos: [
                              {
                                fieldName: "Name"
                              },
                              {
                                fieldName: "Owner"
                              },
                              {
                                fieldName: "Length"
                              }
                            ]
                          }]
                        }
                    });

                    this.setState((prevState, props) => {
                        // update oldGraphic if `graphic` in the previous state exists
                        const prevLoc = prevState.locations[`${data.message}`];
                        const oldGraphic = (prevLoc && prevLoc.graphic) ? prevLoc.graphic : null;

                        const newState = { ...prevState };
                        newState.locations[`${data.message}`] = {
                            lat: data.lat,
                            lon: data.lon,
                            oldGraphic: oldGraphic,
                            graphic: graphic
                        };
                        return newState;
                    });
                }).catch((err) => console.error(err));
                break;
            }
        };

        this.setState({validRoomName: true})
    };

    render() {
        const { classes } = this.props;

        // snapshot of state
        const data = this.state;

        if(!data.validRoomName && !data.initialized) {
            return (
                <div className={classes.root}>
                    <ThemeProvider theme={this.theme}>
                        <Paper className={classes.paper} style={{ minWidth: '100vw', minHeight: '85.5vh' }}>
                            <form noValidate autoComplete="off" onSubmit={this.onSubmit}>
                                <Grid
                                    container
                                    spacing={2}
                                    direction="column"
                                    alignItems="center"
                                    justify="center"
                                    style={{ minHeight: '50vh' }}
                                >
                                    <Grid item xs={3}>
                                        <TextField
                                            id="standard-required"
                                            label="Room Name"
                                            onChange={e => this.setState({roomName: e.target.value})}
                                        />
                                    </Grid>
                                    <Grid item xs={3}>
                                        <Button type="submit" variant="contained" color="primary">
                                            Submit
                                        </Button>
                                    </Grid>
                                </Grid>
                            </form>
                        </Paper>
                    </ThemeProvider>
                </div>
            )
        } else {
            return (
                <div classes={classes.root}>
                    <ThemeProvider theme={this.theme}>
                      <WebMapView locations={data.locations} />
                    </ThemeProvider>
                </div>
            )
        }
    }
}

export default withStyles(styles)(MapPage);
