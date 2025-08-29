import React, { useEffect, useState } from 'react';
import API from '../services/api';

function Maintenance() {
  const [logs, setLogs] = useState([]);

  useEffect(() => {
    async function fetchData() {
      const res = await API.get('maintenance/');
      setLogs(res.data);
    }
    fetchData();
  }, []);

  return (
    <div>
      <h2>Maintenance Logs</h2>
      <ul>
        {logs.map(log => (
          <li key={log.id}>
            Equipment ID: {log.equipment} | {log.maintenance_type} | Status: {log.status}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Maintenance;