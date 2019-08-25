'''
Created on Aug 19, 2019

@author: itap_testbench_02
'''
       
       
tolerance =abs( float('141.921') - float('252.423'))
if tolerance <= 0.900:
    print("ok")
    #step.addEvalResult(LOOK_UP_ANGLE.get(setspeed, "0"), angle , "angle observed from camera read cluster correctly", "Passed")
else:
    print("wrong")
    #step.addEvalResult(LOOK_UP_ANGLE.get(setspeed, "0"), angle , "angle observed from camera read cluster incorrectly", "Failed")