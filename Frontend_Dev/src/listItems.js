import React from 'react';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import ListSubheader from '@material-ui/core/ListSubheader';
import DashboardIcon from '@material-ui/icons/Dashboard';
import ShoppingCartIcon from '@material-ui/icons/ShoppingCart';
import PeopleIcon from '@material-ui/icons/People';
import BarChartIcon from '@material-ui/icons/BarChart';
import LayersIcon from '@material-ui/icons/Layers';
import AssignmentIcon from '@material-ui/icons/Assignment';

export default class MainListItems extends React.Component {
  constructor(props) {
    super(props);
  }

  state = {
    'activeItem': "Dashboard"
  }

  handleItemClick = (name) => {
    this.setState({ activeItem: name });
    this.props.onOptionChange({ newOption: name });
  };


  render() {
    return (
    <div>
      <ListItem button onClick={() => this.handleItemClick("Control_Panel")}>
        <ListItemIcon>
          <DashboardIcon />
        </ListItemIcon>
        <ListItemText primary="Dashboard" />
      </ListItem>
      <ListItem button onClick={() => this.handleItemClick("Team")}>
        <ListItemIcon>
          <PeopleIcon />
        </ListItemIcon>
        <ListItemText primary="Team" />
      </ListItem>
      <ListItem button onClick={() => this.handleItemClick("Status")}>
        <ListItemIcon>
          <BarChartIcon />
        </ListItemIcon>
        <ListItemText primary="Status" />
      </ListItem>
      <ListItem button onClick={() => this.handleItemClick("Notes")}>
        <ListItemIcon>
          <LayersIcon />
        </ListItemIcon>
        <ListItemText primary="Notes" />
      </ListItem>
    </div>
    );
  }
}

export function secondaryListItems(){return <div />;}