def best_set(votes):
    #Plan:
    # get the values of the dict, and then have a count to count how many that value is. The count should be dict because they have the person name => so that will be the key and then we have the values is the increment of how many time that person was called.
    count = {}

    for star in votes.values():
        if star not in count:
            count[star] = 1
        else:
            count[star] += 1
        
    #find the artist with the maximum votes:
    listofStar=[]
    maxVote = max(count.values())
    for artist, voteCount in count.items():
        if voteCount == maxVote:
            listofStar.append(artist)
    return listofStar
            
        

votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print(best_set(votes1))
print(best_set(votes2))