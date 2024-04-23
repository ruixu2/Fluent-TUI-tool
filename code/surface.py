from TUI_tool import TUI_Tool


class Surface(TUI_Tool):
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
