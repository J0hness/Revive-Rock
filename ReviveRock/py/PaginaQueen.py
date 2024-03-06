import cherrypy

class PageQueen():
    page = open("./PaginaQueen.html").read()

    @cherrypy.expose()
    def index(self):
        html = self.page

        return html