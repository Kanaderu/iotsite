import React, { Component } from 'react';
import { MDBCol, MDBCard, MDBCardBody, MDBCardHeader, MDBRow } from 'mdbreact';
import { Line, /*Doughnut, Radar*/ } from 'react-chartjs-2';

class ChartSection4 extends Component {

    render(){
        const dataLine = {
            labels: this.props.data.hourly.data.map((data) => {
                const date = new Date(data.time*1000);
                return date.getHours();
            }),

            datasets: [
              {
                label: 'Temperature',
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
                data: this.props.data.hourly.data.map((data) => (
                    data.temperature
                )),
              },
              {
                label: 'Apparent Temperature',
                fill: false,
                lineTension: 0.1,
                backgroundColor: 'rgba(255,100,100,0.4)',
                borderColor: 'rgba(255,192,192,1)',
                borderCapStyle: 'butt',
                borderDash: [],
                borderDashOffset: 0.0,
                borderJoinStyle: 'miter',
                pointBorderColor: 'rgba(255,100,100,1)',
                pointBackgroundColor: '#fff',
                pointBorderWidth: 1,
                pointHoverRadius: 5,
                pointHoverBackgroundColor: 'rgba(255,100,100,1)',
                pointHoverBorderColor: 'rgba(220,220,220,1)',
                pointHoverBorderWidth: 2,
                pointRadius: 1,
                pointHitRadius: 10,
                data: this.props.data.hourly.data.map((data) => (
                    data.apparentTemperature
                )),
              }
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
            <MDBRow className="mb-4">
                <MDBCol md="12" className="mb-4">
                    <MDBCard className="mb-4">
                        <MDBCardHeader>Temperature</MDBCardHeader>
                        <MDBCardBody>
                            <Line data={dataLine} options={opts} />
                        </MDBCardBody>
                    </MDBCard>
                </MDBCol>
            </MDBRow>
        )
    }

}

export default ChartSection4;
