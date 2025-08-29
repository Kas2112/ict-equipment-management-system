import React, { useEffect, useState } from 'react';
import API from '../services/api';

function Requests() {
  const [requests, setRequests] = useState([]);

  useEffect(() => {
    async function fetchData() {
      const res = await API.get('requests/');
      setRequests(res.data);
    }
    fetchData();
  }, []);

  return (
    <div>
      <h2>Requests</h2>
      <ul>
        {requests.map(r => (
          <li key={r.id}>
            {r.purpose} ({r.status}) - From: {r.required_from_date} To: {r.required_to_date}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Requests;