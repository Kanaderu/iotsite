import React from 'react';
import { loadModules } from 'esri-loader';


const Point = (props) => {
    Object.keys(props.locations).map((location, id) => {
        // remove old graphic if it exists
        props.locations[`${location}`].oldGraphic &&
        props.view.graphics.remove(props.locations[`${location}`].oldGraphic);

        // add new graphic
        props.locations[`${location}`].graphic &&
        props.view.graphics.add(props.locations[`${location}`].graphic);

        return null;
    });
    return null;
};

class WebMapView extends React.Component {
  constructor(props) {
    super(props);
    this.locations = props.locations;
    this.mapRef = React.createRef();
  }

  componentDidMount() {
    // lazy load the required ArcGIS API for JavaScript modules and CSS
    loadModules(['esri/Map', 'esri/views/MapView', 'esri/layers/GeoJSONLayer'], { css: true })
    .then(([ArcGISMap, MapView, GeoJSONLayer]) => {
      // TODO: change hardcoding of url location
      const url = "/linkstations.geojson";
      const renderer = {
          type: "simple",
          symbol: {
              type: "simple-marker",
              color: "green",
              outline: {
                  color: "white"
              }
          },
      };
      const template = {
          title: "Link Bike Station",
          content: "{name}"
      };

      const geojsonLayer = new GeoJSONLayer({
          url: url,
          //copyright: "None",
          popupTemplate: template,
          renderer: renderer
      });


      const map = new ArcGISMap({
        basemap: 'streets-navigation-vector',
        layers: [geojsonLayer]
      });

      this.view = new MapView({
        container: this.mapRef.current,
        map: map,
        center: [-84.1745444, 39.7346451],
        zoom: 14
      });
    });
  }

  componentWillUnmount() {
    if (this.view) {
      // destroy the map view
      this.view.container = null;
    }
  }

  render() {
    return (
      <div style={{width: '100%', height: '85.5vh'}} ref={this.mapRef} view={this.view}>
        <Point locations={this.locations} view={this.view} />
        {this.props.children}
      </div>
    );
  }
}

export default WebMapView;
