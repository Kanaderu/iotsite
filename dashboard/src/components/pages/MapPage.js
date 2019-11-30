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

import { w3cwebsocket as W3CWebSocket } from 'websocket';
import { Map } from '@esri/react-arcgis';
import { loadModules } from 'esri-loader';

const styles = theme => ({
    root: {
        flexGrow: 1,
    },
    paper: {
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

class MapPage extends Component {
    constructor(props) {
        super(props);
        const group_name = 'test';
        this.client = new W3CWebSocket('ws://127.0.0.1:8088/ws/live/' + group_name + '/');
        this.state = {
            locations: {},
        }
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


    UNSAFE_componentWillMount() {
        this.client.onopen = () => {
            console.log('Websocket Client Connected');
        };

        this.client.onclose = () => {
            console.log('Websocket closed unexpectedly');
        };

        this.client.onmessage = (message) => {
            const data = JSON.parse(message.data);

            loadModules(['esri/Graphic']).then(([Graphic]) => {
                // create a point
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
        }
    }

    render() {
        const { classes } = this.props;

        // snapshot of state
        const data = this.state;

        return (
            <div classes={classes.root}>
                <ThemeProvider theme={this.theme}>
                    <Map
                        class="full-screen-map"
                        style={{ width: '100%', height: '85.5vh' }}
                        mapProperties={{
                            basemap: 'streets-navigation-vector'
                        }}
                        viewProperties={{
                            center: [-84.1745444, 39.7346451],
                            zoom: 14
                        }}
                    >
                        <Point locations={data.locations} />
                    </Map>
                </ThemeProvider>
            </div>
        )
    }
}

export default withStyles(styles)(MapPage);
