import flet as ft

from src.database import Database

def repeat(object, times=None):
    # repeat(10, 3) --> 10 10 10
    if times is None:
        while True:
            yield object
    else:
        for i in range(times):
            yield object

def zip_longest(*args, fillvalue=None):
    # zip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-
    iterators = [iter(it) for it in args]
    num_active = len(iterators)
    if not num_active:
        return
    while True:
        values = []
        for i, it in enumerate(iterators):
            try:
                value = next(it)
            except StopIteration:
                num_active -= 1
                if not num_active:
                    return
                iterators[i] = repeat(fillvalue)
                value = fillvalue
            values.append(value)
        yield tuple(values)

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

        for row in zip_longest(*(sample['values'] for sample in self.sample_data),fillvalue="-"):

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
        )
        