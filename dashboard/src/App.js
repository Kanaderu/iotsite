import React, { Component } from 'react';
import { ThemeProvider } from "@material-ui/styles";
import { createMuiTheme } from "@material-ui/core/styles";
import MenuIcon from '@material-ui/icons/Menu';
import ChevronLeft from '@material-ui/icons/ChevronLeft';
import ChevronRight from '@material-ui/icons/ChevronRight';
import Typography from "@material-ui/core/Typography";

import { Root, Header, Nav, Content, Footer, presets } from 'mui-layout';
import Routes from './components/Routes';
import SideNavigation from './components/SideNavigation';

class App extends Component {
  render() {
  return (
    <ThemeProvider theme={createMuiTheme()}>
      <Root config={presets.createContentBasedLayout()}>
        <Header renderMenuIcon={open => (open ? <ChevronLeft /> : <MenuIcon />)}>
          <Typography variant="h6">UD Sensors</Typography>
        </Header>
        <Nav renderIcon={collapsed => collapsed ? <ChevronRight /> : <ChevronLeft />}>
          <SideNavigation />
        </Nav>
        <Content>
          <main>
            <Routes />
          </main>
        </Content>
        <Footer>
            <Typography align='center' variant='body2'>
                &copy; {new Date().getFullYear()} Applied IoT.
            </Typography>
        </Footer>
      </Root>
    </ThemeProvider>
  );
  }
}

export default App;
