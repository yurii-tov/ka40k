# ka40k

Choose exercises for current workout

## Main use case

During the training process, you need to work equally on a fairly large list of exercises. Naturally, every day you devote time not to all these exercises, but only to a small subset.
This small program will help you choose the exercises for your current workout, based on previous exercises, thus evenly distributing strength between all exercises in a long-term perspective.

## Usage

### 1. Run the program without arguments

At this moment, program will create empty file for exercises list

```sh
$ python -m ka40k
File 'exercises' not found, so it has been created for you. Please put list of exercises into it.
```

### 2. Fill list of exercises

First, you have to put list of exercises in a text file `exercises` in the same directory as the program.
You can use `example` file as a guide

### 3. Run program again with argument

```sh
$ python -m ka40k 3
# Here you see list of exercises
```
