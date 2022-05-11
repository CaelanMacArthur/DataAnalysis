#importing required packages
import pandas as pd
import pandas_profiling
import numpy as np
import sweetviz as sv
import pandas as pd
from autoviz.AutoViz_Class import AutoViz_Class

AV = AutoViz_Class()
sweetVizData = pd.read_csv('path to csv')
avData = AV.AutoViz('path to csv',chart_format='html')
reportSweetViz = sv.analyze(sweetVizData)
reportSweetViz.show_html('example.html') 



