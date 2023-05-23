import React, { useState, useEffect } from 'react';

export default function Image(props) {
  const [imageData, setImageData] = useState('');

  useEffect(() => {
    const handleImageRequest = () => {
      let url = "";
      if(props.isEdited){
        url = `http://localhost:8000/get_image?path=${props.filePath}&edit=t&segupper=${props.segUpper}&seglower=${props.segLower}&areaupper=${props.areaUpper}&arealower=${props.areaLower}&axisratio=${props.axisRatio}&task=${props.task}`;
      }
      else{
        url = `http://localhost:8000/get_image?path=${props.filePath}&edit=f`
      }
      fetch(url)
        .then((response) => response.blob())
        .then((blob) => {
          const imageUrl = URL.createObjectURL(blob);
          setImageData(imageUrl);
        })
        .catch((error) => {
          console.error('Error fetching image:', error);
        });
    };

    handleImageRequest();
  }, [props.filePath, props.segUpper, props.segLower, props.areaUpper, props.areaLower, props.axisRatio]);

  return (
    <div>
      {imageData && (
        <div style={{ width: '100%', height: '100%' }}>
          <img src={imageData} alt="Awaiting Input" style={{ width: '100%', height: '100%', objectFit: 'cover' }} />
        </div>
      )}
    </div>
  );
}