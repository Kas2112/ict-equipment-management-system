import React, { useEffect, useState } from 'react';
import API from '../services/api';
import { Link } from 'react-router-dom';

function EquipmentList() {
  const [equipment, setEquipment] = useState([]);

  useEffect(() => {
    async function fetchData() {
      const res = await API.get('equipment/');
      setEquipment(res.data);
    }
    fetchData();
  }, []);

  return (
    <div>
      <h2>Equipment List</h2>
      <ul>
        {equipment.map(e => (
          <li key={e.id}>
            <Link to={`/equipment/${e.id}`}>{e.model_number} ({e.serial_number})</Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default EquipmentList;