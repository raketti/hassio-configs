# Things to do
Idea is to calculate the median temperature for the past week

## Get the current temperature once an hour
- [x] Getting the current outside temperature from ATW Heat Pump sensor

  - Use service call:
  ```
  service: python_script.ha_med_temp
  data:
    entity_id: sensor.vilp_melcloud_outside_temperature
    mobile_id: mobile_app_gargamel
    output_id: sensor.pannuhuone_outside_temperature
  ```

- [ ] Create sample size h = 24 / d = 7
- This will be done by running the script once an hour and writing the data to a) sensor b) file
- Two options for the median value sensor:

 - [ ] a) Create a statistic sensor in Home Assistant
    - Use: https://www.home-assistant.io/integrations/statistics/
    - Example:

  ```
  - platform: statistics
    name: "Ulkolämpötila - Keskiarvo"
    entity_id: sensor.pannuhuone_outside_temperature
    state_characteristic: average_linear
    precision: 1
    max_age:
      days: 7
  ```

 - [ ] b) Calculate the mean/median/average within the Python script
    - This would require persistent storage
    - If we use a list, this will be cleared on every reboot
    - After sample size is h * d + 1, remove the first sample from the list
    - Then we calculate the median of the sample set

- [ ] Read median value from sensor
```
  sensor.sensor.pannuhuone_outside_temperature
```

- [ ] Use an automation to control the Target Heating Temperature
