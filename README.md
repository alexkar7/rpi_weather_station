# Raspberry Pi Weather Station
A simple Raspberry PI weather station written in Python. This is the final project for Miriadax Practical IoT course.

This basic weather station is able to get next information:

    - Temperature (using DHT11 sensor)
    - Humidity (using DHT11)
    
The execution of this app is done every 5 minutes via crontab.

All the data are sent to Carriots IoT cloud platform.

# Environment variables

    DHT11_GPIO_PIN
    CARRIOTS_API_URL
    CARRIOTS_API_KEY
    CARRIOTS_API_DEVICE

# How to use:
    
    1). Set environment variables:
    
        export DHT11_GPIO_PIN=4
        export CARRIOTS_API_URL="http://api.carriots.com/streams"
        export CARRIOTS_API_KEY="This is a private value, set yours"
        export CARRIOTS_API_DEVICE="rpi1@alexkar7.alexkar7"
     
    2). Execute start.py file:
    
        $ python3 start.py

# Dependencies

    # Adafruit Python DHT Sensor Library
    
        - URL = https://github.com/adafruit/Adafruit_Python_DHT
    
        - Installation:
        
            - Update system:
        
                $> apt-get update
                
            - Install required packages:
            
                $> apt-get install -y build-essential python-dev
            
            - Clone project:
            
                $> cd /tmp
                $> git clone https://github.com/adafruit/Adafruit_Python_DHT
                
            - Install module: 
            
                $> cd Adafruit_Python_DHT/
                $> sudo python3 setup.py install --force-pi
                

            