# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 22:49:12 2023

"""
from graphics import *
from math import *
import random
import time

aleatorio = False

def txt(texto,x,y,tamanho,estilo,win):
    '''Função para escrever texto personalizado mais facilmente'''
    txt= Text(Point(x,y),texto)
    txt.setFace('helvetica'), txt.setSize(tamanho), txt.setStyle(estilo), txt.draw(win)
    
class botao:
    '''Função que constrói botões na janela gráfica'''
    def __init__(self,x1,y1,x2,y2,texto,win):
        self.xmin, self.xmax, self.ymin, self.ymax= min(x1,x2), max(x1,x2), min(y1,y2), max(y1,y2)
        self.botao = Rectangle(Point(x1,y1), Point(x2,y2))
        self.botao.setWidth(2), self.botao.setFill("grey")
        self.botao.draw(win)
        txt= Text(Point((x1+x2)/2,(y1+y2)/2),texto)
        txt.setFace('helvetica'), txt.setSize(16), txt.setStyle('bold italic'), txt.draw(win)
    def ativar(self,x,y):   #Deteta quando o botão é clicado
        if self.xmin <= x <= self.xmax and self.ymin <= y <= self.ymax:
            return True
 
def menu():
    """
    Função que abre o menu
    """
    ficheiro = open("menu.txt", "r")
    linhas = ficheiro.readlines()
    ficheiro.close()
    
    janela = linhas[1].split()
    nome_da_janela = linhas[4]
    
    win=GraphWin(nome_da_janela,janela[0],janela[1])
    win.setCoords(0.0,0.0,100.0,100.0)
    txt('Restaurant Robot Cleaner', 50, 94, 23, 'bold italic', win)
    txt('Menu', 50, 89, 18, 'bold italic', win)
    botoes(win)
    
def botoes(win):
    """
    Função para o utilizador poder escolher que nivel quer através dos botões
    utilização do while para o programa não falhar caso o utilizador carregue fora das areas delimitadas pelos botões
    """
    botao1, botao2, botao3, botao_inf, botao_sair= botao(20,80,80,65,'Nível 1',win), botao(20,60,80,45,'Nível 2',win), botao(20,40,80,25,'Nível 3',win), botao(20,20,47.5,5,'Informações',win), botao(52.5,20,80,5,'Terminar',win)
    while True:
        clique = win.getMouse()
        x,y = clique.getX(),clique.getY()
        if botao1.ativar(x,y):
            win.close()
            nivel=1
            nivel1(nivel)
        elif botao2.ativar(x,y):
            win.close()
            nivel=2
            nivel2(nivel)
        elif botao3.ativar(x,y):
            win.close()
            nivel=3
            menu_nivel3_obstaculos(nivel)
        elif botao_inf.ativar(x,y):
            win.close(), informaçoes()
        elif botao_sair.ativar(x,y):
            win.close()
            
def informaçoes():
    '''Função que desenha a janela gráfica de Informações'''
    win=GraphWin('Informações',600,800)
    win.setCoords(0.0,0.0,100.0,100.0)
    txt('Informações',50,90,25,'bold italic', win)
    txt('Projeto Final de Fundamentos da Programação',50,70,16,'bold italic', win)
    txt('Instituto Superior Técnico 2022/2023',50,65,13,'bold italic', win)
    Image(Point(50,50),'image003 (1).gif').draw(win)
    txt('Realizado por:',50,35,13,'bold italic', win)
    txt('105995 - João Miguel',50,31,12,'bold italic', win)
    txt('106426 - Pedro Rosa',50,28,12,'bold italic', win)
    txt('Instituto Superior Técnico 2022/2023',50,65,13,'bold italic', win)
    botao1= botao(20,10,80,17,'Voltar',win)
    while True:
        clique = win.getMouse()
        x,y = clique.getX(),clique.getY()
        if botao1.ativar(x,y):
            win.close()
            menu()
                      
def botoes_nivel3_obstaculos(win):
    """
    função para o utilizador poder escolher que nivel quer através dos botões
    utilização  while para o programa não falhar caso o utilizador carregue fora das areas delimitadas pelos botões
    """
    botao1=botao(20,60,80,75,'Gerar obstáculos através do bloco de notas',win)
    botao2=botao(20,40,80,55,'Gerar obstáculos aleatoriamente',win)
    botao3=botao(20,25,80,35,'Voltar',win)
    while True:
        clique = win.getMouse()
        x = clique.getX()
        y= clique.getY()
        if botao1.ativar(x,y):
            win.close()
            menu_nivel3_sujidade(3,[],aleatorio)
        elif botao2.ativar(x,y):
            win.close()
            menu_nivel3_tipo_obstáculos(3) 
        elif botao3.ativar(x,y):
            win.close()
            menu()
            
def detetor_do_rato1(win,robot,nivel,x = None,y = None):
    """
    função que deteta se o utilizador carrega na barra de tarefas ou na sala do restaurante
    """
    if x is None or y is None: #esta função permite que o utilizador apenas tenha que carregar uma vez caso tenha carregado na barra antes
        while True:
            clique = win.getMouse()
            x,y = clique.getX(),clique.getY()
            if 86 <= y:
                botoes_da_barra1(win,x,y,robot,nivel)
            else:
                ir_limpar(x, y, win,robot,nivel)
                led('esquerda','red',win)
    else:
        while True:
            if 86 <= y:
                botoes_da_barra1(win,x,y,robotnivel)
            else:
                ir_limpar(x, y, win,robot,nivel)
                led('esquerda','red',win)
                
def botoes_da_barra1(win,x,y,robot,nivel):
    """
    Botões que fazem sair dos niveis e voltar para o menu e para começar o programa
    """ 
    while True:
        if 68 <= x <= 98 and 88 <= y <= 98:
            win.close()
            menu()
        elif y <= 86:
            ir_limpar(x, y, win,robot,nivel) #para caso o utilizador volte a carregar do restaurante
        else:
            clique = win.getMouse()
            x,y = clique.getX(),clique.getY()
            detetor_do_rato1(win,robot,nivel)

def ir_buscar_coordenadas_sujidade(win,inicio,nivel):
    """
    função que cria uma lista com as coordenadas das sujidades
    """
    # Verifica o nível de sujidade para determinar qual arquivo será aberto
    if nivel == 1:
        ficheiro = open("nivel1.txt", "r")
    else:
        ficheiro = open("Limpeza.txt", "r")
    linhas = ficheiro.readlines()
    ficheiro.close()
    fim = len(linhas) # Determina o número de linhas a serem processadas
    coordenadas_de_sujidade = []  # Cria uma lista vazia para armazenar as coordenadas das sujidades
    for linha in range(inicio, fim):    
        # separar a linha em números individuais
        numeros_na_linha = linhas[linha].split()
        for n in numeros_na_linha:
            coordenadas_de_sujidade.append(float(n))  # Converte o número para float e adiciona à lista de coordenadas_de_sujidade
    return coordenadas_de_sujidade

def ir_limpar(x,y,win,robot,nivel):
    """
    Função que manda o robot para onde o utilizador carregou
    """
    led('esquerda','red',win)
    #tirar o número de sujidades e as suas coordenadas
    ficheiro = open("nivel1.txt", "r")
    linhas = ficheiro.readlines()
    ficheiro.close()
    fim = len(linhas)
    coor = ir_buscar_coordenadas_sujidade(win,7,nivel)
    lista = []
    i=0
    for linha in range(7, fim):
        #criar uma lista de quantos pontos há
        lista.append(int(i))
        i+=1
    verificar_se_limpou(x,y,robot,win,lista,coor,nivel)
    fim_do_nivel(win)

def verificar_se_limpou(x,y,robot,win,lista,coor,nivel):
    """
    loop para o robot só voltar para a base quando tiver limpo todas as sujidades
    """
    limpo=[] #lista de pontos de sujidade já limpas
    while set(lista) != set(limpo): #enquanto o robot não limpar todas as sujidades
        if y < 86-3.1 and not(52-3.1<=x<=64+3.1 and 36-3.1<=y<=47+3.1) and 3.1<x and x<100-3.1 and y>3.1:
            desviar_obstaculo(x,y,robot,nivel,aleatorio), robot.mover(x, y)
        elif not(y>= 86):
            carrega_perto_da_mesa(x, y,robot,nivel)
            x,y = carrega_perto_da_mesa(x, y,robot,nivel)
        robot=deteta_e_limpa(limpo,x,y,coor,robot,win,nivel)
        if set(lista) == set(limpo):
            break
        clique = win.getMouse()
        x,y = clique.getX(),clique.getY()
        if 68 <= x <= 98 and 88 <= y <= 98:
            win.close(), menu()
        elif y < 86-3.1 and not(52-3.1<=x<=64+3.1 and 36-3.1<=y<=47+3.1) and 3.1<x and x<100-3.1 and y>3.1:
            desviar_obstaculo(x,y,robot,nivel,aleatorio), robot.mover(x, y)
        carrega_perto_da_mesa(x, y, robot,nivel)
    if x <= 50:
        voltar_x = 5
    else:
        voltar_x = 95
    desviar_obstaculo(voltar_x,43,robot,nivel,aleatorio), robot.ir_para_docking_station(win)

def deteta_e_limpa(limpo,x,y,coor,robot,win,nivel):
    for n in range(0,len(coor)-1,2):
        if ((coor[n]-6)<x<(coor[n]+6)) and ((coor[n+1]-6)<y<(coor[n+1]+6)) and y<86 and not(52-3.1<=x<=64+3.1 and 36-3.1<=y<=47+3.1): #lê se o robot limpou alguma sujidade
            if not(int(n/2) in limpo): #só limpa se ainda não tiver limpo o ponto
                limpo.append(int(n/2)) #coloca o número da sujidade que limpou
                limpeza_da_sujidade(x, y, robot, win, coor, n,nivel,aleatorio)
                if 52-3.1<=x<=52 and 36-3.1<=y<=47+3.1: 
                    robot = Waiter(52-3.7, y, win,0)
                elif 64<=x<=64+3.1 and 36-3.1<=y<=47+3.1:
                    robot = Waiter(64+3.7, y, win,0)
                elif 36-3.1<=y<=36 and 52<=x<=64:
                    robot = Waiter(x, 36-3.7, win,0)
                elif 47<=y<=47+3.1 and 52<=x<=64:
                    robot = Waiter(x, 47+3.7, win,0)
                else:
                    robot = Waiter(x, y, win, 0) #volta a desenhar o robot
    return robot

def carrega_perto_da_mesa(x, y,robot,nivel):
    lista = lista_de_coordenadas_obstaculos(nivel,aleatorio)
    for i in range(0,len(lista),4):
        x1,y1,x2,y2 = lista[i],lista[i+1],lista[i+2],lista[i+3]
        if x1-3.1<=x<=x1 and y1-3.1<=y<=y2+3.1:
            desviar_obstaculo(x1-3.7,y,robot,nivel,aleatorio), robot.mover(x1-3.7,y)
            x=x1-3.7
        elif x2<=x<=x2+3.1 and y1-3.1<=y<=y2+3.1:
            desviar_obstaculo(x2+3.7,y,robot,nivel,aleatorio), robot.mover(x2+3.7,y)
            x=x2+3.7
        elif y1-3.1<=y<=y1 and x1<=x<=x2:
            desviar_obstaculo(x,y1-3.7,robot,nivel,aleatorio), robot.mover(x,y1-3.7)
            y=y1-3.7
        elif y2<=y<=y2+3.1 and x1<=x<=x2:
            desviar_obstaculo(x,y2+3.7,robot,nivel,aleatorio), robot.mover(x,y2+3.7)
            y=y2+3.7
        elif 86-3.1<=y<86:
            desviar_obstaculo(x,86+3.2,robot,nivel,aleatorio), robot.mover(x,86-3.2)
            y=86-3.2
        elif 0<=x<=3.1:
            desviar_obstaculo(3.2,y,robot,nivel,aleatorio), robot.mover(3.2,y)
            x=3.2
        elif 100-3.1<=x<=100:
            desviar_obstaculo(100-3.2,y,robot,nivel,aleatorio), robot.mover(100-3.2,y)
            x=100-3.2
        elif 0<=y<=3.1:
            desviar_obstaculo(x,3.2,robot,nivel,aleatorio), robot.mover(x,3.2)
            y=3.2
        return [x,y]

def desviar_obstaculo(x,y,robot,nivel,aleatorio):
    """
    Simulação do caminho que o robot vai faver para ver se passa por cima de algum obstaculo
    """
    x_inicial,y_inicial=robot.tirar_a_posição()
    dx = x - x_inicial
    dy = y - y_inicial
    distância = (dx**2+dy**2)**0.5
    passos = int(distância*10)
    posição_x = x_inicial
    posição_y = y_inicial
    mudou_direção = False
    for n in range(passos):
        if mudou_direção:
            break
        posição_x +=dx/passos
        posição_y +=dy/passos
        mudou_direção = verificar_a_posição_e_desviar_da_mesa(robot, posição_x, posição_y,nivel,mudou_direção,aleatorio)

def verificar_a_posição_e_desviar_da_mesa(robot, posição_x, posição_y,nivel,mudou_direção,aleatorio):
    """
    Função que verifica se o robot passa por cima de algum obstaculo
    """
    lista = lista_de_coordenadas_obstaculos(nivel,aleatorio)
    for i in range(0,len(lista),4):
        x1,y1,x2,y2 = lista[i],lista[i+1],lista[i+2],lista[i+3]
        if x1-3.1<=posição_x<=x2+3.1 and y1-3.1<=posição_y<=y2+3.1:
            if nivel == 2 or nivel == 3:
                muda_a_direção2(x1,x2,y1,y2,posição_x,posição_y,robot)
                mudou_direção = True
            else:
                muda_a_direção1(x1,x2,y1,y2,posição_x,posição_y,robot)
                mudou_direção = False
    return mudou_direção

def muda_a_direção1(x1,x2,y1,y2,posição_x,posição_y,robot):
    if posição_x<=(x1+x2)/2:
        if posição_y<=(y1+y2)/2:
            robot.mover(x1-3.7,y1-3.7)
        elif posição_y>(y1+y2)/2:
            robot.mover(x1-3.7,y2+3.7)
    elif posição_x>(x1+x2)/2:
        if posição_y<=(y1+y2)/2:
            robot.mover(x2+3.7,y1-3.7)
        elif posição_y>41.5:
            robot.mover(x2+3.7,y2+3.7)
    elif posição_y<=(y1+y2)/2:
        if posição_x<=(x1+x2)/2:
            robot.mover(x1-3.7,y1-3.7)
        elif posição_x>(x1+x2)/2:
            robot.mover(x2+3.7,y1-3.7)
    elif posição_y>(y1+y2)/2:
        if posição_x<=(x1+x2)/2:
            robot.mover(x1-3.7,y2+3.7)
        elif posição_x>(x1+x2)/2:
            robot.mover(x2+3.7,y2+3.7)
               
def muda_a_direção2(x1,x2,y1,y2,posição_x,posição_y,robot):
    if posição_y<=(y1+y2)/2:
        if posição_x<=(x1+x2)/2:
            robot.mover(posição_x,y1-3.7), robot.mover(x1-3.7,y1-3.7), robot.mover(x1-3.7,y2+3.7), robot.mover(posição_x,y2+3.7)
        elif posição_x>(x1+x2)/2:
            robot.mover(posição_x,y1-3.7), robot.mover(x2+3.7,y1-3.7), robot.mover(x2+3.7,y2+3.7), robot.mover(posição_x,y2+3.7)
    elif posição_y>(y1+y2)/2:
        if posição_x<=(x1+x2)/2:
            robot.mover(posição_x,y2+3.7), robot.mover(x1-3.7,y2+3.7), robot.mover(x1-3.7,y1-3.7), robot.mover(posição_x,y1-3.7)
        elif posição_x>(x1+x2)/2:
            robot.mover(posição_x,y2+3.7), robot.mover(x2+3.7,y2+3.7), robot.mover(x2+3.7,y1-3.7), robot.mover(posição_x,y1-3.7)
    
def fim_do_nivel(win):
    """
    função com mensagem de fim de nivel e de clique para sair para o menu
    """
    retangulo = Rectangle(Point(25,40),Point(75,46))
    retangulo.setFill("white")
    retangulo.setOutline("white")
    retangulo.draw(win)
    Text(Point(50,43), "Limpeza concluida!\nCarregue no botão \"sair\" para voltar para o menu").draw(win)
    while True:
        clique = win.getMouse()
        x,y = clique.getX(),clique.getY()
        if 68 <= x <= 98 and 88 <= y <= 98:
            win.close()
            menu()
    
def limpeza_da_sujidade(x,y,robot,win,coor,n,nivel,aleatorio):
    """
    Função que faz desaparecer a sujidade: desenha uma sujidade da cor do pavimento (sujidade desaparece) e coloca o robot por de cima 
    """
    robot.movimento_espiral(nivel,aleatorio)
    robot.mover(x,y)
    robot.troca()
    sujidade(coor[n],coor[n+1],"white","white",win)
    
def sujidade(suj_x,suj_y,cor1,cor2,win):
    """
    Sujidade feita de tal modo que está sempre contida numa circunferência de centro (x,y) e raio 1
    """
    impureza1, impureza2, impureza3 = Oval(Point(suj_x-.75,suj_y+.5), Point(suj_x,suj_y)), Point(suj_x-.1, suj_y-.2), Circle(Point(suj_x+.5,suj_y), .25)
    impureza4,  impureza5,  impureza6 = Point(suj_x-.6, suj_y-.2), Point(suj_x+.3, suj_y+.6), Point(suj_x+.3, suj_y-.5)
    impureza1.setFill(cor1), impureza1.setOutline(cor2), impureza2.setOutline(cor2), impureza3.setFill(cor1), impureza3.setOutline(cor2)
    impureza4.setOutline(cor2), impureza5.setOutline(cor2), impureza6.setOutline(cor2)
    impureza1.draw(win), impureza2.draw(win), impureza3.draw(win), impureza4.draw(win), impureza5.draw(win), impureza6.draw(win)
    
def led(doc_stat, cor, win):
    '''Leds das docking satations'''
    if doc_stat=='esquerda':
        led= Rectangle(Point(.5,40), Point(1.2,46))
    elif doc_stat=='direita':
        led= Rectangle(Point(99.5,40), Point(98.8,46))
    led.setFill(cor)
    led.draw(win)

def sujidade_e_mesa(win,nivel,inicio=7):
    """
    Esta função separa as coordenadas dos pontos de sujidade e coloca-as no sitio assim como a mesa
    """
    tipos_de_mesa=['oval', 'circular', 'retangular']
    tipo_de_mesa=random.choice(tipos_de_mesa)
    x1,y1,x2,y2 = lista_de_coordenadas_obstaculos(nivel,aleatorio)
    mesa = Table(x1, y1, x2, y2, win,tipo_de_mesa)
    coordenadas_de_sujidade=ir_buscar_coordenadas_sujidade(win,inicio,nivel)
    desenho1(coordenadas_de_sujidade,win,nivel,aleatorio)

def desenho1(coordenadas_de_sujidade,win,nivel,aleatorio):
    """
    desenha a sujidade do nivel 1 e 3
    """
    lista = lista_de_coordenadas_obstaculos(nivel, aleatorio)
    x = 0
    while x <= len(coordenadas_de_sujidade) - 1:
        suj_x, suj_y = coordenadas_de_sujidade[x], coordenadas_de_sujidade[x + 1]
        # verificar se a coordenada está dentro da janela e não está de baixo da mesa
        for i in range(0,len(lista),4):
            x1,y1,x2,y2 = lista[i],lista[i+1],lista[i+2],lista[i+3]
            if 0 <= suj_x <= win.getWidth() and 0 <= suj_y <= 85 and not(x1-1 <= suj_x <= x2+1 and y1-1 <= suj_y <= y2+1):
               sujidade(suj_x,suj_y,'brown','black',win)
            else:
                mensagem_de_erro(win)
        x += 2

def lista_de_coordenadas_obstaculos(nivel,aleatorio):
    """
    função com a lista de coordenadas da cada nivel 
    """
    if nivel == 1:
        lista_de_coordenadas_obs=[52,36,64,47]
        return lista_de_coordenadas_obs
    elif nivel == 2:
        ficheiro = open("nivel2.txt", "r")
        linhas = ficheiro.readlines()
        ficheiro.close()
        lista_de_coordenadas_obs = []
        for n in range(7, len(linhas)):
            linha = linhas[n].split() # separar os valores da linha por espaços em branco
            for i in range(1, 5):
                lista_de_coordenadas_obs.append(float(linha[i])) # converter o valor para um número inteiro e adicionar à lista
        return lista_de_coordenadas_obs
    elif nivel == 3:
        lista_de_coordenadas_obs = nivel_3_acrescento(aleatorio)
        return lista_de_coordenadas_obs
        
def nivel_3_acrescento(aleatorio):
    if aleatorio:
        ficheiro = open("dados.txt", "r")
        linhas = ficheiro.readlines()
        ficheiro.close()
        lista_de_coordenadas_obs = []
        for n in range(1, len(linhas)):
            linha = linhas[n].split() # separar os valores da linha por espaços em branco
            for i in range(1, 5):
                lista_de_coordenadas_obs.append(float(linha[i])) # converter o valor para um número inteiro e adicionar à lista
        return lista_de_coordenadas_obs
    else:
        ficheiro = open("Sala.txt", "r")
        linhas = ficheiro.readlines()
        ficheiro.close()
        lista_de_coordenadas_obs = []
        for n in range(1, len(linhas)):
            linha = linhas[n].split() # separar os valores da linha por espaços em branco
            for i in range(1, 5):
                lista_de_coordenadas_obs.append(int(linha[i])) # converter o valor para um número inteiro e adicionar à lista
        return lista_de_coordenadas_obs
    
def mensagem_de_erro(win):   
    """
    mensagem de quando as Coordenadas fora da janela ou a intersetar um obstáculo
    """
    retangulo = Rectangle(Point(0,0),Point(100,100))
    retangulo.setFill("white"), retangulo.setOutline("white") 
    retangulo.draw(win)
    Text(Point(50,50), "Erro nas coordenadas!\nCoordenadas fora da janela ou a intersetar um obstáculo\nClique em qualquer lugar para voltar para o menu").draw(win)
    win.getMouse()
    win.close()
    menu()
    
def nivel1(nivel):
    """
    Função que abre o nivel 1
    """
    ficheiro = open("nivel1.txt", "r")
    linhas = ficheiro.readlines()
    ficheiro.close()
    janela = linhas[1].split()
    nome_da_janela = linhas[4]
    win=GraphWin(nome_da_janela,janela[0],janela[1],autoflush=False)
    win.setCoords(0.0,0.0,100.0,100.0), win.setBackground("white")
    txt('Restaurante',30,95,18,'bold italic',win), txt('Insira no bloco de notas os pontos de sujidade.',30,92,10,'bold italic',win), txt('Clique onde desejar que o robot vá limpar.',30,90,10,'bold italic',win)
    sujidade_e_mesa(win,nivel,inicio=7)   # o início remete para a primeira linha do bloco de notas
    linha = Line(Point(0,86), Point(100,86))
    linha.setWidth(2), linha.draw(win)
    botao_de_terminar=botao(68,88,98,98,'Sair',win)
    docking_stations=Docking_Stations(win)
    led('direita','red',win), led('esquerda',color_rgb(51,255,51),win)
    robot = Waiter(5, 43, win,0)   # Cria um objeto Waiter na posição (5, 43)
    detetor_do_rato1(win,robot,nivel)

def nivel2(nivel):
    """
    Função que abre o nivel 2
    """
    ficheiro = open("nivel2.txt", "r")
    linhas = ficheiro.readlines()
    ficheiro.close()
    janela = linhas[1].split()
    nome_da_janela = linhas[4]
    win=GraphWin(nome_da_janela,janela[0],janela[1],autoflush=False)
    win.setCoords(0.0,0.0,100.0,100.0), win.setBackground("white")
    txt('Restaurante',50,95,18,'bold italic',win), txt('Clique para adicionar sujidades',50,92,10,'bold italic',win)
    linha = Line(Point(0,86), Point(100,86))
    linha.setWidth(2), linha.draw(win)
    botao_de_terminar,botao_de_começar=botao(68,88,98,98,'Sair',win),botao(2,88,32,98,'Começar',win)
    docking_stations=Docking_Stations(win)
    led('direita','red',win), led('esquerda',color_rgb(51,255,51),win)
    ler_tipo_de_obstaculo(nivel,win)
    robot = Waiter(5, 43, win, 0)       # Cria um objeto Waiter na posição (5, 43)
    coor=[] #lista onde vamos guardar as coordenadas da sujidade para depois serem limpas
    detetor_do_rato2(win,nivel,coor,robot,aleatorio)
    
def menu_nivel3_obstaculos(nivel):
    """
    Função que abre o menu do nivel 3
    """  
    ficheiro = open("nivel3.txt", "r")
    linhas = ficheiro.readlines()
    ficheiro.close()
    janela = linhas[1].split()
    nome_da_janela = linhas[4] 
    win=GraphWin(nome_da_janela,janela[0],janela[1],autoflush=False)
    win.setCoords(0.0,0.0,100.0,100.0), win.setBackground("white")
    txt(">>>  Menu do Nível 3 - Obstáculos <<<",50,90,20,'bold italic',win)
    botoes_nivel3_obstaculos(win)
    
class Input_Box:
    """Esta classe serve para criar as input boxes do menu nivel 3 dos obstáculos aleatórios"""
    def __init__(self, win,x,y,caracteres,texto):
        self.win=win
        self.input_box = input_box=Entry(Point(x,y), caracteres)
        input_box.setText(str(texto))
        input_box.setSize(20)
        input_box.draw(win)
    
    def analisar_valores(self,win):
        nr= int(self.input_box.getText())
        return nr
   
    def zerar_valores(self,win):
        self.input_box.setText("0")
    
def mesagem_de_erro_nr_objetos(win):
    """Mensagem de erro quando o número de obstáculos é diferente de 5"""
    retangulo = Rectangle(Point(20,92),Point(80,98))
    retangulo.setFill("white")
    retangulo.setWidth(3)
    retangulo.draw(win)
    txt('A soma do número de objetos tem que ser 5!',50,95,13,'bold italic',win)
    
def layout_menu_aleat(win):
    '''layout do meu para escolher o numero de obstaculos do nivel 3 - disposição esparsa dos objetos'''
    txt('Escolha exatamente 5 objetos!',50,95,12,'bold italic',win), txt("N.° de mesas:",15,75,12,'bold italic',win), txt("N.° de cadeiras:",15,60,12,'bold italic',win)
    txt("N.° de vasos:",15,45,12,'bold italic',win), txt("N.° de pianos:",15,30,12,'bold italic',win)
    vaso(80,80,86,86,win), piano(90, 30, 70, 45, win), cadeira(55, 55, 60, 50, win)
    mesa1, mesa2, mesa3 =Table(50,70,62,81,win,'oval'), Table(75,55,87,66,win,'retangular'), Table(40,30,52,41,win,'circular'), 
    
def avaliar_numero_objetos(nr_mesas,nr_cadeiras,nr_vasos,nr_pianos,input_mesas, input_cadeiras, input_vasos,input_pianos,win):
    '''Avalia de o número de obstáculos escolhidos é igual a 5'''
    if nr_mesas+nr_cadeiras+nr_vasos+nr_pianos==5:
        lista_obstaculos=[nr_pianos,nr_mesas,nr_cadeiras,nr_vasos]
        coord_aleatorias(lista_obstaculos,win)
    else:
        mesagem_de_erro_nr_objetos(win)
        input_mesas.zerar_valores(win), input_cadeiras.zerar_valores(win), input_vasos.zerar_valores(win), input_pianos.zerar_valores(win)

def periferia_obstáculo_x(i,win):
    '''Define, para cada obstáculo, a periferia de coordenadas que tem que ser eliminada'''
    if i==1:    #Obstáculo = Mesa
        return 22
    elif i ==2 or i==3:   #Obstáculo = Vaso ou Cadeira
        return 14
    elif i==0:      #Obstáculo = Piano
        return 31
     
def periferia_obstáculo_y(i,win):
    if i==1:    #Obstáculo = Mesa
        return 20
    elif i ==2 or i==3: #Obstáculo = Vaso ou Cadeira
        return 14
    elif i==0:      #Obstáculo = Piano
        return 15
        
def coord_aleatorias(lista_obstaculos,win): #NB: lista_obstaculos=[nr_mesas,nr_cadeiras,nr_vasos,nr_pianos]
    """Esta função cria uma lista com todas as coordenadas do restaurante em que é possível posicionar um objeto. Consoante uma das coordenadas é atribúida a um determinado objeto, 
    as coordenadas da periferia desse objeto são eliminadas de modo a não ocorrer sobreposição. Note-se que considera-se cada coordenada como o centro do objeto!"""
    
    coordenadas_totais,coordenadas_obstaculos=[],[]
    for x in range(20,81):
        for y in range(15,75):
            coordenadas_totais.append([x,y])
    for i in range(len(lista_obstaculos)):
        if lista_obstaculos[i]==0:
            coordenadas_obstaculos.append([]) 
        else:
            lista_auxiliar=[]
            for obstaculo in range(lista_obstaculos[i]):
                coordenada=random.choice(coordenadas_totais)
                x,y=coordenada[0], coordenada[1]
                lista_auxiliar.append(coordenada)
                for a in range(-periferia_obstáculo_x(i,win),periferia_obstáculo_x(i,win)+1):
                    for b in range(-periferia_obstáculo_y(i,win),periferia_obstáculo_y(i,win)+1):
                        if [x+a,y+b] in coordenadas_totais:
                            coordenadas_totais.remove([x+a,y+b])
            coordenadas_obstaculos.append(lista_auxiliar)
    aleatorio = True
    win.close()
    menu_nivel3_sujidade(3,coordenadas_obstaculos,aleatorio)

def desenhar_objetos_aleatorios(coordenadas_obstaculos,win):
    '''Função que desenha cada obstáculo de acordo com a lista de coordenadas aleatória'''
    coord_mesa, coord_cadeira, coord_vaso, coord_piano=coordenadas_obstaculos[1],coordenadas_obstaculos[2],coordenadas_obstaculos[3],coordenadas_obstaculos[0]
    guardar_dados(coord_mesa, coord_cadeira, coord_vaso, coord_piano)
    
    for i in range(len(coord_mesa)):
        tipos_de_mesa=['oval', 'circular', 'retangular']
        tipo_de_mesa=random.choice(tipos_de_mesa)
        mesa=Table(coord_mesa[i][0]-6,coord_mesa[i][1]-5.5,coord_mesa[i][0]+6,coord_mesa[i][1]+5.5,win, tipo_de_mesa)
    for i in range(len(coord_cadeira)):
        cadeira(coord_cadeira[i][0]-2.5,coord_cadeira[i][1]-2.5,coord_cadeira[i][0]+2.5,coord_cadeira[i][1]+2.5,win)
    for i in range(len(coord_vaso)):
        vaso(coord_vaso[i][0]-3,coord_vaso[i][1]-3,coord_vaso[i][0]+3,coord_vaso[i][1]+3,win)
    for i in range(len(coord_piano)):
        piano(coord_piano[i][0]-10,coord_piano[i][1]-3,coord_piano[i][0]+10,coord_piano[i][1]+3,win)
 
def guardar_dados(coord_mesa, coord_cadeira, coord_vaso, coord_piano):
    linhas = ["Localizacao dos objectos:\n"]
    for i in range(len(coord_mesa)):
        linhas.append("Mesa "), linhas.append(str(coord_mesa[i][0]-6)+" "), linhas.append(str(coord_mesa[i][1]-5.5)+" "), linhas.append(str(coord_mesa[i][0]+6)+" "), linhas.append(str(coord_mesa[i][1]+5.5)+"\n")
    for i in range(len(coord_cadeira)):
        linhas.append("Cadeira "), linhas.append(str(coord_cadeira[i][0]-2.5)+" "), linhas.append(str(coord_cadeira[i][1]-2.5)+" "), linhas.append(str(coord_cadeira[i][0]+2.5)+" "), linhas.append(str(coord_cadeira[i][1]+2.5)+"\n")
    for i in range(len(coord_vaso)):
        linhas.append("Vaso "), linhas.append(str(coord_vaso[i][0]-3)+" "), linhas.append(str(coord_vaso[i][1]-3)+" "), linhas.append(str(coord_vaso[i][0]+3)+" "), linhas.append(str(coord_vaso[i][1]+3)+"\n")
    for i in range(len(coord_piano)):
        linhas.append("Piano "), linhas.append(str(coord_piano[i][0]-10)+" "), linhas.append(str(coord_piano[i][1]-3)+" "), linhas.append(str(coord_piano[i][0]+10)+" "), linhas.append(str(coord_piano[i][1]+3)+"\n") 
    with open("dados.txt", "w") as ficheiro:
       ficheiro.writelines(linhas)
       
def gerar_numero_aleat(input_mesas, input_cadeiras, input_vasos,input_pianos,win):
    '''Função para gerar de forma random o número de obstáculo de cada tipo (a soma do nr de obstáculos é igual a 5)'''
    lista=[]
    a=True
    while a:
        for i in range(1,5):
            nr=random.randint(0,4)
            lista.append(nr)
        if sum(lista) ==5:
            a=False
        else:
            lista=[]
            a=True

    input_mesas.input_box.setText(lista[0]), input_cadeiras.input_box.setText(lista[1])
    input_vasos.input_box.setText(lista[2]), input_pianos.input_box.setText(lista[3])
 
def  menu_nivel3_tipo_obstáculos(nivel):
    '''Função que cria a janela gráfica do menu para decidir o modo de gerar obstáculos no nível 3'''
    win=GraphWin('Nível 3 - Disposição esparsa dos objetos',800,700,autoflush=False)
    win.setCoords(0.0,0.0,100.0,100.0)
    win.setBackground("white")
    input_mesas, input_cadeiras, input_vasos,input_pianos = Input_Box(win,25,75,1,0), Input_Box(win,25,60,1,0), Input_Box(win,25,45,1,0), Input_Box(win,25,30,1,0)
    layout_menu_aleat(win)
    bot_1,bot_2,bot_3=botao(20,5,80,20,'Começar',win),botao(5,7.5,15,17.5,'Gerar',win),botao(85,7.5,95,17.5,'Voltar',win)
    while True:
        clique = win.getMouse()
        x,y = clique.getX(),clique.getY()
        if bot_2.ativar(x,y):
            gerar_numero_aleat(input_mesas, input_cadeiras, input_vasos,input_pianos,win)     
        if bot_1.ativar(x,y):
            nr_mesas, nr_cadeiras, nr_vasos, nr_pianos = input_mesas.analisar_valores(win), input_cadeiras.analisar_valores(win), input_vasos.analisar_valores(win), input_pianos.analisar_valores(win)
            avaliar_numero_objetos(nr_mesas,nr_cadeiras,nr_vasos,nr_pianos,input_mesas, input_cadeiras, input_vasos,input_pianos,win)
        if bot_3.ativar(x,y):
            win.close()
            menu_nivel3_obstaculos(3)
        
def menu_nivel3_sujidade(nivel,lista_coordenadas,aleatorio):
    """
    Função que abre o menu do nivel 3 (decidir a forma de gerar sujidade)
    """  
    ficheiro = open("nivel3.txt", "r")
    linhas = ficheiro.readlines()
    ficheiro.close()
    janela = linhas[1].split()
    nome_da_janela = linhas[4]
    win=GraphWin(nome_da_janela,janela[0],janela[1],autoflush=False)
    win.setCoords(0.0,0.0,100.0,100.0)
    win.setBackground("white")
    txt('Menu Nível 3 - Coordenadas',50,90,20,'bold italic',win)
    botoes_nivel3_sujidade(win,lista_coordenadas,aleatorio)
    
def botoes_nivel3_sujidade(win,lista_coordenadas,aleatorio):
    """
    função para o utilizador poder escolher que nivel quer através dos botões
    utilização do while para o programa não falhar caso o utilizador carregue fora das areas delimitadas pelos botões
    """
    bot_1=botao(20,60,80,75,'Gerar sujidade através do ficheiro',win)
    bot_2=botao(20,40,80,55,'Gerar sujidade através de cliques',win)
    bot_3=botao(20,25,80,35,'Voltar',win)
    while True:
        clique = win.getMouse()
        x = clique.getX()
        y = clique.getY()
        if bot_1.ativar(x,y):
            coor = ir_buscar_coordenadas_sujidade(win,1,3)
            win.close()
            nivel3(win,lista_coordenadas,3,aleatorio,coor)
        elif bot_2.ativar(x,y):
            coor = []
            win.close()
            nivel3(win,lista_coordenadas,3,aleatorio,coor)
        elif bot_3.ativar(x,y):
            win.close()
            menu()

def nivel3(win,lista_coordenadas,nivel,aleatorio,coor):
    """
    Função que abre o nivel 3
    """
    ficheiro = open("nivel3.txt", "r")
    linhas = ficheiro.readlines()
    ficheiro.close()
    janela = linhas[1].split()
    nome_da_janela = linhas[7]
    win=GraphWin(nome_da_janela,janela[0],janela[1],autoflush=False)
    win.setCoords(0.0,0.0,100.0,100.0)
    win.setBackground("white")
    linha = Line(Point(0,86), Point(100,86))
    linha.setWidth(2),linha.draw(win)
    txt('Restaurante',50,93,20,'bold italic',win)
    docking_stations=Docking_Stations(win)
    led('direita','red',win), led('esquerda',color_rgb(51,255,51),win)
    botoes_nivel3(win,lista_coordenadas,nivel,aleatorio,coor)
    
def botoes_nivel3(win,lista_coordenadas,nivel,aleatorio,coor):
    '''Função que cria os botões na janela gráfica do menu do nível 3'''
    botao_de_terminar=botao(68,88,98,98,'Sair',win)
    botao_de_começar=botao(2,88,32,98,'Começar',win)
    if aleatorio:
        desenhar_objetos_aleatorios(lista_coordenadas, win)
    else:
        ler_tipo_de_obstaculo(nivel,win)
    robot = Waiter(5, 43, win, 0)  # Cria um objeto Waiter na posição (5, 43)
    if coor == []:
        detetor_do_rato2(win,nivel,coor,robot,aleatorio)
    else:
        desenho1(coor,win,nivel,aleatorio)
        while True:
            clique = win.getMouse()
            x,y = clique.getX(),clique.getY()
            if botao_de_terminar.ativar(x,y):
                win.close()
                menu()
            elif botao_de_começar.ativar(x,y):
                começar(robot,nivel,win,coor,aleatorio)
    
def detetor_do_rato2(win,nivel,coor,robot,aleatorio,x = None,y = None):
    if x is None or y is None:
        while True:
            clique = win.getMouse()
            x,y = clique.getX(),clique.getY()
            desisão(win,x,y,nivel,coor,robot,aleatorio)      
    else:
        while True:
            desisão(win,x,y,nivel,coor,robot,aleatorio)
            
                
def desisão(win,x,y,nivel,coor,robot,aleatorio):
    if 86 <= y:
        botoes_da_barra2(win,x,y,nivel,coor,robot,aleatorio)
    elif carregou_perto_da_mesa(x,y,nivel,aleatorio) != [x,y]:
        x,y = carregou_perto_da_mesa(x,y,nivel,aleatorio)
        coor = sujidade2(x, y, win,nivel,coor,robot,aleatorio) 
    elif não_carregou_em_cima_de_obstaculo(x,y,nivel,aleatorio):
        coor = sujidade2(x, y, win,nivel,coor,robot,aleatorio)
       
    
def botoes_da_barra2(win,x,y,nivel,coor,robot,aleatorio):
    """
    Botões que faz sair dos niveis e voltar para o menu e para começar o programa
    """   
    while True:
        if 68 <= x <= 98 and 88 <= y <= 98:
            win.close()
            menu()
        elif 2 <= x <= 32 and 88 <= y <= 98:
            começar(robot,nivel,win,coor,aleatorio)
        elif y <= 86 and carregou_em_cima_de_obstaculo(x,y,nivel,aleatorio):
            coor = sujidade2(x, y, win,nivel,coor,robot,aleatorio)
        else:
            clique = win.getMouse()
            x,y = clique.getX(),clique.getY()
            detetor_do_rato2(win,nivel,coor,robot,aleatorio)

def começar(robot,nivel,win,coor,aleatorio):
    """
    função que faz o robot andar
    """
    led('esquerda','red',win)
    robot.mover(3,43)
    ir_voltar(3,"ir",robot,nivel,coor,win,aleatorio)
    ir_voltar(96,"voltar",robot,nivel,coor,win,aleatorio)
    robot.ir_para_docking_station(win)
    coor = []
    detetor_do_rato2(win,nivel,coor,robot,aleatorio)

def ir_voltar(x,ir_ou_voltar,robot,nivel,coor,win,aleatorio):
    lista = lista_de_coordenadas_obstaculos(nivel,aleatorio)
    volta = 0 # vamos usar este numero para distinguir entre as voltas pares e impares
    while True:
        if robot.atualizar_leds():
            return
        if ir_ou_voltar == "ir" and x >=97: # 100 - raio do robot = 97
            break
        elif ir_ou_voltar == "voltar" and x <=3:
            break
        if volta%2 == 0:
            y = 83
            if volta != 0:
                robot.mover(x,3)
            x=andar_por_ai(robot,x,y,nivel,coor,win,ir_ou_voltar,lista,volta,aleatorio)
        else:
            y = 3
            robot.mover(x,83)
            x=andar_por_ai(robot,x,y,nivel,coor,win,ir_ou_voltar,lista,volta,aleatorio)
        volta += 1
    if ir_ou_voltar == "ir":
        robot.mover(97,3), robot.mover(97,83)
    else:
        robot.mover(3,3), robot.mover(3,43)
    return

def andar_por_ai(robot,x,y,nivel,coor,win,ir_ou_voltar,lista,volta,aleatorio):
    if ir_ou_voltar == "ir":
        detetar_obstaculos_e_sujidade(robot,x,y,volta,nivel,coor,win,aleatorio)
        for i in range(0,len(lista),4):
            desviar_obstaculo(x, y, robot, nivel,aleatorio)
        robot.mover(x,y)
        x += 6
    else:
        for i in range(0,len(lista),4):
            desviar_obstaculo(x, y, robot, nivel,aleatorio)
        robot.mover(x,y)
        x -=6
    return x
        
def detetar_obstaculos_e_sujidade(robot,x,y,volta,nivel,coor,win,aleatorio):
    lista = lista_de_coordenadas_obstaculos(nivel,aleatorio)
    for n in range(0,len(coor),2):
        if x-3 <= coor[n] <= x+3:
            y = coor[n+1]
            for i in range(0,len(lista),4):
                desviar_obstaculo(x, y, robot, nivel,aleatorio)
            robot.mover(x,y)
            limpeza_da_sujidade(x,y,robot,win,coor,n,nivel,aleatorio)
    else:
        for i in range(0,len(lista),4):
            desviar_obstaculo(x, y, robot, nivel,aleatorio)
                   
def sujidade2(x,y,win,nivel,coor,robot,aleatorio):
    """
    função para escolher onde pôr a sujidade com o clique do rato
    """
    sujidade(x, y, "brown", "black", win)
    coor.append(x), coor.append(y)
    while True:
        clique = win.getMouse()
        x,y = clique.getX(),clique.getY()
        if 86 <= y:
            botoes_da_barra2(win,x,y,nivel,coor,robot,aleatorio)
        elif carregou_perto_da_mesa(x,y,nivel,aleatorio) != [x,y]:
            x,y = carregou_perto_da_mesa(x,y,nivel,aleatorio)
            sujidade(x, y, "brown", "black", win)
            coor.append(x), coor.append(y)
        elif não_carregou_em_cima_de_obstaculo(x,y,nivel,aleatorio):
            sujidade(x, y, "brown", "black", win)
            coor.append(x), coor.append(y)
    return coor

def carregou_perto_da_mesa(x,y,nivel,aleatorio):
    lista=lista_de_coordenadas_obstaculos(nivel,aleatorio)
    for n in range(0,len(lista),4):
        x1,y1,x2,y2 = lista[n],lista[n+1],lista[n+2],lista[n+3]
        if x1-3.1<=x<=x1 and y1-3.1<=y<=y2+3.1:
            x = x1-4.1
        elif x2<=x<=x2+3.1 and y1-3.1<=y<=y2+3.1:
            x = x2+4.1
        elif y1-3.1<=y<=y1 and x1<=x<=x2:
            y = y1-3.2
        elif y2<=y<=y2+3.1 and x1<=x<=x2:
            y = y2+3.2
    novas_coordenadas=[x,y]
    return novas_coordenadas

def não_carregou_em_cima_de_obstaculo(x,y,nivel,aleatorio):
    lista=lista_de_coordenadas_obstaculos(nivel,aleatorio)
    for n in range(0,len(lista),4):
        x1,y1,x2,y2 = lista[n],lista[n+1],lista[n+2],lista[n+3]
        if x1<=x<=x2 and y1<=y<=y2 or ((0 <= x <= 10 or 90 <= x <= 100) and 37 <= y <= 47) : #ver se o pontos está dentro se um obstáculo ou docking station
            return False
    return True

def ler_tipo_de_obstaculo(nivel,win):
    """
    função que averigua o tipo de obstáculos '''
    """
    if nivel == 2:
        ficheiro = open("nivel2.txt", "r")
        linha = 7
    else:
        ficheiro = open("Sala.txt", "r")
        linha = 1
    linhas=ficheiro.readlines()
    ficheiro.close()
    i=0
    for n in range(linha, len(linhas)):
        linha = linhas[n].split() # separar os valores da linha por espaços em branco
        desenhar_obstaculos(linha, nivel,win,i)
        i += 4
        
def desenhar_obstaculos(linha,nivel,win,i):
    """
    função que percebe que obstaculo foi pedido e desenha-o
    """
    lista = lista_de_coordenadas_obstaculos(nivel,aleatorio)
    if linha[0] == "Mesa":
        tipos_de_mesa=['oval', 'circular'] #random fora da classe Table pois no nível 2 não é permitido mesa retangular
        tipo_de_mesa=random.choice(tipos_de_mesa)
        x1,y1,x2,y2 = lista[i],lista[i+1],lista[i+2],lista[i+3]
        mesa = Table(x1, y1, x2, y2, win,tipo_de_mesa)
    elif linha[0] == "Cadeira":
        x1,y1,x2,y2 = lista[i],lista[i+1],lista[i+2],lista[i+3]
        cadeira(x1,y1,x2,y2,win)
    elif linha[0] == "Vaso":
        x1,y1,x2,y2 = lista[i],lista[i+1],lista[i+2],lista[i+3]
        vaso(x1,y1,x2,y2,win)
    elif linha[0] == "Piano":
        x1,y1,x2,y2 = lista[i],lista[i+1],lista[i+2],lista[i+3]
        piano(x1,y1,x2,y2,win)

def vaso(x1,y1,x2,y2,win):    #desenhar vaso 6x6
    x,y=(x1+x2)/2,(y1+y2)/2
    circ_exterior, circ_interior= Circle(Point(x,y), 2.5), Circle(Point(x,y), 2) 
    folha1=Oval(Point(x,y), Point(x+1,y+1.5))
    folha1.setFill(color_rgb(0, 128, 0)), folha1.setOutline(color_rgb(0, 66, 54))
    folha2,folha3,folha4,folha5,folha6,folha7,folha8=folha1.clone(),folha1.clone(),folha1.clone(),folha1.clone(),folha1.clone(),folha1.clone(),folha1.clone()
    folha2.move(.5,-.5) ,folha3.move(-.5,-.9), folha4.move(-1,-1.5), folha5.move(-1.7,-1.2), folha6.move(.2,-1.5), folha7.move(-1.5,-.5), folha8.move(-1,.1)
    circ_exterior.setFill(color_rgb(150, 75, 0)), circ_interior.setFill(color_rgb(66, 38, 0))
    circ_exterior.draw(win), circ_interior.draw(win), folha1.draw(win), folha2.draw(win), folha3.draw(win), folha4.draw(win), folha5.draw(win), folha6.draw(win), folha7.draw(win), folha8.draw(win)

def piano(x1,y1,x2,y2,win):     #desenhar piano 20x6
    x, y=(x1+x2)/2, (y1+y2)/2
    base=Rectangle(Point(x-10,y+3), Point(x+10,y-3))
    base.setFill('black')
    base.draw(win)
    base_teclas=Rectangle(Point(x-9,y-2.3), Point(x+9,y))
    base_teclas.setFill('white')
    base_teclas.draw(win)
    k1,k2=0,1
    for i in range(18):
        linha=Line(Point(x-9+k1,y-2.7), Point(x-9+k1,y))
        linha.draw(win)
        k1+=1
    for i in range(9):
        linha=Line(Point(x-9+k2,y-1.2), Point(x-9+k2,y))
        linha.setWidth(5), linha.draw(win)
        k2+=2
    
def cadeira(x1,y1,x2,y2,win):   #desenhar cadeira 5x5
    x=(x1+x2)/2
    y=(y1+y2)/2
    base=Rectangle(Point(x-2.5,y-2.5), Point(x+2.5,y+2.5))
    base.setFill(color_rgb(210,180,140))
    base.draw(win)
    apoio1, apoio2, apoio3 = Rectangle(Point(x-2.5,y-2.5), Point(x-1.5,y+2.5)), Rectangle(Point(x+2.5,y-2.5), Point(x+1.5,y+2.5)), Rectangle(Point(x-2.5,y+2.5), Point(x+2.5,y+1.5))
    apoios = [apoio1,apoio2,apoio3]
    for apoio in apoios:
        apoio.setFill(color_rgb(130, 100, 70))
        apoio.setWidth(1.6)
        apoio.draw(win)
    
class Docking_Stations:     #Classe que permite gerar na janela gráfica docking stations
    def __init__(self, win):
        self.win=win
        self.docking_stations = [Rectangle(Point(0, 38), Point(9, 48)),Rectangle(Point(100, 38), Point(91, 48))]
        for doc_stat in self.docking_stations:
            doc_stat.setFill(color_rgb(20,20,20)), doc_stat.setOutline(color='black')
            doc_stat.draw(self.win)
        led1= Rectangle(Point(.5,40), Point(1.2,46))
        led1.setFill('red')
        led1.draw(win)
        led2= Rectangle(Point(99.5,40), Point(98.8,46))
        led2.setFill('red')
        led2.draw(win)
            
class Waiter:   #Classe que permite gerar o robot
    def __init__(self, x, y, win ,distancia_percorrida):
        self.x = x
        self.y = y
        self.color = "black"
        self.win = win
        self.robot = Circle(Point(x, y), 3)
        self.robot.setFill(self.color)
        self.robot.setWidth(3)
        self.robot.setOutline("green")
        self.robot.draw(self.win)
        self.distância_percorrida = distancia_percorrida
        self.bateria_maxima = 4000
        self.bateria_atual = self.bateria_maxima
        self.carregar = False
        self.atualizar_leds()
        
    def troca(self):    #permite colocar o robot por de cima da sujidade limpa
        self.robot.undraw()

    def mover(self, x, y):  # Move o robot para a posição (x, y)
        dx, dy = x - self.x , y - self.y
        dist = ((dx**2) + (dy**2)) ** 0.5
        passos = int(dist)  # Calcula o número de passos necessários para mover a distância total
        posiçãox_animação=self.x
        posiçãoy_animação=self.y
        for i in range(passos):     # Move o robot em cada passo intermédio (animação)
            self.robot.move(dx/passos, dy/passos)
            posiçãox_animação+=dx/passos
            posiçãoy_animação+=dy/passos
            update(50)
            self.atualizar_leds()
        self.robot.move(x-posiçãox_animação, y-posiçãoy_animação) # Move o robot no último passo
        self.x = x
        self.y = y
        self.distancia_percorrida(dist) # Atualiza a posição do robot
        
    def ir_para_docking_station(self,win):  # Move o robot de volta para a doc mais próxima
        if self.x <= 50:
            voltar_x = 5
            doc_stat='esquerda'
        else:
            voltar_x = 95
            doc_stat='direita'       # Encontra a doc mais próxima
        texto = Text(Point(50,83),"A carregar aguarde").draw(win)
        texto.setTextColor("blue")
        self.carregar = True
        self.mover(voltar_x, 43)    # Move o robot de volta para a doc mais próxima
        led(doc_stat,color_rgb(51,255,51),win)
        time.sleep(2)   # Pausa de 2 segundos para recarregar a bateria
        texto.undraw()
        self.carregar = False
        self.bateria_atual = self.bateria_maxima
        self.atualizar_leds()
    
    def movimento_espiral(self,nivel,aleatorio):  # Move o robot em uma trajetória espiral circular
        lista = lista_de_coordenadas_obstaculos(nivel,aleatorio)
        for i in range(1 *  36):
            for n in range(0,len(lista),4): #parar antes de bater num obstaculo
                x1,y1,x2,y2 = lista[n],lista[n+1],lista[n+2],lista[n+3]
                if (x1-3<=self.x<=x2+3 and y1-3<=self.y<=y2+3) or 86-3<=self.y or self.y<=3 or self.x <= 3 or self.x > 100-3:
                    return
            x = self.x + .1 * i * cos(i)
            y = self.y + .1 * i * sin(i)
            self.mover(x, y)
        
    def tirar_a_posição(self): #função que dá uma lista com as coordenada de onde o robot se encontra
        posição_inicial =[self.x,self.y]
        return posição_inicial
    
    def distancia_percorrida(self,dist): #conta a distancia percorrida pelo robot
        self.distância_percorrida += dist
        self.bateria_atual -= dist
    
    def atualizar_leds(self): #atualiza os leds da bateria do robot
        if self.carregar:
            self.robot.undraw(), self.robot.setOutline("blue")
            self.robot.draw(self.win)
        elif self.bateria_atual > self.bateria_maxima * 0.75:
            self.robot.undraw(), self.robot.setOutline("green")
            self.robot.draw(self.win)
            return False
        elif self.bateria_atual > self.bateria_maxima * 0.5:
            self.robot.undraw(), self.robot.setOutline("yellow")
            self.robot.draw(self.win)
            return False
        elif self.bateria_atual > self.bateria_maxima * 0.25:
            self.robot.undraw(), self.robot.setOutline("orange")
            self.robot.draw(self.win)
            return False
        else:
            self.robot.undraw(), self.robot.setOutline("red")
            self.robot.draw(self.win)
            if self.bateria_atual > self.bateria_maxima * 0.10:
                return False
            else:
                return True
            
class Table: #cria uma mesa de diferentes formatos
    def __init__(self, x1,y1,x2,y2,win,tipo_de_mesa):
        x, y = min(x1,x2), min(y1,y2)
        if tipo_de_mesa=='oval':    #mesa oval 12x11
            formato=Oval(Point(x1,y1), Point(x2,y2))
            formato.setFill(color_rgb(137, 107, 73)), formato.setOutline(color_rgb(66, 38, 0)), formato.setWidth(1.5)
            cor_individual=color_rgb(0, 139, 139)
        elif tipo_de_mesa=='retangular':    #mesa retangular 12x11
            formato=Rectangle(Point(x1,y1), Point(x2,y2))
            formato.setFill(color_rgb(137, 107, 73)), formato.setOutline(color_rgb(66, 38, 0)), formato.setWidth(1.5)
            cor_individual=color_rgb(238, 173, 0)
        elif tipo_de_mesa=='circular':  #mesa circular de raio 6
            formato=Circle(Point(((x1+x2)/2),(y1+y2)/2), 6)
            formato.setFill(color_rgb(137, 107, 73)), formato.setOutline(color_rgb(66, 38, 0)), formato.setWidth(1.5)
            cor_individual=color_rgb(255, 105, 97)   
        prato1,circulo1,talher1,copo1,individual1 = Circle(Point((x1+x2)/2,y+3), 1.5), Circle(Point((x1+x2)/2,y+3),1.1), Line(Point(x+4, y+1.8),Point(x+4,y+4.2)), Circle(Point(x+7.5,y+5), 0.6), Rectangle(Point(x+3,y+1.2), Point(x+9,y+4.9))
        individual1.setFill(cor_individual), talher1.setWidth(1.2), talher1.setOutline(color_rgb(71,71,71)), prato1.setFill("white"), copo1.setFill(color_rgb(200,255,255))
        prato2, circulo2, copo2, individual2, talher2,talher3,talher4 = prato1.clone(), circulo1.clone(), copo1.clone(), individual1.clone(), talher1.clone(),talher1.clone(),talher1.clone()
        prato2.move(0,5), circulo2.move(0,5), talher2.move(4,0), talher3.move(0,5.2), talher4.move(4,5.2), copo2.move(-3.2,1.1), individual2.move(0,5)
        formato.draw(win), individual1.draw(win), individual2.draw(win), prato1.draw(win), prato2.draw(win), circulo1.draw(win), circulo2.draw(win)
        talher1.draw(win), talher2.draw(win), talher3.draw(win), talher4.draw(win), copo1.draw(win), copo2.draw(win)
        return
    
menu()