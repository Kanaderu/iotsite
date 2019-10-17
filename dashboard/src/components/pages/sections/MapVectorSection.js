import React, { Component } from 'react';
import { withStyles } from '@material-ui/core/styles';
import { Card, CardContent, CardHeader, Paper } from '@material-ui/core';
import { Scene } from '@esri/react-arcgis';

const styles = theme => ({
    card: {
        height: 600
    }
});

class MapVectorSection extends Component {
    render() {
        const { classes } = this.props;
        return (
            <Card className={classes.card}>
                <CardHeader
                    title={this.props.title}
                    titleTypographyProps={{variant: 'h6'}}
                />
                <CardContent>
                        <link rel="stylesheet" href="https://js.arcgis.com/4.10/esri/css/main.css"></link>
                        <Scene
                            mapProperties={{
                                basemap: 'streets-navigation-vector',
                                ground: 'world-elevation'
                            }}
                            viewProperties={{
                                center: [-84.1935444, 39.7316451 ],
                                zoom: 16.5
                            }}
                        />
                </CardContent>
            </Card>
        )
    }
}

export default withStyles(styles)(MapVectorSection);
