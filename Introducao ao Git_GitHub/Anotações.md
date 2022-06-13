#Introdução ao Git
##Entendendo o que é Git e sua importância
<ol>
 <li>Foi criado em 2015 - repositório de versões de código. Criar e monitorar diversas versões de nossos códigos.</li>
 <li>Software é colaborativo - não é trabalho de um homem só.</li>
 <li>Git ≠ GitHub</li>
 <li>Benefícios</li>
	<ol>
		<li>Controle de versão</li>
		<li>Armazenamento em nuvem</li>
		<li>Trabalho em equipe</li>
		<li>Melhorar seu código</li>
		<li>Reconhecimento</li>
	</ol>
</ol>

##Navegação via command line interface e instalação
<ol>
###Comandos básicos para um bom desempenho no terminal
	<ol>
		<li>Não tem interface gráfica - linha de comando.</li>
		<li>Comandos WIN</li>
			<ol>
				<li>Listar pastas: dir</li>
				<li>Ir para uma pasta específica: cd</li>
				<li>cd / → vai para raiz</li>
				<li>cd nome_da_pasta → vai para a pasta</li>
				<li>cd .. → retorna ao diretório acima</li>
				<li>limpar tela → cls</li>
				<li>Tecla TAB → auto completa o nome das pastas e arquivos</li>
				<li>Criar pastas → mkdir</li>
				<li>Criar arquivos → echo texto > nome_do_arquivo.extensão</li>
				<li>Deletar arquivos dentro da pasta → del nome_da_pasta</li>
				<li>Remover diretórios → rmdir nome_da_pasta /S /Q</li>
				<li>Ajuda do comando: nome_do_comando /?</li>
			</ol>
	</ol>
			
###Realizando a instalação do GIT
 - Aula prática

