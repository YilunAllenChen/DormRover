import React from 'react';
import clsx from 'clsx';
import { withStyles, makeStyles } from '@material-ui/core/styles';
import CssBaseline from '@material-ui/core/CssBaseline';
import Drawer from '@material-ui/core/Drawer';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import List from '@material-ui/core/List';
import Typography from '@material-ui/core/Typography';
import Divider from '@material-ui/core/Divider';
import IconButton from '@material-ui/core/IconButton';
import Badge from '@material-ui/core/Badge';
import MenuIcon from '@material-ui/icons/Menu';
import ChevronLeftIcon from '@material-ui/icons/ChevronLeft';
import NotificationsIcon from '@material-ui/icons/Notifications';
import MainListItems from './listItems';
import Main_View from './Main_View'

//keyboard event  reference: https://usehooks.com/useKeyPress/

const drawerWidth = 240;

const classes = theme => ({
  root: {
    display: 'flex',
  },
  toolbar: {
    paddingRight: 24, // keep right padding when drawer closed
  },
  toolbarIcon: {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'flex-end',
    padding: '0 8px',
    ...theme.mixins.toolbar,
  },
  appBar: {
    zIndex: theme.zIndex.drawer + 1,
    transition: theme.transitions.create(['width', 'margin'], {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.leavingScreen,
    }),
  },
  appBarShift: {
    marginLeft: drawerWidth,
    width: `calc(100% - ${drawerWidth}px)`,
    transition: theme.transitions.create(['width', 'margin'], {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.enteringScreen,
    }),
  },
  menuButton: {
    marginRight: 36,
  },
  menuButtonHidden: {
    display: 'none',
  },
  title: {
    flexGrow: 1,
  },
  drawerPaper: {
    position: 'relative',
    whiteSpace: 'nowrap',
    width: drawerWidth,
    transition: theme.transitions.create('width', {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.enteringScreen,
    }),
  },
  drawerPaperClose: {
    overflowX: 'hidden',
    transition: theme.transitions.create('width', {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.leavingScreen,
    }),
    width: theme.spacing(7),
    [theme.breakpoints.up('sm')]: {
      width: theme.spacing(9),
    },
  },
  appBarSpacer: theme.mixins.toolbar,
});




class Dashboard extends React.Component {
  
  constructor() {
    super();
    const fixedHeightPaper = clsx(classes.paper, classes.fixedHeight);
  }

  state = {
    "open": true,
    "option": "Control_Panel"
  }
  
  handleDrawerOpen = () => {
    this.setState({"open":true});
  };

  handleDrawerClose = () => {
    this.setState({"open":false});
  };
  

  _handleKeyDown = (event) => {
      switch( event.keyCode ) {
          case ESCAPE_KEY:
              this.state.activePopover.hide();
              break;
          default: 
              break;
      }
  };

  render() {
    console.log(this.state.option);
    const {classes} = this.props;
    return (
      <div className={classes.root}>
        <CssBaseline />
        <AppBar position="absolute" className={clsx(classes.appBar, this.state.open && classes.appBarShift)}>
          <Toolbar className={classes.toolbar}>
            <IconButton
              edge="start"
              color="inherit"
              aria-label="open drawer"
              onClick={this.handleDrawerOpen}
              className={clsx(classes.menuButton, this.state.open && classes.menuButtonHidden)}
            >
              <MenuIcon />
            </IconButton>
            <Typography component="h1" variant="h6" color="inherit" noWrap className={classes.title}>
              Dashboard
          </Typography>
            <IconButton color="inherit">
              <Badge badgeContent={4} color="secondary">
                <NotificationsIcon />
              </Badge>
            </IconButton>
          </Toolbar>
        </AppBar>
        <Drawer
          variant="permanent"
          classes={{
            paper: clsx(classes.drawerPaper, !this.state.open && classes.drawerPaperClose),
          }}
          open={this.state.open}
        >
          <div className={classes.toolbarIcon}>
            <IconButton onClick={this.handleDrawerClose}>
              <ChevronLeftIcon />
            </IconButton>
          </div>
          <Divider />
          <List>
            <MainListItems onOptionChange={({ newOption }) => { this.setState({ option: newOption }) }} />
          </List>
        </Drawer>
        <main className={classes.content}>
          <div className={classes.appBarSpacer} />
          <Main_View option={this.state.option}/>
        </main>
      </div>
    );
  }
}


let keys = {
  KeyW: false,
  KeyA: false,
  KeyS: false,
  KeyD: false
}

document.addEventListener('keydown', pressKey);
document.addEventListener('keyup', releaseKey);


function pressKey(e) {
   if(['KeyW', 'KeyA', 'KeyS', 'KeyD'].includes(e.code)) {
     keys[e.code] = true;
   }
   updateMotionControl();
}

function releaseKey(e) {
  if(['KeyW', 'KeyA', 'KeyS', 'KeyD'].includes(e.code)) {
    keys[e.code] = false;
  } 
  updateMotionControl();
}


async function send_key(key){
  //let ref = window.location.href //production
  let ref = "http://localhost:5000/"; //debug
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

function updateMotionControl(){
  console.log(keys);
  if(keys.KeyW && !keys.KeyS) send_key('w');
  if(keys.KeyS && !keys.KeyW) send_key('s');
  if(keys.KeyA && !keys.KeyD) send_key('a');
  if(keys.KeyD && !keys.KeyA) send_key('d');
}



export default withStyles(classes)(Dashboard)
