# Raspberry Pi Weather Station
A simple Raspberry PI weather station written in Python. This is the final project for Miriadax Practical IoT course.

This basic weather station is able to get next information:

    - Temperature (DHT11 and DHT22 sensors)
    - Humidity (DHT11 and DHT22 sensors)
   
All the data are sent to Carriots IoT cloud platform.

The project is structured into the next modules:

    - managers:
    
        - Main module.
        - The module gets data from sensors and upload it to Carriots cloud.
        
    - sensors:
    
        - This module gets information for temperature and humidity.
        - Supported physical sensors are:
        
            - DHT11
    
    - carriots:
    
        - Uploads information to Carriots platform.
        
# Environment variables

    -----------------------------------------
    | NAME                        DATA TYPE |
    -----------------------------------------
    | DHT11_GPIO_PIN              INTEGER   |
    | CARRIOTS_API_URL            STRING    |
    | CARRIOTS_API_KEY            STRING    |
    | CARRIOTS_API_DEVICE         STRING    |
    -----------------------------------------

# How to use
    
    1). Set environment variables:
   
        export DHT11_GPIO_PIN=...
        export CARRIOTS_API_URL=...
        export CARRIOTS_API_KEY=...
        export CARRIOTS_API_DEVICE=...
     
    2). Execute start.py file:
    
        $ python3 start.py
        
# Automatic execution (every 10 minutes)

    - Create a script like this:
    
        - NOTE: Set correctly your own paths and environment variables
    
        # Environment variables
        export DHT11_GPIO_PIN=...
        export CARRIOTS_API_URL=...
        export CARRIOTS_API_KEY=...
        export CARRIOTS_API_DEVICE=...
          
        # Start weather station
        /usr/bin/python3 $PATH_TO_SCRIPT/rpi_weather_station/start.py
            
    - Set crontab execution:
     
        $> crontab -l | grep -i weather_station
        */10 * * * * $PATH_TO_SCRIPT/rpi_weather_station.sh
   
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
                

            