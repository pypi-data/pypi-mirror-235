from string import ascii_uppercase
from typing import Any

from gspread import service_account
from gspread_formatting import format_cell_ranges

from .format import Format


class Client:
    def __init__(self, file: str, title: str) -> None:
        self._path = file
        self._name = title
        self._account = service_account(filename=self._path)
        self._worksheet = self._account.open(self._name).sheet1
        self._column_names: tuple | None = None

    def create_data_table(self, *columns: Any) -> None:
        columns_ = len(columns)
        letters = tuple(ascii_uppercase)

        if columns_ > 26:
            raise ValueError(f"Количество колонок не может превышать {len(letters)}.")

        self._column_names = columns

        self._worksheet.batch_update(
            [
                {
                    "range": f"A1:{letters[columns_ - 1]}1",
                    "values": [[value for value in columns]]
                }
            ]
        )

    def _get_last_row_id(self) -> int:
        return len(self._worksheet.get_all_values())

    @property
    def last_row_id(self) -> int:
        return self._get_last_row_id()

    def format_cells(self, range_: str, cell_format: Format) -> None:
        format_cell_ranges(worksheet=self._worksheet, ranges=[(range_, cell_format.get_format())])

    def _set_row(self, range_: str, *columns: Any) -> None:
        self._worksheet.batch_update(
            [
                {
                    "range": range_,
                    "values": [[value for value in columns]]
                }
            ]
        )

    def insert_row(self, *columns: Any, column_format: Format | None = None) -> None:
        if self._column_names is None:
            raise RuntimeError(
                "Для создания колонок требуется вызвать метод 'create_data_table' для инициализации таблицы."
            )

        if len(columns) != len(self._column_names):
            raise ValueError(f"Необходимо заполнить все {len(self._column_names)} колонок.")

        letters = tuple(ascii_uppercase)
        row_id = self._get_last_row_id() + 1
        range_ = f"A{row_id}:{letters[len(columns) - 1]}{row_id}"

        self._set_row(range_=range_, *columns)
        self.format_cells(range_=range_, cell_format=column_format)

    def update_row(self, *columns: Any, row_id: int, column_format: Format | None = None) -> None:
        if self._column_names is None:
            raise RuntimeError(
                "Для обновления колонок требуется вызвать метод 'create_data_table' для инициализации таблицы."
            )

        if len(columns) != len(self._column_names):
            raise ValueError(f"Необходимо заполнить все {len(self._column_names)} колонок.")

        letters = tuple(ascii_uppercase)
        range_ = f"A{row_id}:{letters[len(columns) - 1]}{row_id}"

        self._set_row(range_=range_, *columns)
        self.format_cells(range_=range_, cell_format=column_format)
