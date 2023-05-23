import React, { useState } from 'react';
import Typography from '@mui/material/Typography';
import DualSlider from './Components/DualSlider';
import { Container, Grid, Card} from '@mui/material';
import Dropdown from './Components/Dropdown';
import Image from './Components/Image';

export default function Task1() {
  const [selectedValue, setSelectedValue] = useState('camera 11/2022_12_15_15_51_19_927_rgb_left.png');

  const handleDropdownChange = (value) => {
    setSelectedValue(value);
  };

  return (
    <Container>
      <Grid container spacing={2}>
        <Grid item xs={6}>
          <Card>
            <Image filePath={selectedValue} isEdited={false} />
          </Card>
        </Grid>
        <Grid item xs={6}>
          <Card>
            <Image filePath={selectedValue} isEdited={true} />
          </Card>
        </Grid>
      </Grid>
      <DualSlider />
      <Dropdown selectedValue={selectedValue} onDropdownChange={handleDropdownChange} />
    </Container>
  );
}