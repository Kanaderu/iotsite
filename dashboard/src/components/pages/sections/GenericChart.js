import React, { Component } from 'react';
import { withStyles } from '@material-ui/core/styles';
import { Card, CardContent, CardHeader, Paper } from '@material-ui/core';
import { Chart, Line } from 'react-chartjs-2';
import Hammer from 'react-hammerjs';
import zoom from 'chartjs-plugin-zoom';

const styles = theme => ({
    card: {
        //height: 400
    }
});

class GenericChart extends Component {

    UNSAFE_componentWillMount(){
        Chart.plugins.register(zoom);
    }

    render(){
        const { classes } = this.props;
        const dataLine = {
            labels: this.props.labels,

            datasets: this.props.data.map((item) => {
                return (
                    {
                        label: item.label,
                        fill: false,
                        lineTension: 0.1,
                        backgroundColor: item.backgroundColor,
                        borderColor: item.borderColor,
                        borderCapStyle: 'butt',
                        borderDash: [],
                        borderDashOffset: 0.0,
                        borderJoinStyle: 'miter',
                        pointBorderColor: item.pointBorderColor,
                        pointBackgroundColor: item.pointBackgroundColor,
                        pointBorderWidth: 1,
                        pointHoverRadius: 5,
                        pointHoverBackgroundColor: item.pointHoverBackgroundColor,
                        pointHoverBorderColor: item.pointHoverBorderColor,
                        pointHoverBorderWidth: 2,
                        pointRadius: 1,
                        pointHitRadius: 10,
                        data: item.data
                    }
                );
            })
        };
        const opts = {
            responsive: true,
            scales: {
                xAxes: [{
                    ticks: { display: true },
                    scaleLabel: {
                        display: true,
                        labelString: this.props.xlabel
                    },
                    gridLines: {
                        display: true,
                        drawBorder: true
                    }
                }],
                yAxes: [{
                    ticks: { display: true },
                    scaleLabel: {
                        display: true,
                        labelString: this.props.ylabel
                    },
                    gridLines: {
                        display: true,
                        drawBorder: true
                    }
                }]
            },
            plugins: {
                zoom: {
                    pan: {
                        enabled: true,
                        mode: 'xy'
                    },
                    zoom: {
                        enabled: true,
                        mode: 'xy'
                    }
                }
            }
        };

        return (
            <Card className={classes.card}>
                <CardHeader
                    title={this.props.title}
                    titleTypographyProps={{variant: 'h6'}}
                />
                <CardContent>
                    <Line data={dataLine} options={opts} />
                </CardContent>
            </Card>
        )
    }
}

export default withStyles(styles)(GenericChart);
