import React from 'react';
import { MDBCollapse, MDBIcon, MDBProgress, MDBBtn, MDBCard, MDBCardBody, MDBCardImage, MDBCardTitle, MDBCardText, MDBCol } from 'mdbreact';

const WeatherCard = () => {
  return (
    <MDBCol>
      <MDBCard style={{ width: "22rem" }}>
        <MDBCardImage className="img-fluid" src="https://mdbootstrap.com/img/Photos/Others/images/43.jpg" waves />
        <MDBCardBody>
          <MDBCardTitle>
          <h4 class="card-title font-weight-bold">Dayton, OH</h4>
          </MDBCardTitle>
          <MDBCardText>
            <div className="d-flex justify-content-between">
                    <p className="display-1 degree">23</p>
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
            {/*
          <MDBBtn href="#">MDBBtn</MDBBtn>
            */}
        </MDBCardBody>
      </MDBCard>
    </MDBCol>
  )
}

export default WeatherCard;
