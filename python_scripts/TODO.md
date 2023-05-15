# Things to do
Idea is to calculate the median temperature for the past week

## Get the current temperature once an hour
- [x] Getting the current outside temperature from ATW Heat Pump sensor
- [ ] Create sample size h = 24 / d = 7
- This will be done by running the script once an hour and writing the data to a) sensor b) file
- Two options for the median value sensor:

 - [ ] a) Create a statistic sensor in Home Assistant
    - Use: https://www.home-assistant.io/integrations/statistics/
    - Example:

  ```
  sensor:
    - platform: statistics
      name: "Outside temperature mean over last 7 days"
      entity_id: sensor.atw_heat_pump_temperature
      state_characteristic: mean
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
  sensor.atw_heat_pump_temperature
```

- [ ] Use an automation to control the Target Heating Temperature
