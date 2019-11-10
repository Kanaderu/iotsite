import React, { Component } from 'react';
import { withStyles } from '@material-ui/core/styles';
import { Card, CardContent, CardHeader } from '@material-ui/core';
import { Scene } from '@esri/react-arcgis';

const styles = theme => ({
    card: {
        height: 700
    }
});

class MapSection extends Component {
    render() {
        const { classes } = this.props;
        return (
            <Card className={classes.card}>
                <CardHeader
                    title={this.props.title}
                    titleTypographyProps={{variant: 'h6'}}
                />
                <CardContent>
                    <Scene
                        style={{ width: '100%', height: '100vh' }}
                        mapProperties={{
                            basemap: 'satellite',
                            ground: 'world-elevation'
                        }}
                        viewProperties={{
                            camera: {
                                position: {
                                    x: -84.1935444,
                                    y: 39.7252851,
                                    z: 350
                                },
                                tilt: 75
                            }
                        }}
                    />
                </CardContent>
            </Card>
        )
    }
}

export default withStyles(styles)(MapSection);
