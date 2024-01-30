
names = ["John", "Paul", "George", "Ringo"]
scores = [100, 90, 80, 70]

for name, score in zip(names, scores):
    print(f"{name} scored {score}")

scores.pop(-1)

for name, score in zip(names, scores):
    print(f"{name} scored {score}")

score_dict = dict(zip(names, scores))
print(score_dict)
