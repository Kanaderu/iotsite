import React, { Component } from 'react';
import { createStore, applyMiddleware } from "redux";
import { Provider } from 'react-redux'
import thunk from "redux-thunk";
import { ThemeProvider } from "@material-ui/styles";
import { createMuiTheme } from "@material-ui/core/styles";
import MenuIcon from '@material-ui/icons/Menu';
import ChevronLeft from '@material-ui/icons/ChevronLeft';
import ChevronRight from '@material-ui/icons/ChevronRight';
import Typography from "@material-ui/core/Typography";

import { Root, Header, Nav, Content, Footer, presets } from 'mui-layout';
import Routes from './components/Routes';
import SideNavigation from './components/SideNavigation';
import blue from '@material-ui/core/colors/blue';
import red from '@material-ui/core/colors/red';

import ponyApp from './components/reducers';

let store = createStore(ponyApp, applyMiddleware(thunk));

const theme = createMuiTheme({
    palette: {
        primary: {
            main: '#002F87',
        },
        secondary: {
            main: '#D70036',
        },
        error: red[0],
        contrastThreshold: 3,
        tonalOffset: 0.2,
    },
});

class App extends Component {
    render() {
        return (
            <Provider store={store}>
                <ThemeProvider theme={theme}>
                    <Root config={presets.createContentBasedLayout()}>
                        <Header color="primary" renderMenuIcon={open => (open ? <ChevronLeft color="secondary" /> : <MenuIcon color="secondary" />)}>
                            <Typography variant="h6">UD Sensors</Typography>
                        </Header>
                        <Nav renderIcon={collapsed => collapsed ? <ChevronRight color="secondary" /> : <ChevronLeft color="secondary" />}>
                            <SideNavigation />
                        </Nav>
                        <Content>
                            <main>
                                <Routes />
                            </main>
                        </Content>
                        <Footer>
                            <Typography align="center">
                                &copy; {new Date().getFullYear()}
                            </Typography>
                        </Footer>
                    </Root>
                </ThemeProvider>
            </Provider>
        );
    }
}

export default App;
