class TUI_tool():
    def create_plane_surface(name="plane_name",p="zx",value=0):
        """
        name:
        p: yz,zx,xy
        value:
        """
        tui_str=f"/surface/plane-surface {name} {p}-plane {value}"
        return tui_str
    def set_tui_version(ver="19.0"):
        tui_str=f'/file/set-tui-version "{ver}"'
        return tui_str
    def read_case_and_data(cas_name=""):
        tui_str=f'file/read-case-data "{cas_name}"'
    def export_tecplot():
        pass
    def set_iterate_num(num=1000):
        tui_str=f'solve/iterate {num}'
        return tui_str