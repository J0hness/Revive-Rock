import cherrypy

class PagePortifolioJM():
    page = open("./portifolioJM.html").read()

    @cherrypy.expose()
    def index(self):
        html = self.page

        return html