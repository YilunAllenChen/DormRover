import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import Title from './Title';



const useStyles = makeStyles({
  depositContext: {
    flex: 1,
  },
});

export default function Tipss() {
  const classes = useStyles();
  return (
    <React.Fragment>
      <Title>TIPS</Title>
      <Typography>W, A, S, D: Move the robot</Typography>
      <Typography>More functionality WIP</Typography>
    </React.Fragment>
  );

}