import pygtk
import gtk
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///database.sqlite', echo=True)
Session = sessionmaker(bind=engine)


class Anime(Base):
    __tablename__ = 'Anime'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    tags = Column(String)
    plot = Column(String)
    star = Column(Integer)

    def __repr__(self):
        return self.name


class Window1:
    """ This is just a test function """

    def __init__(self):
        self.session = Session()
        self.gladefile = "myultimate.glade"
        self.builder = gtk.Builder()
        self.builder.add_from_file(self.gladefile)

        dic = {"on_btnQuit_clicked": self.btnQuit_clicked,
               "on_btnSave_clicked": self.btnSave_clicked}

        self.gtkName = self.builder.get_object('txtboxName')
        self.gtkTags = self.builder.get_object('txtboxTags')
        self.gtkPlot = self.builder.get_object('txtboxPlot')
        self.gtkStar = self.builder.get_object('txtboxStar')

        self.builder.connect_signals(dic)
        self.window = self.builder.get_object("window1")
        self.window.show_all()
        if (self.window):
            self.window.connect("destroy", gtk.main_quit)

    def get_plot(self):
        self.start = self.gtkPlot.get_buffer().get_start_iter()
        self.end = self.gtkPlot.get_buffer().get_end_iter()
        self.textbuffer = self.gtkPlot.get_buffer().get_text(
            self.start,
            self.end)
        self.plot = unicode(self.textbuffer, "utf-8")
# putting it back self.backTobytes = u.encode(self.textbuffer, "utf-8")
        return self.plot

    def btnSave_clicked(self, widget):
        self.anime_on_session = Anime(
             name=self.gtkName.get_text(),
             tags=self.gtkTags.get_text(),
             plot=self.get_plot(),
             star=self.gtkStar.get_text()
        )
        self.session.add(self.anime_on_session)
        print "Saving to database..."
        self.session.commit()

    def btnQuit_clicked(self, widget):
        self.anime_on_db = self.session
        for name, plot in self.anime_on_db.query(Anime.name, Anime.plot):
            print "anime name: %s" % name
            print "anime plot: %s" % plot
#        gtk.main_quit()


if __name__ == "__main__":
    app = Window1()
    #Base.metadata.create_all(engine)
    gtk.main()
