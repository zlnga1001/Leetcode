def lineup(artists, set_times):
    thisDict = {}
    #len(artist) = 4
    #range(len(artist)) = [0,1,2,3]
    for i in range(len(artists)): #O(1)
            thisDict[artists[i]] = set_times[i]
    return thisDict

#timecomplexity: O(n)
artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

print(lineup(artists1, set_times1))
print(lineup(artists2, set_times2))