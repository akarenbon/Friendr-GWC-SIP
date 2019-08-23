//moving
#include <Servo.h>                           // Include servo library

Servo servoLeft;                             // Declare left servo signal
Servo servoRight;  // Declare right servo signal
void setup(){
  servoLeft.attach(13);                      // Attach left signal to pin 13
  servoRight.attach(12);                     // Attach right signal to pin 12
  servoLeft.writeMicroseconds(1500);        // Calibrate left servo
  servoRight.writeMicroseconds(1500);       // Calibrate right servo
}

void forward(){
  servoLeft.writeMicroseconds(1000);        
  servoRight.writeMicroseconds(2000);
  delay(2000);
}

//whisker code sends message to console when pressed
int lftwh = 5;
int rhtwh = 7;
void set() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  //first part of printing to console
  pinMode(lftwh, INPUT);
  pinMode(rhtwh, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int lftwhValue = digitalRead(lftwh);
  int rhtwhValue = digitalRead(rhtwh);
  //receives input from digread + sets to variable
  //print info
  //make sophisticated

  if(lftwhValue == 0 && rhtwhValue ==0){
    Serial.println("Left and Right are being pressed");
    delay(300);
  }
  else if(lftwhValue == 0){
    Serial.println("Left is being pressed");
    delay(300);
  }
  else if(rhtwhValue == 0){
    Serial.println("Right is being pressed");
    delay(300);
  }
  else{
    Serial.println("You're good");
    delay(3000);
  }
}
setup()
