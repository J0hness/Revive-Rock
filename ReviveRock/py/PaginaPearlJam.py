import cherrypy

class PagePearlJam():
    page = open("./PaginaPearlJam.html").read()

    @cherrypy.expose()
    def index(self):
        html = self.page

        return html