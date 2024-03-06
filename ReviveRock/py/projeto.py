import cherrypy
import os

from PaginaBeatles import PageBeatles
from PaginaElvis import PageElvis
from PaginaFooFighters import PageFooFighters
from PaginaJimiHendrix import PageJimiHendrix
from PaginaLed import PageLed
from PaginaLegiaoUrbana import PageLegiaoUrbana
from PaginaLinkinPark import PageLinkinPark
from PaginaMamonas import PageMamonas
from PaginaNirvana import PageNirvana
from PaginaPearlJam import PagePearlJam
from PaginaPinkFloyd import PagePinkFloyd
from PaginaPrincipal import PagePrincipal
from PaginaQueen import PageQueen
from portifolioJGD import PagePortifolioJGD
from portifolioJGM import PagePortifolioJGM
from portifolioJM import PagePortifolioJM
from portifolioVH import PagePortifolioVH
from portifolioJGS import PagePortifolioJGS

local_dir = os.path.dirname(__file__)

class Principal():
    topo = open("html/cabecalho.html").read()
    rodape = open("html/rodape.html").read()
    @cherrypy.expose()
    def index(self):
        html = self.topo
        html = html + '''<br/>
        <p>Aqui vai o conteúdo central da página inicial do projeto...</p>
        <p class="cor1">Home do Sistema Pet</p><br/>
        '''
        html = html + self.rodape

        return html

server_config={
'server.socket_host': '127.0.0.1',
'server.socket_port': 80
}
cherrypy.config.update(server_config)

#Para que o cherrypy possa encontrar os arquivos dentro do diretório da aplicação
local_config = {
    "/":{"tools.staticdir.on":True,
         "tools.staticdir.dir":local_dir},
}

#objetos utilizados para rota de navegação
root = Principal() #rota principal
root.especie = PaginaEspecie()
root.equipe = PaginaEquipe()
cherrypy.quickstart(root,config=local_config)
