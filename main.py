import pygtk, gtk

class Window1:
    """ This is just a test function """
    def __init__(self):
        self.gladefile = "myultimate.glade"
        self.builder = gtk.Builder()
        self.builder.add_from_file(self.gladefile)
        
        dic = { "on_btnQuit_clicked": self.btnQuit_clicked,
                "on_btnOpen_clicked": self.btnOpen_clicked
             }
        self.builder.connect_signals(dic)
        self.window = self.builder.get_object("window1")
        self.window.show_all()
        if (self.window):
            self.window.connect("destroy", gtk.main_quit)

    def btnQuit_clicked(self, widget):
        gtk.main_quit()

    def btnOpen_clicked(self, widget):
        print "btnOpen_clicked is clicked"


if __name__ == "__main__":
    app = Window1()
    gtk.main()
