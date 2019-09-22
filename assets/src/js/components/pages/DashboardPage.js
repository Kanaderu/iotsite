import React, { Component } from 'react';
import { MDBRow } from 'mdbreact';
/*
import AdminCardSection1 from './sections/AdminCardSection1';
import AdminCardSection2 from './sections/AdminCardSection2';
import TableSection from './sections/TableSection';
import BreadcrumSection from './sections/BreadcrumSection';
import ChartSection1 from './sections/ChartSection1';
import ChartSection2 from './sections/ChartSection2';
import MapSection from './sections/MapSection';
import ModalSection from './sections/ModalSection';
import ChartSection3 from './sections/ChartSection3';

import CityCard from './sections/CityCard';
import WeatherCard from './sections/WeatherCard';
*/
import DarkSkyCard from './sections/DarkSkyCard';

import ChartSection4 from './sections/ChartSection4';
import ChartSection5 from './sections/ChartSection5';
import ChartSection6 from './sections/ChartSection6';

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
                console.log("Error!");
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
            <ChartSection4 data={data} />
            <ChartSection5 data={data} />
            <ChartSection6 data={data} />
          </React.Fragment>
        )
    }

}

export default DashboardPage;
