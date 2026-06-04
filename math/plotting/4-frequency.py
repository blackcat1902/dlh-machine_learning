#!/usr/bin/env python3
"""Module that plotting a histogram of student scores for a project."""

import numpy as np
import matplotlib.pyplot as plt

def frequency():
    """The function that dşsplays students scores for a project"""

    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    plt.figure(figsize=(6.4, 4.8))

    plt.xlabel("Grades")
    plt.ylabel("Number of Students")
    x = np.arange(0, 100, 10)
    plt.title("Project A")
    plt.hist(student_grades, bins = 10, edgecolor = 'black')
    plt.xticks(bins)
    plt.show()
