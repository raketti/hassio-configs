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
### Plan A (didn't work out - but a great excersize! 😄)
- [x] Create sample size h = 24 / d = 7
- This will be done by running the script once an hour and writing the data to a) sensor b) file
- Two options for the median value sensor:

 - [x] a) Create a statistic sensor in Home Assistant
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

 - [x] b) Calculate the mean/median/average within the Python script
    - This would require persistent storage
    - If we use a list, this will be cleared on every reboot
    - After sample size is h * d + 1, remove the first sample from the list
    - Then we calculate the median of the sample set
  - Done in:
    - https://github.com/raketti/python-learning/blob/main/ifs-and-loops/random_generator.py
    - However, since HA doesn't have ```open```, ```close``` or ```write```  available from Python, we need another solution

 <s>- [ ] Read median value from sensor</s>
```
  sensor.sensor.pannuhuone_outside_temperature
```
  - Scrapped.
    - We can save a value to the sensor and use it as an average in a Lovelace Dashboard
    - The average value isn't exposed as such, only current state, so we can't use that as a trigger in an automation

### Plan B (Not as lightweight solution as the Plan A - then again, more training! 👍 🤓)
  - Use the random_generator.py
  - [ ] Install InnoluxDB Add-on to Home Assistant
  - [ ] Save the temperature state to DB
  - [ ] Read the temperature from latest to ```sampleSize```
  - [ ] Calculate the average temperature within the Python script
  - [ ] Save the average value to HA sensor
  - [ ] Use an automation to control the Target Heating Temperature
