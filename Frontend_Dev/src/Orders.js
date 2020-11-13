import React, { Component } from 'react';
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
  return { id, sensor_model, timestamp, reading_name, readings, unit, error_msg };
}


function preventDefault(event) {
  event.preventDefault();
}

const useStyles = makeStyles((theme) => ({
  seeMore: {
    marginTop: theme.spacing(3),
  },

}));

export default class Orders extends Component {


  constructor() {
    super();
    this.state.rows = [
      createData(0, "Example", "now", "some_data", 'N/A', "m/s^2", "Example"),
      createData(1, "LSM9DS1  IMU", Date.now(), "velocity_x", 'N/A', "m/s", 'N/A'),
      createData(2, "VL53L0X  Lidar sensor", Date.now(), "distance", 'N/A', 'm', "N/A")
    ];
    this.getData = this.getData.bind(this);
  };

  onChange(state) {
    this.setState(state);
  }

  getData() {
    let self = this;
    let _json;
    fetch("http://localhost:5000/sensor_data/temp").then(res => res.json().then(json => {
      _json = json;
      this.setState({
        rows: [
          createData(0, "Example", "now", "some_data", -65536, "m/s^2", "Example"),
          createData(1, "LSM9DS1  IMU", Date.now(), "velocity_x", 'N/A', "m/s", 'N/A'),
          createData(3, "LSM9DS1  IMU", Date.now(), "temperature", _json, 'm', 'N/A'),
          createData(2, "VL53L0X  Lidar sensor", Date.now(), "distance", 'N/A', 'm', 'N/A'),
        ]
      });
    }
    ));

  }

  state = {
    rows: [],
  }

  componentDidMount() {
    // need to make the initial call to getData() to populate
    // data right away
    this.getData();

    // Now we need to make it run at a specified interval
    setInterval(this.getData, 1000); // runs every 5 seconds.
  }

  render() {
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
            {this.state.rows.map((row) => (
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
      </React.Fragment >
    );
  }
}