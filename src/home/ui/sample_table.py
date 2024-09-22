import flet as ft

from src.database import Database

from itertools import zip_longest

class SampleTable(ft.DataTable):
    def __init__(self,sample_data:list):
        self.sample_data = sample_data
        columns = []
        rows=[]

        for sample in self.sample_data:
            columns += [
                ft.DataColumn(
                    label=ft.Text(f'{sample["symbol"]}, {sample["name"]}')
                )
            ]

        for row in zip_longest(*(sample['values'] for sample in self.sample_data)):

            rows += [
                ft.DataRow(
                    cells=[
                        ft.DataCell(
                            ft.Text(text)
                        )
                        for text in row
                    ]
                )
            ]

        super().__init__(
            columns=columns,
            rows=rows,
            vertical_lines=ft.BorderSide(0.5, "black"),            
        )
        