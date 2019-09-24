import React from 'react';
import * as ReactDOM from 'react-dom';
import { /*Map*/ Scene } from '@esri/react-arcgis';
import { MDBCol, MDBCard, MDBCardBody, MDBCardHeader} from 'mdbreact';

const MapSection = () => {
  return (
      <MDBCol lg="12" className="mb-12">
        <MDBCard>
          <MDBCardHeader>Google Map</MDBCardHeader>
          <MDBCardBody style={{width: '100%', height: '700px'}} className="text-center">
          <link rel="stylesheet" href="https://js.arcgis.com/4.10/esri/css/main.css"></link>
          <Scene
            mapProperties={{
                /*basemap: 'streets-navigation-vector',*/
                basemap: 'satellite',
                ground: 'world-elevation'
            }}
            viewProperties={{
                /*center: [-84.1935444, 39.7252851, 350]*/
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
          </MDBCardBody>
        </MDBCard>
      </MDBCol>
  )
}

export default MapSection;

