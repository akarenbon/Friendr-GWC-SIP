
#include <Servo.h>                           // Include servo library

Servo servoLeft;                             // Declare left servo signal
Servo servoRight;                            // Declare right servo signal

void setup()
{
  pinMode(PIEZOPIN, OUTPUT);                 // Attach piezo to pin 5. 
  servoLeft.attach(13);                      // Attach left signal to pin 13
  servoRight.attach(12);                     // Attach right signal to pin 12
  servoLeft.writeMicroseconds(1500);        // Calibrate left servo
  servoRight.writeMicroseconds(1500);       // Calibrate right servo
  // Attach LED pins here.
}  

void right()
{
  servoLeft.writeMicroseconds(1000);
  servoRight.writeMicroseconds(0);
  delay(2000);
}

void left()
{
  servoLeft.writeMicroseconds(0);        
  servoRight.writeMicroseconds(1300);
  delay(2000);
}

void back()
{
  servoLeft.writeMicroseconds(2000);        
  servoRight.writeMicroseconds(1000);
  delay(2000);
}
void forward()
{
  servoLeft.writeMicroseconds(1000);        
  servoRight.writeMicroseconds(2000);
  delay(2000);
}
void loop()
{
  right();
  left();
  back();
  forward();
  right();
  back();
  right();
  back();
}
