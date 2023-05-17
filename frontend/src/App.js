import React, { Component } from 'react';
import { BrowserRouter } from 'react-router-dom';
import { Route } from 'react-router-dom';
import  Task1 from './Task1';
import  Task2 from './Task2';
import  Task3 from './Task3';
import ResponsiveAppBar from './Components/ResponsiveAppBar';
import Footer from './Components/Footer'
import { Box } from '@mui/material';
import './App.css';

/*
const BaseLayout = () => (
<Box className="base-layout">
<ResponsiveAppBar></ResponsiveAppBar>
    <div className="content">
      <Route path="/" component={CustomersList} />
      <Route path="/task1" exact component={Task1} />
      <Route path="/task2"  exact component={Task2} />
      <Route path="/task3" exact component={Task3} />

    </div>
  <Footer></Footer>
</Box>
)
*/

class App extends Component {
  render() {
    return (
      <BrowserRouter>
      <Box>
        <ResponsiveAppBar/>
        <div className="content">
          <Route path="/task1" exact component={Task1} />
          <Route path="/task2"  exact component={Task2} />
          <Route path="/task3" exact component={Task3} />
        </div>
        <Footer/>
      </Box>
      </BrowserRouter>
    );
  }
}

export default App;
