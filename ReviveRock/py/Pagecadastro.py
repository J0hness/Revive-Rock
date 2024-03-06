import cherrypy
from classes.especie import *

class PaginaEspecie():
    topo = open("html/cabecalho.html").read()
    rodape = open("html/rodape.html").read()

    @cherrypy.expose()
    def index(self):
        return self.montaFormulario()

    def montaFormulario(self, pId=0, pBanda='', pEstilo='', pLink='', pFoto=''):
        html = self.topo
        html += '''
                <h2>Cadastro de Bandas</h2>
                <form name="FormCadastro" action="gravarBanda" method="post">
                <p>
                 <input type="hidden" id="txtId" name="txtId" value="%s"/>
        		 <label for="txtBanda">Banda</label>
                 <br/>
                 <input type="text" id="txtBanda" name="txtBanda" value="%s" size="30" maxlength="30" required="required"/>
                 <br/>
        		 <label for="txtEstilo">Estilo Musical</label>
                 <br/>
                 <input type="text" id="txtEstilo" name="txtEstilo" value="%s" size="20" maxlength="20" required="required"/>
                </p>
                <br/>
                <form name="FormCadastro" action="gravarBanda" method="post">
                <p>
                 <input type="hidden" id="txtLink" name="txtLink" value="%s"/>
        		 <label for="txtLink">Link</label>
        		 <br/>
        		 <form name="FormCadastro" action="gravarBanda" method="post">
                <p>
                 <input type="hidden" id="txtFoto" name="txtFoto" value="%s"/>
        		 <label for="txtFoto">Foto</label>
        		 <br/>
                <input type="submit" id="btnGravar" name="btnGravar" value="Gravar"/>
                </form>
                ''' % (pId, pBanda, pEstilo,pLink,pFoto)
        html+= self.montaTabela()
        html+= self.rodape
        return html

    def montaTabela(self):
        html = '''<table class="alinha">
                    <tr>
                       <th> ID </th>
                       <th> Banda </th>
                       <th> Estilo </th>
                       <th> Link </th>
                       <th> Foto </th>
                    </tr>'''
        objArtistas = Artistas() # criando um objeto do tipo Especie
        dados = objArtistas.obterArtistas() # lista com os dados  do SQL
        for esp in dados:
            html += '''<tr>
                         <td> %s </td>
                         <td> %s </td>
                         <td> %s </td>
                         <td style="text-align:center">
                          <a href="alterarArtistas?idEsp=%s">[Alterar]</a>
                          <a href="excluirArtistas?idEsp=%s">[Excluir]</a>  
                         </td>
                       </tr> ''' % (esp["ID"],esp["Nome"],esp["Estilo"],esp["Link"],esp["Foto"])

        html += '</table> <br/> <br/>'
        return html

    @cherrypy.expose()
    def gravarEspecie(self,txtId,txtBanda,txtEstilo,txtLink,txtFoto,btnGravar):
        if len(txtBanda)>0:
            objArtistas = Artistas()
            objArtistas.set_descricao(txtBanda)
            objArtistas.set_origem(txtEstilo)
            objArtistas.set_origem(txtLink)
            objArtistas.set_origem(txtFoto)

            retorno = 0 # variável para controlar o sucesso!!
            if int(txtId) == 0: # novo registro no banco
                retorno = objArtistas.gravar()
            else: # gravar a alteração de um registro
                # neste caso da alteração a gente precisa carregar o id no objeto, quanto é uma nova espécie não precisa porque o id é gerado de forma automática
                objArtistas.set_id(int(txtId))
                retorno = objArtistas.alterar()
            if retorno > 0:
                return '''
                    <script>
                       alert("A espécie %s foi gravada com sucesso!!");
                       window.location.href = "/especie"
                    </script>
                ''' % (txtBanda)
            else:
                return '''
                   <h2>Erro ao gravar a espécie <b>%s</b>. </h2>
                   <a href="/">voltar</a> 
                '''  % (txtBanda)
        else: #if len(txtDescr)>0:
            return '''
               <h2>A descrição da espécie deve ser informada.</h2>
               <a href="/">voltar</a> 
            '''

    @cherrypy.expose()
    def excluirEspecie(self,idEsp):
        objArtistas = Artistas()
        objArtistas.set_id(int(idEsp))
        if objArtistas.excluir() > 0:
            raise cherrypy.HTTPRedirect('/especie')
        else:
            return '''
            <h2> Não foi possível excluir a espécie!!</h2>
            [<a href="/">Voltar</a>]
            '''

    @cherrypy.expose()
    def alterarEspecie(self, idEsp):
        objArtistas = Artistas()
        # estamos buscando o objeto com os dados que foram passados por parâmetro neste método
        dadosArtistasSelec = objArtistas.obterArtistas(idEsp)
        # chamando o método para montar o formulário com os valores do banco de dados nos campos do formulário
        return self.montaFormulario(dadosArtistasSelec[0]['esp_id'],
                          dadosArtistasSelec[0]['esp_banda'], dadosArtistasSelec[0]['esp_origem'])