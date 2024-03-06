import cherrypy

class PagePortifolioJGD():
    page = open("./portifolioJGD.html").read()

    @cherrypy.expose()
    def index(self):
        html = self.page

        return html