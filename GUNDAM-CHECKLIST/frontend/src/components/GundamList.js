import React, { useEffect, useState } from "react";
import "./GundamList.css";

const GundamList = () => {
  const [gundams, setGundams] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/gundams/")
      .then((res) => res.json())
      .then((data) => setGundams(data));
  }, []);

  return (
    <div className="gundam-container">
      {gundams.map((gundam) => (
        <div key={gundam.id} className="gundam-card">
          <img src={gundam.image} alt={gundam.name} />
          <h3>{gundam.name}</h3>
          <p>Size: {gundam.size}</p>
        </div>
      ))}
    </div>
  );
};

export default GundamList;
