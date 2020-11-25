import React from 'react';
import {
  Box,
  Container,
  makeStyles,
  Card,
  CardContent,
} from '@material-ui/core';
//import { Pagination } from '@material-ui/lab';
import Page from 'src/components/Page';
import Toolbar from './Toolbar';
//import MarsRover from "../public/static/images/marsrover";


const useStyles = makeStyles((theme) => ({
  root: {
    backgroundColor: theme.palette.background.dark,
    minHeight: '100%',
    paddingBottom: theme.spacing(3),
    paddingTop: theme.spacing(3)
  },
  productCard: {
    height: '100%'
  }
}));

const ProjectDescription = () => {
  const classes = useStyles();

  return (
    <Page
      className={classes.root}
      title="ProjectDescription"
    >
      <Container maxWidth={false}>
        <Toolbar />
        <Box mt={3}>
        <Card>
          <CardContent>
            <Box maxWidth={500}>
            Baseline:<br></br>
           A Raspberry Pi-based rover robot that can be remotely controlled via a web GUI.<br></br>
           The rover robot will have these components (and their configuration circuits) on the board:<br></br>
           Motors and Dual H-bridge for motors control<br></br>
           Pi Camera<br></br>
           External battery<br></br>
           IMU<br></br>
           At least one other sensor (temperature / luminosity / speaker / etc)<br></br>
           The GUI will include these features and functionalities:<br></br>
           Keyboard control over the rover<br></br>
           Video stream of what the rover’s camera is capturing.<br></br>
           Motion status of the rover (velocity, acceleration)<br></br>
           Sensor data captured by the onboard sensors (temperature / luminosity / speaker / etc)<br></br>
          <br></br>
          Add-on Features (If time permits):<br></br>
           More sensors on the board and more sensor data displayed/delivered through the web GUI<br></br>
           Environment sensors like temperature, humidity, luminosity, etc<br></br>
           Location (with GPS)<br></br>
           Sound<br></br>
           More<br></br>
           Automatic obstacle avoidance (motion control override) with Lidar sensors<br></br>
           Auto navigation with Google Coral TPU ML Accelerator and pre-trained deep learning models<br></br>
           Mapping of the surrounding area<br></br>        
              
            </Box>
          </CardContent>
        </Card>
      </Box>

        <Box
          mt={3}
          display="flex"
          justifyContent="center"
        >
          
        </Box>
      </Container>
    </Page>
  );
};

export default ProjectDescription;
