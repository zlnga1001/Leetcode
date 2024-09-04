def num_popular_pairs(popularity_scores):
    vals = {}
    total_pair= 0
    maximum_val = []
    for i in popularity_scores:
        if i not in vals:
            vals[i] = 1
        else:
            vals[i] += 1
        
    for j in vals.values():
        if j > 1:
            num_pairs = int((j * (j-1))/2)
            total_pair += num_pairs
    return total_pair
        

popularity_scores1 = [1, 2, 3, 1, 1, 3]
popularity_scores2 = [1, 1, 1, 1]
popularity_scores3 = [1, 2, 3]

print(num_popular_pairs(popularity_scores1))
print(num_popular_pairs(popularity_scores2))
print(num_popular_pairs(popularity_scores3)) 
