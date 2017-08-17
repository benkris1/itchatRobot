#!/bin/bash
WORKING_DIR=/opt/itchatRobot
docker run -P --name itchatRobot --net="host" -it -v $WORKING_DIR/logs:/opt/itchatRobot/logs  -v $WORKING_DIR/tmp:/opt/itchatRobot/tmp -d itchat_robot:0.1