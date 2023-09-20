#include <FastLED.h>

#define NUM_LEDS  32
#define LED_PIN   D4

CRGB leds[NUM_LEDS];

void setup() {
  FastLED.addLeds<WS2812B, LED_PIN, GRB>(leds, NUM_LEDS);
  FastLED.setBrightness(50);
}

int i = 1;

void loop() {
  Lights();
}

void Lights() {

  if (i <= 1) {

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
    delay(500);
    
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
    delay(500);
    
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
    
  }
  else if (i >= 2) {
    leds[0] = CRGB::White;
    leds[1] = CRGB::White;
    leds[2] = CRGB::White;
    leds[3] = CRGB::White;
    leds[4] = CRGB::White;
    leds[5] = CRGB::White;
    leds[6] = CRGB::White;
    leds[7] = CRGB::White;

    FastLED.show();
    delay(500);
    
    leds[0] = CRGB::White;
    leds[1] = CRGB::White;
    leds[2] = CRGB::White;
    leds[3] = CRGB::White;
    leds[4] = CRGB::White;
    leds[5] = CRGB::White;
    leds[6] = CRGB::White;
    leds[7] = CRGB::White;

    FastLED.show();
    delay(2000);
  }

  leds[8] = CRGB::White;
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
  
  leds[8] = CRGB::White;
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
  delay(2000);
}




    
 