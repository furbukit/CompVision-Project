import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Task1 from './Task1';
import Task2 from './Task2';
import Task3 from './Task3';
import ResponsiveAppBar from './Components/ResponsiveAppBar';
import Footer from './Components/Footer';
import { Box } from '@mui/material';
import './App.css';

function App() {
  return (
    <BrowserRouter>
      <Box>
        <ResponsiveAppBar />
        <div className="content">
          <Routes>
            <Route path="/task1" element={<Task1 />} />
            <Route path="/task2" element={<Task2 />} />
            <Route path="/task3" element={<Task3 />} />
          </Routes>
        </div>
        <Footer />
      </Box>
    </BrowserRouter>
  );
}

export default App;