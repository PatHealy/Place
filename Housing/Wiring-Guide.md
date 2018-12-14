#VML/Place Panel Wiring Guide

##Materials

- [Adafruit 32x32 LED Panel](https://www.adafruit.com/product/1484)
- [Arduino Uno](https://store.arduino.cc/usa/arduino-uno-rev3)
- [Raspberry Pi](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/)
- Jumper Wires

##Instructions

###Internal Wiring

Instructions for wiring the Adafruit panel inputs to the onboard Arduino Uno can be found [here](https://learn.adafruit.com/32x16-32x32-rgb-led-matrix/connecting-with-jumper-wires). Instructions for powering the panel can be found [here](https://learn.adafruit.com/32x16-32x32-rgb-led-matrix/powering).

As specified in these instructions, there are three ground ports on the panel. In order to reserve ground connections on the Arduino for later use, join these three connections and wire them to a single `GND` pin. Once the data connections have been made, split the power input to the panel and attach it with a jumper cable to the `5V` pin on the Arduino. Similarly, split the ground to the panel and attach to one of the two remaining `GND` pins on the Arduino.

###External Wiring

At this point, all necessary connections between the onboard Arduino and the LED panel have been made, so to check them power the devices and follow the directions [here](https://learn.adafruit.com/32x16-32x32-rgb-led-matrix/test-example-code) to perform some tests.

The only remaining step to take before casing the panel and Arduino is to set the wires for communication with the master controller. In this project, that is a Raspberry Pi and we will be using I2C communications protocols. To complete onboard wiring, attach jumpers to the `SDA`, `SCL`, and final remaining `GND` pins on the Arduino. These wires should be long enough to reach outside the panel if necessary, in order to form a common set of connections with all active panels and the master controller.

###Housing the Setup

Housing designs for the display and its onboard Arduino can be found [here](https://github.com/Vibrant-Media-Lab/Place/tree/master/Housing). The files are in a .stl format, and printing took us approximately 5.5 hours. We suggest using PLA as a material, but other print plastics will work as well. Once the components are completed. remove the support from the openings in them, and line up the inner and outer sections by those openings. You may need to tamp down wires to the back of the panel, but it should fit cleanly above the inner housing. Slide the outer housing down over the entire setup, ensuring the common `SDA`, `SCL`, and `GND` connections reach outside it. Using electrical tape or hot glue, connect the two pieces of housing at the back, and the project is complete!