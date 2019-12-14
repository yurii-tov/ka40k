import csv, sys, os.path

def read_exercises_from_csv(filename):
    exercises = list()
    with open(filename) as r:
        for (exercise, weight) in csv.reader(r):
            exercises.append([exercise, int(weight)])
    return exercises


def save_exercises_to_csv(exercises, filename):
    with open(filename, mode='w') as fw:
        w = csv.writer(fw, dialect='unix')
        for r in exercises:
            w.writerow(r)
    return


def select_exercises(exercises, amount=3):
    exercises_1 = sorted(exercises, key=lambda x: x[1])
    selected = list()
    upto = min(amount, len(exercises))
    for i in range(0, upto):
        (exercise, weight) = exercises_1.pop(i)
        selected.append(exercise)
        exercises_1.append([exercise, weight + 1])
    return (selected, exercises_1)


def main():
    exercises_file = 'exercises.csv'
    exercises = read_exercises_from_csv(exercises_file)
    if len(exercises) is 0:
        print("You don't have any exercises in file {0}".format(exercises_file))
        return
    (selected, new_list) = select_exercises(exercises)
    for exercise in selected:
        print(exercise)
    save_exercises_to_csv(new_list, exercises_file)
        

if __name__ == "__main__":
    # execute only if run as a script
    main()
