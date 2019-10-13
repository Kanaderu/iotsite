import React, { Component } from 'react';
import { MDBRow } from 'mdbreact';

import DarkSkyCard from './sections/DarkSkyCard';
import ChartSection4 from './sections/ChartSection4';
import ChartSection5 from './sections/ChartSection5';
import ChartSection6 from './sections/ChartSection6';
import MapSection from './sections/MapSection';
import MapVectorSection from './sections/MapVectorSection';
import LoRaGatewayChart from './sections/LoRaGatewayChart';
import FeatherChart from './sections/FeatherChart';

class DashboardPage extends Component {
    state = {
        latitude: undefined,
        longitude: undefined,
        timezone: undefined,
        offset: undefined,
        currently: {
            data: []
        },
        hourly: {
            data: []
        },
        daily: {
            data: []
        },
        minutely: {
            data: []
        },
        flags: {}
    }

    fetchDarkSkyData() {
        fetch('https://udsensors.tk/ws/darksky/')
            .then(response => response.json())
            .then((data) => {
                this.setState({
                    latitude: data.latitude,
                    longitude: data.longitude,
                    timezone: data.timezone,
                    offset: data.offset,
                    currently: data.currently,
                    hourly: data.hourly,
                    daily: data.daily,
                    minutely: data.minutely,
                    flags: data.flags
                });
            })
            .catch((error) => {
                console.log(error);
            })
    }

    componentDidMount() {
        this.fetchDarkSkyData()
    }

    render() {
        const data = this.state;
        return (
          <React.Fragment>
            <MDBRow className="mb-4">
                <DarkSkyCard data={data} />
            </MDBRow>
            <MDBRow className="mb-4">
                <LoRaGatewayChart />
                <FeatherChart />
            </MDBRow>
            <MDBRow className="mb-4">
                <ChartSection4 data={data} />
                <ChartSection5 data={data} />
                <ChartSection6 data={data} />
            </MDBRow>
            <MDBRow className="mb-6">
                <MapSection />
                <MapVectorSection />
            </MDBRow>
          </React.Fragment>
        )
    }
}

export default DashboardPage;
