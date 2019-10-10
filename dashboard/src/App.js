import React, { Component } from 'react';
import Routes from './components/Routes';
//import TopNavigation from './components/topNavigation';
import TopNavigationMaterial from './components/topNavigationMaterial';
//import Footer from './components/Footer';
import FooterMaterial from './components/FooterMaterial';
import './index.css';

class App extends Component {

    render() {
        return (
            <div className="flexible-content">
                {/*<TopNavigation />*/}
                <TopNavigationMaterial />
                <main className="p-5">
                    <Routes />
                </main>
                {/*<Footer />*/}
                <FooterMaterial />
            </div>
        );
    }
}

export default App;
