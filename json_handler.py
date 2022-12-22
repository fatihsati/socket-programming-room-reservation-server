import json

#################### Room Server ####################
def add_room(roomname):
    # add room to json file
    # if roomname is already in the json file, return 403
    # else return 200
    
    return 403


def remove_room(roomname):
    # delete room from json file
    # if roomname is not in the json file, return 403
    # else return 200
    
    return 403


def reserve_room(roomname, day, hour, duration):
    # reserve room in json file
    # if any of the input is invalid return 400
    # if room is already reserved return 403
    # else return 200
    
    return 403


def check_availability(roomname, day):
    # if roomname is not exists return 404, None
    # if day is not a valid day return 400, None
    # else return 200, "available hours"
    
    return 404, "9 10 11 12 16 17 18" # clocks are sperated by single space


#################### Activity Server ####################
def add_activity(activityname):
    # add activity to json file
    # if activityname is already in the json file, return 403
    # else return 200
    
    return 403

def remove_activity(activityname):
    # delete activity from json file
    # if activityname is not in the json file, return 403
    # else return 200
    
    return 403

def check_activity(activityname):
    # check if activity is in json file
    # if activityname is not in the json file, return 404
    # else return 200
    
    return 404
    