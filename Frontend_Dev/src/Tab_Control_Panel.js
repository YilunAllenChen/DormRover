import React from 'react';
import clsx from 'clsx';
import Container from '@material-ui/core/Container';
import Grid from '@material-ui/core/Grid';
import Paper from '@material-ui/core/Paper';
import Tips from './Tips';
import Databoard from './Databoard';
import { makeStyles, withStyles } from '@material-ui/core/styles';



const classes = (theme) => ({
  root: {
    display: 'flex',
  },
  appBarSpacer: theme.mixins.toolbar,
  content: {
    flexGrow: 1,
    height: '100vh',
    overflow: 'auto',
  },
  container: {
    paddingTop: theme.spacing(4),
    paddingBottom: theme.spacing(4),
  },
  paper: {
    padding: 20,
    display: 'flex',
    overflow: 'auto',
    flexDirection: 'column',
  },
  fixedHeight: {
    height: 240,
  },
});

const fixedHeightPaper = clsx(classes.paper, classes.fixedHeight);

class Control_Panel extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    const {classes} = this.props;
    console.log(classes);
    return (
      <Container mawidth="lg" className={classes.container}>
        <Grid container spacing={3}>
          {/* Chart */}
          <Grid item xs={12} md={8} lg={9}>
            <Paper style={{"display": "flex", "padding": 20, "overflow": "auto", "flexDirection": "column"}}>
              <img src="http://localhost:5000/video_feed" alt="video_feed" width={600}></img>
            </Paper>
          </Grid>
          {/* Recent Tips */}
          <Grid item xs={12} md={4} lg={3}>
            <Paper style={{"display": "flex", "padding": 20, "overflow": "auto", "flexDirection": "column"}}>
              <Tips />
            </Paper>
          </Grid>
          {/* Recent Orders */}
          <Grid item xs={12}>
            <Paper style={{"padding":20}} className={classes.paper}>
              <Databoard />
            </Paper>
          </Grid>
        </Grid>
      </Container>
    );
  }
}

export default withStyles(classes)(Control_Panel)
