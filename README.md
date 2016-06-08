# sara_web
Web interface for SARA. Aim to work on the BeagleBone Black screen, but can be use from any device.

##installation
On SARA computer :
sudo apt-get install ros-indigo-rosbridge-server
sudo apt-get install apache2-mpm-prefork
sudo nano /etc/apache2/sites-available/000-default.conf
-Change the following line : DocumentRoot /var/www/html for DocumentRoot /home/wm/sara_web/html
sudo nano /etc/apache2/apache2.conf
-Change the following line : <Directory /var/www/> for <Directory /home/wm/sara_web/>
sudo apache2ctl restart
 
On BeagleBone :
sudo apt-get install chromium-browser

##SARA computer launch 
sudo apache2ctl restart
roslaunch rosbridge_server rosbridge_websocket.launch

##BeagleBone launch
script file need to be chmod u+x </br>
setup the ip of the apache server</br>
launch the bash script, this will start chromium-browser in kiosk mode </br>

> ./web_startup.sh
