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
    call_list = []
    hangup_list = []
    
    f = open(filename, "r")
    for line in f:
        parts = line.split()
        if parts[0] == "call":
            '''
            All the integers are long in Python3,
            so we can use int() to convert a string to long here.
            '''
            call_list.append(Call(parts[1], parts[2], int(parts[3])))
        elif parts[0] == "hangup":
            hangup_list.append(Hangup(parts[1], parts[2], int(parts[3])))
        else:
            print("Invalid input")
    f.close()
    
    return call_list, hangup_list

# Get call durations for each caller.
def get_caller_call_durations(call_list, hangup_list):
    caller_call_durations = {}
    for call in call_list:
        caller = call._from
        for i, hangup in enumerate(hangup_list):
            if caller == hangup._from or caller == hangup._to:
                call_duration = hangup.timestamp - call.timestamp
                
                if caller not in caller_call_durations:
                    caller_call_durations[caller] = [call_duration]
                else:
                    caller_call_durations[caller].append(call_duration)
                    
                del hangup_list[i]
                break
            
    return caller_call_durations

# Get suspects who have average call duration less than 5 minutes.
def get_suspects(caller_call_durations):
    suspects = []
    for caller, call_durations in caller_call_durations.items():
        if sum(call_durations) / len(call_durations) < 5:
            suspects.append(caller)
    
    return suspects

def main():
    call_list, hangup_list = readData("exampleInput.txt")
    caller_call_durations = get_caller_call_durations(call_list, hangup_list)
    suspects = get_suspects(caller_call_durations)
    print(suspects)
    
if __name__ == '__main__':
    main()
        


