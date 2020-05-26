

![Tilt_Camera_Xojo Logo](/Tilt_Camera_Xojo.png)

# Tilt_Camera_Xojo

Cell Eleven is implementing an 8MP camera with a 180° tilt feature.  This is a test application that takes a picture using a python script and sets the tilt of the G90 servo.

![Tilt_Camera_Xojo ScreenShot](/Tilt_Camera_Xojo_screenShot.png)


## Support Websites
[XOJO](https://www.xojo.com/) is a cross-platform IDE (Integrated development environment).  It is used to rapidly build applications for Desktop, Web, Mobile & Raspberry Pi.

[WiringPi](http://wiringpi.com/download-and-install/) is a Raspberry Pi package that allows XOJO to communicate with the GPIO pins.

## Getting started
 1. Download [XOJO](https://www.xojo.com/)
 2. Notes on  [WiringPi](http://wiringpi.com/download-and-install/)
 3. [Setup XOJO Debug for the raspberry Pi](https://docs.xojo.com/UserGuide:Getting_Started_with_Raspberry_Pi)
 4. Download this Zip
 5. Open ```Tilt_Camera_Xojo.xojo_binary_project``` with XOJO
 6. Run Remotley on Raspberry Pi <kbd>Alt</kbd>+<kbd>Command</kbd>+<kbd>R</kbd>
 7.  **RUN**
 
 **NOTES:** Raspberry Pi needs  ```>>>sudo apt-get install wiringpi```

## User Manual
1. Run  ```Tilt_Camera_Xojo.xojo_binary_project``` remotely on the raspberry pi
2. Download  ```TakePicture.py``` to the Raspberry Pi
3. *Shell Path* Field is the location of the  ```TakePicture.py```  file.  <br>**EXAMPLE**  ```/home/pi/Desktop/TakePicture.py``` 
4. *Save Path* Field is the location you want the pictures saved.  <br>**EXAMPLE** ```/home/pi/Desktop/``` 
5. *Tilt* RadioButton moves the servo; <br>Forward = 0 °<br>Down = 90°<br> Back = 180°
6. *Take Picture* button, executes the servo, takes a picture using the python script, save the image to the path, and updates the image list.
7. Clicking on an item on the *Images* list will scale and display the selected image.

## Authors

* **[S James Parsons Jr](https://www.linkedin.com/in/sjamesparsonsjr/)** 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Donations
Please consider donating to the future of Cell Eleven
[paypal.me/sjamesparsonsjr](https://www.paypal.com/paypalme/my/profile)


[![Donation](https://www.thenewatlantis.com/imgLib/20200417_paypal.jpg)](https://www.paypal.com/paypalme/my/profile)
