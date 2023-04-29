# We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
#       True: weekday = False or vacation = True
#       False: weekday = True 

def verify_sleep_in(weekday, vacation):
    if weekday == False or vacation == True:
        return True
    if weekday == True:
        return False
