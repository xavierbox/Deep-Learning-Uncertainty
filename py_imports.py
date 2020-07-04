
from typing import Any
import random, pickle, sys, itertools, string, sys, re, datetime, time, shutil, copy
import sys 
import re 
import copy;
import json;

import pandas as pd
from pandas import DataFrame 
from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype

import numpy as np; 
 
import random
from numpy.random import seed


from IPython.lib.deepreload import reload as dreload
from IPython.display import display

import PIL, os,  math, collections, threading, json,  random, scipy#, cv2 #bcolz,

import IPython, warnings, pdb  #,graphviz,  sklearn_pandas, 
import contextlib
from abc import abstractmethod
from glob import glob, iglob
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


from itertools import chain
from functools import partial
from collections import Iterable, Counter, OrderedDict
#from isoweek import Week
#from pandas_summary import DataFrameSummary
from IPython.lib.display import FileLink
from PIL import Image, ImageEnhance, ImageOps

from operator import itemgetter, attrgetter
from pathlib import Path
from distutils.version import LooseVersion




np.set_printoptions(precision=5, linewidth=110, suppress=True)

from ipykernel.kernelapp import IPKernelApp



def setSeeds(seedNumber):
    seed(seedNumber)
    #tf set_random_seed(seedNumber)
    random.seed(seedNumber)

def setSeed(seedNumber):
    setSeeds(seedNumber)


    
def in_notebook(): return IPKernelApp.initialized()

def in_ipynb():
    try:
        cls = get_ipython().__class__.__name__
        return cls == 'ZMQInteractiveShell'
    except NameError:
        return False

import tqdm as tq
from tqdm import tqdm_notebook, tnrange

def clear_tqdm():
    inst = getattr(tq.tqdm, '_instances', None)
    if not inst: return
    try:
        for i in range(len(inst)): inst.pop().close()
    except Exception:
        pass

if in_notebook():
    def tqdm(*args, **kwargs):
        clear_tqdm()
        return tq.tqdm(*args, file=sys.stdout, **kwargs)
    def trange(*args, **kwargs):
        clear_tqdm()
        return tq.trange(*args, file=sys.stdout, **kwargs)
else:
    from tqdm import tqdm, trange
    tnrange=trange
    tqdm_notebook=tqdm
    
"""


"""
