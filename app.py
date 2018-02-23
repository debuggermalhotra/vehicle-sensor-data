import dash
import dash_core_components as dcc
import dash_html_components as html
from pandas_datareader.data import DataReader
import time
from collections import deque
import plotly.graph_objs as go
import random


app = dash.Dash('vehicle-data')

max_length = 20
times = deque(maxlen=max_length)
oil_temps = deque(maxlen=max_length)
intake_temps = deque(maxlen=max_length)
coolant_temps = deque(maxlen=max_length)
rpms = deque(maxlen=max_length)
speeds = deque(maxlen=max_length)
throttle_pos = deque(maxlen=max_length)

data-dict={
    "Oil_Temperature":oil_temps,
    "Intake_temperature":intake_temps,
    "Coolant_temperature":coolant_temps,
    "RPM":rpms,
    "Speed":speeds,
    "Throttle Position":throttle_pos
}