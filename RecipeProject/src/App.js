import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

// pages
import Home from './pages/Home';
import Login from './pages/Login';
import Signup from './pages/Signup';
import Activate from './pages/Activate';
import ResetPassword from './pages/ResetPassword';
import ResetPasswordConfirm from './pages/ResetPasswordConfirm';

import Layout from './layout/Layout';

// import { Provider } from 'react-redux'
// import store from './store';

const App = () => (
    <Router>
        <Layout>
            <Switch>
                <Route exact path="/" component={Home} />
                <Route exact path="/login" component={Login} />
                <Route exact path="/signup" component={Signup} />
                <Route exact path="/reset_password" component={ResetPassword} />
                <Route
                    exact
                    path="/password/reset/confirm/:uid/:token"
                    component={ResetPasswordConfirm}
                />
                <Route
                    exact
                    path="/activate/:uid/:token"
                    component={Activate}
                />
            </Switch>
        </Layout>
    </Router>
);

export default App;
