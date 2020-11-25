import React from 'react';
import Box from '@material-ui/core/Box';
import Container from '@material-ui/core/Container';
import Control_Panel from './Tab_Control_Panel'
import Team from './Tab_Team'


import Typography from '@material-ui/core/Typography';
import Link from '@material-ui/core/Link';

function Copyright() {
  return (
    <Typography variant="body2" color="textSecondary" align="center">
      {'Copyright © '}
      <Link color="inherit" href="https://material-ui.com/">
        DORO
      </Link>{' '}
      {new Date().getFullYear()}
      {'.'}
    </Typography>
  );
}


export default class Main_View extends React.Component {

  state = {
  }

  constructor(props) {
    super(props);
  };



  render() {
    let rendered_view;
    switch (this.props.option) {
      case "Control_Panel":
        rendered_view = <Control_Panel />;
        break;
      case "Team":
        rendered_view = <Team />;
        break;
    }
    return (
      <Container maxWidth="lg" >
        {rendered_view}
        <Box pt={4}>
          <Copyright />
        </Box>
      </Container>
    );
  }
}