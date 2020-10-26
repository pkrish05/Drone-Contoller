# **Drone-Contoller**

## **TODO LIST**
- [x] **Manual Controller :hammer_and_wrench:**
- [ ] **PID Controller :robot:**
- - [ ] Read GyroScope Values and Convert them into Roll, Pitch & Yaw angles
- - [ ] Make a PID Control-Loop Model - Scipy
- - [ ] Implement the PID Model to the PID Controller
- - [ ] ...

## ***Manual Controller :hammer_and_wrench:***
### **How Does it Work ?**
To manually control the speed of the motors we need and input method (Buttons, Switches, Potentiometer, etc). 
Here the most suitable way of controlling the motor speed is the Potentiometer as we can reach analog values between 0-1023.
Now that we have a way to reach values in a range of 1024 values we can use them to build a manual controller.

1. Read Analog Values on the Potentiometer (0-1023)
2. Convert them values to the ESC Controller input Range (0-180) (In our case we are using Arduino Servo.h library thus the range of 0-180)
3. Write those Values (0-180) to the input of the ESC Controller
4. Using the visual abilities of the human eyes we can try to control the Drone to make it Stable.

PS. Before Doing the Manual controller we need to make sure the ESCs are Calibrated before their usage.

## ***PID Controller :robot: using Gyroscope for error measurement***
### **How Does it Work ?**

1. ...
2. ...

PS. For Automation Purpose we need to implement a Program to make sure the ESCs are Calibrated before their usage.

## Drone Parts
### ESC Controllers :
### Brushless Motors :
### Gyroscopic Sensor :
### LiPo Battery :
### ...
