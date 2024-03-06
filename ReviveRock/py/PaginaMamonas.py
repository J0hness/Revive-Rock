import cherrypy

class PageMamonas():
    page = open("./PaginaMamonas.html").read()

    @cherrypy.expose()
    def index(self):
        html = self.page

        return html