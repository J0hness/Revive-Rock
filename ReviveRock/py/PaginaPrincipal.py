import cherrypy

class PagePrincipal():
    page = open("./PaginaPrincipal.html").read()

    @cherrypy.expose()
    def index(self):
        html = self.page

        return html