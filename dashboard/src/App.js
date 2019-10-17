import React, { Component } from 'react';
import Routes from './components/Routes';
import TopNavigationMaterial from './components/topNavigationMaterial';
import FooterMaterial from './components/FooterMaterial';
import './index.css';

class App extends Component {

    render() {
        return (
            <div className="flexible-content">
                <TopNavigationMaterial />
                <main className="p-5">
                    <Routes />
                </main>
                <FooterMaterial />
            </div>
        );
    }
}

export default App;
