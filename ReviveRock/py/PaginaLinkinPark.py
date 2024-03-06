import cherrypy

class PageLinkinPark():
    page = open("./PaginaLinkinPark.html").read()

    @cherrypy.expose()
    def index(self):
        html = self.page

        return html