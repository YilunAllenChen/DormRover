import React, { Component } from 'react';
import Link from '@material-ui/core/Link';
import { makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Title from './Title';

// let ref = "http://172.20.10.13:5000/" //debug
let ref = window.location.href // production

export default class Databoard extends Component {


  constructor() {
    super();
    this.state.sensor_data = {}

    let sensors = ['IMU', 'lidar', 'temp'];
    for (let ndx in sensors) {
      this.state.sensor_data[sensors[ndx]] = {
        "id": ndx,
        "sensor_model": sensors[ndx],
        "timestamp": Date.now(),
        "reading": -1,
        "error_msg": "No error"
      };
    }
    this.getData = this.getData.bind(this);
  };

  getData() {
    let self = this;
    let _json;
    fetch(ref + "sensor_data/temp").then(res => res.json().then(json => {
      console.log("temp data: " + json);
      this.state.sensor_data['temp']['timestamp'] = Date.now();
      this.state.sensor_data['temp']['reading'] = json;
    }));

    fetch(ref + "sensor_data/lidar").then(res => res.json().then(json => {
      console.log("lidar data:" + json);
      this.state.sensor_data['lidar']['timestamp'] = Date.now();
      this.state.sensor_data['lidar']['reading'] = JSON.stringify(json);
    }));

    fetch(ref + "sensor_data/imu").then(res => res.json().then(json => {
      console.log("imu data: " + json);
      this.state.sensor_data['IMU']['timestamp'] = Date.now();
      this.state.sensor_data['IMU']['reading'] = JSON.stringify(json);
    }));
    this.setState({'dummy':!this.state.dummy});

  }

  state = {
    rows: [],
    sensor_data: {},
    dummy: true
  }

  componentDidMount() {
    // need to make the initial call to getData() to populate
    // data right away
    this.getData();
    // Now we need to make it run at a specified interval
    setInterval(this.getData, 5000); // runs every 5 seconds.
  }

  render() {

    let list = [];
    for (let sensor in this.state.sensor_data) {
      list.push(
        <TableRow key={sensor}>
          <TableCell>{sensor}</TableCell>
          <TableCell>{this.state.sensor_data[sensor]['timestamp']}</TableCell>
          <TableCell>{this.state.sensor_data[sensor]['reading']}</TableCell>
          <TableCell align="right">{this.state.sensor_data[sensor]['error_msg']}</TableCell>
        </TableRow>
      );
    }

    return (
      <React.Fragment>
        <Title>Sensor Readings</Title>
        <Table size="small">
          <TableHead>
            <TableRow key='head'>
              <TableCell>Sensor Model</TableCell>
              <TableCell>Time Stamp</TableCell>
              <TableCell>Readings</TableCell>
              <TableCell align="right">Error Message</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {list}
          </TableBody>
        </Table>
      </React.Fragment >
    );
  }
}