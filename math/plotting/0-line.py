#!/usr/bin/env python3
"""Module that plots a cubic line graph"""

import matplotlib.pyplot as plt
import numpy as np


def line():
    """Displays a cubic line graph"""
    y = np.arange(0, 11) ** 3
    plt.figure(figsize=(6.4, 4.8))

    x = np.arange(0, 11)
    plt.plot(x, y, color='red', linestyle='-')
    plt.xlim(0, 10)
    plt.show()
