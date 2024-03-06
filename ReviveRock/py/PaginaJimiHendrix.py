import cherrypy

class PageJimiHendrix():
    page = open("./PaginaJimiHendrix.html").read()

    @cherrypy.expose()
    def index(self):
        html = self.page

        return html