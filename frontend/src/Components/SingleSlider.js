import React from 'react';
import Box from '@mui/material/Box';
import Slider from '@mui/material/Slider';
import Typography from '@mui/material/Typography';
import PropTypes from 'prop-types';

export default function SingleSlider({ title, start, stop, step, value, onSliderChange }) {
  const minRange = start;
  const maxRange = stop;
  const stepSize = step;

  const marks = [];
  let counter = 0;

  for (let i = minRange; i <= maxRange; i += stepSize) {
    const formattedValue = i.toFixed(2);
    
    if (counter % 5 === 0) {
      marks.push({ value: formattedValue, label: formattedValue });
    }
    
    counter++;
  }

  return (
    <Box sx={{ m: 3 }}>
      <Typography gutterBottom>{title}</Typography>
      <Slider
        getAriaLabel={() => title}
        value={value}
        onChange={onSliderChange}
        min={minRange}
        max={maxRange}
        step={stepSize}
        marks={marks}
      />
    </Box>
  );
}

SingleSlider.propTypes = {
  title: PropTypes.string.isRequired,
  start: PropTypes.number.isRequired,
  stop: PropTypes.number.isRequired,
  step: PropTypes.number.isRequired,
  value: PropTypes.number.isRequired,
  onSliderChange: PropTypes.func.isRequired,
};