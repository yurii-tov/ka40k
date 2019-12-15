import csv, sys, os.path


def read_exercises_list(filename):
    with open(filename) as r:
        return [exercise.strip()
                for exercise
                in r]


def read_weights(filename):
    if not os.path.exists(filename):
        return []
    with open(filename) as r:
        return [[exercise, int(weight)]
                for (exercise, weight)
                in csv.reader(r)]


def update_weights(weights, exercises):
    weights_set = {w[0] for w in weights}
    exercises_set = set(exercises)
    if weights_set.symmetric_difference(exercises_set):
        return [[e, 0] for e in exercises]
    return weights

    
def save_weights(weights, filename):
    with open(filename, mode='w') as fw:
        w = csv.writer(fw, dialect='unix')
        for r in weights:
            w.writerow(r)


def select_exercises(weights, amount=3):
    weights = sorted(weights, key=lambda x: x[1])
    selected = list()
    upto = min(amount, len(weights))
    for i in range(0, upto):
        (exercise, weight) = weights.pop(0)
        selected.append(exercise)
        weights.append([exercise, weight + 1])
    return (selected, weights)


def main():
    exercises_file = 'exercises'
    if not os.path.exists(exercises_file):
        with open(exercises_file, 'w'):
            pass
        print("File '{0}' not found, so it has been created for you. Please put list of exercises into it:\n{1}".format(exercises_file, os.path.abspath(exercises_file)))
        return
    if len(sys.argv) < 2:
        print("Usage: ka40k number-of-exercises-to-choose")
        return
    try:
        num_of_exercises = int(sys.argv[1])
    except ValueError:
        print("Natural number expected")
        return
    exercises = read_exercises_list(exercises_file)
    if len(exercises) is 0:
        print("You don't have any exercises in file '{0}'".format(exercises_file))
        return
    weights_file = 'weights.csv'
    weights = update_weights(read_weights(weights_file), exercises)
    (selected, weights) = select_exercises(weights, amount=num_of_exercises)
    for exercise in selected:
        print(exercise)
    save_weights(weights, weights_file)
    

if __name__ == "__main__":
    # execute only if run as a script
    main()
