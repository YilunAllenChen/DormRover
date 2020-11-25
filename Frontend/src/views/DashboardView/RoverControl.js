import React from 'react';
import clsx from 'clsx';
import PropTypes from 'prop-types';


import {
  Button,
  Box,
  Card,
  CardContent,
  Grid,
  Typography,
  colors,
  makeStyles
} from '@material-ui/core';
//import Container from 'react-bootstrap/Container';
//import Row from 'react-bootstrap/Row';
//import Col from 'react-bootstrap/Col';
import ArrowUpwardIcon from '@material-ui/icons/ArrowUpward';
import ArrowDownwardIcon from '@material-ui/icons/ArrowDownward';
import ArrowForwardIcon from '@material-ui/icons/ArrowForward';
import ArrowBackIcon from '@material-ui/icons/ArrowBack';
//import { Button, Grid } from '@material-ui/core';

const useStyles = makeStyles((theme) => ({
  root: {
    height: '100%'
  },
  avatar: {
    backgroundColor: colors.red[600],
    height: 56,
    width: 56
  },
  differenceIcon: {
    color: colors.red[900]
  },
  differenceValue: {
    color: colors.red[900],
    marginRight: theme.spacing(1)
  }
}));

const Controls = ({ className, ...rest }) => {
  const classes = useStyles();

  return (
    <Card
      className={clsx(classes.root, className)}
      {...rest}
    >
      <CardContent>
        <Grid
          container
          justify="space-between"
          spacing={3}
        >
          <Grid item>
            <Typography
              color="textSecondary"
              gutterBottom
              variant="h6"
            >
              Rover Control
            </Typography>
              <React.Fragment>
                <Grid style={{ padding: 30}}>
                  <Button onClick={() => send_key('w')}>
                  <ArrowUpwardIcon />
                  </Button>
                </Grid>
                <Grid style={{'margin': 'auto'}}>
                  <Button onClick={() => send_key('a')}>
                  <ArrowBackIcon />
                  </Button>
                
                
                  <Button onClick={() => send_key('d')}>
                  <ArrowForwardIcon />
                  </Button>
                </Grid>
                <Grid style={{padding: 30}}>
                  <Button onClick={() => send_key('s')}>
                  <ArrowDownwardIcon />
                  </Button>
                </Grid>
              </React.Fragment>
          </Grid>
          
        </Grid>
        <Box
          mt={2}
          display="flex"
          alignItems="center"
        >
          
        </Box>
      </CardContent>
    </Card>
  );
};

Controls.propTypes = {
  className: PropTypes.string
};

// let ref = 'http://localhost:5000/' // debug
let ref = window.location.href //production

async function send_key(key){
  let response = await fetch(ref + 'command', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                  "key" : key
                })
        })
  return response
}

export default Controls;
