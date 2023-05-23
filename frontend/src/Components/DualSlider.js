// For a range (e.g. a max and min value)
import * as React from 'react';
import Box from '@mui/material/Box';
import Slider from '@mui/material/Slider';
import Typography from '@mui/material/Typography'
import { SliderThumb } from '@mui/material/Slider';
import styled from '@emotion/styled';
import PropTypes from 'prop-types';


const DualSlide = styled(Slider)(({ title, upperBound, lowerBound, onSliderChange }) => ({
    color: '#3a8589',
    height: 3,
    padding: '13px 0',
    '& .MuiSlider-thumb': {
        height: 27,
        width: 27,
        backgroundColor: '#fff',
        border: '1px solid currentColor',
        '&:hover': {
        boxShadow: '0 0 0 8px rgba(58, 133, 137, 0.16)',
        },
        '& .airbnb-bar': {
        height: 9,
        width: 1,
        backgroundColor: 'currentColor',
        marginLeft: 1,
        marginRight: 1,
        },
    },
    '& .MuiSlider-track': {
        height: 3,
    },
    '& .MuiSlider-rail': {
        color: '#d8d8d8',
        opacity: 1,
        height: 3,
    },
}));

function DualSliderThumbComponent(props) {
    const { children, ...other } = props;
    return (
        <SliderThumb {...other}>
        {children}
        <span className="airbnb-bar" />
        <span className="airbnb-bar" />
        <span className="airbnb-bar" />
        </SliderThumb>
    );
}
  
DualSliderThumbComponent.propTypes = {
    children: PropTypes.node,
};

export default function DualSlider({ title, start, stop, step, lowerBound, upperBound, onSliderChange }) {
    const minRange = start;
    const maxRange = stop;
    const stepSize = step;

    const marks = [];
    for (let i = minRange; i <= maxRange; i += stepSize) {
        if ((i - minRange) % (step*20) === 0) {
            marks.push({ value: i, label: i.toString() });
          }
    }

    return (
      <Box sx={{ m: 3 }}>
        <Typography gutterBottom>{title}</Typography>
        <DualSlide
          slots={{ thumb: DualSliderThumbComponent }}
          getAriaLabel={(index) => (index === 0 ? 'Minimum price' : 'Maximum price')}
          value={[lowerBound, upperBound]}
          onChange={onSliderChange}
          min={minRange}
          max={maxRange}
          step={stepSize}
          marks={marks}
        />
      </Box>
    );
  }