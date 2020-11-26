import React from 'react';
import Card from '@material-ui/core/Card';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardContent from '@material-ui/core/CardContent';

import Link from '@material-ui/core/Link'

import Typography from '@material-ui/core/Typography';
import { withStyles } from '@material-ui/core/styles';
import { Grid } from '@material-ui/core';



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

class Team extends React.Component {

  /*constructor(props) {
    super(props);
  }*/

  render() {
    const { classes } = this.props;
    console.log(classes);

    let team_members = [
      {
        name: "Allen Chen",
        desc: "4th year computer engineering student with a deep passion for robotics. Upcoming SWE @ DRW. Ex-intern @ Uber Advanced Technology Group and Volkswagen AG. Undergraduate research assistant at Georgia Tech Robotarium and LIDAR lab. ",
        contact: {
          "LinkedIn": "https://www.linkedin.com/in/yilun-allen-chen-572b71141/"
        }
      },
      {
        name: "Yida Wang",
        desc: "I am Han Pi!!!", 
        contact: {
          "LinkedIn": "https://www.linkedin.com/in/yida-wang-10221097/"
        }
      }, {
        name: "Xi Li",
        desc: "I am Xi Li, 3rd year electrical engineering Bachelor in Georgia Tech. Academic focus are analog circuits analysis and design, embedded system design, and control system design. Having experience to build and assemble an op amp with 1.7 percent error from designed feedback loop gain.", 
        contact: {
          "LinkedIn": "https://www.linkedin.com/in/xi-li-b98422194/"
        }
      }, {
        name: "Zhenjie Chu",
        desc: "MS ECE student with four years of experience working as Lead Electrical Engineer in the automotive supply manafacturing industry. Led and managed a multi-discipline engineer team to design and build automation solutions such as ABB robotic system to meet critical automotive production requirements. Currently shifting focus more towards software and embedded systems.", 
        contact: {
          "LinkedIn": "https://www.linkedin.com/in/zhenjie-chu-1139a882/"
        }
      },
    ]

    let members = [];
    for (let ndx in team_members) {
      members.push(
        <Grid item xs={12} md={6} lg={3}>
          <Card style={{ "display": "flex", "padding": 20, "overflow": "auto", "flexDirection": "column", "height": 400 }}>
            <CardActionArea>
              <CardContent>
                <Typography gutterBottom variant="h5" component="h2">
                  {team_members[ndx].name}
                </Typography>
                <Typography variant="body2" color="textSecondary" component="p">
                  {team_members[ndx].desc}
                </Typography>


                <Typography style={{"padding-top": 20, "padding-bottom": 10}}>Contact</Typography>
                <Link href={team_members[ndx].contact.LinkedIn}>
                  LinkedIn
                  </Link>
              </CardContent>
            </CardActionArea>
          </Card>
        </Grid>
      )
    }

    return (
      <Grid container style={{ "flexGrow": 1 }} direction="row" justify="center" alignItems="center">
        <div className={classes.appBarSpacer}></div>
        {members}
      </Grid>
    );
  }
}

export default withStyles(classes)(Team)
