import React, { useState } from "react";
import "./../App.css";

const FileUpload = () => {
  const [file, setFile] = useState(null);
  const [dragging, setDragging] = useState(false);

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
  };

  const handleCancel = () => {
    setFile(null);
  };

  return (
    <div className="file-upload-container">
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
