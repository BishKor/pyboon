__author__ = 'BisharaKorkor'

import numpy as np
from math import exp, pow, sqrt, pi, fmod

def movingaverage(a, w):
    """ An array b of length len(a)-w is returned where b_n = (a_n + a_n-1 + ... + a_n-w)/w """
    return [np.mean(a[i:i+w]) for i in range(len(a)-w)]

def gaussiankernel(sigma, width):
    """Generates gaussian kernel"""
    #  tmp is a non-normalized gaussian kernel
    tmp = [exp(-pow((width/2 - i) / sigma, 2)/2)/(sigma * sqrt(2 * pi)) for i in range(width)]
    #  compute sum for normalization
    s = np.sum(tmp)
    #  return the normalized kernel
    return [i / s for i in tmp]

def movingbaseline(array, width):
    """ Each array value is assigned to be it's value divided by the average of the preceding width (inclusive)
    elements"""
    mva = movingaverage(array, width)
    return [array[i+width]/mva[i] for i in range(len(mva))]

def exponentialsmoothing(array, alpha):

    sa = [array[0]]  #smoothed array

    for i in range(len(array)):
        sa += [alpha * array[i] + (1-alpha) * sa[i]]

    del sa[0]
    return sa

def histogramfrom2Darray(array, nbins):
    """
    Creates histogram of elements from 2 dimensional array

    :param array: input 2 dimensional array

    :param nbins: number of bins so that bin size = (maximum value in array - minimum value in array) / nbins
        the motivation for returning this array is for the purpose of easily plotting with matplotlib

    :return: list of three elements:
            list[0] = length nbins list of integers, a histogram of the array elements
            list[1] = length nbins list of values of array element types, values of the lower end of the bins
            list[2] = [minimum in list, maximum in list]
        this is just good to know sometimes.
    """

    #find minimum
    minimum = np.min(array)
    #find maximu
    maximum = np.max(array)

    #compute bin size
    binsize = (maximum - minimum) / nbins

    #create bin array
    bins = [minimum + binsize * i for i in range(nbins)]
    histo = [0 for b in range(nbins)]

    for x in array:
        for y in x:
            #find the lower end of the affiliated bin
            ab = y - (minimum + fmod(y - minimum, binsize))
            histo[int(ab/binsize)-1] += 1

    return [histo, bins, [minimum, maximum]]


def sum_of_subset(array, x, y, dx, dy):
    summ = 0  # summ because sum is native
    for ix in range(x, x + dx):
        for iy in range(y, y + dy):
            summ += array[ix][iy]
    return summ


def subset(array, x, y, dx, dy):
    ss = []
    for ix in range(x, x + dx):
        for iy in range(y, y + dy):
            ss.appen(array[ix][iy])
    return ss
