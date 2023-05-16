# Home Assistant configs and scirpts

Configuration and additional sensors for Home Assistant

## Python script(s)

### Requirements

The configuration.yaml needs the following line to be added:
 ```
 python_scripts:
 ```
Create the folder:
 ```
 <config>/python_scripts
 ```
The script can be called from the <b>Developer Tools -> Services</b>
Example:
 ```
 service: python_script.my_script
 data:
  entity_id: sensor.livingroom_temperature
 ```
 More information and examples: https://www.home-assistant.io/integrations/python_script/
