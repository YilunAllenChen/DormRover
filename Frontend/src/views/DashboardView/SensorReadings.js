import React, { Component } from 'react';
//import Link from '@material-ui/core/Link';
import {
  Card,
  CardHeader,
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableRow
} from '@material-ui/core';

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
      <Card
      
    >
      <CardHeader title="Sensor Readings" />


      <React.Fragment>
        <Table size="small">
          <TableHead>
            <TableRow key='head'>
              <TableCell>Sensor Type</TableCell>
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
      </Card>
    );
  }
}