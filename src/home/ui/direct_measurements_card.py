import flet as ft

from src.shemes import DataSample

class DirectMeasurementsCard(ft.Card):
    def __init__(self,data:DataSample):
        self.data = DataSample(**data)