# RPi-Shutdown-Bttn

 The Raspberry Pi needs a script that tells it to shutdown if it gets the shutdown signal. This is a Python script that waits for this signal on a specified GPIO pin. We'll watch out for GPIO pin 7. On the model B this is GPIO4. 
 
 clone this git into the /home/pi/ directory
 git clone https://github.com/ericw357/pishutdown.git 

A shell script that starts our Python script with root access.
pishutdown.sh

The logging directory:
/home/pi/pishutdown/logs

Use crontab to autostart the script. Open the crontab editor by typing sudo crontab -e in the Console. Append the following line:
@reboot sh /home/pi/pishutdown/pishutdown.sh >/home/pi/pishutdown/logs/cronlog 2>&1

Reboot...
