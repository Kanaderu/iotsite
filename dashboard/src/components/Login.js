import React, { Component } from 'react';
import { connect } from "react-redux";
import { Link, Redirect } from "react-router-dom";

import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import TextField from '@material-ui/core/TextField';

import { auth } from "./actions";

class Login extends Component {

    onSubmit = e => {
        e.preventDefault();
        this.props.login(this.state.username, this.state.password);
    }

    render() {
        const { classes } = this.props;

        if (this.props.isAuthenticated) {
            return <Redirect to="/" />
        }

        return (
            <div>
            <Card>
                <CardContent>
                    <TextField
                        required
                        id="standard-required"
                        label="Username"
                        margin="normal"
                    />
                    <br />
                    <TextField
                        id="standard-password-input"
                        label="Password"
                        type="password"
                        autoComplete="current-password"
                        margin="normal"
                    />
                </CardContent>
            </Card>
            <form onSubmit={this.onSubmit}>
                <fieldset>
                    <legend>Login</legend>
                    {/* display errors */}
                    {this.props.errors.length > 0 && (
                        <ul>
                            {this.props.errors.map(error => (
                                <li key={error.field}>{error.message}</li>
                            ))}
                        </ul>
                    )}
                    {/* build login form */}
                    <p>
                        <label htmlFor="username">Username:</label>
                        <input
                            type="text" id="username"
                            onChange={e => this.setState({username: e.target.value})} />
                    </p>
                    <p>
                      <label htmlFor="password">Password</label>
                      <input
                            type="password" id="password"
                            onChange={e => this.setState({password: e.target.value})} />
                    </p>
                    <p>
                        <button type="submit">Login</button>
                    </p>

                    <p>
                        Don't have an account? <Link to="/register">Register</Link>
                    </p>
                </fieldset>
            </form>
            </div>
        )
    }
}

const mapStateToProps = state => {
  let errors = [];
  if (state.auth.errors) {
    errors = Object.keys(state.auth.errors).map(field => {
      return {field, message: state.auth.errors[field]};
    });
  }
  return {
    errors,
    isAuthenticated: state.auth.isAuthenticated
  };
}

const mapDispatchToProps = dispatch => {
  return {
    login: (username, password) => {
      return dispatch(auth.login(username, password));
    }
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(Login);

