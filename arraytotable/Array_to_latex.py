import numpy as np


class LatexTable:
    __array: np.ndarray
    __caption: str
    __label: str
    __centering: bool
    __data_align: str
    __label_align: str

    __vline: bool
    __hline_top:bool
    __hline_bottom:bool
    __hline_header:bool
    __hline_rows:bool

    __bold_column_labels:bool
    __bold_row_labels:bool

    __row_labels = list[str] | None
    __column_labels = list[str] | None

    __row_colors = list[str|None]
    __column_colors = list[str|None]

    __scientific_notation: bool
    __precision: int
    __round: bool

    __unit: str

    def __init__(self, array:np.ndarray,
                 centering:bool=True,

                 vline:bool=False,
                 hline_top:bool=True,
                 hline_bottom:bool=True,
                 hline_header:bool=True,
                 hline_rows:bool=False,

                 bold_column_labels:bool=True,
                 bold_row_labels:bool=True,

                 scientific_notation:bool=False,
                 precision:int = 2,
                 round:bool = False,

                 unit:str = "",

                 caption:str='caption',
                 label:str='tab:my-label',
                 data_align:str="center",
                 label_align:str="left"):

        self.__array = array
        self.__row_colors = [None for _ in range(self.array.shape[0])]
        self.__column_colors = [None for _ in range(self.array.shape[1])]
        self.__caption = caption
        self.__label = label
        self.__centering = centering

        self.__vline = vline
        self.__hline_top = hline_top
        self.__hline_bottom = hline_bottom
        self.__hline_header = hline_header
        self.__hline_rows = hline_rows

        self.__bold_column_labels = bold_column_labels
        self.__bold_row_labels = bold_row_labels

        self.__data_align = data_align
        self.__label_align = label_align
        self.__data_align_options = ["left", "center", "right"]

        self.__row_labels = None
        self.__column_labels = None

        self.__scientific_notation = scientific_notation
        self.__precision = precision
        self.__round = round

        self.__unit = unit

    @property
    def array(self):
        return self.__array

    @array.setter
    def array(self, array:np.ndarray):
        assert array.ndim == 2

        if array.shape[0] != self.__array.shape[0]:
            self.row_labels = None
            self.__row_colors = [None for _ in range(self.array.shape[0])]

        if array.shape[1] != self.__array.shape[1]:
            self.column_labels = None
            self.__column_colors = [None for _ in range(self.array.shape[1])]

        self.__array = array

    @property
    def caption(self):
        return self.__caption

    @caption.setter
    def caption(self, caption:str):
        self.__caption = caption

    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label:str):
        self.__label = label

    @property
    def centering(self):
        return self.__centering

    @centering.setter
    def centering(self, centering:bool):
        self.__centering = centering

    @property
    def data_align(self):
        return self.__data_align

    @data_align.setter
    def data_align(self, data_align:str):
        assert data_align in self.__data_align_options, f"data alignment must be 'left', 'center', or 'right', is {data_align}"
        self.__data_align = data_align

    @property
    def label_align(self):
        return self.__label_align

    @label_align.setter
    def label_align(self, label_align:str):
        assert label_align in self.__data_align_options, f"label alignment must be 'left', 'center', or 'right', is {label_align}"
        self.__label_align = label_align

    @property
    def row_labels(self):
        return self.__row_labels

    @row_labels.setter
    def row_labels(self, row_labels:list[str]):
        assert len(row_labels) == self.array.shape[0]
        self.__row_labels = row_labels

    @property
    def column_labels(self):
        return self.__column_labels

    @column_labels.setter
    def column_labels(self, column_labels:list[str]):
        assert len(column_labels) == self.array.shape[1]
        self.__column_labels = column_labels

    @property
    def vline(self):
        return self.__vline

    @vline.setter
    def vline(self, vline:bool):
        self.__vline = vline

    @property
    def hline_top(self):
        return self.__hline_top

    @hline_top.setter
    def hline_top(self, hline_top:bool):
        self.__hline_top = hline_top

    @property
    def hline_bottom(self):
        return self.__hline_bottom

    @hline_bottom.setter
    def hline_bottom(self, hline_bottom:bool):
        self.__hline_bottom = hline_bottom

    @property
    def hline_header(self):
        return self.__hline_header

    @hline_header.setter
    def hline_header(self, hline_header:bool):
        self.__hline_header = hline_header

    @property
    def hline_rows(self):
        return self.__hline_rows

    @hline_rows.setter
    def hline_rows(self, hline_rows:bool):
        self.__hline_rows = hline_rows

    @property
    def bold_column_labels(self):
        return self.__bold_column_labels

    @bold_column_labels.setter
    def bold_column_labels(self, bold_column_labels:bool):
        self.__bold_column_labels = bold_column_labels

    @property
    def bold_row_labels(self):
        return self.__bold_row_labels

    @bold_row_labels.setter
    def bold_row_labels(self, bold_row_labels:bool):
        self.__bold_row_labels = bold_row_labels

    @property
    def scientific_notation(self):
        return self.__scientific_notation

    @scientific_notation.setter
    def scientific_notation(self, scientific_notation:bool):
        self.__scientific_notation = scientific_notation

    @property
    def precision(self):
        return self.__precision

    @precision.setter
    def precision(self, precision:int):
        self.__precision = precision

    @property
    def round(self):
        return self.__round

    @round.setter
    def round(self, round:bool):
        self.__round = round

    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, unit:str):
        self.__unit = unit

    def set_column_color(self, idx:int, color:str|None):
        self.__column_colors[idx] = color

    def set_row_color(self, idx:int, color:str|None):
        self.__row_colors[idx] = color

    def __get_row_color(self, row:int, column:int) -> str|None:
        assert 0 <= row < self.array.shape[0], "row index invalid"
        assert 0 <= column < self.array.shape[1], "column index invalid"

        if self.__column_colors[column] is not None:
            return self.__column_colors[column]

        elif self.__row_colors[row] is not None:
            return self.__row_colors[row]
        else:
            return None


    def __get_align_letter(self, align:str):
        if align == "center":
            return "c"
        elif align == "right":
            return "r"
        elif align == "left":
            return "l"
        else:
            raise AssertionError("If you're seeing this something is very wrong, alignment must be left, right or center")

    def __print_table_start(self):
        print("\\begin{table}")
        if self.centering:
            print("\t\\centering")

        print("\t\\caption{"+self.caption+"}")
        print("\t\\label{"+self.label+"}")
        print("\t\\begin{tabular}{", end="")

        if self.vline:
            print("|", end="")
        if self.row_labels is not None:
            print(self.__get_align_letter(self.label_align), end="")
            if self.vline:
                print("|", end="")

        print(self.array.shape[1]*self.__get_align_letter(self.data_align), end="")
        print("}")

    def __print_header(self):
        if self.column_labels is not None:
            if self.hline_top:
                print("\t\t\\hline")

            print("\t\t", end="")

            if self.row_labels is not None:
                print(" & ", end="")

            for i,label in enumerate(self.column_labels):
                if self.bold_column_labels:
                    print(r"\textbf{", end="")
                print(label, end="")
                if self.bold_column_labels:
                    print(r"}", end="")

                if i < len(self.column_labels) - 1:
                    print(" & ", end="")

            print(r"\\")
            if self.hline_header:
                print("\t\t\\hline")

    def __print_table_body(self):
        rowlabels = self.row_labels
        for i in range(self.array.shape[0]):
            print("\t\t", end="")
            if rowlabels is not None:
                if self.bold_row_labels:
                    print(r"\textbf{", end="")

                print(rowlabels[i], end="")

                if self.bold_row_labels:
                    print("}", end="")

                print(" & ", end="")

            for j, val in enumerate(self.array[i,:]):
                if self.__get_row_color(i, j) is not None:
                    print(r"\cellcolor{"+self.__get_row_color(i, j)+r"}", end="")

                print(r"\SI{", end="")

                if self.scientific_notation:
                    print(f"{val:.{self.precision}e}", end="")

                elif self.round:
                    print(f"{round(val, self.precision)}")
                else:
                    print(f"{val}", end="")

                print(r"}{"+self.unit+"}", end="")

                if j < (self.array.shape[1] - 1):
                    print(f" & ", end="")

            print(r"\\")

            if self.hline_rows and i < (self.array.shape[0] - 1):
                print("\t\t\\hline")

        if self.hline_bottom:
            print("\t\t\\hline")

    def __print_table_end(self):
        print("\t\\end{tabular}")
        print("\\end{table}")



    def print_table(self):
        self.__print_table_start()
        self.__print_header()
        self.__print_table_body()
        self.__print_table_end()

if __name__ == "__main__":
    a = np.array([[1,2,3,4,5],[6,7,8,9,10]])
    table= LatexTable(a)
    table.row_labels = ["row1", "row2"]
    table.column_labels = ["col1", "col2","col3","col4","col5"]
    table.set_row_color(-1, "lightgray")
    table.set_column_color(-1, "lightgray")
    table.scientific_notation = True
    table.print_table()

