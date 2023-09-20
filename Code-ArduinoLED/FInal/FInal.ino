#include <FastLED.h>

#define NUM_LEDS  32
#define LED_PIN   D4

CRGB leds[NUM_LEDS];


#include <Wire.h>

#define echoPin D8               // CHANGE PIN NUMBER HERE IF YOU WANT TO USE A DIFFERENT PIN
#define trigPin D7               // CHANGE PIN NUMBER HERE IF YOU WANT TO USE A DIFFERENT PIN
long duration, distance;



void setup() {
  Serial.begin (9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  FastLED.addLeds<WS2812B, LED_PIN, GRB>(leds, NUM_LEDS);
  FastLED.setBrightness(50);
}

void loop() {
  Lights();
  Blink();
  Sonic();
}


void Lights() {

  if (distance >= 200) {

    leds[0] = CRGB::Red;
    leds[1] = CRGB::Red;
    leds[2] = CRGB::Red;
    leds[3] = CRGB::Red;
    leds[4] = CRGB::Red;
    leds[5] = CRGB::Red;
    leds[6] = CRGB::Red;
    leds[7] = CRGB::Red;
    leds[16] = CRGB::Red;
    leds[17] = CRGB::Red;
    leds[18] = CRGB::Red;
    leds[19] = CRGB::Red;
    leds[20] = CRGB::Red;
    leds[21] = CRGB::Red;
    leds[22] = CRGB::Red;
    leds[23] = CRGB::Red;
    
    FastLED.show();
    delay(1000);
    
    leds[0] = CRGB::Black;
    leds[1] = CRGB::Black;
    leds[2] = CRGB::Black;
    leds[3] = CRGB::Black;
    leds[4] = CRGB::Black;
    leds[5] = CRGB::Black;
    leds[6] = CRGB::Black;
    leds[7] = CRGB::Black;
    leds[16] = CRGB::Black;
    leds[17] = CRGB::Black;
    leds[18] = CRGB::Black;
    leds[19] = CRGB::Black;
    leds[20] = CRGB::Black;
    leds[21] = CRGB::Black;
    leds[22] = CRGB::Black;
    leds[23] = CRGB::Black;

    FastLED.show();
    delay(500);
    
    leds[0] = CRGB::Green;
    leds[1] = CRGB::Green;
    leds[2] = CRGB::Green;
    leds[3] = CRGB::Green;
    leds[4] = CRGB::Green;
    leds[5] = CRGB::Green;
    leds[6] = CRGB::Green;
    leds[7] = CRGB::Green;
    leds[16] = CRGB::Green;
    leds[17] = CRGB::Green;
    leds[18] = CRGB::Green;
    leds[19] = CRGB::Green;
    leds[20] = CRGB::Green;
    leds[21] = CRGB::Green;
    leds[22] = CRGB::Green;
    leds[23] = CRGB::Green;

    FastLED.show();
    delay(1000);
    
    leds[0] = CRGB::Black;
    leds[1] = CRGB::Black;
    leds[2] = CRGB::Black;
    leds[3] = CRGB::Black;
    leds[4] = CRGB::Black;
    leds[5] = CRGB::Black;
    leds[6] = CRGB::Black;
    leds[7] = CRGB::Black;
    leds[16] = CRGB::Black;
    leds[17] = CRGB::Black;
    leds[18] = CRGB::Black;
    leds[19] = CRGB::Black;
    leds[20] = CRGB::Black;
    leds[21] = CRGB::Black;
    leds[22] = CRGB::Black;
    leds[23] = CRGB::Black;

    FastLED.show();
    delay(500);
    
  }
  else if (distance <= 200) {
    leds[0] = CRGB::White;
    leds[1] = CRGB::White;
    leds[2] = CRGB::White;
    leds[3] = CRGB::White;
    leds[4] = CRGB::White;
    leds[5] = CRGB::White;
    leds[6] = CRGB::White;
    leds[7] = CRGB::White;
    leds[16] = CRGB::White;
    leds[17] = CRGB::White;
    leds[18] = CRGB::White;
    leds[19] = CRGB::White;
    leds[20] = CRGB::White;
    leds[21] = CRGB::White;
    leds[22] = CRGB::White;
    leds[23] = CRGB::White;

    FastLED.show();
    delay(1500);
    
    leds[0] = CRGB::Black;
    leds[1] = CRGB::Black;
    leds[2] = CRGB::Black;
    leds[3] = CRGB::Black;
    leds[4] = CRGB::Black;
    leds[5] = CRGB::Black;
    leds[6] = CRGB::Black;
    leds[7] = CRGB::Black;
    leds[16] = CRGB::Black;
    leds[17] = CRGB::Black;
    leds[18] = CRGB::Black;
    leds[19] = CRGB::Black;
    leds[20] = CRGB::Black;
    leds[21] = CRGB::Black;
    leds[22] = CRGB::Black;
    leds[23] = CRGB::Black;

    FastLED.show();
    delay(1000);
  }

}


void Blink(){
  leds[9] = CRGB::White;
  leds[10] = CRGB::White;
  leds[11] = CRGB::White;
  leds[12] = CRGB::White;
  leds[13] = CRGB::White;
  leds[14] = CRGB::White;
  leds[15] = CRGB::White;
  leds[24] = CRGB::White;
  leds[25] = CRGB::White;
  leds[26] = CRGB::White;
  leds[27] = CRGB::White;
  leds[28] = CRGB::White;
  leds[29] = CRGB::White;
  leds[30] = CRGB::White;
  leds[31] = CRGB::White;

  FastLED.show();
  delay(50);

  leds[8] = CRGB::Black;
  leds[9] = CRGB::Black;
  leds[10] = CRGB::Black;
  leds[11] = CRGB::Black;
  leds[12] = CRGB::Black;
  leds[13] = CRGB::Black;
  leds[14] = CRGB::Black;
  leds[15] = CRGB::Black;
  leds[24] = CRGB::Black;
  leds[25] = CRGB::Black;
  leds[26] = CRGB::Black;
  leds[27] = CRGB::Black;
  leds[28] = CRGB::Black;
  leds[29] = CRGB::Black;
  leds[30] = CRGB::Black;
  leds[31] = CRGB::Black;

  FastLED.show();
  delay(500);
}

void Sonic(){
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  duration = pulseIn(echoPin, HIGH);
  distance = duration / 58.2;
  String disp = String(distance);

  Serial.print("Distance: ");       // used for debugging
  Serial.print(disp);               // used for debugging
  Serial.println(" cm");            // used for debugging
  delay(1500);
}