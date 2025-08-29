import React, { useEffect, useState } from 'react';
import API from '../services/api';
import { useParams } from 'react-router-dom';

function EquipmentDetail() {
  const { id } = useParams();
  const [equipment, setEquipment] = useState(null);

  useEffect(() => {
    async function fetchData() {
      const res = await API.get(`equipment/${id}/`);
      setEquipment(res.data);
    }
    fetchData();
  }, [id]);

  if (!equipment) return <div>Loading...</div>;

  return (
    <div>
      <h2>Equipment Detail</h2>
      <div>Model: {equipment.model_number}</div>
      <div>Serial: {equipment.serial_number}</div>
      <div>Status: {equipment.current_status}</div>
      <div>Location: {equipment.current_location}</div>
      <div>Notes: {equipment.notes}</div>
    </div>
  );
}

export default EquipmentDetail;