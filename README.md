# RPi-Shutdown-Bttn

 git clone https://github.com/ericw357/RPI-Shutdown-Bttn.git 

The Raspberry Pi needs a script that tells it to shutdown if it gets the shutdown signal. So the next thing we' ll do is write a Python script that waits for this signal on a specified GPIO pin. Here we' ll watch out for GPIO pin 7. On the model B this is GPIO4. Save this short script in something like /home/pi/pishutdown/pishutdown.py.

Next we need a shell script that starts our Python script with root access. Put the shell script in the same directory as our Python script. 

pishutdown.sh

Add a logging directory by typing:
mkdir /home/pi/pishutdown/logs

Use crontab to autostart the script. Open the crontab editor by typing sudo crontab -e in the Console. Append the following line:
@reboot sh /home/pi/pishutdown/pishutdown.sh >/home/pi/pishutdown/logs/cronlog 2>&1

Reboot...
