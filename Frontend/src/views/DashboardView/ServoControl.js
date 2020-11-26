import React from 'react';
import clsx from 'clsx';
import PropTypes from 'prop-types';
import ArrowForwardIcon from '@material-ui/icons/ArrowForward';
import ArrowBackIcon from '@material-ui/icons/ArrowBack';
import AllInclusiveIcon from '@material-ui/icons/AllInclusive';
import {
  Card,
  Grid,
  Button,
  CardHeader,
  Divider,
  makeStyles
} from '@material-ui/core';


const useStyles = makeStyles(({
  root: {
    height: '100%'
  },
  image: {
    height: 48,
    width: 48
  }
}));


// let ref = 'http://localhost:5000/' // debug
let ref = window.location.href //production

async function send_key(key) {
  let response = await fetch(ref + 'command', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      "key": key
    })
  })
  return response
}



const LatestProducts = ({ className, ...rest }) => {
  const classes = useStyles();

  return (
    <Card
      className={clsx(classes.root, className)}
      {...rest}
    >
      <CardHeader        
        title="Servo Control"
      />
      <Divider />

      <Grid style={{'height': 50}} />
      <Grid style={{'text-align': 'center' }}>
        <Button onClick={() => send_key('servo_left')}>
          <ArrowBackIcon />
        </Button>
        <Button onClick={() => send_key('servo_reset')}>
          <AllInclusiveIcon />
        </Button>
        <Button onClick={() => send_key('servo_right')}>
          <ArrowForwardIcon />
        </Button>
      </Grid>
      <Grid style={{'height': 50}} />

    </Card>
  );
};

LatestProducts.propTypes = {
  className: PropTypes.string
};

export default LatestProducts;
