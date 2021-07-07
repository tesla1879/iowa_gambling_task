import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="button click")
        self.set_border_width(10)
        list_box = Gtk.ListBox()
        list_box.set_selection_mode(Gtk.SelectionMode.NONE)
        self.add(list_box)

        # Checkbox
        row1 = Gtk.ListBoxRow()
        box1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=100)
        row1.add(box1)
        label = Gtk.Label("This is a test label for checkbox:")
        check = Gtk.CheckButton()
        box1.pack_start(label, True, True, 0)
        box1.pack_start(check, True, True, 0)
        list_box.add(row1)

        # Toggle
        row2 = Gtk.ListBoxRow()
        box2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=100)
        row2.add(box2)
        label = Gtk.Label("This is a test label for switch: ")
        switch = Gtk.Switch()
        box2.pack_start(label, True, True, 0)
        box2.pack_start(switch, True, True, 0)

        list_box.add(row2)

    def button_clicked(self, Widget):
        print("Game time")

    def add_label(self, Widget):
        print("button 2")



window = MainWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()