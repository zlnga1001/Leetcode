def max_audience_performances(audiences):
    vals = {}
    for i in audiences:
        if i not in vals:
            vals[i] = 1
        else:
            vals[i] += 1

        max_size = max(vals.keys())

        total_count = max_size * vals[max_size]
        
    return total_count




audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))

