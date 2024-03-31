from collections import deque

'''
This project analyzes call events to identify suspicious call behavior based on the duration of the calls. 
It processes call and hangup events to calculate the average call duration for each caller 
and identifies suspects whose average call duration is under 5 seconds.
'''

'''
CallEvent class represents a call event with the following attributes:
    _from (string): the person originating the event
    _to (string): the person receiving the event
    timestamp (long): seconds since the beginning of the Unix epoch
'''
class CallEvent:     
    def __init__(self, _from, _to, timestamp):
        self._from = _from
        self._to = _to
        self.timestamp = timestamp

'''
Call class inherits from CallEvent class and represents a call event.
'''
class Call(CallEvent):
    pass

'''
Hangup class inherits from CallEvent class and represents a hangup event.
'''
class Hangup(CallEvent):
    pass

# Read call events from file and split them into call and hangup events.
def readData(filename):
    '''
    Initialize a list to store call events and a dictionary to store hangup events.
    '''
    calls = []
    hangups = {}
    
    f = open(filename, "r")
    for line in f:
        parts = line.split()
        if parts[0] == "call":
            '''
            All the integers are long in Python3,
            so we can use int() to convert a string to long here.
            '''
            curr_call = Call(parts[1], parts[2], int(parts[3]))
            calls.append(curr_call)
        elif parts[0] == "hangup":
            curr_hangup = Hangup(parts[1], parts[2], int(parts[3]))
            curr_hangup_key = (curr_hangup._from, curr_hangup._to)
            alternative_hangup_key = (curr_hangup._to, curr_hangup._from)
            if curr_hangup_key not in hangups:
                q = deque()
                q.append(curr_hangup)
                hangups[curr_hangup_key] = q
            else:
                hangups[curr_hangup_key].append(curr_hangup)
            '''
            Create a mirror hangup event for the other direction.
            '''
            hangups[alternative_hangup_key] = hangups[curr_hangup_key]
        else:
            print("Invalid input")
    f.close()
    
    return calls, hangups

# Get call durations for each caller.
def get_caller_call_durations(calls, hangups):
    caller_call_durations = {}
    
    for curr_call in calls:
        curr_hangup_key = (curr_call._from, curr_call._to)
        if curr_hangup_key not in hangups:
            continue
        
        '''
        Pop the first hangup event from the queue for the current call.
        '''
        curr_hangup = hangups[curr_hangup_key].popleft()
        curr_call_duration = curr_hangup.timestamp - curr_call.timestamp
        curr_caller = curr_call._from
        
        if curr_caller not in caller_call_durations:
            caller_call_durations[curr_caller] = [curr_call_duration]
        else:
            caller_call_durations[curr_caller].append(curr_call_duration)
            
    return caller_call_durations

# Get suspects who have average call duration less than 5 minutes.
def get_suspicious_callers(caller_call_durations):
    suspicious_callers = []
    for caller, call_durations in caller_call_durations.items():
        if (sum(call_durations) / len(call_durations)) < 5:
            suspicious_callers.append(caller)
    
    return suspicious_callers

def main():
    filename = input("Please enter the name of the data file (e.g. exampleInput.txt):")
    calls, hangups = readData(filename)
    caller_call_durations = get_caller_call_durations(calls, hangups)
    suspicious_callers = get_suspicious_callers(caller_call_durations)
    print("The list of suspicious callers is as follows.")
    print(suspicious_callers)
    
if __name__ == '__main__':
    main()
        


