def identify_conflicts(venue1_schedule, venue2_schedule):
    conflict = {}
    for movie, time in venue1_schedule.items():
        if movie in venue2_schedule and venue2_schedule[movie] == time:
            conflict[movie] = time
    return conflict

venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

print(identify_conflicts(venue1_schedule, venue2_schedule))