import cherrypy

class PageLed():
    page = open("./PaginaLed.html").read()

    @cherrypy.expose()
    def index(self):
        html = self.page

        return html