import flet as ft

from dataclasses import dataclass

from src.utils import on_change_obj, ClassicalTextButton


@dataclass
class DataSampleCard:
    symbol:str
    name:str
    device_error:str
    values:list[int]

class SampleCard(ft.Card):

    class MyTextField(ft.TextField):
        def __init__(self,label:str,input_filter:ft.InputFilter=None,value='',max_length:int=None):
            super().__init__(
                value=value,
                label=label,
                input_filter=input_filter,
                max_length=max_length,
                col={"md": 4,"xs": 4},
                hint_text="(Обязательно)",
                label_style=ft.TextStyle(size=11),
                hint_style=ft.TextStyle(size=11),
                multiline=False,
                on_change=on_change_obj,
            )

    class NumbersAndDotInputFilter(ft.InputFilter):
        def __init__(self):
            super().__init__(regex_string=r"[0-9,.]")

    class TextInputFilter(ft.InputFilter):
        def __init__(self):
            super().__init__(regex_string=r"[a-zA-ZА-Яа-я]")

    def __init__(self,number:int,data:DataSampleCard={}):
        super().__init__()

        self.values = []

        self.number = number

        self.symbol = self.MyTextField(
            label="Обозначение\n(Символ)",
            max_length=1,
        )
        
        self.name = self.MyTextField(
            label="Наименование\n(Ед.измерения)",
            max_length=8,
            input_filter=self.TextInputFilter(),
        )
        
        self.device_error = self.MyTextField(
            label="Приборная\nпогрешность",
            input_filter=ft.NumbersOnlyInputFilter(),
        )


        self.column_with_row = ft.Column(
            expand=1,
            tight=1,
        )

        self.expansion_tile = ft.ExpansionTile(
            title=ft.Text("Данные выборки"),
            leading=ft.Icon("analytics"),
            affinity=ft.TileAffinity.PLATFORM,
            
            controls=[self.column_with_row,ClassicalTextButton(text='Добавить данные',icon="add",on_click=self.add_ft)]
        )

        if data:
            self.data = DataSampleCard(**data)
            self.symbol.value =  self.data.symbol
            self.name.value =  self.data.name
            self.device_error.value =  self.data.device_error
            self.values = self.data.values
            for value in self.values:
                self.add_ft(value=str(value),need_update=False)

        self.content=ft.Container(
                padding=10,
                content=ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Icon("insert_chart_outlined"),
                                ft.Text(
                                    value=f"Выборка: {self.number}",
                                    size=15,
                                    weight=ft.FontWeight.BOLD
                                )
                            ]
                        ),
                        ft.ResponsiveRow(
                            controls=[
                                self.symbol,
                                self.name,
                                self.device_error
                            ]
                        ),
                        self.expansion_tile
                    ]
                )
            )

    def add_ft(self,e:ft.ControlEvent=None,value:str="",need_update:bool = True):
        self.column_with_row.controls += [self.MyTextField(f"Строка: {len(self.column_with_row.controls)+1}",value=value)]
        if need_update:
            self.column_with_row.update()

    @property
    def value(self):
        if all([self.symbol.value,self.name.value,self.device_error.value,*self.values]):
            return { 
                "symbol":self.symbol.value,
                "name":self.name.value,
                "device_error":int(self.device_error.value),
                "values":[int(tf.value) for tf in self.column_with_row.controls],
            }
        else:
            return False
