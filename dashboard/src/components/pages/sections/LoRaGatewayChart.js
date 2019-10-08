import React, { Component } from 'react';
import { MDBCol, MDBCard, MDBCardBody, MDBCardHeader, MDBRow } from 'mdbreact';
import { Chart, Line } from 'react-chartjs-2';
import Hammer from 'react-hammerjs';
import zoom from 'chartjs-plugin-zoom';

class LoRaGatewayChart extends Component {
    constructor(props) {
        super(props);
        this.state = {
            data: []
        };
    }

    fetchLoRaGateway() {
        fetch('https://udsensors.tk/ws/api/LoRaGateway/')
            .then(response => response.json())
            .then(responses => {
                this.setState({
                    data: responses.map(response => ({
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

    componentDidMount() {
        this.fetchLoRaGateway();
    }

    render(){
        const dataLine = {
            labels: this.state.data.map((data) => {
                return data.counter;
            }),
            datasets: [
                {
                    label: 'T1',
                    fill: false,
                    lineTension: 0.1,
                    backgroundColor: 'rgba(0,255,154,0.4)',
                    borderColor: 'rgba(0,255,154,1)',
                    borderCapStyle: 'butt',
                    borderDash: [],
                    borderDashOffset: 0.0,
                    borderJoinStyle: 'miter',
                    pointBorderColor: 'rgba(0,255,154,1)',
                    pointBackgroundColor: '#fff',
                    pointBorderWidth: 1,
                    pointHoverRadius: 5,
                    pointHoverBackgroundColor: 'rgba(0,255,154,1)',
                    pointHoverBorderColor: 'rgba(220,220,220,1)',
                    pointHoverBorderWidth: 2,
                    pointRadius: 1,
                    pointHitRadius: 10,
                    data: this.state.data.map((data) => {
                        return parseFloat(data.payload_fields.t1);
                    }),
                },
                {
                    label: 'T2',
                    fill: false,
                    lineTension: 0.1,
                    backgroundColor: 'rgba(255,0,154,0.4)',
                    borderColor: 'rgba(255,0,154,1)',
                    borderCapStyle: 'butt',
                    borderDash: [],
                    borderDashOffset: 0.0,
                    borderJoinStyle: 'miter',
                    pointBorderColor: 'rgba(255,0,154,1)',
                    pointBackgroundColor: '#fff',
                    pointBorderWidth: 1,
                    pointHoverRadius: 5,
                    pointHoverBackgroundColor: 'rgba(255,0,154,1)',
                    pointHoverBorderColor: 'rgba(220,220,220,1)',
                    pointHoverBorderWidth: 2,
                    pointRadius: 1,
                    pointHitRadius: 10,
                    data: this.state.data.map((data) => {
                        return parseFloat(data.payload_fields.t2);
                    }),
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
                        labelString: 'Counter'
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
            <MDBCol md="8" className="mb-8">
                <MDBCard>
                    <MDBCardHeader>LoRa Gateway Temperatures</MDBCardHeader>
                    <MDBCardBody>
                        <Line data={dataLine} options={opts} />
                    </MDBCardBody>
                </MDBCard>
            </MDBCol>
        )
    }
}

export default LoRaGatewayChart;
