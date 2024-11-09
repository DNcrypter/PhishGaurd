import React, { useState } from "react";
import Popup from "./Popup";
import "./../App.css";

const FileUpload = () => {
  const [file, setFile] = useState(null);
  const [dragging, setDragging] = useState(false);
  const [showUploadPopup, setShowUploadPopup] = useState(false);
  const [showReportPopup, setShowReportPopup] = useState(false);

  const handleDragOver = (e) => {
    e.preventDefault();
    setDragging(true);
  };

  const handleDragLeave = (e) => {
    e.preventDefault();
    setDragging(false);
  };

  const handleDrop = (e) => {
    e.preventDefault();
    setFile(e.dataTransfer.files[0]);
    setDragging(false);
  };

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = () => {
    // Handle the file upload logic
    console.log("Uploading:", file);
    setShowUploadPopup(true);

    // Trigger the second popup after 6 seconds
    setTimeout(() => {
      setShowReportPopup(true);
      // Reset the file upload container after the popup
      setTimeout(() => {
        setFile(null);
        setShowUploadPopup(false);
        setShowReportPopup(false);
      }, 3000);
    }, 6000);
  };

  const handleCancel = () => {
    setFile(null);
  };

  return (
    <div className="file-upload-container">
      <Popup message="File is uploaded successfully" show={showUploadPopup} duration={3000} />
      <Popup message="Report is sent to your email and Slack channel" show={showReportPopup} duration={3000} />
      <div 
        className={`drop-area ${dragging ? "dragging" : ""}`}
        onDragOver={handleDragOver}
        onDragLeave={handleDragLeave}
        onDrop={handleDrop}
      >
        <input 
          type="file"
          id="fileInput"
          onChange={handleFileChange}
          style={{ display: "none" }}
        />
        {file ? (
          <p>{file.name}</p>
        ) : (
          <p>Drag & drop your file here or click to select</p>
        )}
        <label htmlFor="fileInput" className="select-button">Select File</label>
      </div>
      {file && (
        <div className="buttons">
          <button className="upload-button" onClick={handleUpload}>Upload</button>
          <button className="cancel-button" onClick={handleCancel}>Cancel</button>
        </div>
      )}
    </div>
  );
};

export default FileUpload;
