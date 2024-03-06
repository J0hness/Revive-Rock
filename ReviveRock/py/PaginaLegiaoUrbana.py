import cherrypy

class PageLegiaoUrbana():
    page = open("./PaginaLegiaoUrbana.html").read()

    @cherrypy.expose()
    def index(self):
        html = self.page

        return html