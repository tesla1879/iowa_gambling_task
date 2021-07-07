import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="button click")
        self.box = Gtk.Box(10)
        self.add(self.box)
        # Button
        self.button = Gtk.Button(label="button")
        self.button.connect("clicked", self.button_clicked)
        self.box.pack_start(self.button, True, True, 0)


        self.button2 = Gtk.Button(label="add label")
        self.button2.connect("clicked", self.add_label)
        self.box.pack_start(self.button2, True, True, 0)
        # self.add(self.button)


    def button_clicked(self, Widget):
        print("Game time")

    def add_label(self, Widget):
        self.label = Gtk.Label()
        self.label.set_label("this is a test label")
        self.add(self.label)



window = MainWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()