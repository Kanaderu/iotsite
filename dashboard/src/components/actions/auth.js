export const login = (username, password) => {
    return (dispatch, getState) => {
        let headers = { "Content-Type": "application/json" };
        let body = JSON.stringify({ username, password });

        return fetch("/ws/api/login/", { headers, body, method: "POST" })
            .then(res => {
                if (res.status < 500) {
                    return res.json().then(data => {
                        return { status: res.status, data };
                    })
                } else {
                    console.log("Server Error!");
                    throw res;
                }
            })
            .then(res => {
                if (res.status === 200) {
                    dispatch({ type: 'LOGIN_SUCCESSFUL', data: res.data });
                    return res.data;
                } else if (res.status === 403 || res.status === 401) {
                    dispatch({ type: "AUTHENTICATION_ERROR", data: res.data });
                    throw res.data;
                } else {
                    dispatch({ type: "LOGIN_FAILED", data: res.data });
                    throw res.data;
                }
            })
    }
}

export const register = (username, password) => {
    return (dispatch, getState) => {
        let headers = { "Content-Type": "application/json" };
        let body = JSON.stringify({ username, password });

        return fetch("/ws/api/register/", { headers, body, method: "POST" })
            .then(res => {
                if (res.status < 500) {
                    return res.json().then(data => {
                        return { status: res.status, data };
                    })
                } else {
                    console.log("Server Error!");
                    throw res;
                }
            })
            .then(res => {
                if (res.status === 200) {
                    dispatch({type: 'REGISTRATION_SUCCESSFUL', data: res.data });
                    return res.data;
                } else if (res.status === 403 || res.status === 401) {
                    dispatch({type: "AUTHENTICATION_ERROR", data: res.data});
                    throw res.data;
                } else {
                    dispatch({type: "REGISTRATION_FAILED", data: res.data});
                    throw res.data;
                }
            }
        )
    }
}

export const logout = () => {
  return (dispatch, getState) => {
    const access = localStorage.access;
    let headers = { "Content-Type": "application/json",
                    "Authorization": `Bearer ${ access }`
                    };

    const refresh = localStorage.refresh;
    let body = JSON.stringify({ refresh });

    return fetch("/ws/api/logout/", { headers, body, method: "POST" })
    .then(res => {
          dispatch({ type: 'LOGOUT_SUCCESSFUL' });
          return res.json().then(data => data);
    })
    .then(res => {
        if (res.status === 204) {
            return {status: res.status, data: {}};
        } else if (res.status < 500) {
            return res.json().then(data => {
                return {status: res.status, data};
            })
        } else {
            console.log("Server Error!");
            throw res;
        }
    })
    /*
      .then(res => {
        if (res.status === 204) {
          dispatch({ type: 'LOGOUT_SUCCESSFUL' });
          return res.data;
        } else if (res.status === 403 || res.status === 401) {
          dispatch({ type: "AUTHENTICATION_ERROR", data: res.data });
          throw res.data;
        }
      })
      */
  }
}

export const getAccountFetch = () => {
    return dispatch => {
        const token = localStorage.access;
        let body = JSON.stringify({ token });
        if (token) {
            return fetch("/ws/api/verify/", {
                method: "POST",
                headers: {
                  "Content-Type": "application/json",
                  Accept: "application/json",
                  //"Authorization": `Bearer ${ token }`
                },
                body
            })
            .then(res => {
                if (res.status == 200) {
                    return res.json().then(data => {
                        return { status: res.status, data };
                    })
                } else {
                    throw res;
                    console.log("Server Error!");
                }
            })
            .then(res => {
                if (res.status === 200) {
                    dispatch({
                        type: 'USER_LOADED',
                        data: res.data
                    });
                    {/* TODO: set user info */}
                    return res.data;
                } else if (res.status === 401) {
                    {/* TODO: refresh login */}
                    console.log("401!")
                    console.log(res.data)
                } else {
                    console.log("LOGIN FAILED");
                    dispatch({
                        type: 'LOGIN_FAILED',
                        data: res.data
                    });
                    throw res.data;
                }
            })
            /*
            .then(resp => resp.json())
            .then(data => {
                if (data.message) {
                    // An error will occur if the token is invalid.
                    // If this happens, you may want to remove the invalid token.
                    localStorage.removeItem("token")
                } else {
                    dispatch(loginUser(data.user))
                }
            })
            */
        }
    }
}
