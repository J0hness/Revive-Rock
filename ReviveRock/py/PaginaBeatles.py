import cherrypy

class PageBeatles():
    page = open("./PaginaBeatles.html").read()

    @cherrypy.expose()
    def index(self):
        html = self.page

        return html