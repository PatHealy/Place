#include <RGBmatrixPanel.h>
#include <Wire.h>

//#define CLK  8   // USE THIS ON ARDUINO UNO, ADAFRUIT METRO M0, etc.
//#define CLK A4 // USE THIS ON METRO M4 (not M0)
#define CLK 11 // USE THIS ON ARDUINO MEGA
#define OE   9
#define LAT 10
#define A   A0
#define B   A1
#define C   A2
#define D   A3

RGBmatrixPanel matrix(A, B, C, D, CLK, LAT, OE, false);

// int[c][x][y]
// c - color plane (r, g, b)
// x - x coordinate
// y - y coordinate
char matrix_data[3][32][32];

#define ADDR 0x04

void clearMatrix();
void setPixel(byte x, byte y, byte r, byte g, byte b);

void setup() {

  Wire.begin(ADDR);
  Wire.onReceive(receiveEvent);

  matrix.begin();

  // do some bootup display
  matrix.fillRect(0, 0, 32, 32, matrix.Color333(0, 0, 0));
  delay(1000);
  matrix.fillRect(0, 0, 32, 32, matrix.Color333(1, 0, 0));
  delay(1000);
  matrix.fillRect(0, 0, 32, 32, matrix.Color333(0, 1, 0));
  delay(1000);
  matrix.fillRect(0, 0, 32, 32, matrix.Color333(0, 0, 1));
  delay(1000);
  clearMatrix();
  delay(1000);
}

void loop() {
  
}

void clearMatrix(){
  for(int c = 0; c < 3; c++){
    for(int x = 0; x < 32; x++){
      for(int y = 0; y < 32; y++){
        setPixel((char)x, (char)y, (char)0, (char)0, (char)0);
      }
    }
  }
}

void setPixel(char x, char y, char r, char g, char b){
  matrix.drawPixel(x, y, matrix.Color888(matrix_data[0][x][y] = r, matrix_data[1][x][y] = g, matrix_data[2][x][y] = b));
  //matrix.drawPixel(x, y, matrix.Color333(r, g, b));
}

// byte 0 - set pixel (AF)
void receiveEvent(int howMany){
  Wire.read();
  if(!Wire.available()){
    return;
  }
  char type = Wire.read();

  if((byte)type == (byte)0xaf){ // draw pixel
    // byte 1 - x coordinate
    // byte 2 - y coordinate
    // byte 3 - r color
    // byte 4 - g color
    // byte 5 - b color
    char data[5];
    int i=0;
    
    while(Wire.available()){
      data[i] = (char)Wire.read();
      i++;
    }
    
    matrix.drawPixel(data[0], data[1], matrix.Color444(data[2], data[3], data[4]));
  } else if((byte)type == (byte)0xad){ // fill rect
    // byte 1 - x start coordinate
    // byte 2 - y start coordinate
    // byte 3 - x end coordinate
    // byte 4 - y end coordinate
    // byte 5 - r color
    // byte 6 - g color
    // byte 7 - b color
    char data[7];
    int i=0;
    
    while(Wire.available()){
      data[i] = (char)Wire.read();
      i++;
    }
    
    matrix.fillRect(data[0], data[1], data[2], data[3], matrix.Color444(data[4], data[5], data[6]));
  }

  while(Wire.available()){
    Wire.read();
  }
}
