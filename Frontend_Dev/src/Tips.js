import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import Title from './Title';


import ArrowUpwardIcon from '@material-ui/icons/ArrowUpward';
import ArrowDownwardIcon from '@material-ui/icons/ArrowDownward';
import ArrowForwardIcon from '@material-ui/icons/ArrowForward';
import ArrowBackIcon from '@material-ui/icons/ArrowBack';
import { Button, Grid } from '@material-ui/core';


const useStyles = makeStyles({
  depositContext: {
    flex: 1,
  },
});

export default function Tipss() {
  const classes = useStyles();
  return (
    <React.Fragment>
      <Title>Motion Control</Title>
      <Grid style={{'margin': 'auto'}}>
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
      <Grid style={{'margin': 'auto'}}>
        <Button onClick={() => send_key('s')}>
          <ArrowDownwardIcon />
        </Button>
      </Grid>
    </React.Fragment>
  );

}

let ref = 'http://localhost:5000/' // debug
// let ref = window.location.href //production




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