import React, { useState } from 'react';
import Typography from '@mui/material/Typography';
import DualSlider from './Components/DualSlider';
import { Container, Grid, Card} from '@mui/material';
import Dropdown from './Components/Dropdown';
import Image from './Components/Image';
import SingleSlider from './Components/SingleSlider'

export default function Task1() {
  const [selectedValue, setSelectedValue] = useState('');
  const [sliderValue1, setSliderValue1] = useState(90);
  const [sliderValues2, setSliderValues2] = useState({ lowerBound: 6, upperBound: 210 });
  const [sliderValue3, setSliderValue3] = useState(0.40)
  const [sliderValue4, setSliderValue4] = useState(30)

  const handleDropdownChange = (value) => {
    console.log(selectedValue)
    setSelectedValue(value);
  };

  const handleSliderChange1 = (event, value) => {
    setSliderValue1(value);
  };

  const handleSliderChange2 = (event, values) => {
    setSliderValues2({ lowerBound: values[0], upperBound: values[1] });
  };

  const handleSliderChange3 = (event, value) => {
    setSliderValue3(value);
  };

  const handleSliderChange4 = (event, value) => {
    setSliderValue4(value);
  };


  return (
    <Container>
      <Grid container spacing={2}>
        <Grid item xs={6}>
          <br></br>
          {selectedValue && (
            <Card>
              <Image filePath={selectedValue} isEdited={false}/>
            </Card>
          )}
          <br></br>
        </Grid>
        <Grid item xs={6}>
          <br></br>
          {selectedValue && (
            <Card>
              <Image filePath={selectedValue} isEdited={true} 
                    segUpper={sliderValue1} segLower={sliderValue4}
                    areaUpper={sliderValues2.upperBound} areaLower={sliderValues2.lowerBound}
                    axisRatio={sliderValue3} 
                    task={2}/>
            </Card>
          )}
          <br></br>
        </Grid>
      </Grid>
      <Dropdown selectedValue={selectedValue} onDropdownChange={handleDropdownChange} />
      <SingleSlider title="tMin - Segmentation Mask" start={0} stop={255} step={10}value={sliderValue1} onSliderChange={handleSliderChange1}/>
      <SingleSlider title="tDiffColor - Segmentation Mask" start={0} stop={255} step={10}value={sliderValue4} onSliderChange={handleSliderChange4}/>
      <DualSlider title="Area Threshold" start={0} stop={300} step={2} lowerBound={sliderValues2.lowerBound} upperBound={sliderValues2.upperBound} onSliderChange={handleSliderChange2} />
      <SingleSlider title="Minor and Major Axis Ratio Threshold" start={0} stop={2} step={0.05} value={sliderValue3} onSliderChange={handleSliderChange3}/>
    </Container>
  );
}