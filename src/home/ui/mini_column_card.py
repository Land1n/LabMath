import flet as ft

from dataclasses import dataclass

from src.utils import on_change_obj


@dataclass
class DataMiniColumnCard:
    number:int
    symbol:str
    name:str
    device_error:str

class MiniColumnCard(ft.Card):

    class MyTextField(ft.TextField):
        def __init__(self,label:str,input_filter:ft.InputFilter=None,max_length:int=1):
            super().__init__(
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

    def __init__(self,dd_row:int,number:int=0,data:DataMiniColumnCard={}):
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

        self.column_with_row = ft.ExpansionTile(
            title=ft.Text("Значение строк"),
            subtitle=ft.Text("Этот раздел обязателен",color="grey"),
            leading=ft.Icon("analytics"),
            affinity=ft.TileAffinity.PLATFORM,
            controls=[
                ft.Column(
                    spacing=10,
                    controls=[
                        ft.TextField(
                            label=f"Cтрока: {i}",
                            on_change=on_change_obj,
                            input_filter=ft.NumbersOnlyInputFilter()
                        ) for i in range(1,dd_row+1)
                    ]
                )
            ]
        )

        if data:
            self.data = DataMiniColumnCard(**data)
            
            self.number =  self.data.number
            self.symbol.value =  self.data.symbol
            self.name.value =  self.data.name
            self.device_error.value =  self.data.device_error


        self.content=ft.Container(
                padding=10,
                content=ft.Column(
                    controls=[
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.Icon("event_note"),
                                        ft.Text(
                                            value=f"Столбец: {self.number}",
                                            size=15,
                                            weight=ft.FontWeight.BOLD
                                        )
                                    ]
                                ),
                            ],
                        ),
                        ft.ResponsiveRow(
                            controls=[
                                self.symbol,
                                self.name,
                                self.device_error
                            ]
                        ),
                        self.column_with_row
                    ]
                )
            )

    @property
    def value(self):
        if all([self.symbol.value,self.name.value,self.device_error.value,*self.values]):
            return { 
                "symbol":self.symbol.value,
                "name":self.name.value,
                "device_error":int(self.device_error.value),
                "values":[int(tf.value) for tf in self.column_with_row.controls[0].controls],
            }
        else:
            return False
