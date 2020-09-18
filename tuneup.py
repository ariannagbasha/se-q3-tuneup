#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment

Use the timeit and cProfile libraries to find bad code.
"""

__author__ = "Gabby, collabs: Shanquel & Sondos and got help from Daniel"

import cProfile
import pstats
import functools
import timeit
import statistics


def profile(func):
    """A cProfile decorator function that can be used to
    measure performance.
    """
    # Be sure to review the lesson material on decorators.
    # You need to understand how they are constructed and used.
    # Wrapping the function in additional functionality
    def wrapper(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        result = func(*args, **kwargs)
        pr.disable()
        sort_by = 'cumulative'
        ps = pstats.Stats(pr).sort_stats(sort_by)
        ps.print_stats()
        return result
    return wrapper

def read_movies(src):
    """Returns a list of movie titles."""
    print(f'Reading file: {src}')
    with open(src, 'r') as f:
        return f.read().splitlines()


def is_duplicate(title, movies):
    """Returns True if title is within movies list."""
    return title in movies

@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list."""
    movies = read_movies(src)
    duplicates = []
    while movies:
        movie = movies.pop()
        if is_duplicate(movie, movies):
            duplicates.append(movie)
    return duplicates


def timeit_helper():
    """Part A: Obtain some profiling measurements using timeit."""
    num_repeats = 5
    runs_per_repeat = 3
    t = timeit.Timer(stmt="print(type(l))", setup="l = []")
    result = t.repeat(repeat=num_repeats, number=runs_per_repeat)
    time_cost = min(result) / runs_per_repeat # How many times in total 
    print(f'Best time across {num_repeats} repeats of {runs_per_repeat} runs per repeat: {time_cost}')


def main():
    """Computes a list of duplicate movie entries."""
    result = find_duplicate_movies('movies.txt')
    print(f'Found {len(result)} duplicate movies:')
    print('\n'.join(result))


if __name__ == '__main__':
    main()
    timeit_helper()
    
