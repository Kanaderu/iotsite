import React, { Component } from 'react';
import { MDBCol, MDBCard, MDBCardBody, MDBCardHeader, MDBRow } from 'mdbreact';
import { Line, /*Doughnut, Radar*/ } from 'react-chartjs-2';

class ChartSection2 extends Component {

    state = {
        sensors: [],
	    /*
	package_id: [],
	timestamp: [],
	relay_id: [],
	sensor_id: [],
	sensor_type: [],
	units: [],
        data: [],
	    */
    }

    componentDidMount() {
        fetch('/ws/api/sensors/?format=json')
        .then(res => res.json())
        .then((data) => {
            this.setState({ sensors: data })
        })
        .catch(console.log)
    }
    
    render(){
        const dataLine = {
	    labels: this.state.sensors.map((sensor) => (
		    sensor.timestamp
	    )),

            datasets: [
              {
                label: 'KU Green Roof',
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
                data: this.state.sensors.map((sensor) => (
		    sensor.units
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
            <MDBRow className="mb-12">
                <MDBCol md="12" lg="8" className="mb-12">
                    <MDBCard className="mb-12">
                    <MDBCardHeader>Temperature</MDBCardHeader>
                    <MDBCardBody>
		        <Line data={dataLine} options={opts} />
                    </MDBCardBody>
                    </MDBCard>
                </MDBCol>
                <MDBCol md="12" lg="4" className="mb-4">
                    <MDBCard className="mb-12">
                    <MDBCardHeader>Duplicate?</MDBCardHeader>
                    <MDBCardBody>
		        <Line data={dataLine} options={opts} />
                    </MDBCardBody>
                    </MDBCard>
                </MDBCol>
            </MDBRow>
        )
    }

}

export default ChartSection2;

