import React from 'react';
import { Route, Switch } from 'react-router-dom';
import DashboardPage from './pages/DashboardPage';
import SensorsPage from './pages/SensorsPage';
import AboutPage from './pages/AboutPage';
import TokenPage from './pages/TokenPage';
import Login from './Login';
import Register from './Register';

class Routes extends React.Component {
    render() {
        return (
            <Switch>
                <Route path='/' exact component={DashboardPage} />
                <Route path='/ws' exact component={DashboardPage} />
                <Route path='/dashboard' exact component={DashboardPage} />
                <Route path='/sensors' exact component={SensorsPage} />
                <Route path='/about' exact component={AboutPage} />
                <Route path="/login" exact component={Login} />
                <Route path="/register" exact component={Register} />
                <Route path="/token" exact component={TokenPage} />
            </Switch>
        );
    }
}

export default Routes;
