#include <Servo.h>

// Motor - ESC Control Pins
const int esc_left = 9;
const int esc_right = 10;

// Potentiometer - Analog Read Pins
const int potentiometer_left = A0;
const int potentiometer_right = A1;

// Min & Max Speed
const int min_speed = 0;
const int max_speed = 20;

// ESC - Motor Controller Class Objects
Servo ESC1;
Servo ESC2;

void setup() {
  ESC1.attach(esc_left,1000,2000);
  ESC2.attach(esc_right,1000,2000);
  Serial.begin(9600);
}

void loop() {
  // Define Potentiometer Read variables
  int read_right;
  int read_left;

  // Reading Potentiometer Values
  read_right = analogRead(potentiometer_right);
  read_left = analogRead(potentiometer_left);
    
  // Mapping Read Values to ESC Compatible Inputs
  read_right = map(read_right, 0, 1023, min_speed, max_speed);
  read_left = map(read_left, 0, 1023, min_speed, max_speed);  

  // Printing Values for Verification
  Serial.print(read_left);delay(7000);
  Serial.print(" ");
  Serial.println(read_right);
  
  // Sending ESC Command (from min_speed to max_speed) to control Motor Speed
  if (read_right >= min_speed && read_right <= max_speed){
    ESC1.write(read_right);
  }
  if (read_left >= min_speed && read_left <= max_speed){
    ESC2.write(read_left);
  }
}
