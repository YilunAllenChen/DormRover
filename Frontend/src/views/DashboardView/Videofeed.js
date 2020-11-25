import React from 'react';
import clsx from 'clsx';
import PropTypes from 'prop-types';
//import { Bar } from 'react-chartjs-2';
import {
  Box,
  Button,
  Card,
  CardContent,
  CardHeader,
  Divider,
  //useTheme,
  makeStyles
} from '@material-ui/core';
import ArrowDropDownIcon from '@material-ui/icons/ArrowDropDown';
//import ArrowRightIcon from '@material-ui/icons/ArrowRight';

const useStyles = makeStyles(() => ({
  root: {}
}));

const Video_feed = ({ className, ...rest }) => {
  const classes = useStyles();
  //const theme = useTheme();  

  return (
    <Card
      className={clsx(classes.root, className)}
      {...rest}
    >
      <CardHeader
        action={(
          <Button
            endIcon={<ArrowDropDownIcon />}
            size="small"
            variant="text"
          >
            Front
          </Button>
        )}
        title="Live View"
      />
      <Divider />
      <CardContent>
        <Box
          height={400}
          position="relative"
        >        
        <img src="video_feed" alt="video_feed" width={600}></img>   
        </Box>
      </CardContent>
      <Divider />      
    </Card>
  );
};

Video_feed.propTypes = {
  className: PropTypes.string
};

export default Video_feed;
