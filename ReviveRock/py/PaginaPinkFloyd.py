import cherrypy

class PagePinkFloyd():
    page = open("./PaginaPinkFloyd.html").read()

    @cherrypy.expose()
    def index(self):
        html = self.page

        return html