import React, { useEffect, useState } from 'react';
import Select from '@mui/material/Select';
import MenuItem from '@mui/material/MenuItem';
import ListSubheader from '@mui/material/ListSubheader';

export default function Dropdown({ selectedValue, onDropdownChange }) {
  const [groupItems, setGroupItems] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/dropdown_data/')
      .then((response) => response.json())
      .then((data) => {
        const groups = {};
        data.forEach((file) => {
          if (groups[file.group]) {
            groups[file.group].push(file);
          } else {
            groups[file.group] = [file];
          }
        });
        const groupMenuItems = Object.entries(groups).map(([group, files]) => [
          <ListSubheader key={group}>{group}</ListSubheader>,
          ...files.map((file) => (
            <MenuItem key={`${group}/${file.name}`} value={`${group}/${file.name}`}>
              {file.name}
            </MenuItem>
          )),
        ]);
        setGroupItems(groupMenuItems.flat());
      })
      .catch((error) => {
        console.error('Error fetching file information:', error);
      });
  }, []);

  const handleChange = (event) => {
    const value = event.target.value;
    onDropdownChange(value); // Pass the key to the callback
  };

  return (
    <Select
      value={selectedValue}
      onChange={handleChange}
      style={{ minWidth: '300px', fontSize: '18px' }}
    >
      {groupItems}
    </Select>
  );
}