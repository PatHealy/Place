# Place

VML/Place allows all users of the VML to leave their digital mark on the lab through playful interaction over the web!

[VML/Place](http://pathealy.pythonanywhere.com) has a mutable array of pixels that can be edited one at a time.

## Raspberry Pi
The brain of the displays is the Raspberry Pi.  It controls all of the arduino-controlled displays through addressed I2C communication.

The Pi contains this repository under `~/Desktop/VML-Place/Pi`.  To run the system, you'll need to either boot with the display or VNC/SSH into the Pi to start `PanelMaster.py`.

### Panel Master
The Panel Master uses a combination of `HTTP`, `SMBus`, and the custom `Panel` libraries to handle the web and I2C interaction.

Panels are entered into a 2D list which _should_ match the configuration on the website. The behavior is unexpected when there is a panel entered where there is no expected panel from the website.

## Arduino
Each panel is driven by an Arduino Uno or Arduino Mega with the [RGBMatrixPanel](https://github.com/adafruit/RGB-matrix-Panel) library from Adafruit.

Each Arduino must have a unique I2C address assigned to it on `line 22` of [MatrixPanel.ino](Arduino/MatrixPanel/MatrixPanel.ino).  Addresses must lie within the range of 0x04 and 0x7F and must be unique between panels. 

New panels can be made using the guide over at [Adafruit](https://learn.adafruit.com/32x16-32x32-rgb-led-matrix/overview).