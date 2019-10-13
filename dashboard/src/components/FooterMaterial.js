import React, { Component } from 'react';
import { withStyles } from '@material-ui/core/styles';
import BottomNavigation from '@material-ui/core/BottomNavigation';
import BottomNavigationAction from '@material-ui/core/BottomNavigationAction';

import HomeRoundedIcon from '@material-ui/icons/HomeRounded';
import GitHubIcon from '@material-ui/icons/GitHub';
import InfoRoundedIcon from '@material-ui/icons/InfoRounded';

import CssBaseline from '@material-ui/core/CssBaseline';
import useScrollTrigger from '@material-ui/core/useScrollTrigger';
import Slide from '@material-ui/core/Slide';
import PropTypes from 'prop-types';

const styles = theme => ({
    footer: {
        width: '100%',
        position: 'fixed',
        top: 'auto',
        bottom: 0,
    },
});


class FooterMaterial extends Component {
    constructor(props) {
        super(props);
        this.state = {
            value: 0
        }
    }

        //const [value, setValue] = React.useState(0);
    render() {
        const { classes } = this.props;

        return (
            <React.Fragment>
                <CssBaseline />
                <BottomNavigation
                    value={this.state.value}
                    onChange={(event, newValue) => {
                        this.setState({value: newValue});
                    }}
                    showLabels
                    className={classes.footer}
                >
                    <BottomNavigationAction label="Home" icon={<HomeRoundedIcon />} />
                    <BottomNavigationAction label="Git Source" icon={<GitHubIcon />} />
                    <BottomNavigationAction label="About" icon={<InfoRoundedIcon />} />
                </BottomNavigation>
            </React.Fragment>
        )
    }
}

export default withStyles(styles)(FooterMaterial);
