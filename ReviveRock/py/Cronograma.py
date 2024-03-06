import cherrypy

class PageCronograma():
    page = open("./Cronograma.html").read()

    @cherrypy.expose()
    def index(self):
        html = self.page

        return html