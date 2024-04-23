class TUI_Tool:
    def __init__(self):
        self.piece = ""
        self.tui_list = []
        self.tui_list_str = None
        self.line_name = []
        self.point_name = []
        self.array_name = []
        self.static_var_name = ["velocity magenitue",'x-velocity',"y-velocity",'z-velocity']
        self.var_var_name = [f"{self.piece}", f"molef-{self.piece}", f"concentration-{self.piece}"]

    def add_tui_list(self, tui_str):
        self.tui_list.append(tui_str)
        return self.tui_list

    def add_line_list(self, line_name):
        self.line_name.append(line_name)

    def add_point_list(self, point_name):
        self.point_name.append(point_name)

    def add_array_list(self, array_name):
        self.array_name.append(array_name)

    def create_plane_surface(self, name="plane_name", p="zx", value=0):
        """
        name:
        p: yz,zx,xy
        value:
        """
        tui_str = f"/surface/plane-surface {name} {p}-plane {value}"
        self.add_tui_list(tui_str)
        return tui_str

    def set_tui_version(self, ver="19.0"):
        tui_str = f'/file/set-tui-version "{ver}"'
        self.add_tui_list(tui_str)
        return tui_str

    def read_case_and_data(self, cas_name=""):
        tui_str = f'file/read-case-data "{cas_name}"'
        self.add_tui_list(tui_str)
        return tui_str

    def export_tecplot(self, tecplot_name="tec.plt", location=["line-1"],
                       vars=["sf6", "molef-sf6", "concentration-sf6"]):
        """
        :param tecplot_name:
        :param location:
        :param vars:
        :return:
        """
        tui_str = f'/file/export/tecplot "{tecplot_name}" '
        vars_str = ""
        location_str = ""
        for var in vars:
            vars_str += f"{var} "
        for loc in location:
            location_str += f'{loc} '
        tui_str += location_str + " () " + vars_str + "quit"
        self.add_tui_list(tui_str)
        return tui_str

    def set_iterate_num(self, num=1000):
        tui_str = f'solve/iterate {num}'
        self.add_tui_list(tui_str)
        return tui_str

    def create_array_points(self, x1, x2, y1, y2, z1, z2, count_num=10):
        x1 = round(x1, 4)
        x2 = round(x2, 4)
        y1 = round(y1, 4)
        y2 = round(y2, 4)
        z1 = round(z1, 4)
        z2 = round(z2, 4)
        array_name = f"array-x{x1}_{x2}-y{y1}_{y2}-z{z1}_{z2}"
        tui_str = f"/surface/point-array {array_name} {count_num} {round(x1, 4)} {round(y1, 4)}  {round(z1, 4)} {round(x2, 4)} {round(y2, 4)} {round(z2, 4)} "
        self.add_tui_list(tui_str)
        self.add_array_list(array_name)
        return tui_str

    def generate_jou(self, jou_name="jou.jou"):
        self.tui_list_str = ""
        for item in self.tui_list:
            self.tui_list_str += item + "\n"
        f = open(jou_name, "w")
        f.write(self.tui_list_str)
        f.close()

    def create_line(self, line_name="line", x1=0, y1=0, z1=0, x2=0, y2=0, z2=0):
        tui_str = f"/surface/line-surface {line_name} {x1} {y1} {z1} {x2} {y2} {z2} "
        self.add_tui_list(tui_str)
        self.add_line_list(line_name)
        return tui_str
