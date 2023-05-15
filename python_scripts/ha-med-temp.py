# Test that we get the entity data

# From: https://community.home-assistant.io/t/how-to-manually-set-state-value-of-sensor/43975/3
#--------------------------------------------------------------------------------------------------
# Get the state for the entity specified in the Automation Action
#--------------------------------------------------------------------------------------------------

# Data for the Automation Action required:

#service: python_script.ha_med_temp
#data:
#  entity_id: <entity_id_from_HA>

# We could hard code the Entity ID for this since we only use it now for the ATW Heat Pump (Entity ID: sensor.vilp_melcloud_outside_temperature)

inputEntity = data.get('entity_id')
inputStateObject = hass.states.get(inputEntity)
inputState = inputStateObject.state

if inputEntity is None:
  logger.warning("===== entity_id is required if you want to set something.")
else:
  logger.warning("===== Got Entity ID: %s", inputEntity)
  
if inputState is None:
  logger.warning("===== Fail - inputState: %s", inputState)
else:
  logger.warning("===== Success - inputState: %s", inputState)

if inputStateObject is None:
  logger.warning("===== Fail - inputStateObject: %s", inputStateObject)
else:
  logger.warning("===== Success - inputStateObject: %s", inputStateObject)

"""
Now we get the correct value from entity_id.state
Problem: HA doesn't support writing to a file (permission issue)

We need a solution to store long term (7 days running) data to calculate the median value of those
"""
