import React, { useEffect, useState } from "react";
import "./../App.css";

const Popup = ({ message, show, duration = 3000 }) => {
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    if (show) {
      setVisible(true);
      setTimeout(() => {
        setVisible(false);
      }, duration);
    }
  }, [show, duration]);

  return (
    visible && (
      <div className="popup">
        <p>{message}</p>
      </div>
    )
  );
};

export default Popup;
