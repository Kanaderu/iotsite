import React, { Component } from 'react';
import { /*MDBCollapse, MDBIcon, MDBProgress, MDBBtn, */MDBCard, MDBCardBody, MDBCardImage, MDBCardTitle, MDBCardText, MDBCol } from 'mdbreact';

class CityCard extends Component {

    state = {
        city_info: {
            name: undefined,
            country: undefined,
            coord:{
              lat: undefined,
              lon: undefined
            },
            timezone: undefined,
            sunrise: undefined,
            sunset: undefined,
            cnt: undefined
        },
        cnt: undefined,
        list: []
    };

    fetchCityData(){
        //fetch('http://api.openweathermap.org/data/2.5/forecast?id=4509884&APPID=4687e81acdb537f9488ce1bacea4cab3')
        fetch('http://localhost:3000/curl_pp.json')
            .then(response => response.json())
            .then((data) => {
                this.setState({
                    city_info: data.city,
                    cnt: data.cnt,
                    list: data.list
                });
            })
            .catch((error) => {
                console.error(error);
            })
    }

    componentDidMount() {
        this.fetchCityData()
    }

    render() {
        const sunrise = new Date(this.state.city_info.sunrise * 1000).toGMTString();
        const sunset = new Date(this.state.city_info.sunset * 1000).toGMTString();
        return (
        <MDBCol>
            <MDBCard style={{ width: "22rem" }}>
                <MDBCardImage className="img-fluid" src="https://mdbootstrap.com/img/Photos/Others/images/43.jpg" waves />
                <MDBCardBody>
                    {/*<h4 className="card-title font-weight-bold">{ this.state.city_info.name }</h4>*/}
                    <MDBCardTitle className="card-title font-weight-bold">
                        { this.state.city_info.name } <br/>
                    </MDBCardTitle>
                    <MDBCardText>
                        UTC { this.state.city_info.timezone / 3600 } <br/>
                        Sunrise: { sunrise } <br/>
                        Sunset: { sunset } <br/>
                        Lat: { this.state.city_info.coord.lat },
                        Lon: { this.state.city_info.coord.lon } <br/>
                    {/*
                    <div className="d-flex justify-content-between">
                    <p className="display-1 degree">23</p>0
                    <i className="fas fa-sun-o fa-5x pt-3 amber-text"></i>
                    <MDBIcon icon="sun" size="5x" className="amber-text" />
                    </div>
                    <div class="d-flex justify-content-between mb-4">
                    <p><MDBIcon icon="tint" size="lg" className="cyan-text pr-2"/>3% Precipitation</p>
                    <p><MDBIcon icon="leaf" size="lg" className="grey-text pr-2"/>21 hm/h Winds</p>
                    </div>
                    <MDBProgress material value={25} height="10px" color="success" />
                    <ul class="list-unstyled d-flex justify-content-between font-small text-muted mb-4">
                    <li class="pl-4">8AM</li>
                    <li>11AM</li>
                    <li>2PM</li>
                    <li>5PM</li>
                    <li class="pr-4">8PM</li>
                    </ul>
                    {/*
                    <div class="progress md-progress">
                    <div class="progress-bar black" role="progressbar" aria-valuenow="40" aria-valuemin="0" aria-valuemax="100"></div>
                    </div>
                    Some quick example text to build on the card title and make
                    up the bulk of the card&apos;s content.
                    */}
                    </MDBCardText>
                    { this.state.list.map((item) => (
                        <div>
                            { item.dt_txt }<br/>
                            { item.weather.map((detail, index) => (
                                <p key={index}>{ detail.description }</p>
                            )) }<br/>
                        </div>
                    )) }
                </MDBCardBody>
            </MDBCard>
        </MDBCol>
        )
    }
}

export default CityCard;
