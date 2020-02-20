const initialState = {
    access: localStorage.getItem("access"),
    refresh: localStorage.getItem("refresh"),
    isAuthenticated: null,
    isLoading: true,
    user: null,
    errors: {},
};


export default function auth(state=initialState, action) {

    let ret = {}
    switch (action.type) {

        case 'USER_LOADING':
            ret = {...state, isLoading: true};
            return ret;
        case 'USER_LOADED':
            ret = {...state, isAuthenticated: true, isLoading: false, user: action.user};
            return ret;

        case 'LOGIN_SUCCESSFUL':
            localStorage.setItem("access", action.data.access);
            localStorage.setItem("refresh", action.data.refresh);
            ret = {...state, ...action.data, isAuthenticated: true, isLoading: false, errors: null};
            return ret;
        case 'LOGIN_FAILED':

        case 'LOGOUT_SUCCESSFUL':
            localStorage.removeItem("access");
            localStorage.removeItem("refresh");
            ret = {...state, errors: action.data, access: null, refresh: null, user: null,
                isAuthenticated: false, isLoading: false};
            return ret;

        case 'REGISTRATION_SUCCESSFUL':
            localStorage.setItem("access", action.data.access);
            localStorage.setItem("refresh", action.data.refresh);
            ret = {...state, ...action.data, isAuthenticated: true, isLoading: false, errors: null};
            return ret;
        case 'REGISTRATION_FAILED':

        case 'AUTHENTICATION_ERROR':
            ret = {...state, ...action.data, isAuthenticated: false, errors: action.data}
            return ret;

        default:
            return state;
    }
}
