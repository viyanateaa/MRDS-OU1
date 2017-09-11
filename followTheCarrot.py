"""
MRDS Assigment 1 
Emelie Andersson
Viyan Ateaa

"""

import httplib, json, time 
from math import sin,cos,pi,atan2
from givenCode import *
from Path.py import *


"""
Method diff_points
Calcs the difference between points
"""

"""
Method diff_angels
Calcs the the difference between angles
"""


def main():
    try:
        pose = getPose()
        print('Current position: ', pose['Pose']['Position'])
        for t in range(30):    
            print('Current heading vector: X:{X:.3}, Y:{Y:.3}'.format(**getHeading()))
            laser = getLaser()
            print('Distance %.3f meters.'%(laser['Echoes'][135]))
            if (laser['Echoes'][135] < 0.3):
                print('Danger! Brace for impact! Hit the brakes!')
                response = postSpeed(0,-0.1)
            time.sleep(1)
        except UnexpectedResponse as ex:
            print('Unexpected response from server when reading position:', ex)
    

