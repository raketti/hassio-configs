# Test that we get the entity data

# From: https://community.home-assistant.io/t/how-to-manually-set-state-value-of-sensor/43975/3
#--------------------------------------------------------------------------------------------------
# Get the state for the entity specified in the Automation Action
#--------------------------------------------------------------------------------------------------

# Data for the Automation Action required:

#service: python_script.ha_med_temp
#data:
#  entity_id: <entity_id_from_HA> - for the temperature sensor
#  mobile_id: <entity_id_from_HA> - for notified mobile
#  output_id: <entity_id_from_HA> - sensor to calculate median temperature

# Idea for mobile notification from: https://github.com/custom-components/pyscript/issues/274

# Get the needed data from the Entity
inputEntity = data.get('entity_id')
inputStateObject = hass.states.get(inputEntity)
inputState = inputStateObject.state

# Define the mobile to notify
inputMobile = data.get('mobile_id')

# Get the output entity
outputEntity = data.get('output_id')

def get_temperature():
  if inputEntity is None:
    # Send a notification on error - and create a log entry
    hass.services.call('notify', inputMobile, {'title' : "Pyscript: Temp", 'message': "Didn't get entity_id from Service Call!"})
    logger.warning("===== entity_id is required if you want to set something.")
  
  elif inputState is None:
    # Send a notification on error - and create a log entry
    hass.services.call('notify', inputMobile, {'title' : "Pyscript: Temp", 'message': "Didn't get inputState from inputEntity!"})
    logger.warning("===== Fail - inputState: %s", inputState)

  elif inputStateObject is None:
    # Send a notification on error - and create a log entry
    hass.services.call('notify', inputMobile, {'title' : "Pyscript: Temp", 'message': "Didn't get inputStateObject from inputState!"})
    logger.warning("===== Fail - inputStateObject: %s", inputStateObject)
get_temperature()

def set_temperature():
# Set the temperature value to a sensor
  hass.states.set(outputEntity, inputState)
set_temperature()

"""
Now we get the correct value from entity_id.state
Problem: HA doesn't support writing to a file (permission issue)

We need a solution to store long term (7 days running) data to calculate the median value of those
"""
