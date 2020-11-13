import React from 'react';
import Link from '@material-ui/core/Link';
import { makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Title from './Title';

// Generate Order Data
function createData(id, sensor_model, timestamp, reading_name, readings, unit, error_msg) {
  return {id, sensor_model, timestamp, reading_name, readings, unit, error_msg};
}

function fetch_sensor_data(name){
  let timestamp, reading, error_msg;
  fetch('http://localhost:5000/sensor_data/' + name).then(res => {
    
  }).then(data => {
    console.log('data', data);
  })
}

const rows = [
  createData(1, "LSM9DS1  IMU", Date.now(), "velocity_x", fetch_sensor_data('lidar'), "m/s", null),
  createData(2, "VL53L0X  Lidar sensor", Date.now(), "distance", 10.3, 'm',null)
];

function preventDefault(event) {
  event.preventDefault();
}

const useStyles = makeStyles((theme) => ({
  seeMore: {
    marginTop: theme.spacing(3),
  },
}));

export default function Orders() {
  const classes = useStyles();
  return (
    <React.Fragment>
      <Title>Sensor Readings</Title>
      <Table size="small">
        <TableHead>
          <TableRow key='head'>
              <TableCell>Sensor Model</TableCell>
              <TableCell>Time Stamp</TableCell>
              <TableCell>Data Key</TableCell>
              <TableCell>Data Value</TableCell>
              <TableCell>Data Unit</TableCell>
              <TableCell align="right">Error Message</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow key={row.id}>
              <TableCell>{row.sensor_model}</TableCell>
              <TableCell>{row.timestamp}</TableCell>
              <TableCell>{row.reading_name}</TableCell>
              <TableCell>{row.readings}</TableCell>
              <TableCell>{row.unit}</TableCell>
              <TableCell align="right">{row.error_msg}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
      <div className={classes.seeMore}>
        <Link color="primary" href="#" onClick={preventDefault}>
          See more orders
        </Link>
      </div>
    </React.Fragment>
  );
}