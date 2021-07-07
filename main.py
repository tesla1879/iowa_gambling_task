import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="button click")
        self.grid = Gtk.Grid()
        self.add(self.grid)
        # Button
        self.button = Gtk.Button(label="button")
        self.button.connect("clicked", self.button_clicked)
        self.button2 = Gtk.Button(label="add label")
        self.button2.connect("clicked", self.add_label)
        # self.add(self.button)

        self.grid.add(self.button)
        self.grid.attach_next_to(self.button2, self.button, Gtk.PositionType.RIGHT, 1, 7)

    def button_clicked(self, Widget):
        print("Game time")

    def add_label(self, Widget):
        print("button 2")



window = MainWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()