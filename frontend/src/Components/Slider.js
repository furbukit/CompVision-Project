// For individual values (just one number e.g. threshold)
import * as React from 'react';
import Box from '@mui/material/Box';
import Slider from '@mui/material/Slider';


export default function Slider({ default, step, marks, min, max }) {
  return (
    <Box sx={{ width: 320 }}>
      <Slider
      aria-label="Temperature"
      defaultValue={default}
      getAriaValueText={valuetext}
      valueLabelDisplay="auto"
      step={step}
      marks = {marks}
      min={min}
      max={max}
      />
    </Box>
)}
