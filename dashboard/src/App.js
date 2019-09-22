import React, { Component } from 'react';
import Routes from './components/Routes';
import TopNavigation from './components/topNavigation';
//import SideNavigation from './components/sideNavigation';
import Footer from './components/Footer';
import './index.css';

class App extends Component {

  render() {
    return (
        <div className="flexible-content">
          <TopNavigation />
	    {
//            <MDBIcon icon="spinner" spin size="3x" fixed />
//            <span className="sr-only">Loading...</span>
          //<SideNavigation />
	    }
	    {
          //<main id="content" className="p-5">
	    }
          <main className="p-5">
            <Routes />
          </main>
          <Footer />
        </div>
    );
  }
}

export default App;
