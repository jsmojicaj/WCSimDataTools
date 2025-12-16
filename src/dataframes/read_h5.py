import pandas as pd
import numpy as np
from wcsimreader import utils

def wcsimroot(filename):
    return utils.read_table(filename, "wcsimRootOptionsT")
    

def geo(filename):
    return utils.read_table(filename, "wcsimGeoT/Geometry")
    

def pmt(filename):
    return utils.read_table(filename, "wcsimGeoT/PMT")
    

def cherenkovhits(filename):
    return utils.read_table(filename, "wcsimT/CherenkovHits")
    

def cherenkovhitstimes(filename):
    return utils.read_table(filename, "wcsimT/CherenkovHitTimes")


def track(filename):
    return utils.read_table(filename, "wcsimT/Tracks")


def trigger(filename):
    return utils.read_table(filename,"wcsimT/Triggers")


def digihits(filename):
    return utils.read_table(filename, "wcsimT/CherenkovDigiHits/DigiHits")

