// import logo from './logo.svg';
import './App.css';
import Navbar from "./Design_components/Navbar";
import FileUpload from './Design_components/FileUpload';
import DemoButton from './Design_components/DemoButton';
function App() {
  return (

    
    <div className="App">
      <Navbar />
      <FileUpload />
      <DemoButton />   
      {/* <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header> */}
    </div>
  );
}

export default App;
