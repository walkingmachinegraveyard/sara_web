# sara_web
Web interface for SARA. Aim to work on the BeagleBone Black screen, but can be use from any device.

##installation
On SARA computer :</br>
git clone https://github.com/WalkingMachine/sara_web.git </br>
sudo apt-get install ros-indigo-rosbridge-server</br>
sudo apt-get install apache2-mpm-prefork</br>
sudo nano /etc/apache2/sites-available/000-default.conf</br>
-Change the following line : DocumentRoot /var/www/html for DocumentRoot /home/wm/sara_web/html</br>
sudo nano /etc/apache2/apache2.conf</br>
-Change the following line : <Directory /var/www/> for <Directory /home/wm/sara_web/html/></br>
sudo apache2ctl restart</br>
 </br>
On BeagleBone :</br>
sudo apt-get install chromium-browser</br>

##SARA computer launch 
sudo apache2ctl restart</br>
roslaunch rosbridge_server rosbridge_websocket.launch</br>

##BeagleBone launch
script file need to be chmod u+x </br>
setup the ip of the apache server</br>
launch the bash script, this will start chromium-browser in kiosk mode </br>

> ./web_startup.sh
