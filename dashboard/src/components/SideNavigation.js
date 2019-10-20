import React, { Component } from 'react';
import { NavLink } from 'react-router-dom';

import { withStyles } from '@material-ui/core/styles';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import Divider from '@material-ui/core/Divider';

import LandscapeIcon from '@material-ui/icons/Landscape';
import GitHubIcon from '@material-ui/icons/GitHub';
import InfoRoundedIcon from '@material-ui/icons/InfoRounded';
import HomeRoundedIcon from '@material-ui/icons/HomeRounded';

const styles = theme => ({
    root: {
        width: '100%',
        maxWidth: 360,
        backgroundColor: theme.palette.background.paper,
    },
});

class SideNavigation extends Component {
    constructor(props) {
        super(props);
        this.state = {
            selectedIndex: 0
        }
    }

    render() {
        const { classes } = this.props;

        const handleListItemClick = (event, index) => {
            this.setState({selectedIndex: index});
        };

        return (
            <div className={classes.root}>
                <List component="nav" aria-label="main mailbox folders">
                    <NavLink exact={true} to="/dashboard" style={{ textDecoration: 'none' }}>
                        <ListItem
                            button
                            selected={this.state.selectedIndex === 0}
                            onClick={event => handleListItemClick(event, 0)}
                        >
                            <ListItemIcon>
                                <HomeRoundedIcon />
                            </ListItemIcon>
                            <ListItemText primary="Home" />
                        </ListItem>
                    </NavLink>
                    <NavLink exact={true} to="/test2" style={{ textDecoration: 'none' }}>
                        <ListItem
                            button
                            selected={this.state.selectedIndex === 1}
                            onClick={event => handleListItemClick(event, 1)}
                        >
                            <ListItemIcon>
                                <LandscapeIcon />
                            </ListItemIcon>
                            <ListItemText primary="Sensors" />
                        </ListItem>
                    </NavLink>
                </List>
                <Divider />
                <List component="nav" aria-label="secondary mailbox folder">
                    <a style={{ textDecoration: 'none' }} rel="noopener noreferrer" target="_blank" href="https://github.com/Kanaderu/iotsite">
                        <ListItem
                            button
                            selected={this.state.selectedIndex === 2}
                            onClick={event => handleListItemClick(event, this.state.selectedIndex)}
                        >
                            <ListItemIcon>
                                <GitHubIcon />
                            </ListItemIcon>
                            <ListItemText primary="GitHub Source" />
                        </ListItem>
                    </a>
                    <NavLink exact={true} to="/test2" style={{ textDecoration: 'none' }}>
                        <ListItem
                            button
                            selected={this.state.selectedIndex === 3}
                            onClick={event => handleListItemClick(event, 3)}
                        >
                            <ListItemIcon>
                                <InfoRoundedIcon />
                            </ListItemIcon>
                            <ListItemText primary="About" />
                        </ListItem>
                    </NavLink>
                </List>
            </div>
        )
    }
}

export default withStyles(styles)(SideNavigation);
