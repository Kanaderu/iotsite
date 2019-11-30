import React, { Component } from 'react';
import { Grid } from '@material-ui/core';
import { createMuiTheme, withStyles } from '@material-ui/core/styles';
import { ThemeProvider } from '@material-ui/styles';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import Paper from '@material-ui/core/Paper';

import { w3cwebsocket as W3CWebSocket } from 'websocket';
import { Map } from '@esri/react-arcgis';
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

const Point = (props) => {
    Object.keys(props.locations).map((location, id) => {
        // remove old graphic if it exists
        props.locations[`${location}`].oldGraphic &&
        props.view.graphics.remove(props.locations[`${location}`].oldGraphic);

        // add new graphic
        props.locations[`${location}`].graphic &&
        props.view.graphics.add(props.locations[`${location}`].graphic);

        return null;
    });
    return null;
};

const host = window.location.host;

class MapPage extends Component {
    constructor(props) {
        super(props);
        this.state = {
            locations: {},
            roomName: null,
            validRoomName: false,
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

        const address = 'wss://' + host + '/ws/live/' + this.state.roomName + '/';
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
        };

        this.setState({validRoomName: true})
    };

    render() {
        const { classes } = this.props;

        // snapshot of state
        const data = this.state;

        if(!data.validRoomName) {
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
                        <Map
                            class="full-screen-map"
                            style={{width: '100%', height: '85.5vh'}}
                            mapProperties={{
                                basemap: 'streets-navigation-vector'
                            }}
                            viewProperties={{
                                center: [-84.1745444, 39.7346451],
                                zoom: 14
                            }}
                        >
                            <Point locations={data.locations}/>
                        </Map>
                    </ThemeProvider>
                </div>
            )
        }
    }
}

export default withStyles(styles)(MapPage);
