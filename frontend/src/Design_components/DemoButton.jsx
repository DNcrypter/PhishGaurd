import React from "react";
import file_1 from "./../img/file_1.pdf"; // Example file
import file_2 from "./../img/file_2.pdf";
import file_3 from "./../img/file_3.pdf";


const DownloadButton =()=>{

    const DownloadButton1 = () => {
        const handleDownload = () => {
          const link = document.createElement("a");
          link.href = file_1;
          link.download = "file_1.pdf";
          document.body.appendChild(link);
          link.click();
          document.body.removeChild(link);
        };
      
        return (
          <button onClick={handleDownload} className="download-button">
            Download File
          </button>
        );
      };


      const DownloadButton2 = () => {
        const handleDownload = () => {
          const link = document.createElement("a");
          link.href = file_2;
          link.download = "file_2.pdf";
          document.body.appendChild(link);
          link.click();
          document.body.removeChild(link);
        };
      
        return (
          <button onClick={handleDownload} className="download-button">
            Download File
          </button>
        );
      };


      const DownloadButton3 = () => {
        const handleDownload = () => {
          const link = document.createElement("a");
          link.href = file_3;
          link.download = "file_3.pdf";
          document.body.appendChild(link);
          link.click();
          document.body.removeChild(link);
        };
      
        return (
          <button onClick={handleDownload} className="download-button ">
            Download File
          </button>
        );
      };

      return (
        <div className="text-align">
        <h3 className="text-align">Demo Files</h3>
        <DownloadButton1  />
        <DownloadButton2  />
        <DownloadButton3  />
        </div>
      );


}

export default DownloadButton;
