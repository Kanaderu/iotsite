import React from 'react';
import { Route, Switch } from 'react-router-dom';
import DashboardPage from './pages/DashboardPage';
import SensorsPage from './pages/SensorsPage';

class Routes extends React.Component {
    render() {
        return (
            <Switch>
                <Route path='/' exact component={DashboardPage} />
                <Route path='/ws' exact component={DashboardPage} />
                <Route path='/dashboard' exact component={DashboardPage} />
                <Route path='/sensors' exact component={SensorsPage} />
            </Switch>
        );
    }
}

export default Routes;
