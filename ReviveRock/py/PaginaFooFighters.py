import cherrypy

class PageFooFighters():
    page = open("./PaginaFooFighters.html").read()

    @cherrypy.expose()
    def index(self):
        html = self.page

        return html