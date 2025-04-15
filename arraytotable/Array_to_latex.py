import numpy as np


class LatexTable:
    __array: np.ndarray
    __caption: str
    __label: str
    __centering: bool
    __data_align: str
    __label_align: str

    __row_labels = list[str] | None
    __column_labels = list[str] | None

    def __init__(self, array:np.ndarray, centering:bool=True, caption:str='caption', label:str='tab:my-label', data_align:str="center", label_align:str="left"):
        self.__array = array
        self.__caption = caption
        self.__label = label
        self.__centering = centering

        self.__data_align = data_align
        self.__label_align = label_align
        self.__data_align_options = ["left", "center", "right"]

        self.__row_labels = None
        self.__column_labels = None

    @property
    def array(self):
        return self.__array

    @array.setter
    def array(self, array:np.ndarray):
        assert array.ndim == 2

        if array.shape[0] != self.__array.shape[0]:
            self.row_labels = None

        if array.shape[1] != self.__array.shape[1]:
            self.column_labels = None

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

        if self.row_labels is not None:
            print(self.__get_align_letter(self.label_align), end="")

        print(self.array.shape[1]*self.__get_align_letter(self.data_align), end="")
        print("}")

    def __print_header(self):
        if self.column_labels is not None:
            print("\t\t", end="")

            if self.row_labels is not None:
                print("&", end="")

            for i,label in enumerate(self.column_labels):
                print(label, end="")

                if i < len(self.column_labels) - 1:
                    print("&", end="")

            print(r"\\")

    def __print_table_body(self):
        rowlabels = self.row_labels
        for i in range(self.array.shape[0]):
            print("\t\t", end="")
            if rowlabels is not None:
                print(rowlabels[i]+"&", end="")
            for j, val in enumerate(self.array[i,:]):
                print(f"{val}", end="")
                if j < (self.array.shape[1] - 1):
                    print(f"&", end="")
            print(r"\\")

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
    table.print_table()

