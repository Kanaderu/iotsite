import React from 'react';
import { Route, Switch } from 'react-router-dom';
import { Provider } from 'react-redux'
import { createStore, applyMiddleware } from "redux";
import thunk from "redux-thunk";
import DashboardPage from './pages/DashboardPage';
import SensorsPage from './pages/SensorsPage';
import AboutPage from './pages/AboutPage';
import Login from './Login';
import Register from './Register';

import ponyApp from './reducers';

let store = createStore(ponyApp, applyMiddleware(thunk));

class Routes extends React.Component {
    render() {
        return (
            <Provider store={store}>
                    <Switch>
                        <Route path='/' exact component={DashboardPage} />
                        <Route path='/ws' exact component={DashboardPage} />
                        <Route path='/dashboard' exact component={DashboardPage} />
                        <Route path='/sensors' exact component={SensorsPage} />
                        <Route path='/about' exact component={AboutPage} />
                        <Route path="/login" exact component={Login} />
                        <Route path="/register" exact component={Register} />
                    </Switch>
            </Provider>
        );
    }
}

export default Routes;
