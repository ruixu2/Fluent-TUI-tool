class TUI_Tool:
    @staticmethod
    def create_plane_surface(name="plane_name", p="zx", value=0):
        """
        name:
        p: yz,zx,xy
        value:
        """
        tui_str = f"/surface/plane-surface {name} {p}-plane {value}"
        return tui_str

    @staticmethod
    def set_tui_version(ver="19.0"):
        tui_str = f'/file/set-tui-version "{ver}"'
        return tui_str

    @staticmethod
    def read_case_and_data(cas_name=""):
        tui_str = f'file/read-case-data "{cas_name}"'
        return tui_str

    @staticmethod
    def export_tecplot():
        pass

    @staticmethod
    def set_iterate_num(num=1000):
        tui_str = f'solve/iterate {num}'
        return tui_str

    @staticmethod
    def create_array_points(x1, x2, y1, y2, z1, z2, count_num=10):
        x1 = round(x1, 4)
        x2 = round(x2, 4)add
        y1 = round(y1, 4)
        y2 = round(y2, 4)
        z1 = round(z1, 4)
        z2 = round(z2, 4)
        array_name = f"array-x{x1}_{x2}-y{y1}_{y2}-z{z1}_{z2}"
        tui_str = f"/surface/point-array {array_name} {count_num} {round(x1, 4)} {round(y1, 4)}  {round(z1, 4)} {round(x2, 4)} {round(y2, 4)} {round(z2, 4)} "
        return tui_str
