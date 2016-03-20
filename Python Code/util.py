
def check_week_ind(day):
    """Given a day number 1-7, return if it is a weekday or weekend
       Args: day (int)
       Returns: a string indicator
    """
    if day in [6, 7]:
        return 'Weekends'
    else:
        return 'Weekdays'


def time_interval(minute):
  """Given a time in minutes returns a time interval for every 10 min
     Args: minute: time(int) anynumber between 0-60
     Returns: int indicate which time interval the minute is in
  """
  start = 0
  for i in range(1, 7):
    if minute >= start and minute < start + 10:
      return start + 10 
      break
    start = i*10 

