#!/usr/bin/env python

from sara_web_comm.srv import *
import rospy
import os


def handle_launchScenario(req):

    rospy.logwarn("Launching scenario "+str(req)+"...")
    command = "roslaunch sara_launch scenario_" + str(req.scenario) + (".launch")
    os.system(command)


def launchScenario():
    rospy.init_node('launchScenarioServer')
    rospy.Service('launch_scenario', scenario_launch, handle_launchScenario)
    rospy.loginfo("Ready to launch scenario...")

    rospy.spin()

if __name__ == "__main__":
    launchScenario()
    
