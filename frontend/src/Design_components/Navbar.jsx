import React from "react";
import "./../App.css";

const Navbar = () => {
  return (
    <nav className="navbar">
            <li><a href="/" className="logo">DNcoder</a></li>
      <ul className="navbar-links">
        <li><a href="/">Home</a></li>
        <li><a href="/report">Report</a></li>
        <li><a href="/dashboard">Dashboard</a></li>
        <li><a href="/settings">Settings</a></li>
      </ul>
      <div className="navbar-auth">
        <button className="login-button">Login</button>
        <button className="signup-button">Sign Up</button>
      </div>
    </nav>
  );
};

export default Navbar;
