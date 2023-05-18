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

# Set variables
outputFile = "<config>/python_scripts/temp_data.txt"
h = 24              # Hours
d = 7               # Days
sampleSize = h * d  # Calculate the sample size
avg_str = 0

# Define the mobile to notify
inputMobile = data.get('mobile_id')

# Get the output entity
outputEntity = data.get('output_id')

def get_temperature():
  if inputEntity is None:
    # Send a notification on error - and create a log entry
    logger.warning("===== entity_id is required if you want to set something.")
  
  elif inputState is None:
    # Send a notification on error - and create a log entry
    logger.warning("===== Fail - inputState: %s", inputState)

  elif inputStateObject is None:
    # Send a notification on error - and create a log entry
    logger.warning("===== Fail - inputStateObject: %s", inputStateObject)
get_temperature()

def save_temp_data():

  f = open(outputFile, 'a')
  f.write(inputState + "\n")
  f.close()

save_temp_data()

def removeFirstLine():

# Count the number of lines
  with open(outputFile, 'r') as lc:
    line_count = sum(1 for line in lc)

# If we have enough samples, we remove the first entry
  if line_count >= sampleSize:
    with open(outputFile, 'r+') as fr:
      
        # read an store all lines into list
        lines = fr.readlines()
        
        # move file pointer to the beginning of a file
        fr.seek(0)
        
        # truncate the file
        fr.truncate()

        # start writing lines except the first line
        fr.writelines(lines[1:])
  else:
    print("Not enough samples, sample size:", line_count, "Required:", sampleSize)
    logger.warning("===== Fail - Not enough samples, sample size: %s", line_count, "Required: %s", sampleSize)

removeFirstLine()

def calculateAverage():
  # Initiate lists
  str_list = []
  int_list = []
  
  # Count the number of lines
  with open(outputFile, 'r') as lc:
    line_count = sum(1 for line in lc)

  # Get the values to a list  
  with open(outputFile) as f:
    str_list = [line for line in f]

  # remove new line characters
  with open(outputFile) as f:
    str_list = [line.rstrip() for line in f]

  # Convert string to int
  for x in str_list:
    int_list.append(int(x))

  # Calculate the average from the samples
  sumOfNums = 0
  count = 0
  for number in int_list:
    sumOfNums += number
    count += 1
    average_temp = sumOfNums / count

  # Round the number to two digits
  avg_rounded = round(average_temp, 2)
  
  # Convert to a string for Home Assistant
  avg_str = str(avg_rounded)
calculateAverage()

def set_temperature():
# Set the temperature value to a sensor
  hass.states.set(outputEntity, avg_str)
set_temperature()