import React from 'react';
import Link from '@material-ui/core/Link';
import { makeStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import Title from './Title';

function preventDefault(event) {
  event.preventDefault();
}

const useStyles = makeStyles({
  depositContext: {
    flex: 1,
  },
});

export default function System_status() {
  const classes = useStyles();
  return (
    <React.Fragment>
      <Title>System Status</Title>
      {get_system_status()}
    </React.Fragment>
  );

  function get_system_status() {
    let temp = [];
    let system_status = {
      "Lidar": 1,
      "IMU": 0
    }
    return (<div>{
      Object.keys(system_status).map((sensor, status) => (
        <Typography>{sensor} : {status ? "ON" : "OFF"}</Typography>
      ))}</div>)
  }
}