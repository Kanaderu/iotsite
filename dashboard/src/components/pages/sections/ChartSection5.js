import React, { Component } from 'react';
import { MDBCol, MDBCard, MDBCardBody, MDBCardHeader, MDBRow } from 'mdbreact';
import { Line } from 'react-chartjs-2';

class ChartSection5 extends Component {

    render(){

        const weekday = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];

        const dataLine = {
            labels: this.props.data.daily.data.map((data) => {
                const date = new Date(data.time*1000);
                return weekday[date.getDay()];
            }),

            datasets: [
              {
                label: 'Temperature High',
                fill: false,
                lineTension: 0.1,
                backgroundColor: 'rgba(255,51,51,0.4)',
                borderColor: 'rgba(255,51,51,1)',
                borderCapStyle: 'butt',
                borderDash: [],
                borderDashOffset: 0.0,
                borderJoinStyle: 'miter',
                pointBorderColor: 'rgba(255,51,51,1)',
                pointBackgroundColor: '#fff',
                pointBorderWidth: 1,
                pointHoverRadius: 5,
                pointHoverBackgroundColor: 'rgba(255,51,51,1)',
                pointHoverBorderColor: 'rgba(220,220,220,1)',
                pointHoverBorderWidth: 2,
                pointRadius: 1,
                pointHitRadius: 10,
                data: this.props.data.daily.data.map((data) => (
                    data.temperatureHigh
                )),
              },
              {
                label: 'Temperature Low',
                fill: false,
                lineTension: 0.1,
                backgroundColor: 'rgba(75,192,192,0.4)',
                borderColor: 'rgba(75,192,192,1)',
                borderCapStyle: 'butt',
                borderDash: [],
                borderDashOffset: 0.0,
                borderJoinStyle: 'miter',
                pointBorderColor: 'rgba(75,192,192,1)',
                pointBackgroundColor: '#fff',
                pointBorderWidth: 1,
                pointHoverRadius: 5,
                pointHoverBackgroundColor: 'rgba(75,192,192,1)',
                pointHoverBorderColor: 'rgba(220,220,220,1)',
                pointHoverBorderWidth: 2,
                pointRadius: 1,
                pointHitRadius: 10,
                data: this.props.data.daily.data.map((data) => (
                    data.temperatureLow
                )),
              },
            ]
        };
        const opts = {
            responsive: true,
            scales: {
                xAxes: [{
                    ticks: { display: true },
                    scaleLabel: {
                        display: true,
                        labelString: 'Timestamp'
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
                        labelString: 'Temperature'
                    },
                    gridLines: {
                        display: true,
                        drawBorder: true
                    }
                }]
            }
    };

        return (
            <MDBCol md="4" className="mb-4">
                <MDBCard className="mb-12">
                    <MDBCardHeader>Daily Temperature High/Low</MDBCardHeader>
                    <MDBCardBody>
                        <Line data={dataLine} options={opts} />
                    </MDBCardBody>
                </MDBCard>
            </MDBCol>
        )
    }
}

export default ChartSection5;
