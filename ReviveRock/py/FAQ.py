import cherrypy

class PageFAQ():
    page = open("./FAQ.html").read()

    @cherrypy.expose()
    def index(self):
        html = self.page

        return html