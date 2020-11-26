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
import ArrowUpwardIcon from '@material-ui/icons/ArrowUpward';
import ArrowDownwardIcon from '@material-ui/icons/ArrowDownward';
import ArrowForwardIcon from '@material-ui/icons/ArrowForward';
import ArrowBackIcon from '@material-ui/icons/ArrowBack';

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
      style={{'margin':'auto'}}
    >
      <CardContent>
        <Grid
          container
          justify="space-between"
          spacing={3}
        >
          <Grid style={{'margin':'auto'}} item>
            <Typography
              color="textSecondary"
              gutterBottom
              variant="h6"
              style={{'textAlign':'center'}}
            >
              Rover Control
            </Typography>
            
              <Grid style={{ 'height': 60 }} />
            <React.Fragment>
              <Grid style={{ padding: 30 }}>
                <Button size='large'  onClick={() => send_key('w')}>
                  <ArrowUpwardIcon />
                </Button>
              </Grid>
              <Grid style={{ 'margin': 'auto' }}>
                <Button size='large'  onClick={() => send_key('a')}>
                  <ArrowBackIcon />
                </Button>              


                <Button size='large'  onClick={() => send_key('d')}>
                  <ArrowForwardIcon />
                </Button>
              </Grid>
              <Grid style={{ padding: 30 }}>
                <Button size='large'  onClick={() => send_key('s')}>
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

export default Controls;
