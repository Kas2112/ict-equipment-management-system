import React from 'react';
import { Link } from 'react-router-dom';

function Navbar() {
  return (
    <nav>
      <Link to="/">Dashboard</Link> |{" "}
      <Link to="/equipment">Equipment</Link> |{" "}
      <Link to="/requests">Requests</Link> |{" "}
      <Link to="/maintenance">Maintenance</Link> |{" "}
      <Link to="/reports">Reports</Link> |{" "}
      <Link to="/login">Login</Link>
    </nav>
  );
}

export default Navbar;