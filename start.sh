#!bin/bash
WORKING_DIR=/opt/itchatRobot
docker run --name itchatRobot --net="host" -v $WORKING_DIR/logs:/opt/itchatRobot/logs -d itchatRobot:0.1
