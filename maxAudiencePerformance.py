def max_audience_performances(audiences):
    target_num_audience = max(audiences)
    sum = 0
    for i in audiences:
        if i == target_num_audience:
            sum += target_num_audience
    return sum



audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))