import React, { useState } from 'react';
import Typography from '@mui/material/Typography';
import DualSlider from './Components/DualSlider';
import { Container, Grid, Card} from '@mui/material';
import Dropdown from './Components/Dropdown';
import Image from './Components/Image';
import SingleSlider from './Components/SingleSlider'


export default function Task2() {
  const [selectedValue, setSelectedValue] = useState('camera 11/2022_12_15_15_51_19_927_rgb_left.png');
  const [sliderValues1, setSliderValues1] = useState({ lowerBound: 50, upperBound: 80 });
  const [sliderValues2, setSliderValues2] = useState({ lowerBound: 50, upperBound: 450 });
  const [sliderValue3, setSliderValue3] = useState(0.50)

  const handleDropdownChange = (value) => {
    setSelectedValue(value);
  };

  const handleSliderChange1 = (event, values) => {
    setSliderValues1({ lowerBound: values[0], upperBound: values[1] });
  };

  const handleSliderChange2 = (event, values) => {
    setSliderValues2({ lowerBound: values[0], upperBound: values[1] });
  };

  const handleSliderChange3 = (event, value) => {
    setSliderValue3(value);
  };

  return (
    <Container>
      <Grid container spacing={2}>
        <Grid item xs={6}>
          <br></br>
          <Card>
            <Image filePath={selectedValue} isEdited={false}/>
          </Card>
          <br></br>
        </Grid>
        <Grid item xs={6}>
          <br></br>
          <Card>
            <Image filePath={selectedValue} isEdited={true} 
                  segUpper={sliderValues1.upperBound} segLower={sliderValues1.lowerBound} 
                  areaUpper={sliderValues2.upperBound} areaLower={sliderValues2.lowerBound}
                  axisRatio={sliderValue3}
                  task={2}/>
          </Card>
          <br></br>
        </Grid>
      </Grid>
      <Dropdown selectedValue={selectedValue} onDropdownChange={handleDropdownChange} />
      <DualSlider title="Rough Segmentation Mask Slider" start={0} stop={255} step={10} lowerBound={sliderValues1.lowerBound} upperBound={sliderValues1.upperBound} onSliderChange={handleSliderChange1} />
      <DualSlider title="Area Threshold" start={0} stop={500} step={10} lowerBound={sliderValues2.lowerBound} upperBound={sliderValues2.upperBound} onSliderChange={handleSliderChange2} />
      <SingleSlider title="Minor and Major Axis Ratio Threshold" start={0} stop={2} step={0.05} value={sliderValue3} onSliderChange={handleSliderChange3}/>
    </Container>
  );
}