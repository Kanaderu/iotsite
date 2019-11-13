import auth from "./auth";
import { combineReducers } from 'redux'

const ponyApp = combineReducers({
    auth,
})
export default ponyApp;