##Entendendo como o GIT funciona por baixo dos panos
###Tópicos fundamentais para entender o funcionamento do GIT
<ol>
	<li>SHA1</li>
		<ol>
			<li>A sigla SHA significa Secure Hash Algorithm (Algoritmo de Hash Seguro), é um conjunto de funções hash criptográficas projetadas pela NSA (Agência de Segurança Nacional dos EUA.</li>
			<li>A encriptação gera conjunto de caracteres identificador de 40 dígitos. É único.</li>
			<li>É uma forma curta de representar um arquivo. </li>
		</ol>
	<li>Objetos internos do GIT</li>
		<ol>
			<li>Objetos Fundamentais</li>
				<ol>
					<li>BLOB</li>
						<ol>
							<li>Bloco básico de composição</li>
							<li>Contém metadados dentro dele</li>
							<li>SHA1; Tipo do objeto (BLOB); tamanho; \0; conteúdo do objeto</li>
							<li>comando correto para retornar a string criptografada de um BLOB:</li>
								<ol>
									<li>usando git hash: echo ‘conteudo’ | git hash-object –stdin</li>
									<li>usando sha1: echo -e ‘blob 9\0conteudo’ | openssl sha1</li>
								</ol>
						</ol>		
					<li>TREE</li>
						<ol>
							<li>Monta a estrutura de onde estão localizados os arquivos. Aponta para Blobs ou outras Trees.</li>
							<li>SHA1; Tipo do objeto (TREE); tamanho; \0; caminho do arquivo</li>
							<li>Se mudar uma estrutura de um arquivo, muda-se a encriptação de toda a árvore.</li>
						</ol>
					<li>COMMIT</li>
						<ol>
							<li>Junta tudo, dá sentido para as alterações que são feitas.</li>
							<li>Aponta para a tree, para o “parente”, para o autor e para a mensagem. Tem um carimbo de tempo (timestamp).</li>
							<li>Commit também possui SHA1 → ele é o hash de toda a informação. Se altera o blob, altera a tree e altera o commit.</li>
							<li>Linha do tempo → o parente é o commit anterior.</li>
							<li>Commit é único para cada autor.</li>
						</ol>
				</ol>		
			<li>Sistema distribuído seguro
				<ol>
					<li>O código hosteado na nuvem. Estado final do código. Versão mais atualizada. Na máquina de todos os colaboradores tem o mesmo código. Todas as versões são confiáveis.</li>
				</ol>
			<li>Chave SSH e Token</li>
				<ol>
					<li>Autenticação (para passar do Git para o GitHub) → nome de usuário e senha. Esse tipo de autenticação foi desligada. </li>
					<li>Chave SSH → é uma forma de estabelecer uma conexão segura e encriptada entre duas máquinas. </li>
					<li>Servidor do GitHub → máquina local.</li>
					<li>Clicar em Chave SSH para clonar o repositório</li>

				</ol>
			<li>Comandos para criar a chave SSH</li>
				<ol>
					<li>ssh-keygen -t ed25519 -C e-mail (igual ao do GitHub)</li>
					<li>entrar na pasta .ssh com cd</li>
					<li>cat (chave pública) → dar ls para ver o nome</li>
					<li>eval $(ssh-agent -s)</li>
					<li>ssh-add (id privado) → fazer esse comando sempre que entrar no computador, dentro da pasta do ssh.</li>
					
				</ol>
		</ol>	
</ol>

 - OBS: Os comandos no Git são diferentes dos que ele ensinou


###Token: para clonar em HTTPS.

#Primeiros comandos com GIT
##Iniciando o Git e criando um commit
<ol>
	<li>git init → inicia um diretório de repositório do git.</li>
	<li>git config → configuração de arquivos dentro do repositório</li>
	<ol>
		<li>comando completo: git config - -global user.email “e-mail”.</li>
		<li>segundo comando: git config –global user.name “nome”.</li>
	</ol>
	<li>git add → para começar a adicionar um commit
	<li>git commit</li>
	<li>comando completo: git commit -m “commit inicial” (neste texto, coloca-se as versões que vão sendo criadas).</li>
	
</ol>

 - OBS: Os comandos no Git são diferentes dos que ele ensinou
 <ol>
	<li>LS → listar</li>
	<li>cd nome_da_pasta</li>
	<li>CTRL+L → limpar (ou clear)</li>
	<li>ls -a → mostrar arquivos ocultos</li>
	<li>mv → mover arquivo</li>

#Ciclo de vida dos arquivos no GIT
##Passo a passo no ciclo de vida
<ol>
	<li>Git add → move o arquivo Untraked para Staged.</li>
	<li>git add * → pega todos os arquivos que precisam ser modificados.</li>
	<li>Unmodified para modified → quando modificamos (editamos) o arquivo. O git compara os SHA1 e faz essa mudança.</li>
	<li>Quando o arquivo está Modified e damos um git add, ele passa para o Staged.</li>
	<li>Se deletar um arquivo Unmodified, ele passa para o estado Untraked.</li>
	<li>Um arquivo que está no estado Staged quando recebe o comando commit passa a ser um arquivo Unmodified, e começa o ciclo novamente.</li>
	<li>Remote repository → GitHub</li>
	<li>Ambiente de desenvolvimento → tudo o que está na máquina local.</li>
	<li>Os arquivos vão ficar sempre alterando entre o Staging Area e o Working Directory. Quando se faz um commit, o arquivo passa a integrar o Repositório Local.</li>
	<li>git status → monitora o status do arquivo no repositório.</li>
</ol>
#Introdução ao GitHub
##Trabalhando com o GitHub
<ol>
	<li>git remote add origin (nome que se dá ao repositório) url (copiar e colar do GitHub).</li>
	<li>git remote -v → mostra a lista de repositórios remotos.</li>
	<li>git push origin master → para colocar o repositório local no remoto.</li>
	<li>Se não der certo, reiniciar a chave ssh.</li>
	<li>git pull origin master → para puxar os arquivos do repositório remoto para o local.</li>
</ol>

#Resolvendo conflitos
##Como os conflitos acontecem no GitHub e como resolvê-los
<ol>
	<li>Conflito MERGE → quando a alteração é feita na mesma linha do código. É necessário abrir os dois arquivos e resolver o conflito manualmente.</li>
	<li>Commita o arquivo novamente</li>
	<li>git clone (url do github) → para clonar um repositório para a máquina local.</li>
</ol>