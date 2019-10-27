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
        MuiSelected: {
            backgroundColor: "#64dd17",
        },
    },
    icon: {
        color: '#000000',
        /*
        '&:hover': {
            color: '#000000',
        },
        */
    },
    itemroot: {
        //color: 'red', // text color
        '&$selected': {
            backgroundColor: '#F80228',
            '&:hover': {
                backgroundColor: '#0200D1',
                color: '#FFFFFF',
            },
        },
        '&:hover': {
            backgroundColor: '#0200D1',
            color: '#FFFFFF',
        },
    },
    selected: {},
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
                    <NavLink exact={true} to="/ws" style={{ textDecoration: 'none' }}>
                        <ListItem
                            button
                            selected={this.state.selectedIndex === 0}
                            onClick={event => handleListItemClick(event, 0)}
                            //className={classes.listitem}
                            classes={{
                                root: classes.itemroot,
                                selected: classes.selected,
                            }}
                        >
                            <ListItemIcon className={classes.icon}>
                                <HomeRoundedIcon />
                            </ListItemIcon>
                            <ListItemText primary="Home" />
                        </ListItem>
                    </NavLink>
                    <NavLink exact={true} to="/sensors" style={{ textDecoration: 'none' }}>
                        <ListItem
                            button
                            selected={this.state.selectedIndex === 1}
                            onClick={event => handleListItemClick(event, 1)}
                            classes={{
                                root: classes.itemroot,
                                selected: classes.selected,
                            }}
                        >
                            <ListItemIcon className={classes.icon}>
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
                            classes={{
                                root: classes.itemroot,
                                selected: classes.selected,
                            }}
                        >
                            <ListItemIcon className={classes.icon}>
                                <GitHubIcon />
                            </ListItemIcon>
                            <ListItemText primary="GitHub Source" />
                        </ListItem>
                    </a>
                    <NavLink exact={true} to="/about" style={{ textDecoration: 'none' }}>
                        <ListItem
                            button
                            selected={this.state.selectedIndex === 3}
                            onClick={event => handleListItemClick(event, 3)}
                            classes={{
                                root: classes.itemroot,
                                selected: classes.selected,
                            }}
                        >
                            <ListItemIcon className={classes.icon}>
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
