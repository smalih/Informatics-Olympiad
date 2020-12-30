clocks = input()
clock1, clock2 = clocks.split(" ")
clock1, clock2 = int(clock1), int(clock2)
list1 = []
list2 = []


# Convert time into hours and minutes
def convert(time):
  hours = 0
  while time >=1440:
    time -=1440
  while time >= 60:
    time -= 60
    hours +=1
  minutes = time
  # Convert to hours
  time/=60

  return hours, minutes



def addTime(hours, minutes, currentHours, currentMinutes):
  if currentMinutes + minutes >=60:
    currentMinutes -= 60
    currentHours+=1
  currentMinutes+= minutes

  if currentHours + hours >= 24:
    currentHours-=24
  currentHours+=hours
  string = f"{currentHours}:{currentMinutes}"
  return string, currentHours, currentMinutes

hours1, minutes1 = convert(clock1)
hours2, minutes2 = convert(clock2)
currentHours1 = currentHours2 = 0
currentMinutes1 = currentMinutes2 = 0

for i in range(1000):
  string, currentHours1, currentMinutes1 = addTime(hours1, minutes1, currentHours1, currentMinutes1)
  list1.append(string)

for i in range(1000):
  string, currentHours2, currentMinutes2 = addTime(hours2, minutes2, currentHours2, currentMinutes2)
  list2.append(string)

print(list1)
print(list2)
