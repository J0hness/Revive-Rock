import cherrypy

class PageNirvana():
    page = open("./PaginaNirvana.html").read()

    @cherrypy.expose()
    def index(self):
        html = self.page

        return html