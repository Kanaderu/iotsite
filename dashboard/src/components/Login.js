import React, { Component } from 'react';
import { connect } from "react-redux";
import { Link, Redirect } from "react-router-dom";

import { withStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import Snackbar from '@material-ui/core/Snackbar';
import SnackbarContent from '@material-ui/core/SnackbarContent';

import { auth } from "./actions";

const styles = theme => ({
    button: {
        margin: theme.spacing(1),
    },
    card: {
        width: 400
    }
});

class Login extends Component {

    state = {
        username: "",
        password: "",
    }

    onSubmit = e => {
        e.preventDefault();
        this.props.login(this.state.username, this.state.password);
    };

    render() {
        const { classes } = this.props;

        if (this.props.isAuthenticated) {
            return <Redirect to="/" />
        }

        return (
            <Card>
                <CardContent>
                    <form onSubmit={this.onSubmit}>
                        {this.props.errors.length > 0 && (
                            <ul>
                                {this.props.errors.map(error => (
                                    <li key={error.field}>{error.message}</li>
                                ))}
                            </ul>
                        )}
                        <TextField
                            required
                            id="username"
                            label="Username"
                            margin="normal"
                            onChange={e => this.setState({username: e.target.value})}
                        />
                        <br />
                        <TextField
                            id="password"
                            label="Password"
                            type="password"
                            autoComplete="current-password"
                            margin="normal"
                            onChange={e => this.setState({password: e.target.value})}
                        />
                        <br />
                        <Button type="submit" variant="contained" color="primary" className={classes.button}>
                            Login
                        </Button>
                        <Link to="/register">
                            <Button variant="contained" color="secondary" className={classes.button}>
                                Register
                            </Button>
                        </Link>
                    </form>
                </CardContent>
            </Card>
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
};

const mapDispatchToProps = dispatch => {
    return {
        login: (username, password) => dispatch(auth.login(username, password)),
    };
};

export default connect(mapStateToProps, mapDispatchToProps)(withStyles(styles)(Login));
