import cherrypy

class PagePortifolioJGM():
    page = open("./portifolioJGM.html").read()

    @cherrypy.expose()
    def index(self):
        html = self.page

        return html