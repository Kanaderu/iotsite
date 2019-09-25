import React from 'react';
import * as ReactDOM from 'react-dom';
import { Scene } from '@esri/react-arcgis';
import { MDBRow, MDBCol, MDBCard, MDBCardBody, MDBCardHeader} from 'mdbreact';

const MapVectorSection = () => {
    return (
        <MDBRow className="mb-4">
            <MDBCol md="12" className="mb-4">
                <MDBCard className="mb-4">
                    <MDBCardHeader>ArcGIS Map Vector</MDBCardHeader>
                    <MDBCardBody style={{width: '100%', height: '700px'}} className="text-center">
                        <link rel="stylesheet" href="https://js.arcgis.com/4.10/esri/css/main.css"></link>
                        <Scene
                            mapProperties={{
                                basemap: 'streets-navigation-vector',
                                ground: 'world-elevation'
                            }}
                            viewProperties={{
                                center: [-84.1935444, 39.7316451 ],
                                zoom: 16.5
                            }}
                        />
                    </MDBCardBody>
                </MDBCard>
            </MDBCol>
        </MDBRow>
    )
}

export default MapVectorSection;