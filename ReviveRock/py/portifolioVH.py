import cherrypy

class PagePortifolioVH():
    page = open("./portifolioVH.html").read()

    @cherrypy.expose()
    def index(self):
        html = self.page

        return html