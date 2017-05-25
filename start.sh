#!/bin/bash
WORKING_DIR=/opt/itchatRobot
docker run --name itchatRobot --net="host" -v $WORKING_DIR/logs:/opt/itchatRobot/logs  $WORKING_DIR/tmp:/opt/itchatRobot/tmp itchat_robot:0.1 1>robot_out.log
