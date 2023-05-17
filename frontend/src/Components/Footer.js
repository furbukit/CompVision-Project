import React from 'react';
import {Link, Typography } from '@mui/material';

const Footer = () => {
    return (
        <div>
        <br></br>
        <Typography variant="body2" color="text.secondary" align="center">
        Matthew Walsh, William Tran, Jasper Greenland
        <br></br>
        <Link color="inherit" href="https://github.com/furbukit/CompVision-Project">
            Our Github
        </Link>
        </Typography>
        </div>
    );
  };
  
  export default Footer;