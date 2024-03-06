import cherrypy

class Pageindex():
    page = open("./index.html").read()

    @cherrypy.expose()
    def index(self):
        html = self.page

        return html