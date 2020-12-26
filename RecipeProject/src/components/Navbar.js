import React, { Fragment } from 'react';
import { Link, NavLink } from 'react-router-dom';
import { connect } from 'react-redux';
import { logout } from '../actions/auth';

const Navbar = ({ isAuthenticated, logout }) => {
    const authLinks = (
        <li>
            <a onClick={logout}>Logout</a>
        </li>
    );

    const guestLinks = (
        <Fragment>
            <li>
                <NavLink exact to="/login">
                    Login
                </NavLink>
            </li>
            <li>
                <NavLink exact to="/signup">
                    Sign Up
                </NavLink>
            </li>
        </Fragment>
    );

    return (
        <nav>
            <Link to="/">Auth System</Link>
            <button type="button">
                <span></span>
            </button>
            <div>
                <ul>
                    <li>
                        <NavLink exact to="/">
                            Home
                        </NavLink>
                    </li>
                    {
                        <Fragment>
                            {isAuthenticated ? authLinks : guestLinks}
                        </Fragment>
                    }
                </ul>
            </div>
        </nav>
    );
};

const mapStateToProps = (state) => ({
    isAuthenticated: state.authReducer.isAuthenticated,
});

export default connect(mapStateToProps, { logout })(Navbar);
