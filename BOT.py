########################################################################################################################
#                                   BOT DE ADVENTURE GAME PARA DISCORD COM DISCORD.PY                                  #
########################################################################################################################

#Usar python 3.6 ou inferior - incompatibilidade com python 3.7.
#Inompatibilidade com rewrite usado o async.
#Ultima modificação: 23/09/2018.


import discord   #API do discord.
import chave     #Função que retorna o token do bot.
import asyncio
import random


TOKEN = chave.token()             #Chama a funçao que tem o token e armazena o resultado na variavel.
client = discord.Client()         #Importa o metodo Client da api do discord e atribui o nome "client".



#Colocar as variaveis e funções aqui - elas serao chamadas dependendo do que o usuario diigitar

historia ="""Aqui voce coloca o bloco de historia do seu jogo"""   #nomei a variavel como quiser mas evite nomes iguais


inicio ="""Deseja começar o jogo: !Sim  !Não"""     #Lembre-se de dar alternativas para que possam chamar outro bloco


#Colocar aqui as funções do bot.

@client.event               #chama os eventos gerados pelo usuario.
async def on_ready():       #funçao propria da API - Gera alteraçoes no back end.
    print('BOT ONLINE')     #imprime uma mensagem de confirmaçao para o bot.



@client.event
async def on_message(message):         #funçao propria da API - Gera alteraçoes no servidor do usuario.

    if message.content.lower().startswith('!jogar'):       #Checa a entrada do usuario deu e  faz um tratamento de erro
        await client.send_message(message.channel, inicio)     #Envia uma resposta ao usuario - neste caso uma variavel

    if message.content.lower().startswith('!sim'):
        await client.send_message(message.channel, historia)



client.run(TOKEN)  #inicia o bot e passa como paramentro o token do bot.

########################################################################################################################
