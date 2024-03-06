import cherrypy

class PagePortifolioJGS():
    page = open("./portifolioJGS.html").read()

    @cherrypy.expose()
    def index(self):
        html = self.page

        return html