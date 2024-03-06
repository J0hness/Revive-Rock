import cherrypy

class PageElvis():
    page = open("./PaginaElvis.html").read()

    @cherrypy.expose()
    def index(self):
        html = self.page

        return html