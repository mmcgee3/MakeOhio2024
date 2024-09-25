/* Sweep
 by BARRAGAN <http://barraganstudio.com>
 This example code is in the public domain.

 modified 8 Nov 2013
 by Scott Fitzgerald
 https://www.arduino.cc/en/Tutorial/LibraryExamples/Sweep
*/

#include <Servo.h>

Servo servo;  // create servo object to control a servo
// twelve servo objects can be created on most boards
String incomingString = "";
int pos = 90;    // variable to store the servo position

void setup() {
  servo.attach(9);  // attaches the servo on pin 9 to the servo object
  Serial.begin(115200);
  Serial.setTimeout(100);
}

void loop() {
  if (Serial.available()>0) {
      // read the incoming byte:
      incomingString = Serial.readString();
      Serial.println(incomingString);
      if(incomingString == "left") {
        for(int i = 0; i<5; i++){
          servo.write(pos-1);
          pos--;
          delay(25);
        }
        //servo.write(pos-5);
        //pos = pos-5;
      } else if (incomingString == "right") {
        for(int i = 0; i<5; i++){
          servo.write(pos+1);
          pos++;
          delay(25);
        }
        //servo.write(pos+5);
        //pos = pos+5;
      }
  }
}
