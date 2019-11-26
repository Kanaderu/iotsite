import React, { Component } from 'react';
import { connect } from "react-redux";
import { NavLink } from 'react-router-dom';

import { withStyles } from '@material-ui/core/styles';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import Divider from '@material-ui/core/Divider';

import { Icon, InlineIcon } from '@iconify/react';
import paperPlane from '@iconify/icons-fe/paper-plane';
import loginIcon from '@iconify/icons-ls/login';
import logoutIcon from '@iconify/icons-ls/logout';
import jupyterIcon from '@iconify/icons-simple-icons/jupyter';
import githubIcon from '@iconify/icons-simple-icons/github';
import roundInfo from '@iconify/icons-ic/round-info';
import sharpLandscape from '@iconify/icons-ic/sharp-landscape';
import baselineHome from '@iconify/icons-ic/baseline-home';
import codefactorIcon from '@iconify/icons-simple-icons/codefactor';
import bookIcon from '@iconify/icons-icomoon-free/book';
import keyIcon from '@iconify/icons-fa-solid/key';
import graphqlIcon from '@iconify/icons-simple-icons/graphql';


import { auth } from './actions';

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
            selectedIndex: 0,
        }
    }

    componentDidMount = () => {
        this.props.getAccountFetch()
    }

    render() {
        const { classes } = this.props;

        const handleListItemClick = (event, index) => {
            this.setState({selectedIndex: index});
        };

        const handleLogout = (event, index) => {
            this.setState({selectedIndex: index});
            this.props.logout();
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
                                <Icon height='2em' icon={baselineHome} />
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
                                <Icon height='2em' icon={sharpLandscape} />
                            </ListItemIcon>
                            <ListItemText primary="Sensors" />
                        </ListItem>
                    </NavLink>
                    <a style={{ textDecoration: 'none' }} rel="noopener noreferrer" target="_blank" href="/ws/api">
                        <ListItem
                            button
                            selected={this.state.selectedIndex === 2}
                            onClick={event => handleListItemClick(event, 2)}
                            classes={{
                                root: classes.itemroot,
                                selected: classes.selected,
                            }}
                        >
                            <ListItemIcon className={classes.icon}>
                                <Icon height='2em' icon={codefactorIcon} />
                            </ListItemIcon>
                            <ListItemText primary="Sensors API" />
                        </ListItem>
                    </a>
                    <a style={{ textDecoration: 'none' }} rel="noopener noreferrer" target="_blank" href="/ws/docs/">
                        <ListItem
                            button
                            selected={this.state.selectedIndex === 3}
                            onClick={event => handleListItemClick(event, this.state.selectedIndex)}
                            classes={{
                                root: classes.itemroot,
                                selected: classes.selected,
                            }}
                        >
                            <ListItemIcon className={classes.icon}>
                                <Icon height='2em' icon={bookIcon} />
                            </ListItemIcon>
                            <ListItemText primary="Documentation" />
                        </ListItem>
                    </a>
                    <a style={{ textDecoration: 'none' }} rel="noopener noreferrer" target="_blank" href="/jupyter">
                        <ListItem
                            button
                            selected={this.state.selectedIndex === 4}
                            onClick={event => handleListItemClick(event, this.state.selectedIndex)}
                            classes={{
                                root: classes.itemroot,
                                selected: classes.selected,
                            }}
                        >
                            <ListItemIcon className={classes.icon}>
                                <Icon height='2em' icon={jupyterIcon} />
                            </ListItemIcon>
                            <ListItemText primary="JupyterHub" />
                        </ListItem>
                    </a>
                    <a style={{ textDecoration: 'none' }} rel="noopener noreferrer" target="_blank" href="/ws/graphql/">
                        <ListItem
                            button
                            selected={this.state.selectedIndex === 5}
                            onClick={event => handleListItemClick(event, this.state.selectedIndex)}
                            classes={{
                                root: classes.itemroot,
                                selected: classes.selected,
                            }}
                        >
                            <ListItemIcon className={classes.icon}>
                                <Icon height='2em' icon={graphqlIcon} />
                            </ListItemIcon>
                            <ListItemText primary="GraphQL" />
                        </ListItem>
                    </a>
                </List>
                <Divider />
                <List component="nav" aria-label="secondary mailbox folder">
                    <a style={{ textDecoration: 'none' }} rel="noopener noreferrer" target="_blank" href="https://github.com/Kanaderu/iotsite">
                        <ListItem
                            button
                            selected={this.state.selectedIndex === 6}
                            onClick={event => handleListItemClick(event, this.state.selectedIndex)}
                            classes={{
                                root: classes.itemroot,
                                selected: classes.selected,
                            }}
                        >
                            <ListItemIcon className={classes.icon}>
                                <Icon height='2em' icon={githubIcon} />
                            </ListItemIcon>
                            <ListItemText primary="GitHub Source" />
                        </ListItem>
                    </a>
                    <NavLink exact={true} to="/about" style={{ textDecoration: 'none' }}>
                        <ListItem
                            button
                            selected={this.state.selectedIndex === 7}
                            onClick={event => handleListItemClick(event, 5)}
                            classes={{
                                root: classes.itemroot,
                                selected: classes.selected,
                            }}
                        >
                            <ListItemIcon className={classes.icon}>
                                <Icon height='2em' icon={roundInfo} />
                            </ListItemIcon>
                            <ListItemText primary="About" />
                        </ListItem>
                    </NavLink>
                </List>
                <Divider />
                { this.props.isAuthenticated &&
                <List component="nav" aria-label="secondary mailbox folder">
                    <NavLink exact={true} to="/token" style={{ textDecoration: 'none' }}>
                        <ListItem
                            button
                            selected={this.state.selectedIndex === 8}
                            onClick={event => handleListItemClick(event, 8)}
                            classes={{
                                root: classes.itemroot,
                                selected: classes.selected,
                            }}
                        >
                            <ListItemIcon className={classes.icon}>
                                <Icon height='2em' icon={keyIcon} />
                            </ListItemIcon>
                            <ListItemText primary="API Tokens" />
                        </ListItem>
                    </NavLink>
                </List>
                }
                { this.props.isAuthenticated &&
                <List component="nav" aria-label="secondary mailbox folder">
                    <NavLink exact={true} to="/" style={{ textDecoration: 'none' }}>
                        <ListItem
                            button
                            selected={this.state.selectedIndex === 9}
                            onClick={event => handleLogout(event, 0)}
                            classes={{
                                root: classes.itemroot,
                                selected: classes.selected,
                            }}
                        >
                            <ListItemIcon className={classes.icon}>
                                <Icon height='2em' icon={logoutIcon} />
                            </ListItemIcon>
                            <ListItemText primary="Logout" />
                        </ListItem>
                    </NavLink>
                </List>
                }
                { this.props.isAuthenticated ||
                <List component="nav" aria-label="secondary mailbox folder">
                    <NavLink exact={true} to="/login" style={{ textDecoration: 'none' }}>
                        <ListItem
                            button
                            selected={this.state.selectedIndex === 8}
                            onClick={event => handleListItemClick(event, 8)}
                            classes={{
                                root: classes.itemroot,
                                selected: classes.selected,
                            }}
                        >
                            <ListItemIcon className={classes.icon}>
                                <Icon height='2em' icon={loginIcon} />
                            </ListItemIcon>
                            <ListItemText primary="Login" />
                        </ListItem>
                    </NavLink>
                    <NavLink exact={true} to="/register" style={{ textDecoration: 'none' }}>
                        <ListItem
                            button
                            selected={this.state.selectedIndex === 9}
                            onClick={event => handleListItemClick(event, 9)}
                            classes={{
                                root: classes.itemroot,
                                selected: classes.selected,
                            }}
                        >
                            <ListItemIcon className={classes.icon}>
                                <Icon height='2em' icon={paperPlane} />
                            </ListItemIcon>
                            <ListItemText primary="Register" />
                        </ListItem>
                    </NavLink>
                </List>
                }
            </div>
        )
    }
}

const mapStateToProps = state => {
    let errors = [];
    if (state.auth.errors) {
        errors = Object.keys(state.auth.errors).map(field => {
            return { field, message: state.auth.errors[field] };
        });
    }
    return {
        errors,
        isAuthenticated: state.auth.isAuthenticated
    };
}

const mapDispatchToProps = dispatch => ({
    getAccountFetch: () => dispatch(auth.getAccountFetch()),
    logout: () => dispatch(auth.logout()),
})

export default connect(mapStateToProps, mapDispatchToProps)(withStyles(styles)(SideNavigation));
