import numpy as np
import sys

#----------------------Entrada de dados-------------------------------
#Print("----------------------Entrada de dados do elemento EPT-RQ4-------------------------------)
#Tipo_de_estrutura
tipoestr = "EPT"
#Tipo_de_elemento
tipoelem = "EP-RQ4_ISO"
#Numero_de_nos
nnos = 12
#Numero_de_materiais
nmats = 1
#Numero_de_secoes_transversais
nsecs = 1
#Numero_de_elementos
nelems = 5
#Numero_de_apoios
naps = 4
#Numero_de_nos_carregados
nnoscar = 1
#Numero_de_elementos_carregados (se for treliça, coloque zero. Outros elementos podem ser carregados ao longo do elemento)
nelemscar = 1
#Coordenadas_dos_nos, onde cada linha são as coordenados de um nó
#____X_____Y
coordnos = np.array([
[   0.0, 0.0],
[   200, 0.0],
[   200, 1800],
[   0.0, 1800],
[   0.0, 2000],
[   200, 2000],
[   1800,2000],
[   1800,1800],
[   2000,2000],
[   2000,1800],
[   2000, 0.0],
[   1800, 0.0]])
#Propriedades_dos_materiais, onde cada linha é um material
#_______E________POISSON______ALPHA
propmats = np.array([[
200000,        0.2,         0.00010]])
#Propriedades_das_seções_transversais, onde cada linha é uma propriedade de uma seção transversal
#___ESPESSURA
propgeo = np.array([
    [500]])
#Propriedades_dos_elementos, onde cada linha é elemento com suas propriedades
#___no1__no2__no3__no4__material__seção
propelems = np.array([
    [1 ,  2 ,  3 ,   4,    1,       1],
    [4 ,  3 ,  6 ,    5,    1,       1],
    [3 ,  8 ,  7 ,   6,    1,       1],
    [8 , 10 ,  9,     7,    1,       1],
    [12 , 11 ,  10 ,   8,    1,       1]])
#Apoios_(r=1_impedido_r=0_livre), onde cada linha representa as restrições de um nó
#__no__rtx_rty
restrsap = np.array([
   [1 , 1 , 1],
   [2 , 1 , 1],
   [12 , 1 , 1],
   [11 , 1 , 1]])
#Elementos_carregados_(idsis=1_global_idsis=0_local),
#Isto é para elementos com cargas distribuídas ao longo do elemento, ou seja, fora dos nós
#________________________el___idsis_____qx1______qy1_____qx2______qy2_____qx3______qy3_____qx4______qy4
cargaselems = np.array([ [1,    0,       0,     0,       0,     0,     0,       0,      0,       0]])

#Nos_carregados, onde a primeira coluna representa o nós carregado, e as outras colunas as forças nas direções.
#__no____fx_____fy  
cargasnos = np.array([
   [5,  10000,    0.0]])

#-----------------Fim da entrada de dados-------------------------------
#########################################################################

#########################################################################
#-----------------DEFINIÇÕES DAS FUNÇÕES DO PROGRAMA---------------------

#1-Esta função define os graus de liberdade e os tipos de carregamentos da estrutura setada.
def Leitura_de_dados(tipoestr, tipoelem):
  #1.1- nesta primeira rodada de condições defini-se a qnt de propriedades da estrutura escolhida
  if tipoestr == "TRELICA_PLANA":
   #1.1.1-Este array possui 4 termos, sendo:
   #o primeiro o número de graus de liberdade por nó do elemento
   #o segundo o número de coordenadas, ou seja, se dois plano se 3 espacial
   #o terceiro o número de propriedades do material que o elemento exige, por exemplo: E, e alpha(para temperatura)
   #o quarto o número de propriedades de seção transversal que o elemento existe, por exemplo: área
    #MATPROPELEM = np.array([[2, 2, 2, 1]])
    nglno= 2
    ncoord= 2
    npropmat= 2
    npropgeo= 1
  elif tipoestr == "PORTICO_PLANO":
    nglno= 3
    ncoord= 2
    npropmat= 2
    npropgeo= 3
  elif tipoestr == "GRELHA":
    nglno= 3
    ncoord= 2
    npropmat= 3
    npropgeo= 3
  elif tipoestr == "TRELICA_ESPACIAL":
    nglno= 3
    ncoord= 3
    npropmat= 2
    npropgeo= 1
  elif tipoestr == "PORTICO_ESPACIAL":
    nglno= 6
    ncoord= 3
    npropmat= 3
    npropgeo= 6
  #elemento finito do tipo 2D quadrado ou Q4 ou 2D com interpolação parabólica Q8
  elif tipoestr == "EPT" or "EPD":
    nglno= 2
    ncoord= 2
    npropmat= 3
    npropgeo= 1
  else:
    print("Erro no tipo de estrutura")
    sys.exit()
    

#1.2-Nesta segunda rodada de condições defini-se os tipos de carregamentos para a estrutura escolhida
  if tipoestr == "TRELICA_PLANA":
    if tipoelem == "TP2":
      #O primeiro termo abaixo é o número de nós por elemento, e o segundo é a quantidade de carregamentos no elemento
      #, ou seja, no caso da treliça não pode ter carregamentos no elemento.
      #Mas, no caso do pórtico podem ter carregamenos em x e y, portanto, 2.
      #No caso de pórtico plano podem ter em x,y e z, portanto, 3.
      nnoselem = 2
      ncarelem = 0
    else:
      print("Elemento incosistente com o tipo de estrutura")
      print("Verifique na entrada de dados se está escrito TP2")
      sys.exit()
  elif tipoestr == "PORTICO_PLANO":
     if tipoelem == "PP2":
      nnoselem = 2
      ncarelem = 2
     else:
      print("Elemento incosistente com o tipo de estrutura")
      print("Verifique na entrada de dados se está escrito PP2")
      sys.exit()
  elif tipoestr == "GRELHA":
     if tipoelem == "GR2":
      nnoselem = 2
      ncarelem = 2
     else:
      print("Elemento incosistente com o tipo de estrutura")
      print("Verifique na entrada de dados se está escrito GR2")
      sys.exit()
  elif tipoestr == "TRELICA_ESPACIAL":
     if tipoelem == "TE2":
      nnoselem = 2
      ncarelem = 0
     else:
      print("Elemento incosistente com o tipo de estrutura")
      print("Verifique na entrada de dados se está escrito GE2")
      sys.exit()
  elif tipoestr == "PORTICO_ESPACIAL":
     if tipoelem == "PE2":
      nnoselem = 2
      ncarelem = 3
     else:
      print("Elemento incosistente com o tipo de estrutura")
      print("Verifique na entrada de dados se está escrito PE2")
      sys.exit()
  elif tipoestr == "EPT" or "EPD":
     #elemento 2D Q4
     if tipoelem == "EP-RQ4":
      nnoselem = 4
      ncarelem = 8
     #elemento 2D Q8
     elif tipoelem == "EP-RQ8":
      nnoselem = 8
      ncarelem = 8
      #elemento 2D Q8
     elif tipoelem == "EP-RQ4_ISO":
      nnoselem = 4
      ncarelem = 8
     else:
      print("Elemento incosistente com o tipo de estrutura")
      print("Verifique na entrada de dados se está escrito EP-RQ4 ou EP-RQ8")
      sys.exit()
  else:
    print("Elemento não implementado")
    sys.exit()
  return nglno, ncoord, npropmat, npropgeo, nnoselem, ncarelem

#2-Esta função define os graus de liberdade total da estrutura e quantidade de equações.
def Grau_de_liberdade(tipoestr, nnos, nglno, naps, restrsap):

#2.1-neste primeiro laço é encontrado a matriz de graus de liberdade
#basicamente, o que é feito aqui é pegar da matriz de restrições do apoio o nó restringido
#depois esse nó será a linha da matriz glno onde serão adicionados os graus de liberdade da matriz de restrição
#"lembre-se", a matriz de restrições restrap tem 3 colunas, onde se define para cada nó sua restrição, ou seja, 0 ou 1
#então, a primeira coluna de restrasp não entra na matriz glno, porque é a coluna dos nós.
  glno = np.zeros((nnos, nglno))  
  for i in range(naps):
    no = restrsap[i][0]
    for j in range(1, nglno+1, 1):
      glno[no-1][j-1] = restrsap[i][j]
  
#2.2-nesta parte transforma-se a matriz glno, que é uma matriz de zeros e uns,
#em uma matriz onde se determina a quantidade de equações disponíveis para o cálculo.
#para isso, onde glno for 1 é trocado para 0, e onde era 1 passa a sera neq=neq+1
#assim, o último delemento de glno será sempre o valor do número de equações.
  neq=0
  for i in range(nnos):
    for j in range(nglno):
      if glno[i][j] == 1:
        glno[i][j] = 0
      else:
        neq = neq + 1
        glno[i][j] = neq
  return glno, neq

  

#3-Definição da função de construção da matriz de rigidez
def MatrizDeRigidezDaEstrutura(tipoestr, tipoelem, nglno, nnoselem, neq, coordnos, propelems, propmats, propgeo, glno):
  
  #cria o tamanho do vetor de graus de liberdade do elemento, por exemplo, se nglno = 2 (graus de liberdade do elemento)
  #e nnoselem = 2 (número de nós por elemento), então o número de graus de liberdade por elemento será 4.
  nglel = nglno * nnoselem
  
  #Assim, este vetor irá guardar, para o exemplo anterior, 4 graus de liberdade, sendo 2 graus por nó.
  #Portanto, o vetor gle = (gdl x do nó 1, gdl y do nó 1, gdl x do nó 2, gdl y do nó 2) totalizando 4 posições para o exemplo anterior
  gle   = np.zeros((1,nglel))
  
  #Aqui é criada a matriz de rigidez global neq por neq, ou seja, nesta matriz já foram retiradas as linhas e colunas dos apoios, quando for encontrar os deslocamentos
  Kestr = np.zeros((neq,neq))
  
  #este laço irá criar a matriz de rigidez global  
  for el in range(nelems):

    #aqui se identifica o material do elemento 
    idmat = propelems[el][nnoselem+0]

    #aqui se identifica a seção do elemento
    idsec = propelems[el][nnoselem+1]

    #aqui pega toda a linha do material daquele elemento
    pmat  = propmats[idmat-1][:]

    #aqui pega toda a linha da propriedade da seção transversal do elemeno
    psec  = propgeo[idsec-1][:]

    #Aqui está chamado de "no", mas na verdade é a barra que vai do nó da posição 1 até a posição 2 do vetor "no"
    no = propelems[el][0:nnoselem]
    
    #Aqui determina-se os senos e cossenos para rotacinar os elemento do local para o global
    if tipoelem == "TP2" or tipoelem == "PP2" or tipoelem == "GR2":
      # Cálculo de L, cs e sn
      dx = coordnos[no[1]-1][0] - coordnos[no[0]-1][0]
      dy = coordnos[no[1]-1][1] - coordnos[no[0]-1][1]
      #o termo "**" significa elevar seria o sinal "^" da cálculadora
      L = (dx**2+dy**2)**0.5
      cs = dx/L
      sn = dy/L
      if L <= 10e-8:
        print("Comprimento do elemento nulo")
        sys.exit()
    elif tipoelem == "TE2" or tipoelem == "PE2":
      # Cálculo de L, dx, dy e dz
      dx = coordnos[no[1]-1][0] - coordnos[no[0]-1][0]
      dy = coordnos[no[1]-1][1] - coordnos[no[0]-1][1]
      dz = coordnos[no[1]-1][2] - coordnos[no[0]-1][2]
      #o termo "**" significa elevar seria o sinal "^" da cálculadora
      L = (dx**2+dy**2+dz**2)**0.5
      cx = dx/L
      cy = dy/L
      cz = dz/L
      if L <= 10e-8:
        print("Comprimento do elemento nulo")
        sys.exit()
    elif tipoelem == "EP-RQ4" or tipoelem == "EP-RQ8" or tipoelem == "EP-RQ4_ISO":
      [cs, sn, a, b] = EP_RQ4_Dimensoes(el, coordnos, no)
    else:
      print("Elemento ainda não implementado")
      sys.exit()

    #Cálculo da matriz de rigidez do elemento no sistema local
    #e determinação da matriz de rotação
    if tipoelem == "TP2":
      #criando a matriz de rigidez do elemento de treliça
      kel = TP2_MatrizDeRigidezDoElemento(pmat[0], psec[0], L)
      Rel = TP2_MatrizDeRotacaoDoElemento(cs, sn)
    elif tipoelem == "PP2":
      #criando a matriz de rigidez do elemento de pórtico
      kel = PP2_MatrizDeRigidezDoElemento(pmat[0], psec[0], psec[0], L)
      Rel = PP2_MatrizDeRotacaoDoElemento(cs, sn)
    elif tipoelem == "GR2":
      #criando a matriz de rigidez do elemento de grelha
      kel = GR2_MatrizDeRigidezDoElemento(pmat[0], pmat[1], psec[0], psec(1), L)
      Rel = GR2_MatrizDeRotacaoDoElemento(cs, sn)
    elif tipoelem == "EP-RQ4":
      #criando a matriz de rigidez do elemento Q4      
      kel = EP_RQ4_MatrizDeRigidezDoElemento(pmat[0], pmat[1], psec[0], tipoestr, a, b)
      Rel = EP_RQ4_MatrizDeRotacaoDoElemento(cs, sn,nnoselem)
    elif tipoelem == "EP-RQ8":
        pass
      #criando a matriz de rigidez do elemento Q8
      #kel = EP_RQ8_MatrizDeRigidezDoElemento(pmat[0], pmat[1], psec[0], tipoestr, a, b)
      #Rel = EP_RQ8_MatrizDeRotacaoDoElemento(cs, sn, nnoselem)
    elif tipoelem == "EP-RQ4_ISO":
      #criando a matriz de rigidez do elemento Q4 ISO
      kel = EP_RQ4_ISO_MatrizDeRigidezDoElemento(pmat[0], pmat[1], psec[0], tipoestr, coordnos, no)
    else: 
      print("Matriz de rigidez do elemento ainda não implementada esta estrutura e este elemento")
      sys.exit()
  
    #Transferindo a matriz de rigidez do elemento do sistema local pra o sistema global
    if tipoelem != "EP-RQ4_ISO":
      kel = np.matmul(np.matmul(np.transpose(Rel),kel),Rel)
        
    #Determinação do grau de liberdade do elemento para compor a matriz de rigidez global
    gle = GrausDeLiberdadeDoElemento(nnoselem,glno,no,nglno)

    #Montagem da matriz de rigidez global da estrutura usando elemento por elemento
    for i in range(nglel):
      if gle[0][i]>0:
        for j in range(nglel):
          if gle[0][j]>0:
            Kestr[int(gle[0][i]-1)][int(gle[0][j]-1)] = Kestr[int(gle[0][i]-1)][int(gle[0][j]-1)] + kel[i][j]
            
    
    #função para construir a matriz de cálculo da reação de apoio.
    #for i in range(nglel):
    #  if gle[0][i] == 0:
     #   for j in range(nglel):
    #      if gle[0][j] == 0:
     #       Kestr[int(restrsap[0][i]-1)][int(gle[0][j]-1)] = Kestr[int(gle[0][i]-1)][int(gle[0][j]-1)] + kel[i][j]
      
        
    #Teste de consistência da matriz de rigidez
  for i in range(neq):      
    if Kestr[i][i] < 10e-8:
      print(i)
      print(Kestr[102][102])
      print("Erro de instalilidade estrutura")
      print("A diagonal principal da matriz de rigidez possui um elemento nulo")
      sys.exit()
  

  return Kestr

#4A-Definição da função de criação de matriz de rigidez do elemento de TRELIÇA
def TP2_MatrizDeRigidezDoElemento(E,A,L):
  kel = np.zeros((4,4))
  a = E*A/L
  kel[0][0] =  a;kel[0][2] = -a
  kel[2][0] = -a;kel[2][2] =  a
  return kel

#4B-Definição da função de criação de matriz de rigidez do elemento de PÓRTICO
def PP2_MatrizDeRigidezDoElemento(E,A,Iz,L):
  kel = np.zeros((6,6))
  a = E*A/L
  b = 12*E*Iz/L^3
  c = 6*E*Iz/L^2
  d = 4*E*Iz/L
  e = 2*E*Iz/L
  kel[0][0]=  a; kel[0][3]= -a; 
  kel[1][1]=  b; kel[1][2]=  c;  kel[1][4]= -b;  kel[1][5]=  c;
  kel[2][1]=  c; kel[2][2]=  d;  kel[2][4]= -c;  kel[2][5]=  e;
  kel[3][0]= -a; kel[3][3]=  a; 
  kel[4][1]= -b; kel[4][2]= -c;  kel[4][4]=  b;  kel[4][5]= -c;
  kel[5][1]=  c; kel[5][2]=  e;  kel[5][4]= -c;  kel[5][5]=  d;
  return kel

#4C-Definição da função de criação de matriz de rigidez do elemento de GRELHA
def GR2_MatrizDeRigidezDoElemento(E, G, Ix, Iz, L):
  kel = np.zeros((6,6))
  a = G*Ix/L
  b = 12*E*Iz/L^3
  c = 6*E*Iz/L^2
  d = 4*E*Iz/L
  e = 2*E*Iz/L

  kel[0][0]=  b; kel[0][2]= -c; kel[0][3]= -b; kel[0][5]= -c;  
  kel[1][1]=  a; kel[1][4]= -a; 
  kel[2][0]= -c; kel[2][2]=  d; kel[2][3]= c; kel[2][5]=  e;
  kel[3][0]= -b; kel[3][2]=  c; kel[3][3]= b; kel[3][5]=  c;   
  kel[4][1]= -a; kel[4][4]=  a; 
  kel[5][0]= -c; kel[5][2]=  e; kel[5][3]= c; kel[5][5]=  d;
  return kel

#4D-Definição da função de criação de matriz de rigidez do elemento Q4
def EP_RQ4_MatrizDeRigidezDoElemento(E, nu, t, tipoestr, a, b):
  
  Kel = np.zeros((8,8))
  if tipoestr == "EPD":
    E = E/(1-nu**2)
    nu = nu/(1-nu)

  Kel[0][0] = (1/6)*E*(a**2*nu-a**2-2*b**2)/(a*(nu**2-1)*b);Kel[0][1] =-(1/8)*E/(-1+nu);
  Kel[0][2] = (1/12)*E*(a**2*nu-a**2+4*b**2)/(a*(nu**2-1)*b);Kel[0][3] =-(1/8)*E*(3*nu-1)/(nu**2-1);
  Kel[0][4] = -(1/12)*E*(a**2*nu-a**2-2*b**2)/(a*(nu**2-1)*b);Kel[0][5] =(1/8)*E/(-1+nu);
  Kel[0][6] = -(1/6)*E*(a**2*nu-a**2+b**2)/(a*(nu**2-1)*b);Kel[0][7] =(1/8)*E*(3*nu-1)/(nu**2-1);
  Kel[1][0] = -(1/8)*E/(-1+nu);Kel[1][1] = -(1/6)*E*(-b**2*nu+2*a**2+b**2)/(a*(nu**2-1)*b);
  Kel[1][2] = (1/8)*E*(3*nu-1)/(nu**2-1);Kel[1][3] = -(1/6)*E*(b**2*nu+a**2-b**2)/(a*(nu**2-1)*b);
  Kel[1][4] = (1/8)*E/(-1+nu);Kel[1][5] = (1/12)*E*(-b**2*nu+2*a**2+b**2)/(a*(nu**2-1)*b);
  Kel[1][6] = -(1/8)*E*(3*nu-1)/(nu**2-1);Kel[1][7] = (1/12)*E*(b**2*nu+4*a**2-b**2)/(a*(nu**2-1)*b);
  Kel[2][0] = (1/12)*E*(a**2*nu-a**2+4*b**2)/(a*(nu**2-1)*b);Kel[2][1] = (1/8)*E*(3*nu-1)/(nu**2-1);
  Kel[2][2] = (1/6)*E*(a**2*nu-a**2-2*b**2)/(a*(nu**2-1)*b);Kel[2][3] = (1/8)*E/(-1+nu);
  Kel[2][4] = -(1/6)*E*(a**2*nu-a**2+b**2)/(a*(nu**2-1)*b);Kel[2][5] = -(1/8)*E*(3*nu-1)/(nu**2-1);
  Kel[2][6] = -(1/12)*E*(a**2*nu-a**2-2*b**2)/(a*(nu**2-1)*b);Kel[2][7] = -(1/8)*E/(-1+nu);
  Kel[3][0] = -(1/8)*E*(3*nu-1)/(nu**2-1);Kel[3][1] = -(1/6)*E*(b**2*nu+a**2-b**2)/(a*(nu**2-1)*b);
  Kel[3][2] = (1/8)*E/(-1+nu);Kel[3][3] = -(1/6)*E*(-b**2*nu+2*a**2+b**2)/(a*(nu**2-1)*b);
  Kel[3][4] = (1/8)*E*(3*nu-1)/(nu**2-1);Kel[3][5] = (1/12)*E*(b**2*nu+4*a**2-b**2)/(a*(nu**2-1)*b);
  Kel[3][6] = -(1/8)*E/(-1+nu);Kel[3][7] = (1/12)*E*(-b**2*nu+2*a**2+b**2)/(a*(nu**2-1)*b);
  Kel[4][0] = -(1/12)*E*(a**2*nu-a**2-2*b**2)/(a*(nu**2-1)*b);Kel[4][1] = (1/8)*E/(-1+nu);
  Kel[4][2] = -(1/6)*E*(a**2*nu-a**2+b**2)/(a*(nu**2-1)*b);Kel[4][3] = (1/8)*E*(3*nu-1)/(nu**2-1);
  Kel[4][4] = (1/6)*E*(a**2*nu-a**2-2*b**2)/(a*(nu**2-1)*b);Kel[4][5] = -(1/8)*E/(-1+nu);
  Kel[4][6] = (1/12)*E*(a**2*nu-a**2+4*b**2)/(a*(nu**2-1)*b);Kel[4][7] = -(1/8)*E*(3*nu-1)/(nu**2-1);
  Kel[5][0] = (1/8)*E/(-1+nu);Kel[5][1] = (1/12)*E*(-b**2*nu+2*a**2+b**2)/(a*(nu**2-1)*b);
  Kel[5][2] = -(1/8)*E*(3*nu-1)/(nu**2-1);Kel[5][3] = (1/12)*E*(b**2*nu+4*a**2-b**2)/(a*(nu**2-1)*b);
  Kel[5][4] = -(1/8)*E/(-1+nu);Kel[5][5] = -(1/6)*E*(-b**2*nu+2*a**2+b**2)/(a*(nu**2-1)*b);
  Kel[5][6] = (1/8)*E*(3*nu-1)/(nu**2-1);Kel[5][7] = -(1/6)*E*(b**2*nu+a**2-b**2)/(a*(nu**2-1)*b);
  Kel[6][0] = -(1/6)*E*(a**2*nu-a**2+b**2)/(a*(nu**2-1)*b);Kel[6][1] = -(1/8)*E*(3*nu-1)/(nu**2-1);
  Kel[6][2] = -(1/12)*E*(a**2*nu-a**2-2*b**2)/(a*(nu**2-1)*b);Kel[6][3] = -(1/8)*E/(-1+nu);
  Kel[6][4] = (1/12)*E*(a**2*nu-a**2+4*b**2)/(a*(nu**2-1)*b);Kel[6][5] = (1/8)*E*(3*nu-1)/(nu**2-1);
  Kel[6][6] = (1/6)*E*(a**2*nu-a**2-2*b**2)/(a*(nu**2-1)*b);Kel[6][7] = (1/8)*E/(-1+nu);
  Kel[7][0] = (1/8)*E*(3*nu-1)/(nu**2-1);Kel[7][1] = (1/12)*E*(b**2*nu+4*a**2-b**2)/(a*(nu**2-1)*b);
  Kel[7][2] = -(1/8)*E/(-1+nu);Kel[7][3] = (1/12)*E*(-b**2*nu+2*a**2+b**2)/(a*(nu**2-1)*b);
  Kel[7][4] = -(1/8)*E*(3*nu-1)/(nu**2-1);Kel[7][5] = -(1/6)*E*(b**2*nu+a**2-b**2)/(a*(nu**2-1)*b);
  Kel[7][6] = (1/8)*E/(-1+nu);Kel[7][7] = -(1/6)*E*(-b**2*nu+2*a**2+b**2)/(a*(nu**2-1)*b);

  Kel=t*Kel;
  return Kel

def EP_RQ4_ISO_MatrizDeRigidezDoElemento(E,nu,t,tipoestr,coordnos,no):
  Kel = np.zeros((8,8))
  x_1=coordnos[no[0]-1,0];
  x_2=coordnos[no[1]-1,0];        
  x_3=coordnos[no[2]-1,0];
  x_4=coordnos[no[3]-1,0];         
  y_1=coordnos[no[0]-1,1];
  y_2=coordnos[no[1]-1,1];  
  y_3=coordnos[no[2]-1,1];
  y_4=coordnos[no[3]-1,1];
  
  if tipoestr == "EPD":
    E = E/(1-nu**2)
    nu = nu/(1-nu)
  
  Kel[0][0] =((.1971687837*y_2-.1971687837*y_4)**2*E/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-.1971687837*x_2+.1971687837*x_4)**2*E*(.5000000000-.5000000000*nu)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2+.1443375673*y_3-.1971687837*y_4)**2*E/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2-.1443375673*x_3+.1971687837*x_4)**2*E*(.5000000000-.5000000000*nu)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*y_2-.1443375673*y_3-0.5283121635e-1*y_4)**2*E/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*x_2+.1443375673*x_3+0.5283121635e-1*x_4)**2*E*(.5000000000-.5000000000*nu)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2-0.5283121635e-1*y_4)**2*E/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2+0.5283121635e-1*x_4)**2*E*(.5000000000-.5000000000*nu)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[0][1] =((.1971687837*y_2-.1971687837*y_4)*E*nu*(-.1971687837*x_2+.1971687837*x_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-.1971687837*x_2+.1971687837*x_4)*E*(.5000000000-.5000000000*nu)*(.1971687837*y_2-.1971687837*y_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2+.1443375673*y_3-.1971687837*y_4)*E*nu*(-0.5283121635e-1*x_2-.1443375673*x_3+.1971687837*x_4)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2-.1443375673*x_3+.1971687837*x_4)*E*(.5000000000-.5000000000*nu)*(0.5283121635e-1*y_2+.1443375673*y_3-.1971687837*y_4)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*y_2-.1443375673*y_3-0.5283121635e-1*y_4)*E*nu*(-.1971687837*x_2+.1443375673*x_3+0.5283121635e-1*x_4)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*x_2+.1443375673*x_3+0.5283121635e-1*x_4)*E*(.5000000000-.5000000000*nu)*(.1971687837*y_2-.1443375673*y_3-0.5283121635e-1*y_4)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2-0.5283121635e-1*y_4)*E*nu*(-0.5283121635e-1*x_2+0.5283121635e-1*x_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2+0.5283121635e-1*x_4)*E*(.5000000000-.5000000000*nu)*(0.5283121635e-1*y_2-0.5283121635e-1*y_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[0][2] =((.1971687837*y_2-.1971687837*y_4)*E*(-.1971687837*y_1+0.5283121635e-1*y_3+.1443375673*y_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-.1971687837*x_2+.1971687837*x_4)*E*(.5000000000-.5000000000*nu)*(.1971687837*x_1-0.5283121635e-1*x_3-.1443375673*x_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2+.1443375673*y_3-.1971687837*y_4)*E*(-0.5283121635e-1*y_1+0.5283121635e-1*y_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2-.1443375673*x_3+.1971687837*x_4)*E*(.5000000000-.5000000000*nu)*(0.5283121635e-1*x_1-0.5283121635e-1*x_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*y_2-.1443375673*y_3-0.5283121635e-1*y_4)*E*(-.1971687837*y_1+.1971687837*y_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*x_2+.1443375673*x_3+0.5283121635e-1*x_4)*E*(.5000000000-.5000000000*nu)*(.1971687837*x_1-.1971687837*x_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2-0.5283121635e-1*y_4)*E*(-0.5283121635e-1*y_1+.1971687837*y_3-.1443375673*y_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2+0.5283121635e-1*x_4)*E*(.5000000000-.5000000000*nu)*(0.5283121635e-1*x_1-.1971687837*x_3+.1443375673*x_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[0][3] =((.1971687837*y_2-.1971687837*y_4)*E*nu*(.1971687837*x_1-0.5283121635e-1*x_3-.1443375673*x_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-.1971687837*x_2+.1971687837*x_4)*E*(.5000000000-.5000000000*nu)*(-.1971687837*y_1+0.5283121635e-1*y_3+.1443375673*y_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2+.1443375673*y_3-.1971687837*y_4)*E*nu*(0.5283121635e-1*x_1-0.5283121635e-1*x_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2-.1443375673*x_3+.1971687837*x_4)*E*(.5000000000-.5000000000*nu)*(-0.5283121635e-1*y_1+0.5283121635e-1*y_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*y_2-.1443375673*y_3-0.5283121635e-1*y_4)*E*nu*(.1971687837*x_1-.1971687837*x_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*x_2+.1443375673*x_3+0.5283121635e-1*x_4)*E*(.5000000000-.5000000000*nu)*(-.1971687837*y_1+.1971687837*y_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2-0.5283121635e-1*y_4)*E*nu*(0.5283121635e-1*x_1-.1971687837*x_3+.1443375673*x_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2+0.5283121635e-1*x_4)*E*(.5000000000-.5000000000*nu)*(-0.5283121635e-1*y_1+.1971687837*y_3-.1443375673*y_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[0][4] =((.1971687837*y_2-.1971687837*y_4)*E*(-0.5283121635e-1*y_2+0.5283121635e-1*y_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-.1971687837*x_2+.1971687837*x_4)*E*(.5000000000-.5000000000*nu)*(0.5283121635e-1*x_2-0.5283121635e-1*x_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2+.1443375673*y_3-.1971687837*y_4)*E*(-.1443375673*y_1-0.5283121635e-1*y_2+.1971687837*y_4)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2-.1443375673*x_3+.1971687837*x_4)*E*(.5000000000-.5000000000*nu)*(.1443375673*x_1+0.5283121635e-1*x_2-.1971687837*x_4)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*y_2-.1443375673*y_3-0.5283121635e-1*y_4)*E*(.1443375673*y_1-.1971687837*y_2+0.5283121635e-1*y_4)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*x_2+.1443375673*x_3+0.5283121635e-1*x_4)*E*(.5000000000-.5000000000*nu)*(-.1443375673*x_1+.1971687837*x_2-0.5283121635e-1*x_4)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2-0.5283121635e-1*y_4)*E*(-.1971687837*y_2+.1971687837*y_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2+0.5283121635e-1*x_4)*E*(.5000000000-.5000000000*nu)*(.1971687837*x_2-.1971687837*x_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[0][5] =((.1971687837*y_2-.1971687837*y_4)*E*nu*(0.5283121635e-1*x_2-0.5283121635e-1*x_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-.1971687837*x_2+.1971687837*x_4)*E*(.5000000000-.5000000000*nu)*(-0.5283121635e-1*y_2+0.5283121635e-1*y_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2+.1443375673*y_3-.1971687837*y_4)*E*nu*(.1443375673*x_1+0.5283121635e-1*x_2-.1971687837*x_4)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2-.1443375673*x_3+.1971687837*x_4)*E*(.5000000000-.5000000000*nu)*(-.1443375673*y_1-0.5283121635e-1*y_2+.1971687837*y_4)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*y_2-.1443375673*y_3-0.5283121635e-1*y_4)*E*nu*(-.1443375673*x_1+.1971687837*x_2-0.5283121635e-1*x_4)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*x_2+.1443375673*x_3+0.5283121635e-1*x_4)*E*(.5000000000-.5000000000*nu)*(.1443375673*y_1-.1971687837*y_2+0.5283121635e-1*y_4)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2-0.5283121635e-1*y_4)*E*nu*(.1971687837*x_2-.1971687837*x_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2+0.5283121635e-1*x_4)*E*(.5000000000-.5000000000*nu)*(-.1971687837*y_2+.1971687837*y_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[0][6] =((.1971687837*y_2-.1971687837*y_4)*E*(.1971687837*y_1-.1443375673*y_2-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-.1971687837*x_2+.1971687837*x_4)*E*(.5000000000-.5000000000*nu)*(-.1971687837*x_1+.1443375673*x_2+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2+.1443375673*y_3-.1971687837*y_4)*E*(.1971687837*y_1-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2-.1443375673*x_3+.1971687837*x_4)*E*(.5000000000-.5000000000*nu)*(-.1971687837*x_1+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*y_2-.1443375673*y_3-0.5283121635e-1*y_4)*E*(0.5283121635e-1*y_1-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*x_2+.1443375673*x_3+0.5283121635e-1*x_4)*E*(.5000000000-.5000000000*nu)*(-0.5283121635e-1*x_1+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2-0.5283121635e-1*y_4)*E*(0.5283121635e-1*y_1+.1443375673*y_2-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2+0.5283121635e-1*x_4)*E*(.5000000000-.5000000000*nu)*(-0.5283121635e-1*x_1-.1443375673*x_2+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[0][7] =((.1971687837*y_2-.1971687837*y_4)*E*nu*(-.1971687837*x_1+.1443375673*x_2+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-.1971687837*x_2+.1971687837*x_4)*E*(.5000000000-.5000000000*nu)*(.1971687837*y_1-.1443375673*y_2-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2+.1443375673*y_3-.1971687837*y_4)*E*nu*(-.1971687837*x_1+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2-.1443375673*x_3+.1971687837*x_4)*E*(.5000000000-.5000000000*nu)*(.1971687837*y_1-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*y_2-.1443375673*y_3-0.5283121635e-1*y_4)*E*nu*(-0.5283121635e-1*x_1+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*x_2+.1443375673*x_3+0.5283121635e-1*x_4)*E*(.5000000000-.5000000000*nu)*(0.5283121635e-1*y_1-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2-0.5283121635e-1*y_4)*E*nu*(-0.5283121635e-1*x_1-.1443375673*x_2+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2+0.5283121635e-1*x_4)*E*(.5000000000-.5000000000*nu)*(0.5283121635e-1*y_1+.1443375673*y_2-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[1][0] =((.1971687837*y_2-.1971687837*y_4)*E*nu*(-.1971687837*x_2+.1971687837*x_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-.1971687837*x_2+.1971687837*x_4)*E*(.5000000000-.5000000000*nu)*(.1971687837*y_2-.1971687837*y_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2+.1443375673*y_3-.1971687837*y_4)*E*nu*(-0.5283121635e-1*x_2-.1443375673*x_3+.1971687837*x_4)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2-.1443375673*x_3+.1971687837*x_4)*E*(.5000000000-.5000000000*nu)*(0.5283121635e-1*y_2+.1443375673*y_3-.1971687837*y_4)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*y_2-.1443375673*y_3-0.5283121635e-1*y_4)*E*nu*(-.1971687837*x_2+.1443375673*x_3+0.5283121635e-1*x_4)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*x_2+.1443375673*x_3+0.5283121635e-1*x_4)*E*(.5000000000-.5000000000*nu)*(.1971687837*y_2-.1443375673*y_3-0.5283121635e-1*y_4)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2-0.5283121635e-1*y_4)*E*nu*(-0.5283121635e-1*x_2+0.5283121635e-1*x_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2+0.5283121635e-1*x_4)*E*(.5000000000-.5000000000*nu)*(0.5283121635e-1*y_2-0.5283121635e-1*y_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[1][1] =((-.1971687837*x_2+.1971687837*x_4)**2*E/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(.1971687837*y_2-.1971687837*y_4)**2*E*(.5000000000-.5000000000*nu)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2-.1443375673*x_3+.1971687837*x_4)**2*E/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2+.1443375673*y_3-.1971687837*y_4)**2*E*(.5000000000-.5000000000*nu)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*x_2+.1443375673*x_3+0.5283121635e-1*x_4)**2*E/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*y_2-.1443375673*y_3-0.5283121635e-1*y_4)**2*E*(.5000000000-.5000000000*nu)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2+0.5283121635e-1*x_4)**2*E/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2-0.5283121635e-1*y_4)**2*E*(.5000000000-.5000000000*nu)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[1][2] =((-.1971687837*x_2+.1971687837*x_4)*E*nu*(-.1971687837*y_1+0.5283121635e-1*y_3+.1443375673*y_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(.1971687837*y_2-.1971687837*y_4)*E*(.5000000000-.5000000000*nu)*(.1971687837*x_1-0.5283121635e-1*x_3-.1443375673*x_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2-.1443375673*x_3+.1971687837*x_4)*E*nu*(-0.5283121635e-1*y_1+0.5283121635e-1*y_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2+.1443375673*y_3-.1971687837*y_4)*E*(.5000000000-.5000000000*nu)*(0.5283121635e-1*x_1-0.5283121635e-1*x_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*x_2+.1443375673*x_3+0.5283121635e-1*x_4)*E*nu*(-.1971687837*y_1+.1971687837*y_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*y_2-.1443375673*y_3-0.5283121635e-1*y_4)*E*(.5000000000-.5000000000*nu)*(.1971687837*x_1-.1971687837*x_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2+0.5283121635e-1*x_4)*E*nu*(-0.5283121635e-1*y_1+.1971687837*y_3-.1443375673*y_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2-0.5283121635e-1*y_4)*E*(.5000000000-.5000000000*nu)*(0.5283121635e-1*x_1-.1971687837*x_3+.1443375673*x_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[1][3] =((-.1971687837*x_2+.1971687837*x_4)*E*(.1971687837*x_1-0.5283121635e-1*x_3-.1443375673*x_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(.1971687837*y_2-.1971687837*y_4)*E*(.5000000000-.5000000000*nu)*(-.1971687837*y_1+0.5283121635e-1*y_3+.1443375673*y_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2-.1443375673*x_3+.1971687837*x_4)*E*(0.5283121635e-1*x_1-0.5283121635e-1*x_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2+.1443375673*y_3-.1971687837*y_4)*E*(.5000000000-.5000000000*nu)*(-0.5283121635e-1*y_1+0.5283121635e-1*y_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*x_2+.1443375673*x_3+0.5283121635e-1*x_4)*E*(.1971687837*x_1-.1971687837*x_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*y_2-.1443375673*y_3-0.5283121635e-1*y_4)*E*(.5000000000-.5000000000*nu)*(-.1971687837*y_1+.1971687837*y_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2+0.5283121635e-1*x_4)*E*(0.5283121635e-1*x_1-.1971687837*x_3+.1443375673*x_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2-0.5283121635e-1*y_4)*E*(.5000000000-.5000000000*nu)*(-0.5283121635e-1*y_1+.1971687837*y_3-.1443375673*y_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[1][4] =((-.1971687837*x_2+.1971687837*x_4)*E*nu*(-0.5283121635e-1*y_2+0.5283121635e-1*y_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(.1971687837*y_2-.1971687837*y_4)*E*(.5000000000-.5000000000*nu)*(0.5283121635e-1*x_2-0.5283121635e-1*x_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2-.1443375673*x_3+.1971687837*x_4)*E*nu*(-.1443375673*y_1-0.5283121635e-1*y_2+.1971687837*y_4)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2+.1443375673*y_3-.1971687837*y_4)*E*(.5000000000-.5000000000*nu)*(.1443375673*x_1+0.5283121635e-1*x_2-.1971687837*x_4)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*x_2+.1443375673*x_3+0.5283121635e-1*x_4)*E*nu*(.1443375673*y_1-.1971687837*y_2+0.5283121635e-1*y_4)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*y_2-.1443375673*y_3-0.5283121635e-1*y_4)*E*(.5000000000-.5000000000*nu)*(-.1443375673*x_1+.1971687837*x_2-0.5283121635e-1*x_4)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2+0.5283121635e-1*x_4)*E*nu*(-.1971687837*y_2+.1971687837*y_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2-0.5283121635e-1*y_4)*E*(.5000000000-.5000000000*nu)*(.1971687837*x_2-.1971687837*x_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[1][5] =((-.1971687837*x_2+.1971687837*x_4)*E*(0.5283121635e-1*x_2-0.5283121635e-1*x_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(.1971687837*y_2-.1971687837*y_4)*E*(.5000000000-.5000000000*nu)*(-0.5283121635e-1*y_2+0.5283121635e-1*y_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2-.1443375673*x_3+.1971687837*x_4)*E*(.1443375673*x_1+0.5283121635e-1*x_2-.1971687837*x_4)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2+.1443375673*y_3-.1971687837*y_4)*E*(.5000000000-.5000000000*nu)*(-.1443375673*y_1-0.5283121635e-1*y_2+.1971687837*y_4)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*x_2+.1443375673*x_3+0.5283121635e-1*x_4)*E*(-.1443375673*x_1+.1971687837*x_2-0.5283121635e-1*x_4)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*y_2-.1443375673*y_3-0.5283121635e-1*y_4)*E*(.5000000000-.5000000000*nu)*(.1443375673*y_1-.1971687837*y_2+0.5283121635e-1*y_4)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2+0.5283121635e-1*x_4)*E*(.1971687837*x_2-.1971687837*x_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2-0.5283121635e-1*y_4)*E*(.5000000000-.5000000000*nu)*(-.1971687837*y_2+.1971687837*y_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[1][6] =((-.1971687837*x_2+.1971687837*x_4)*E*nu*(.1971687837*y_1-.1443375673*y_2-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(.1971687837*y_2-.1971687837*y_4)*E*(.5000000000-.5000000000*nu)*(-.1971687837*x_1+.1443375673*x_2+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2-.1443375673*x_3+.1971687837*x_4)*E*nu*(.1971687837*y_1-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2+.1443375673*y_3-.1971687837*y_4)*E*(.5000000000-.5000000000*nu)*(-.1971687837*x_1+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*x_2+.1443375673*x_3+0.5283121635e-1*x_4)*E*nu*(0.5283121635e-1*y_1-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*y_2-.1443375673*y_3-0.5283121635e-1*y_4)*E*(.5000000000-.5000000000*nu)*(-0.5283121635e-1*x_1+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2+0.5283121635e-1*x_4)*E*nu*(0.5283121635e-1*y_1+.1443375673*y_2-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2-0.5283121635e-1*y_4)*E*(.5000000000-.5000000000*nu)*(-0.5283121635e-1*x_1-.1443375673*x_2+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[1][7] =((-.1971687837*x_2+.1971687837*x_4)*E*(-.1971687837*x_1+.1443375673*x_2+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(.1971687837*y_2-.1971687837*y_4)*E*(.5000000000-.5000000000*nu)*(.1971687837*y_1-.1443375673*y_2-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2-.1443375673*x_3+.1971687837*x_4)*E*(-.1971687837*x_1+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2+.1443375673*y_3-.1971687837*y_4)*E*(.5000000000-.5000000000*nu)*(.1971687837*y_1-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*x_2+.1443375673*x_3+0.5283121635e-1*x_4)*E*(-0.5283121635e-1*x_1+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*y_2-.1443375673*y_3-0.5283121635e-1*y_4)*E*(.5000000000-.5000000000*nu)*(0.5283121635e-1*y_1-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2+0.5283121635e-1*x_4)*E*(-0.5283121635e-1*x_1-.1443375673*x_2+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2-0.5283121635e-1*y_4)*E*(.5000000000-.5000000000*nu)*(0.5283121635e-1*y_1+.1443375673*y_2-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[2][0] =((.1971687837*y_2-.1971687837*y_4)*E*(-.1971687837*y_1+0.5283121635e-1*y_3+.1443375673*y_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-.1971687837*x_2+.1971687837*x_4)*E*(.5000000000-.5000000000*nu)*(.1971687837*x_1-0.5283121635e-1*x_3-.1443375673*x_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2+.1443375673*y_3-.1971687837*y_4)*E*(-0.5283121635e-1*y_1+0.5283121635e-1*y_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2-.1443375673*x_3+.1971687837*x_4)*E*(.5000000000-.5000000000*nu)*(0.5283121635e-1*x_1-0.5283121635e-1*x_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*y_2-.1443375673*y_3-0.5283121635e-1*y_4)*E*(-.1971687837*y_1+.1971687837*y_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*x_2+.1443375673*x_3+0.5283121635e-1*x_4)*E*(.5000000000-.5000000000*nu)*(.1971687837*x_1-.1971687837*x_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2-0.5283121635e-1*y_4)*E*(-0.5283121635e-1*y_1+.1971687837*y_3-.1443375673*y_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2+0.5283121635e-1*x_4)*E*(.5000000000-.5000000000*nu)*(0.5283121635e-1*x_1-.1971687837*x_3+.1443375673*x_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[2][1] =((-.1971687837*x_2+.1971687837*x_4)*E*nu*(-.1971687837*y_1+0.5283121635e-1*y_3+.1443375673*y_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(.1971687837*y_2-.1971687837*y_4)*E*(.5000000000-.5000000000*nu)*(.1971687837*x_1-0.5283121635e-1*x_3-.1443375673*x_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2-.1443375673*x_3+.1971687837*x_4)*E*nu*(-0.5283121635e-1*y_1+0.5283121635e-1*y_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2+.1443375673*y_3-.1971687837*y_4)*E*(.5000000000-.5000000000*nu)*(0.5283121635e-1*x_1-0.5283121635e-1*x_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*x_2+.1443375673*x_3+0.5283121635e-1*x_4)*E*nu*(-.1971687837*y_1+.1971687837*y_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*y_2-.1443375673*y_3-0.5283121635e-1*y_4)*E*(.5000000000-.5000000000*nu)*(.1971687837*x_1-.1971687837*x_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2+0.5283121635e-1*x_4)*E*nu*(-0.5283121635e-1*y_1+.1971687837*y_3-.1443375673*y_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2-0.5283121635e-1*y_4)*E*(.5000000000-.5000000000*nu)*(0.5283121635e-1*x_1-.1971687837*x_3+.1443375673*x_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[2][2] =((-.1971687837*y_1+0.5283121635e-1*y_3+.1443375673*y_4)**2*E/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(.1971687837*x_1-0.5283121635e-1*x_3-.1443375673*x_4)**2*E*(.5000000000-.5000000000*nu)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*y_1+0.5283121635e-1*y_3)**2*E/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*x_1-0.5283121635e-1*x_3)**2*E*(.5000000000-.5000000000*nu)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*y_1+.1971687837*y_3)**2*E/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*x_1-.1971687837*x_3)**2*E*(.5000000000-.5000000000*nu)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*y_1+.1971687837*y_3-.1443375673*y_4)**2*E/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*x_1-.1971687837*x_3+.1443375673*x_4)**2*E*(.5000000000-.5000000000*nu)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[2][3] =((-.1971687837*y_1+0.5283121635e-1*y_3+.1443375673*y_4)*E*nu*(.1971687837*x_1-0.5283121635e-1*x_3-.1443375673*x_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(.1971687837*x_1-0.5283121635e-1*x_3-.1443375673*x_4)*E*(.5000000000-.5000000000*nu)*(-.1971687837*y_1+0.5283121635e-1*y_3+.1443375673*y_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*y_1+0.5283121635e-1*y_3)*E*nu*(0.5283121635e-1*x_1-0.5283121635e-1*x_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*x_1-0.5283121635e-1*x_3)*E*(.5000000000-.5000000000*nu)*(-0.5283121635e-1*y_1+0.5283121635e-1*y_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*y_1+.1971687837*y_3)*E*nu*(.1971687837*x_1-.1971687837*x_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*x_1-.1971687837*x_3)*E*(.5000000000-.5000000000*nu)*(-.1971687837*y_1+.1971687837*y_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*y_1+.1971687837*y_3-.1443375673*y_4)*E*nu*(0.5283121635e-1*x_1-.1971687837*x_3+.1443375673*x_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*x_1-.1971687837*x_3+.1443375673*x_4)*E*(.5000000000-.5000000000*nu)*(-0.5283121635e-1*y_1+.1971687837*y_3-.1443375673*y_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[2][4] =((-.1971687837*y_1+0.5283121635e-1*y_3+.1443375673*y_4)*E*(-0.5283121635e-1*y_2+0.5283121635e-1*y_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(.1971687837*x_1-0.5283121635e-1*x_3-.1443375673*x_4)*E*(.5000000000-.5000000000*nu)*(0.5283121635e-1*x_2-0.5283121635e-1*x_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*y_1+0.5283121635e-1*y_3)*E*(-.1443375673*y_1-0.5283121635e-1*y_2+.1971687837*y_4)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*x_1-0.5283121635e-1*x_3)*E*(.5000000000-.5000000000*nu)*(.1443375673*x_1+0.5283121635e-1*x_2-.1971687837*x_4)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*y_1+.1971687837*y_3)*E*(.1443375673*y_1-.1971687837*y_2+0.5283121635e-1*y_4)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*x_1-.1971687837*x_3)*E*(.5000000000-.5000000000*nu)*(-.1443375673*x_1+.1971687837*x_2-0.5283121635e-1*x_4)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*y_1+.1971687837*y_3-.1443375673*y_4)*E*(-.1971687837*y_2+.1971687837*y_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*x_1-.1971687837*x_3+.1443375673*x_4)*E*(.5000000000-.5000000000*nu)*(.1971687837*x_2-.1971687837*x_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[2][5] =((-.1971687837*y_1+0.5283121635e-1*y_3+.1443375673*y_4)*E*nu*(0.5283121635e-1*x_2-0.5283121635e-1*x_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(.1971687837*x_1-0.5283121635e-1*x_3-.1443375673*x_4)*E*(.5000000000-.5000000000*nu)*(-0.5283121635e-1*y_2+0.5283121635e-1*y_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*y_1+0.5283121635e-1*y_3)*E*nu*(.1443375673*x_1+0.5283121635e-1*x_2-.1971687837*x_4)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*x_1-0.5283121635e-1*x_3)*E*(.5000000000-.5000000000*nu)*(-.1443375673*y_1-0.5283121635e-1*y_2+.1971687837*y_4)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*y_1+.1971687837*y_3)*E*nu*(-.1443375673*x_1+.1971687837*x_2-0.5283121635e-1*x_4)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*x_1-.1971687837*x_3)*E*(.5000000000-.5000000000*nu)*(.1443375673*y_1-.1971687837*y_2+0.5283121635e-1*y_4)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*y_1+.1971687837*y_3-.1443375673*y_4)*E*nu*(.1971687837*x_2-.1971687837*x_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*x_1-.1971687837*x_3+.1443375673*x_4)*E*(.5000000000-.5000000000*nu)*(-.1971687837*y_2+.1971687837*y_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[2][6] =((-.1971687837*y_1+0.5283121635e-1*y_3+.1443375673*y_4)*E*(.1971687837*y_1-.1443375673*y_2-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(.1971687837*x_1-0.5283121635e-1*x_3-.1443375673*x_4)*E*(.5000000000-.5000000000*nu)*(-.1971687837*x_1+.1443375673*x_2+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*y_1+0.5283121635e-1*y_3)*E*(.1971687837*y_1-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*x_1-0.5283121635e-1*x_3)*E*(.5000000000-.5000000000*nu)*(-.1971687837*x_1+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*y_1+.1971687837*y_3)*E*(0.5283121635e-1*y_1-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*x_1-.1971687837*x_3)*E*(.5000000000-.5000000000*nu)*(-0.5283121635e-1*x_1+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*y_1+.1971687837*y_3-.1443375673*y_4)*E*(0.5283121635e-1*y_1+.1443375673*y_2-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*x_1-.1971687837*x_3+.1443375673*x_4)*E*(.5000000000-.5000000000*nu)*(-0.5283121635e-1*x_1-.1443375673*x_2+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[2][7] =((-.1971687837*y_1+0.5283121635e-1*y_3+.1443375673*y_4)*E*nu*(-.1971687837*x_1+.1443375673*x_2+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(.1971687837*x_1-0.5283121635e-1*x_3-.1443375673*x_4)*E*(.5000000000-.5000000000*nu)*(.1971687837*y_1-.1443375673*y_2-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*y_1+0.5283121635e-1*y_3)*E*nu*(-.1971687837*x_1+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*x_1-0.5283121635e-1*x_3)*E*(.5000000000-.5000000000*nu)*(.1971687837*y_1-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*y_1+.1971687837*y_3)*E*nu*(-0.5283121635e-1*x_1+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*x_1-.1971687837*x_3)*E*(.5000000000-.5000000000*nu)*(0.5283121635e-1*y_1-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*y_1+.1971687837*y_3-.1443375673*y_4)*E*nu*(-0.5283121635e-1*x_1-.1443375673*x_2+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*x_1-.1971687837*x_3+.1443375673*x_4)*E*(.5000000000-.5000000000*nu)*(0.5283121635e-1*y_1+.1443375673*y_2-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[3][0] =((.1971687837*y_2-.1971687837*y_4)*E*nu*(.1971687837*x_1-0.5283121635e-1*x_3-.1443375673*x_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-.1971687837*x_2+.1971687837*x_4)*E*(.5000000000-.5000000000*nu)*(-.1971687837*y_1+0.5283121635e-1*y_3+.1443375673*y_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2+.1443375673*y_3-.1971687837*y_4)*E*nu*(0.5283121635e-1*x_1-0.5283121635e-1*x_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2-.1443375673*x_3+.1971687837*x_4)*E*(.5000000000-.5000000000*nu)*(-0.5283121635e-1*y_1+0.5283121635e-1*y_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*y_2-.1443375673*y_3-0.5283121635e-1*y_4)*E*nu*(.1971687837*x_1-.1971687837*x_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*x_2+.1443375673*x_3+0.5283121635e-1*x_4)*E*(.5000000000-.5000000000*nu)*(-.1971687837*y_1+.1971687837*y_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2-0.5283121635e-1*y_4)*E*nu*(0.5283121635e-1*x_1-.1971687837*x_3+.1443375673*x_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2+0.5283121635e-1*x_4)*E*(.5000000000-.5000000000*nu)*(-0.5283121635e-1*y_1+.1971687837*y_3-.1443375673*y_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[3][1] =((-.1971687837*x_2+.1971687837*x_4)*E*(.1971687837*x_1-0.5283121635e-1*x_3-.1443375673*x_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(.1971687837*y_2-.1971687837*y_4)*E*(.5000000000-.5000000000*nu)*(-.1971687837*y_1+0.5283121635e-1*y_3+.1443375673*y_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2-.1443375673*x_3+.1971687837*x_4)*E*(0.5283121635e-1*x_1-0.5283121635e-1*x_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2+.1443375673*y_3-.1971687837*y_4)*E*(.5000000000-.5000000000*nu)*(-0.5283121635e-1*y_1+0.5283121635e-1*y_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*x_2+.1443375673*x_3+0.5283121635e-1*x_4)*E*(.1971687837*x_1-.1971687837*x_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*y_2-.1443375673*y_3-0.5283121635e-1*y_4)*E*(.5000000000-.5000000000*nu)*(-.1971687837*y_1+.1971687837*y_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2+0.5283121635e-1*x_4)*E*(0.5283121635e-1*x_1-.1971687837*x_3+.1443375673*x_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2-0.5283121635e-1*y_4)*E*(.5000000000-.5000000000*nu)*(-0.5283121635e-1*y_1+.1971687837*y_3-.1443375673*y_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[3][2] =((-.1971687837*y_1+0.5283121635e-1*y_3+.1443375673*y_4)*E*nu*(.1971687837*x_1-0.5283121635e-1*x_3-.1443375673*x_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(.1971687837*x_1-0.5283121635e-1*x_3-.1443375673*x_4)*E*(.5000000000-.5000000000*nu)*(-.1971687837*y_1+0.5283121635e-1*y_3+.1443375673*y_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*y_1+0.5283121635e-1*y_3)*E*nu*(0.5283121635e-1*x_1-0.5283121635e-1*x_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*x_1-0.5283121635e-1*x_3)*E*(.5000000000-.5000000000*nu)*(-0.5283121635e-1*y_1+0.5283121635e-1*y_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*y_1+.1971687837*y_3)*E*nu*(.1971687837*x_1-.1971687837*x_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*x_1-.1971687837*x_3)*E*(.5000000000-.5000000000*nu)*(-.1971687837*y_1+.1971687837*y_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*y_1+.1971687837*y_3-.1443375673*y_4)*E*nu*(0.5283121635e-1*x_1-.1971687837*x_3+.1443375673*x_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*x_1-.1971687837*x_3+.1443375673*x_4)*E*(.5000000000-.5000000000*nu)*(-0.5283121635e-1*y_1+.1971687837*y_3-.1443375673*y_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[3][3] =((.1971687837*x_1-0.5283121635e-1*x_3-.1443375673*x_4)**2*E/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-.1971687837*y_1+0.5283121635e-1*y_3+.1443375673*y_4)**2*E*(.5000000000-.5000000000*nu)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*x_1-0.5283121635e-1*x_3)**2*E/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*y_1+0.5283121635e-1*y_3)**2*E*(.5000000000-.5000000000*nu)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*x_1-.1971687837*x_3)**2*E/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*y_1+.1971687837*y_3)**2*E*(.5000000000-.5000000000*nu)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*x_1-.1971687837*x_3+.1443375673*x_4)**2*E/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*y_1+.1971687837*y_3-.1443375673*y_4)**2*E*(.5000000000-.5000000000*nu)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[3][4] =((.1971687837*x_1-0.5283121635e-1*x_3-.1443375673*x_4)*E*nu*(-0.5283121635e-1*y_2+0.5283121635e-1*y_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-.1971687837*y_1+0.5283121635e-1*y_3+.1443375673*y_4)*E*(.5000000000-.5000000000*nu)*(0.5283121635e-1*x_2-0.5283121635e-1*x_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*x_1-0.5283121635e-1*x_3)*E*nu*(-.1443375673*y_1-0.5283121635e-1*y_2+.1971687837*y_4)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*y_1+0.5283121635e-1*y_3)*E*(.5000000000-.5000000000*nu)*(.1443375673*x_1+0.5283121635e-1*x_2-.1971687837*x_4)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*x_1-.1971687837*x_3)*E*nu*(.1443375673*y_1-.1971687837*y_2+0.5283121635e-1*y_4)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*y_1+.1971687837*y_3)*E*(.5000000000-.5000000000*nu)*(-.1443375673*x_1+.1971687837*x_2-0.5283121635e-1*x_4)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*x_1-.1971687837*x_3+.1443375673*x_4)*E*nu*(-.1971687837*y_2+.1971687837*y_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*y_1+.1971687837*y_3-.1443375673*y_4)*E*(.5000000000-.5000000000*nu)*(.1971687837*x_2-.1971687837*x_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[3][5] =((.1971687837*x_1-0.5283121635e-1*x_3-.1443375673*x_4)*E*(0.5283121635e-1*x_2-0.5283121635e-1*x_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-.1971687837*y_1+0.5283121635e-1*y_3+.1443375673*y_4)*E*(.5000000000-.5000000000*nu)*(-0.5283121635e-1*y_2+0.5283121635e-1*y_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*x_1-0.5283121635e-1*x_3)*E*(.1443375673*x_1+0.5283121635e-1*x_2-.1971687837*x_4)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*y_1+0.5283121635e-1*y_3)*E*(.5000000000-.5000000000*nu)*(-.1443375673*y_1-0.5283121635e-1*y_2+.1971687837*y_4)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*x_1-.1971687837*x_3)*E*(-.1443375673*x_1+.1971687837*x_2-0.5283121635e-1*x_4)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*y_1+.1971687837*y_3)*E*(.5000000000-.5000000000*nu)*(.1443375673*y_1-.1971687837*y_2+0.5283121635e-1*y_4)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*x_1-.1971687837*x_3+.1443375673*x_4)*E*(.1971687837*x_2-.1971687837*x_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*y_1+.1971687837*y_3-.1443375673*y_4)*E*(.5000000000-.5000000000*nu)*(-.1971687837*y_2+.1971687837*y_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[3][6] =((.1971687837*x_1-0.5283121635e-1*x_3-.1443375673*x_4)*E*nu*(.1971687837*y_1-.1443375673*y_2-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-.1971687837*y_1+0.5283121635e-1*y_3+.1443375673*y_4)*E*(.5000000000-.5000000000*nu)*(-.1971687837*x_1+.1443375673*x_2+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*x_1-0.5283121635e-1*x_3)*E*nu*(.1971687837*y_1-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*y_1+0.5283121635e-1*y_3)*E*(.5000000000-.5000000000*nu)*(-.1971687837*x_1+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*x_1-.1971687837*x_3)*E*nu*(0.5283121635e-1*y_1-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*y_1+.1971687837*y_3)*E*(.5000000000-.5000000000*nu)*(-0.5283121635e-1*x_1+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*x_1-.1971687837*x_3+.1443375673*x_4)*E*nu*(0.5283121635e-1*y_1+.1443375673*y_2-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*y_1+.1971687837*y_3-.1443375673*y_4)*E*(.5000000000-.5000000000*nu)*(-0.5283121635e-1*x_1-.1443375673*x_2+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[3][7] =((.1971687837*x_1-0.5283121635e-1*x_3-.1443375673*x_4)*E*(-.1971687837*x_1+.1443375673*x_2+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-.1971687837*y_1+0.5283121635e-1*y_3+.1443375673*y_4)*E*(.5000000000-.5000000000*nu)*(.1971687837*y_1-.1443375673*y_2-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*x_1-0.5283121635e-1*x_3)*E*(-.1971687837*x_1+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*y_1+0.5283121635e-1*y_3)*E*(.5000000000-.5000000000*nu)*(.1971687837*y_1-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*x_1-.1971687837*x_3)*E*(-0.5283121635e-1*x_1+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*y_1+.1971687837*y_3)*E*(.5000000000-.5000000000*nu)*(0.5283121635e-1*y_1-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*x_1-.1971687837*x_3+.1443375673*x_4)*E*(-0.5283121635e-1*x_1-.1443375673*x_2+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*y_1+.1971687837*y_3-.1443375673*y_4)*E*(.5000000000-.5000000000*nu)*(0.5283121635e-1*y_1+.1443375673*y_2-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[4][0] =((.1971687837*y_2-.1971687837*y_4)*E*(-0.5283121635e-1*y_2+0.5283121635e-1*y_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-.1971687837*x_2+.1971687837*x_4)*E*(.5000000000-.5000000000*nu)*(0.5283121635e-1*x_2-0.5283121635e-1*x_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2+.1443375673*y_3-.1971687837*y_4)*E*(-.1443375673*y_1-0.5283121635e-1*y_2+.1971687837*y_4)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2-.1443375673*x_3+.1971687837*x_4)*E*(.5000000000-.5000000000*nu)*(.1443375673*x_1+0.5283121635e-1*x_2-.1971687837*x_4)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*y_2-.1443375673*y_3-0.5283121635e-1*y_4)*E*(.1443375673*y_1-.1971687837*y_2+0.5283121635e-1*y_4)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*x_2+.1443375673*x_3+0.5283121635e-1*x_4)*E*(.5000000000-.5000000000*nu)*(-.1443375673*x_1+.1971687837*x_2-0.5283121635e-1*x_4)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2-0.5283121635e-1*y_4)*E*(-.1971687837*y_2+.1971687837*y_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2+0.5283121635e-1*x_4)*E*(.5000000000-.5000000000*nu)*(.1971687837*x_2-.1971687837*x_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[4][1] =((-.1971687837*x_2+.1971687837*x_4)*E*nu*(-0.5283121635e-1*y_2+0.5283121635e-1*y_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(.1971687837*y_2-.1971687837*y_4)*E*(.5000000000-.5000000000*nu)*(0.5283121635e-1*x_2-0.5283121635e-1*x_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2-.1443375673*x_3+.1971687837*x_4)*E*nu*(-.1443375673*y_1-0.5283121635e-1*y_2+.1971687837*y_4)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2+.1443375673*y_3-.1971687837*y_4)*E*(.5000000000-.5000000000*nu)*(.1443375673*x_1+0.5283121635e-1*x_2-.1971687837*x_4)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*x_2+.1443375673*x_3+0.5283121635e-1*x_4)*E*nu*(.1443375673*y_1-.1971687837*y_2+0.5283121635e-1*y_4)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*y_2-.1443375673*y_3-0.5283121635e-1*y_4)*E*(.5000000000-.5000000000*nu)*(-.1443375673*x_1+.1971687837*x_2-0.5283121635e-1*x_4)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2+0.5283121635e-1*x_4)*E*nu*(-.1971687837*y_2+.1971687837*y_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2-0.5283121635e-1*y_4)*E*(.5000000000-.5000000000*nu)*(.1971687837*x_2-.1971687837*x_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[4][2] =((-.1971687837*y_1+0.5283121635e-1*y_3+.1443375673*y_4)*E*(-0.5283121635e-1*y_2+0.5283121635e-1*y_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(.1971687837*x_1-0.5283121635e-1*x_3-.1443375673*x_4)*E*(.5000000000-.5000000000*nu)*(0.5283121635e-1*x_2-0.5283121635e-1*x_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*y_1+0.5283121635e-1*y_3)*E*(-.1443375673*y_1-0.5283121635e-1*y_2+.1971687837*y_4)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*x_1-0.5283121635e-1*x_3)*E*(.5000000000-.5000000000*nu)*(.1443375673*x_1+0.5283121635e-1*x_2-.1971687837*x_4)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*y_1+.1971687837*y_3)*E*(.1443375673*y_1-.1971687837*y_2+0.5283121635e-1*y_4)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*x_1-.1971687837*x_3)*E*(.5000000000-.5000000000*nu)*(-.1443375673*x_1+.1971687837*x_2-0.5283121635e-1*x_4)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*y_1+.1971687837*y_3-.1443375673*y_4)*E*(-.1971687837*y_2+.1971687837*y_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*x_1-.1971687837*x_3+.1443375673*x_4)*E*(.5000000000-.5000000000*nu)*(.1971687837*x_2-.1971687837*x_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[4][3] =((.1971687837*x_1-0.5283121635e-1*x_3-.1443375673*x_4)*E*nu*(-0.5283121635e-1*y_2+0.5283121635e-1*y_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-.1971687837*y_1+0.5283121635e-1*y_3+.1443375673*y_4)*E*(.5000000000-.5000000000*nu)*(0.5283121635e-1*x_2-0.5283121635e-1*x_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*x_1-0.5283121635e-1*x_3)*E*nu*(-.1443375673*y_1-0.5283121635e-1*y_2+.1971687837*y_4)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*y_1+0.5283121635e-1*y_3)*E*(.5000000000-.5000000000*nu)*(.1443375673*x_1+0.5283121635e-1*x_2-.1971687837*x_4)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*x_1-.1971687837*x_3)*E*nu*(.1443375673*y_1-.1971687837*y_2+0.5283121635e-1*y_4)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*y_1+.1971687837*y_3)*E*(.5000000000-.5000000000*nu)*(-.1443375673*x_1+.1971687837*x_2-0.5283121635e-1*x_4)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*x_1-.1971687837*x_3+.1443375673*x_4)*E*nu*(-.1971687837*y_2+.1971687837*y_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*y_1+.1971687837*y_3-.1443375673*y_4)*E*(.5000000000-.5000000000*nu)*(.1971687837*x_2-.1971687837*x_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[4][4] =((-0.5283121635e-1*y_2+0.5283121635e-1*y_4)**2*E/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*x_2-0.5283121635e-1*x_4)**2*E*(.5000000000-.5000000000*nu)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-.1443375673*y_1-0.5283121635e-1*y_2+.1971687837*y_4)**2*E/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1443375673*x_1+0.5283121635e-1*x_2-.1971687837*x_4)**2*E*(.5000000000-.5000000000*nu)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1443375673*y_1-.1971687837*y_2+0.5283121635e-1*y_4)**2*E/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1443375673*x_1+.1971687837*x_2-0.5283121635e-1*x_4)**2*E*(.5000000000-.5000000000*nu)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*y_2+.1971687837*y_4)**2*E/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(.1971687837*x_2-.1971687837*x_4)**2*E*(.5000000000-.5000000000*nu)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[4][5] =((-0.5283121635e-1*y_2+0.5283121635e-1*y_4)*E*nu*(0.5283121635e-1*x_2-0.5283121635e-1*x_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*x_2-0.5283121635e-1*x_4)*E*(.5000000000-.5000000000*nu)*(-0.5283121635e-1*y_2+0.5283121635e-1*y_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-.1443375673*y_1-0.5283121635e-1*y_2+.1971687837*y_4)*E*nu*(.1443375673*x_1+0.5283121635e-1*x_2-.1971687837*x_4)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1443375673*x_1+0.5283121635e-1*x_2-.1971687837*x_4)*E*(.5000000000-.5000000000*nu)*(-.1443375673*y_1-0.5283121635e-1*y_2+.1971687837*y_4)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1443375673*y_1-.1971687837*y_2+0.5283121635e-1*y_4)*E*nu*(-.1443375673*x_1+.1971687837*x_2-0.5283121635e-1*x_4)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1443375673*x_1+.1971687837*x_2-0.5283121635e-1*x_4)*E*(.5000000000-.5000000000*nu)*(.1443375673*y_1-.1971687837*y_2+0.5283121635e-1*y_4)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*y_2+.1971687837*y_4)*E*nu*(.1971687837*x_2-.1971687837*x_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(.1971687837*x_2-.1971687837*x_4)*E*(.5000000000-.5000000000*nu)*(-.1971687837*y_2+.1971687837*y_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[4][6] =((-0.5283121635e-1*y_2+0.5283121635e-1*y_4)*E*(.1971687837*y_1-.1443375673*y_2-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*x_2-0.5283121635e-1*x_4)*E*(.5000000000-.5000000000*nu)*(-.1971687837*x_1+.1443375673*x_2+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-.1443375673*y_1-0.5283121635e-1*y_2+.1971687837*y_4)*E*(.1971687837*y_1-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1443375673*x_1+0.5283121635e-1*x_2-.1971687837*x_4)*E*(.5000000000-.5000000000*nu)*(-.1971687837*x_1+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1443375673*y_1-.1971687837*y_2+0.5283121635e-1*y_4)*E*(0.5283121635e-1*y_1-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1443375673*x_1+.1971687837*x_2-0.5283121635e-1*x_4)*E*(.5000000000-.5000000000*nu)*(-0.5283121635e-1*x_1+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*y_2+.1971687837*y_4)*E*(0.5283121635e-1*y_1+.1443375673*y_2-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(.1971687837*x_2-.1971687837*x_4)*E*(.5000000000-.5000000000*nu)*(-0.5283121635e-1*x_1-.1443375673*x_2+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[4][7] =((-0.5283121635e-1*y_2+0.5283121635e-1*y_4)*E*nu*(-.1971687837*x_1+.1443375673*x_2+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*x_2-0.5283121635e-1*x_4)*E*(.5000000000-.5000000000*nu)*(.1971687837*y_1-.1443375673*y_2-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-.1443375673*y_1-0.5283121635e-1*y_2+.1971687837*y_4)*E*nu*(-.1971687837*x_1+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1443375673*x_1+0.5283121635e-1*x_2-.1971687837*x_4)*E*(.5000000000-.5000000000*nu)*(.1971687837*y_1-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1443375673*y_1-.1971687837*y_2+0.5283121635e-1*y_4)*E*nu*(-0.5283121635e-1*x_1+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1443375673*x_1+.1971687837*x_2-0.5283121635e-1*x_4)*E*(.5000000000-.5000000000*nu)*(0.5283121635e-1*y_1-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*y_2+.1971687837*y_4)*E*nu*(-0.5283121635e-1*x_1-.1443375673*x_2+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(.1971687837*x_2-.1971687837*x_4)*E*(.5000000000-.5000000000*nu)*(0.5283121635e-1*y_1+.1443375673*y_2-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[5][0] =((.1971687837*y_2-.1971687837*y_4)*E*nu*(0.5283121635e-1*x_2-0.5283121635e-1*x_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-.1971687837*x_2+.1971687837*x_4)*E*(.5000000000-.5000000000*nu)*(-0.5283121635e-1*y_2+0.5283121635e-1*y_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2+.1443375673*y_3-.1971687837*y_4)*E*nu*(.1443375673*x_1+0.5283121635e-1*x_2-.1971687837*x_4)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2-.1443375673*x_3+.1971687837*x_4)*E*(.5000000000-.5000000000*nu)*(-.1443375673*y_1-0.5283121635e-1*y_2+.1971687837*y_4)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*y_2-.1443375673*y_3-0.5283121635e-1*y_4)*E*nu*(-.1443375673*x_1+.1971687837*x_2-0.5283121635e-1*x_4)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*x_2+.1443375673*x_3+0.5283121635e-1*x_4)*E*(.5000000000-.5000000000*nu)*(.1443375673*y_1-.1971687837*y_2+0.5283121635e-1*y_4)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2-0.5283121635e-1*y_4)*E*nu*(.1971687837*x_2-.1971687837*x_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2+0.5283121635e-1*x_4)*E*(.5000000000-.5000000000*nu)*(-.1971687837*y_2+.1971687837*y_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[5][1] =((-.1971687837*x_2+.1971687837*x_4)*E*(0.5283121635e-1*x_2-0.5283121635e-1*x_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(.1971687837*y_2-.1971687837*y_4)*E*(.5000000000-.5000000000*nu)*(-0.5283121635e-1*y_2+0.5283121635e-1*y_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2-.1443375673*x_3+.1971687837*x_4)*E*(.1443375673*x_1+0.5283121635e-1*x_2-.1971687837*x_4)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2+.1443375673*y_3-.1971687837*y_4)*E*(.5000000000-.5000000000*nu)*(-.1443375673*y_1-0.5283121635e-1*y_2+.1971687837*y_4)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*x_2+.1443375673*x_3+0.5283121635e-1*x_4)*E*(-.1443375673*x_1+.1971687837*x_2-0.5283121635e-1*x_4)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*y_2-.1443375673*y_3-0.5283121635e-1*y_4)*E*(.5000000000-.5000000000*nu)*(.1443375673*y_1-.1971687837*y_2+0.5283121635e-1*y_4)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2+0.5283121635e-1*x_4)*E*(.1971687837*x_2-.1971687837*x_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2-0.5283121635e-1*y_4)*E*(.5000000000-.5000000000*nu)*(-.1971687837*y_2+.1971687837*y_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[5][2] =((-.1971687837*y_1+0.5283121635e-1*y_3+.1443375673*y_4)*E*nu*(0.5283121635e-1*x_2-0.5283121635e-1*x_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(.1971687837*x_1-0.5283121635e-1*x_3-.1443375673*x_4)*E*(.5000000000-.5000000000*nu)*(-0.5283121635e-1*y_2+0.5283121635e-1*y_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*y_1+0.5283121635e-1*y_3)*E*nu*(.1443375673*x_1+0.5283121635e-1*x_2-.1971687837*x_4)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*x_1-0.5283121635e-1*x_3)*E*(.5000000000-.5000000000*nu)*(-.1443375673*y_1-0.5283121635e-1*y_2+.1971687837*y_4)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*y_1+.1971687837*y_3)*E*nu*(-.1443375673*x_1+.1971687837*x_2-0.5283121635e-1*x_4)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*x_1-.1971687837*x_3)*E*(.5000000000-.5000000000*nu)*(.1443375673*y_1-.1971687837*y_2+0.5283121635e-1*y_4)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*y_1+.1971687837*y_3-.1443375673*y_4)*E*nu*(.1971687837*x_2-.1971687837*x_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*x_1-.1971687837*x_3+.1443375673*x_4)*E*(.5000000000-.5000000000*nu)*(-.1971687837*y_2+.1971687837*y_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[5][3] =((.1971687837*x_1-0.5283121635e-1*x_3-.1443375673*x_4)*E*(0.5283121635e-1*x_2-0.5283121635e-1*x_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-.1971687837*y_1+0.5283121635e-1*y_3+.1443375673*y_4)*E*(.5000000000-.5000000000*nu)*(-0.5283121635e-1*y_2+0.5283121635e-1*y_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*x_1-0.5283121635e-1*x_3)*E*(.1443375673*x_1+0.5283121635e-1*x_2-.1971687837*x_4)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*y_1+0.5283121635e-1*y_3)*E*(.5000000000-.5000000000*nu)*(-.1443375673*y_1-0.5283121635e-1*y_2+.1971687837*y_4)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*x_1-.1971687837*x_3)*E*(-.1443375673*x_1+.1971687837*x_2-0.5283121635e-1*x_4)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*y_1+.1971687837*y_3)*E*(.5000000000-.5000000000*nu)*(.1443375673*y_1-.1971687837*y_2+0.5283121635e-1*y_4)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*x_1-.1971687837*x_3+.1443375673*x_4)*E*(.1971687837*x_2-.1971687837*x_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*y_1+.1971687837*y_3-.1443375673*y_4)*E*(.5000000000-.5000000000*nu)*(-.1971687837*y_2+.1971687837*y_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[5][4] =((-0.5283121635e-1*y_2+0.5283121635e-1*y_4)*E*nu*(0.5283121635e-1*x_2-0.5283121635e-1*x_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*x_2-0.5283121635e-1*x_4)*E*(.5000000000-.5000000000*nu)*(-0.5283121635e-1*y_2+0.5283121635e-1*y_4)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-.1443375673*y_1-0.5283121635e-1*y_2+.1971687837*y_4)*E*nu*(.1443375673*x_1+0.5283121635e-1*x_2-.1971687837*x_4)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1443375673*x_1+0.5283121635e-1*x_2-.1971687837*x_4)*E*(.5000000000-.5000000000*nu)*(-.1443375673*y_1-0.5283121635e-1*y_2+.1971687837*y_4)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1443375673*y_1-.1971687837*y_2+0.5283121635e-1*y_4)*E*nu*(-.1443375673*x_1+.1971687837*x_2-0.5283121635e-1*x_4)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1443375673*x_1+.1971687837*x_2-0.5283121635e-1*x_4)*E*(.5000000000-.5000000000*nu)*(.1443375673*y_1-.1971687837*y_2+0.5283121635e-1*y_4)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*y_2+.1971687837*y_4)*E*nu*(.1971687837*x_2-.1971687837*x_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(.1971687837*x_2-.1971687837*x_4)*E*(.5000000000-.5000000000*nu)*(-.1971687837*y_2+.1971687837*y_4)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[5][5] =((0.5283121635e-1*x_2-0.5283121635e-1*x_4)**2*E/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*y_2+0.5283121635e-1*y_4)**2*E*(.5000000000-.5000000000*nu)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(.1443375673*x_1+0.5283121635e-1*x_2-.1971687837*x_4)**2*E/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1443375673*y_1-0.5283121635e-1*y_2+.1971687837*y_4)**2*E*(.5000000000-.5000000000*nu)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1443375673*x_1+.1971687837*x_2-0.5283121635e-1*x_4)**2*E/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1443375673*y_1-.1971687837*y_2+0.5283121635e-1*y_4)**2*E*(.5000000000-.5000000000*nu)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*x_2-.1971687837*x_4)**2*E/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-.1971687837*y_2+.1971687837*y_4)**2*E*(.5000000000-.5000000000*nu)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[5][6] =((0.5283121635e-1*x_2-0.5283121635e-1*x_4)*E*nu*(.1971687837*y_1-.1443375673*y_2-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*y_2+0.5283121635e-1*y_4)*E*(.5000000000-.5000000000*nu)*(-.1971687837*x_1+.1443375673*x_2+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(.1443375673*x_1+0.5283121635e-1*x_2-.1971687837*x_4)*E*nu*(.1971687837*y_1-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1443375673*y_1-0.5283121635e-1*y_2+.1971687837*y_4)*E*(.5000000000-.5000000000*nu)*(-.1971687837*x_1+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1443375673*x_1+.1971687837*x_2-0.5283121635e-1*x_4)*E*nu*(0.5283121635e-1*y_1-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1443375673*y_1-.1971687837*y_2+0.5283121635e-1*y_4)*E*(.5000000000-.5000000000*nu)*(-0.5283121635e-1*x_1+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*x_2-.1971687837*x_4)*E*nu*(0.5283121635e-1*y_1+.1443375673*y_2-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-.1971687837*y_2+.1971687837*y_4)*E*(.5000000000-.5000000000*nu)*(-0.5283121635e-1*x_1-.1443375673*x_2+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[5][7] =((0.5283121635e-1*x_2-0.5283121635e-1*x_4)*E*(-.1971687837*x_1+.1443375673*x_2+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*y_2+0.5283121635e-1*y_4)*E*(.5000000000-.5000000000*nu)*(.1971687837*y_1-.1443375673*y_2-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(.1443375673*x_1+0.5283121635e-1*x_2-.1971687837*x_4)*E*(-.1971687837*x_1+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1443375673*y_1-0.5283121635e-1*y_2+.1971687837*y_4)*E*(.5000000000-.5000000000*nu)*(.1971687837*y_1-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1443375673*x_1+.1971687837*x_2-0.5283121635e-1*x_4)*E*(-0.5283121635e-1*x_1+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1443375673*y_1-.1971687837*y_2+0.5283121635e-1*y_4)*E*(.5000000000-.5000000000*nu)*(0.5283121635e-1*y_1-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*x_2-.1971687837*x_4)*E*(-0.5283121635e-1*x_1-.1443375673*x_2+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-.1971687837*y_2+.1971687837*y_4)*E*(.5000000000-.5000000000*nu)*(0.5283121635e-1*y_1+.1443375673*y_2-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[6][0] =((.1971687837*y_2-.1971687837*y_4)*E*(.1971687837*y_1-.1443375673*y_2-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-.1971687837*x_2+.1971687837*x_4)*E*(.5000000000-.5000000000*nu)*(-.1971687837*x_1+.1443375673*x_2+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2+.1443375673*y_3-.1971687837*y_4)*E*(.1971687837*y_1-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2-.1443375673*x_3+.1971687837*x_4)*E*(.5000000000-.5000000000*nu)*(-.1971687837*x_1+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*y_2-.1443375673*y_3-0.5283121635e-1*y_4)*E*(0.5283121635e-1*y_1-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*x_2+.1443375673*x_3+0.5283121635e-1*x_4)*E*(.5000000000-.5000000000*nu)*(-0.5283121635e-1*x_1+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2-0.5283121635e-1*y_4)*E*(0.5283121635e-1*y_1+.1443375673*y_2-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2+0.5283121635e-1*x_4)*E*(.5000000000-.5000000000*nu)*(-0.5283121635e-1*x_1-.1443375673*x_2+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[6][1] =((-.1971687837*x_2+.1971687837*x_4)*E*nu*(.1971687837*y_1-.1443375673*y_2-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(.1971687837*y_2-.1971687837*y_4)*E*(.5000000000-.5000000000*nu)*(-.1971687837*x_1+.1443375673*x_2+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2-.1443375673*x_3+.1971687837*x_4)*E*nu*(.1971687837*y_1-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2+.1443375673*y_3-.1971687837*y_4)*E*(.5000000000-.5000000000*nu)*(-.1971687837*x_1+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*x_2+.1443375673*x_3+0.5283121635e-1*x_4)*E*nu*(0.5283121635e-1*y_1-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*y_2-.1443375673*y_3-0.5283121635e-1*y_4)*E*(.5000000000-.5000000000*nu)*(-0.5283121635e-1*x_1+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2+0.5283121635e-1*x_4)*E*nu*(0.5283121635e-1*y_1+.1443375673*y_2-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2-0.5283121635e-1*y_4)*E*(.5000000000-.5000000000*nu)*(-0.5283121635e-1*x_1-.1443375673*x_2+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[6][2] =((-.1971687837*y_1+0.5283121635e-1*y_3+.1443375673*y_4)*E*(.1971687837*y_1-.1443375673*y_2-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(.1971687837*x_1-0.5283121635e-1*x_3-.1443375673*x_4)*E*(.5000000000-.5000000000*nu)*(-.1971687837*x_1+.1443375673*x_2+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*y_1+0.5283121635e-1*y_3)*E*(.1971687837*y_1-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*x_1-0.5283121635e-1*x_3)*E*(.5000000000-.5000000000*nu)*(-.1971687837*x_1+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*y_1+.1971687837*y_3)*E*(0.5283121635e-1*y_1-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*x_1-.1971687837*x_3)*E*(.5000000000-.5000000000*nu)*(-0.5283121635e-1*x_1+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*y_1+.1971687837*y_3-.1443375673*y_4)*E*(0.5283121635e-1*y_1+.1443375673*y_2-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*x_1-.1971687837*x_3+.1443375673*x_4)*E*(.5000000000-.5000000000*nu)*(-0.5283121635e-1*x_1-.1443375673*x_2+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[6][3] =((.1971687837*x_1-0.5283121635e-1*x_3-.1443375673*x_4)*E*nu*(.1971687837*y_1-.1443375673*y_2-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-.1971687837*y_1+0.5283121635e-1*y_3+.1443375673*y_4)*E*(.5000000000-.5000000000*nu)*(-.1971687837*x_1+.1443375673*x_2+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*x_1-0.5283121635e-1*x_3)*E*nu*(.1971687837*y_1-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*y_1+0.5283121635e-1*y_3)*E*(.5000000000-.5000000000*nu)*(-.1971687837*x_1+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*x_1-.1971687837*x_3)*E*nu*(0.5283121635e-1*y_1-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*y_1+.1971687837*y_3)*E*(.5000000000-.5000000000*nu)*(-0.5283121635e-1*x_1+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*x_1-.1971687837*x_3+.1443375673*x_4)*E*nu*(0.5283121635e-1*y_1+.1443375673*y_2-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*y_1+.1971687837*y_3-.1443375673*y_4)*E*(.5000000000-.5000000000*nu)*(-0.5283121635e-1*x_1-.1443375673*x_2+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[6][4] =((-0.5283121635e-1*y_2+0.5283121635e-1*y_4)*E*(.1971687837*y_1-.1443375673*y_2-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*x_2-0.5283121635e-1*x_4)*E*(.5000000000-.5000000000*nu)*(-.1971687837*x_1+.1443375673*x_2+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-.1443375673*y_1-0.5283121635e-1*y_2+.1971687837*y_4)*E*(.1971687837*y_1-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1443375673*x_1+0.5283121635e-1*x_2-.1971687837*x_4)*E*(.5000000000-.5000000000*nu)*(-.1971687837*x_1+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1443375673*y_1-.1971687837*y_2+0.5283121635e-1*y_4)*E*(0.5283121635e-1*y_1-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1443375673*x_1+.1971687837*x_2-0.5283121635e-1*x_4)*E*(.5000000000-.5000000000*nu)*(-0.5283121635e-1*x_1+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*y_2+.1971687837*y_4)*E*(0.5283121635e-1*y_1+.1443375673*y_2-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(.1971687837*x_2-.1971687837*x_4)*E*(.5000000000-.5000000000*nu)*(-0.5283121635e-1*x_1-.1443375673*x_2+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[6][5] =((0.5283121635e-1*x_2-0.5283121635e-1*x_4)*E*nu*(.1971687837*y_1-.1443375673*y_2-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*y_2+0.5283121635e-1*y_4)*E*(.5000000000-.5000000000*nu)*(-.1971687837*x_1+.1443375673*x_2+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(.1443375673*x_1+0.5283121635e-1*x_2-.1971687837*x_4)*E*nu*(.1971687837*y_1-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1443375673*y_1-0.5283121635e-1*y_2+.1971687837*y_4)*E*(.5000000000-.5000000000*nu)*(-.1971687837*x_1+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1443375673*x_1+.1971687837*x_2-0.5283121635e-1*x_4)*E*nu*(0.5283121635e-1*y_1-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1443375673*y_1-.1971687837*y_2+0.5283121635e-1*y_4)*E*(.5000000000-.5000000000*nu)*(-0.5283121635e-1*x_1+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*x_2-.1971687837*x_4)*E*nu*(0.5283121635e-1*y_1+.1443375673*y_2-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-.1971687837*y_2+.1971687837*y_4)*E*(.5000000000-.5000000000*nu)*(-0.5283121635e-1*x_1-.1443375673*x_2+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[6][6] =((.1971687837*y_1-.1443375673*y_2-0.5283121635e-1*y_3)**2*E/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-.1971687837*x_1+.1443375673*x_2+0.5283121635e-1*x_3)**2*E*(.5000000000-.5000000000*nu)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(.1971687837*y_1-.1971687837*y_3)**2*E/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*x_1+.1971687837*x_3)**2*E*(.5000000000-.5000000000*nu)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*y_1-0.5283121635e-1*y_3)**2*E/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_1+0.5283121635e-1*x_3)**2*E*(.5000000000-.5000000000*nu)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*y_1+.1443375673*y_2-.1971687837*y_3)**2*E/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_1-.1443375673*x_2+.1971687837*x_3)**2*E*(.5000000000-.5000000000*nu)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[6][7] =((.1971687837*y_1-.1443375673*y_2-0.5283121635e-1*y_3)*E*nu*(-.1971687837*x_1+.1443375673*x_2+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-.1971687837*x_1+.1443375673*x_2+0.5283121635e-1*x_3)*E*(.5000000000-.5000000000*nu)*(.1971687837*y_1-.1443375673*y_2-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(.1971687837*y_1-.1971687837*y_3)*E*nu*(-.1971687837*x_1+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*x_1+.1971687837*x_3)*E*(.5000000000-.5000000000*nu)*(.1971687837*y_1-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*y_1-0.5283121635e-1*y_3)*E*nu*(-0.5283121635e-1*x_1+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_1+0.5283121635e-1*x_3)*E*(.5000000000-.5000000000*nu)*(0.5283121635e-1*y_1-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*y_1+.1443375673*y_2-.1971687837*y_3)*E*nu*(-0.5283121635e-1*x_1-.1443375673*x_2+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_1-.1443375673*x_2+.1971687837*x_3)*E*(.5000000000-.5000000000*nu)*(0.5283121635e-1*y_1+.1443375673*y_2-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[7][0] =((.1971687837*y_2-.1971687837*y_4)*E*nu*(-.1971687837*x_1+.1443375673*x_2+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-.1971687837*x_2+.1971687837*x_4)*E*(.5000000000-.5000000000*nu)*(.1971687837*y_1-.1443375673*y_2-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2+.1443375673*y_3-.1971687837*y_4)*E*nu*(-.1971687837*x_1+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2-.1443375673*x_3+.1971687837*x_4)*E*(.5000000000-.5000000000*nu)*(.1971687837*y_1-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*y_2-.1443375673*y_3-0.5283121635e-1*y_4)*E*nu*(-0.5283121635e-1*x_1+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*x_2+.1443375673*x_3+0.5283121635e-1*x_4)*E*(.5000000000-.5000000000*nu)*(0.5283121635e-1*y_1-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2-0.5283121635e-1*y_4)*E*nu*(-0.5283121635e-1*x_1-.1443375673*x_2+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2+0.5283121635e-1*x_4)*E*(.5000000000-.5000000000*nu)*(0.5283121635e-1*y_1+.1443375673*y_2-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[7][1] =((-.1971687837*x_2+.1971687837*x_4)*E*(-.1971687837*x_1+.1443375673*x_2+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(.1971687837*y_2-.1971687837*y_4)*E*(.5000000000-.5000000000*nu)*(.1971687837*y_1-.1443375673*y_2-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2-.1443375673*x_3+.1971687837*x_4)*E*(-.1971687837*x_1+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2+.1443375673*y_3-.1971687837*y_4)*E*(.5000000000-.5000000000*nu)*(.1971687837*y_1-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*x_2+.1443375673*x_3+0.5283121635e-1*x_4)*E*(-0.5283121635e-1*x_1+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*y_2-.1443375673*y_3-0.5283121635e-1*y_4)*E*(.5000000000-.5000000000*nu)*(0.5283121635e-1*y_1-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_2+0.5283121635e-1*x_4)*E*(-0.5283121635e-1*x_1-.1443375673*x_2+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*y_2-0.5283121635e-1*y_4)*E*(.5000000000-.5000000000*nu)*(0.5283121635e-1*y_1+.1443375673*y_2-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[7][2] =((-.1971687837*y_1+0.5283121635e-1*y_3+.1443375673*y_4)*E*nu*(-.1971687837*x_1+.1443375673*x_2+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(.1971687837*x_1-0.5283121635e-1*x_3-.1443375673*x_4)*E*(.5000000000-.5000000000*nu)*(.1971687837*y_1-.1443375673*y_2-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*y_1+0.5283121635e-1*y_3)*E*nu*(-.1971687837*x_1+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*x_1-0.5283121635e-1*x_3)*E*(.5000000000-.5000000000*nu)*(.1971687837*y_1-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*y_1+.1971687837*y_3)*E*nu*(-0.5283121635e-1*x_1+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*x_1-.1971687837*x_3)*E*(.5000000000-.5000000000*nu)*(0.5283121635e-1*y_1-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*y_1+.1971687837*y_3-.1443375673*y_4)*E*nu*(-0.5283121635e-1*x_1-.1443375673*x_2+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*x_1-.1971687837*x_3+.1443375673*x_4)*E*(.5000000000-.5000000000*nu)*(0.5283121635e-1*y_1+.1443375673*y_2-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[7][3] =((.1971687837*x_1-0.5283121635e-1*x_3-.1443375673*x_4)*E*(-.1971687837*x_1+.1443375673*x_2+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-.1971687837*y_1+0.5283121635e-1*y_3+.1443375673*y_4)*E*(.5000000000-.5000000000*nu)*(.1971687837*y_1-.1443375673*y_2-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*x_1-0.5283121635e-1*x_3)*E*(-.1971687837*x_1+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*y_1+0.5283121635e-1*y_3)*E*(.5000000000-.5000000000*nu)*(.1971687837*y_1-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*x_1-.1971687837*x_3)*E*(-0.5283121635e-1*x_1+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*y_1+.1971687837*y_3)*E*(.5000000000-.5000000000*nu)*(0.5283121635e-1*y_1-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*x_1-.1971687837*x_3+.1443375673*x_4)*E*(-0.5283121635e-1*x_1-.1443375673*x_2+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*y_1+.1971687837*y_3-.1443375673*y_4)*E*(.5000000000-.5000000000*nu)*(0.5283121635e-1*y_1+.1443375673*y_2-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[7][4] =((-0.5283121635e-1*y_2+0.5283121635e-1*y_4)*E*nu*(-.1971687837*x_1+.1443375673*x_2+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*x_2-0.5283121635e-1*x_4)*E*(.5000000000-.5000000000*nu)*(.1971687837*y_1-.1443375673*y_2-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-.1443375673*y_1-0.5283121635e-1*y_2+.1971687837*y_4)*E*nu*(-.1971687837*x_1+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1443375673*x_1+0.5283121635e-1*x_2-.1971687837*x_4)*E*(.5000000000-.5000000000*nu)*(.1971687837*y_1-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1443375673*y_1-.1971687837*y_2+0.5283121635e-1*y_4)*E*nu*(-0.5283121635e-1*x_1+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1443375673*x_1+.1971687837*x_2-0.5283121635e-1*x_4)*E*(.5000000000-.5000000000*nu)*(0.5283121635e-1*y_1-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*y_2+.1971687837*y_4)*E*nu*(-0.5283121635e-1*x_1-.1443375673*x_2+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(.1971687837*x_2-.1971687837*x_4)*E*(.5000000000-.5000000000*nu)*(0.5283121635e-1*y_1+.1443375673*y_2-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[7][5] =((0.5283121635e-1*x_2-0.5283121635e-1*x_4)*E*(-.1971687837*x_1+.1443375673*x_2+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*y_2+0.5283121635e-1*y_4)*E*(.5000000000-.5000000000*nu)*(.1971687837*y_1-.1443375673*y_2-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(.1443375673*x_1+0.5283121635e-1*x_2-.1971687837*x_4)*E*(-.1971687837*x_1+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1443375673*y_1-0.5283121635e-1*y_2+.1971687837*y_4)*E*(.5000000000-.5000000000*nu)*(.1971687837*y_1-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1443375673*x_1+.1971687837*x_2-0.5283121635e-1*x_4)*E*(-0.5283121635e-1*x_1+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1443375673*y_1-.1971687837*y_2+0.5283121635e-1*y_4)*E*(.5000000000-.5000000000*nu)*(0.5283121635e-1*y_1-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*x_2-.1971687837*x_4)*E*(-0.5283121635e-1*x_1-.1443375673*x_2+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-.1971687837*y_2+.1971687837*y_4)*E*(.5000000000-.5000000000*nu)*(0.5283121635e-1*y_1+.1443375673*y_2-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[7][6] =((.1971687837*y_1-.1443375673*y_2-0.5283121635e-1*y_3)*E*nu*(-.1971687837*x_1+.1443375673*x_2+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-.1971687837*x_1+.1443375673*x_2+0.5283121635e-1*x_3)*E*(.5000000000-.5000000000*nu)*(.1971687837*y_1-.1443375673*y_2-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(.1971687837*y_1-.1971687837*y_3)*E*nu*(-.1971687837*x_1+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-.1971687837*x_1+.1971687837*x_3)*E*(.5000000000-.5000000000*nu)*(.1971687837*y_1-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*y_1-0.5283121635e-1*y_3)*E*nu*(-0.5283121635e-1*x_1+0.5283121635e-1*x_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_1+0.5283121635e-1*x_3)*E*(.5000000000-.5000000000*nu)*(0.5283121635e-1*y_1-0.5283121635e-1*y_3)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*y_1+.1443375673*y_2-.1971687837*y_3)*E*nu*(-0.5283121635e-1*x_1-.1443375673*x_2+.1971687837*x_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_1-.1443375673*x_2+.1971687837*x_3)*E*(.5000000000-.5000000000*nu)*(0.5283121635e-1*y_1+.1443375673*y_2-.1971687837*y_3)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  Kel[7][7] =((-.1971687837*x_1+.1443375673*x_2+0.5283121635e-1*x_3)**2*E/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(.1971687837*y_1-.1443375673*y_2-0.5283121635e-1*y_3)**2*E*(.5000000000-.5000000000*nu)/((.1971687837*x_1*y_2-.1971687837*x_1*y_4-.1971687837*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+0.5283121633e-1*x_3*y_4+.1971687837*x_4*y_1-0.5283121633e-1*x_4*y_3+.1443375673*x_2*y_4-.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(-.1971687837*x_1+.1971687837*x_3)**2*E/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(.1971687837*y_1-.1971687837*y_3)**2*E*(.5000000000-.5000000000*nu)/((0.5283121633e-1*x_1*y_2-.1971687837*x_1*y_4-0.5283121633e-1*x_2*y_1+0.5283121633e-1*x_2*y_3-0.5283121633e-1*x_3*y_2+.1971687837*x_3*y_4+.1971687837*x_4*y_1-.1971687837*x_4*y_3+.1443375673*x_1*y_3-.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_1+0.5283121635e-1*x_3)**2*E/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(0.5283121635e-1*y_1-0.5283121635e-1*y_3)**2*E*(.5000000000-.5000000000*nu)/((.1971687837*x_1*y_2-0.5283121633e-1*x_1*y_4-.1971687837*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+0.5283121633e-1*x_3*y_4+0.5283121633e-1*x_4*y_1-0.5283121633e-1*x_4*y_3-.1443375673*x_1*y_3+.1443375673*x_3*y_1)*(-1.*nu**2+1.))+(-0.5283121635e-1*x_1-.1443375673*x_2+.1971687837*x_3)**2*E/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.))+(0.5283121635e-1*y_1+.1443375673*y_2-.1971687837*y_3)**2*E*(.5000000000-.5000000000*nu)/((0.5283121633e-1*x_1*y_2-0.5283121633e-1*x_1*y_4-0.5283121633e-1*x_2*y_1+.1971687837*x_2*y_3-.1971687837*x_3*y_2+.1971687837*x_3*y_4+0.5283121633e-1*x_4*y_1-.1971687837*x_4*y_3-.1443375673*x_2*y_4+.1443375673*x_4*y_2)*(-1.*nu**2+1.)));
  
  Kel=t*Kel;
  return Kel

#5A-Definição da função de ROTAÇÃO do elemento de TRELIÇA
def TP2_MatrizDeRotacaoDoElemento(cs, sn):
  Rel = np.zeros((4,4))
  Rel[0][0]=  cs; Rel[0][1]= sn; 
  Rel[1][0]= -sn; Rel[1][1]= cs;
  Rel[2][2]=  cs; Rel[2][3]= sn; 
  Rel[3][2]= -sn; Rel[3][3]= cs;
  return Rel

#5B-Definição da função de ROTAÇÃO do elemento de PÓRTICO
def PP2_MatrizDeRotacaoDoElemento(cs, sn):
  Rel= np.zeros(6,6);
  Rel[0][0]=  cs; Rel[0][1]= sn; 
  Rel[1][0]= -sn; Rel[1][1]= cs;
  Rel[2][2]=1;
  Rel[3][3]=  cs; Rel[3][4]= sn; 
  Rel[4][3]= -sn; Rel[4][4]= cs;
  Rel[5][5]=1;
  return Rel

#5C-Definição da função de ROTAÇÃO do elemento de GRELHA
def GR2_MatrizDeRotacaoDoElemento(cs, sn):
  Rel= np.zeros(6,6);
  Rel[0][0]=1;
  Rel[1][1]=  cs; Rel[1][2]= sn; 
  Rel[2][1]= -sn; Rel[2][2]= cs;
  Rel[3][3]=1;
  Rel[4][4]=  cs; Rel[4][5]= sn; 
  Rel[5][4]= -sn; Rel[5][5]= cs;
  return Rel

#5D-Definição da função de ROTAÇÃO dos elementos Q4 e Q8, funciona para os dois
def EP_RQ4_MatrizDeRotacaoDoElemento(cs, sn, nnoselem):
  Rel = np.zeros((2*nnoselem,2*nnoselem))
  for i in range(0, 2*nnoselem - 1, 2):
    Rel[i][i]     = cs
    Rel[i][i+1]   = sn
    Rel[i+1][i]   = -sn
    Rel[i+1][i+1] = cs
  return Rel

#6-Definição dos graus de liberdade do elemento, vetor gle
def GrausDeLiberdadeDoElemento(nnoselem,glno,no,nglno):
  V = 0
  gle = np.zeros((1,nnoselem*nglno))
  
  for i in range(nnoselem):
    for j in range(nglno):
      gle[0][V] = glno[no[i]-1][j]
      V = V+1
  return gle

#7-Definição da função que cria os vetor de forças externas na estrutura
def VetorDeForcasDaEstrutura(tipoestr, tipoelem, nglno, nnoselem, nnoscar, nelemscar, neq, coordnos, propelems, cargasnos, cargaselems, glno, ncarelem):
  
  Festr = np.zeros((neq,1))
  nglel = nnoselem*nglno
  
  #Forças externas aplicadas nos nós
  for i in range(nnoscar):
    no = cargasnos[i][0]
    for j in range(nglno):
      gl = glno[int(no-1)][j];
      if gl > 0:
        Festr[int(gl-1)][0] = Festr[int(gl-1)][0] + cargasnos[i][j+1]
 
  #anexando o número de elementos carregados
  for i in range(nelemscar):
    #acessa a matriz de carregamentos e pega linha por linha dentro até o número de elementos carregados (devido ao for acima)
    el = cargaselems[i][0]

    #propriedade do elemento el, neste vetor terá dados referente se o carregamento é local ou global
    idsist = cargaselems[i][1]
    
    #cargas do elemento
    q   = np.zeros((1,ncarelem))
    qel = np.zeros((1,ncarelem))
    q = cargaselems[i][2:(ncarelem+2)] 

    #identificação do no
    no = propelems[int(el-1)][0:nnoselem] 
  
    if tipoestr == "TRELICA_PLANA" or tipoestr == "PORTICO_PLANO" or tipoestr == "GRELHA":           
      # Cálculo de L, cs e sn
      dx = coordnos[no[1]-1][0] - coordnos[no[0]-1][0]
      dy = coordnos[no[1]-1][1] - coordnos[no[0]-1][1]
      #o termo "**" significa elevar seria o sinal "^" da cálculadora
      L = (dx**2+dy**2)**0.5
      cs = dx/L
      sn = dy/L
      if L <= 10e-8:
        print("Comprimento do elemento nulo")
        sys.exit()
    elif tipoestr == "TRELICA_ESPACIAL":
      # Cálculo de L, cx, cy e cz
      dx = coordnos[no[1]-1][0] - coordnos[no[0]-1][0]
      dy = coordnos[no[1]-1][1] - coordnos[no[0]-1][1]
      dz = coordnos[no[1]-1][2] - coordnos[no[0]-1][2]
      #o termo "**" significa elevar seria o sinal "^" da cálculadora
      L = (dx**2+dy**2)**0.5
      cx = dx/L
      cy = dy/L
      cz = dz/L
      if L <= 10e-8:
        print("Comprimento do elemento nulo")
        sys.exit()
    elif tipoelem == "EP-RQ4" or tipoestr == "EP-RQ8" or tipoelem == "EP-RQ4_ISO":           
      [cs, sn, a, b] = EP_RQ4_Dimensoes(el, coordnos, no) 
    else:
      print("Elemento ainda não implementado")
      sys.exit()

    #Vetor de forças equivalentes do elemento no sistema local
    #e da matriz de rotação
    if tipoelem == "PP2":
      [Feq,q] = PP2_VetorDeCargasEquivalentesDoElemento(q, L, idsist, cs, sn)
      Rel     = PP2_MatrizDeRotacaoDoElemento(cs, sn)
      
    elif tipoelem == "GR2":
      Feq = GR2_VetorDeCargasEquivalentesDoElemento(q, L)
      Rel = GR2_MatrizDeRotacaoDoElemento(cs, sn)

    elif tipoelem == "EP-RQ4":
      qel = np.zeros((1,8))
      if idsist == 1:        
        qel[0][0] = q[0][0]*cs + q[0][1]*sn
        qel[0][1] =-q[0][0]*sn + q[0][1]*cs
        qel[0][2] = q[0][2]*cs + q[0][3]*sn
        qel[0][3] =-q[0][2]*sn + q[0][3]*cs
        qel[0][4] = q[0][4]*cs + q[0][5]*sn
        qel[0][5] =-q[0][4]*sn + q[0][5]*cs
        qel[0][6] = q[0][6]*cs + q[0][7]*sn
        qel[0][7] =-q[0][6]*sn + q[0][7]*cs
      else:
        for k in range(8):
          qel[0][int(k)] = q[int(k)]          
      
      Feq = EP_RQ4_VetorDeCargasEquivalentesDoElemento(qel, a, b, propgeo[0][0])
      Rel = EP_RQ4_MatrizDeRotacaoDoElemento(cs, sn, nnoselem) 

    elif tipoelem == "EP-RQ4_ISO":
      if idsist == 1:
        qel[0][0] = q[0][0]*cs + q[0][1]*sn
        qel[0][1] =-q[0][0]*sn + q[0][1]*cs
        qel[0][2] = q[0][2]*cs + q[0][3]*sn
        qel[0][3] =-q[0][2]*sn + q[0][3]*cs
        qel[0][4] = q[0][4]*cs + q[0][5]*sn
        qel[0][5] =-q[0][4]*sn + q[0][5]*cs
        qel[0][6] = q[0][6]*cs + q[0][7]*sn
        qel[0][7] =-q[0][6]*sn + q[0][7]*cs
      else:
        for k in range(8):
          qel[0][int(k)] = q[int(k)]

      Feq = EP_RQ4_ISO_VetorDeCargasEquivalentesDoElemento(qel, a, b, propgeo[0][0]) 

    else:
      print("Forças para este elemento ainda não implementado")
      sys.exit()

    #Cálculo do vetor de forças do elemeno no sistema global
    if tipoelem != "EP-RQ4_ISO":
      Feq = np.matmul(np.transpose(Rel),Feq)

    #Cálculo dos graus de liberdade do elemento
    gle = GrausDeLiberdadeDoElemento(nnoselem, glno, no, nglno)

    #montagem do vetor de forças da estrutura
    nglel = nnoselem * nglno
    for i in range(nglel):
      if gle[0][i]>0:
        Festr[int(gle[0][i]-1)][0] = Festr[int(gle[0][i]-1)][0] + Feq[i][0]
  return Festr

# 8A-Função para criação das forças equivalentes do elemento de PÓRTICO
def PP2_VetorDeCargasEquivalentesDoElemento(q, L, idsist, cs, sn):

  #Caso esteja no sistema local faça
  if idsist == 0:
    qx = q[0]
    qy = q[1]
  else:   #caso colocar no sistema local
    Qx = q[0]
    Qy = q[1]
    #------------
    qx = Qx*cs+Qy*sn
    qy = -Qx*sn+Qy*cs
  
  q[0] = qx
  q[1] = qy
  
  #Vetor de forças esquivalentes
  Feq = np.zeros((6,1))
  Feq[0][0] = qx*L/2
  Feq[1][0] = qy*L/2
  Feq[2][0] = qy*L^2/12
  Feq[3][0] = qx*L/2
  Feq[4][0] = qy*L/2
  Feq[5][0] = -qx*L^2/12

  return Feq, q 

# 8B-Função para criação das forças equivalentes do elemento de GRELHA
def GR2_VetorDeCargasEquivalentesDoElemento(q, L):
  #Cargas aplicadas
  qz = q[0] 
  mx = q[1]
  
  #Vetor de forças esquivalentes
  Feq = np.zeros((6,1))

  Feq[0][0] = qz*L/2
  Feq[1][0] = mx*L/2
  Feq[2][0] = -qz*L^2/12
  Feq[3][0] = qz*L/2
  Feq[4][0] = mx*L/2
  Feq[5][0] = qz*L^2/12

  return Feq

# 8C-Função para criação das forças equivalentes do elemento Q4
def EP_RQ4_VetorDeCargasEquivalentesDoElemento(q, a, b, t):
  
  #Vetor de forças esquivalentes
  Feq = np.zeros((8,1))
  Feq[0][0] = a*q[0][0] + b*q[0][6] 
  Feq[1][0] = a*q[0][1] + b*q[0][7] 
  Feq[2][0] = a*q[0][1] + b*q[0][2] 
  Feq[3][0] = a*q[0][1] + b*q[0][3]
  Feq[4][0] = a*q[0][4] + b*q[0][2] 
  Feq[5][0] = a*q[0][5] + b*q[0][3] 
  Feq[6][0] = a*q[0][4] + b*q[0][6] 
  Feq[7][0] = a*q[0][5] + b*q[0][7] 
  Feq = t*Feq
  return Feq

# 8D-Função para criação das forças equivalentes do elemento Q4 ISOPARAMÉTRICO
def EP_RQ4_ISO_VetorDeCargasEquivalentesDoElemento(q, a, b, t):
  Feq = np.zeros((8,1))
    #Vetor de forças esquivalentes
  Feq = np.zeros((8,1))
  Feq[0][0] = a*q[0][0] + b*q[0][6] 
  Feq[1][0] = a*q[0][1] + b*q[0][7] 
  Feq[2][0] = a*q[0][1] + b*q[0][2] 
  Feq[3][0] = a*q[0][1] + b*q[0][3]
  Feq[4][0] = a*q[0][4] + b*q[0][2] 
  Feq[5][0] = a*q[0][5] + b*q[0][3] 
  Feq[6][0] = a*q[0][4] + b*q[0][6] 
  Feq[7][0] = a*q[0][5] + b*q[0][7] 
  Feq = t*Feq
  return Feq

# 9-Função para determinação dos deslocamento nodal da estrutura
def DescolamentosNodais(tipoestr, nglno, nnos, Kestr, Festr, neq, glno):
  #cálculo dos descalmentos livres
  Uestr = np.zeros((nglno*nnos,1))
  
  #determiniação dos deslocamentos nodais livres
  Uestr = np.matmul(np.linalg.inv(Kestr),Festr)

  #vetor total de deslocamento, incluindo os restritos
  UestrTotal = np.zeros((nglno*nnos,1))

  for i in range(nnos):
    for j in range(nglno):
      if glno[i][j] != 0:
        UestrTotal[int(j+nglno*(i))] = Uestr[int(glno[i][j]-1)]

  
  return Uestr, UestrTotal


def EsforcosDaEstrutura(nelems, propelems, nnoselem, propmats, propgeo, coordnos, nglno, glno, tipoelem, Uestr, ncarelem, cargaselems):
  nglel = nglno * nnoselem
  
  idc   = 0
  a     = 0
  b     = 0
  #aqui são criados as matrizes de esforço, para cada elemento deve ser implementada a quantidade de matrizes Esf correta.
  #Note que para treliça plana só existe uma matriz Esf, isso porque só existe esforço normal.
  if tipoelem == "TP2":
    ns   = 1
    x    = 0
    Esf  = np.zeros((nelems, ns))
  elif tipoelem == "PP2":
    ns   = 3
    x    = np.zeros((nelems, ns))
    Esf1  = np.zeros((nelems, ns))
    Esf2  = np.zeros((nelems, ns))
    Esf3  = np.zeros((nelems, ns))
  elif tipoelem == "EP-RQ4" or tipoelem == "EP-RQ8":
    Deformacao  = np.zeros((nelems, 4))
    Tensao      = np.zeros((nelems, 4))
  elif tipoelem == "EP-RQ4_ISO":
    # o 5 é o número de pontos de integração de gauss
    Deformacao  = np.zeros((3, 5))
    Tensao      = np.zeros((3, 5))
  else:
    print("Não é possível criar as matrizes de esforços da estrutura deste elemeneto")

  for el in range(nelems):
    Uel1 = np.zeros((nglno * nnoselem,1))
    Uel2 = np.zeros((nglno * nnoselem,1))
    Fel1 = np.zeros((nglel,1))
    Fel2 = np.zeros((nglel,1))
    feq  = np.zeros((nglel,1))
    q    = np.zeros((ncarelem,1))

    #propriedades dos elementos (OBS: a matriz propelems tem em suas primeiras colunas os nós que forma um elemento, e estes nós são usados para encontrar as coordenadas na matriz coordnos)
    idmat = propelems[el][nnoselem+0]
    idsec = propelems[el][nnoselem+1]
    pmat  = propmats[idmat-1][:]
    psec  = propgeo[idsec-1][:]
    no    = propelems[el][0:nnoselem]

    #Cálculo dos parâmetros pra rotação
    if tipoelem == "TP2" or tipoelem == "PP2" or tipoelem == "GR2":      
      dx = coordnos[int(no[1]-1)][0] - coordnos[int(no[0]-1)][0]
      dy = coordnos[int(no[1]-1)][1] - coordnos[int(no[0]-1)][1]      
      #o termo "**" significa elevar seria o sinal "^" da cálculadora
      L = (dx**2+dy**2)**0.5
      cs = dx/L
      sn = dy/L
      if L <= 10e-8:
        print("Comprimento do elemento nulo")
        sys.exit()    
    elif tipoelem == "EP-RQ4" or tipoelem == "EP-RQ8" or tipoelem == "EP-RQ4_ISO":      
      [cs, sn, a, b] = EP_RQ4_Dimensoes(el, coordnos, no)      
    else:
      print("Problemas nos esforços, possivelemnte este elemento implementado")
      sys.exit() 
    
    #cálculo da matriz de rigidez do elemento no sistema local
    if tipoelem == "TP2":
      #criando a matriz de rigidez do elemento de treliça
      kel = TP2_MatrizDeRigidezDoElemento(pmat[0], psec[0], L)
      Rel = TP2_MatrizDeRotacaoDoElemento(cs, sn)
    elif tipoelem == "PP2":
      #criando a matriz de rigidez do elemento de pórtico
      kel = PP2_MatrizDeRigidezDoElemento(pmat[0], psec[0], psec(1), L)
      Rel = PP2_MatrizDeRotacaoDoElemento(cs, sn)
    elif tipoelem == "GR2":
      #criando a matriz de rigidez do elemento de grelha
      kel = GR2_MatrizDeRigidezDoElemento(pmat[0], pmat[1], psec(0), psec(1), L)
      Rel = GR2_MatrizDeRotacaoDoElemento(cs, sn)
    elif tipoelem == "EP-RQ4":
      #criando a matriz de rigidez do elemento Q4      
      kel = EP_RQ4_MatrizDeRigidezDoElemento(pmat[0], pmat[1], psec[0], tipoestr, a, b)
      Rel = EP_RQ4_MatrizDeRotacaoDoElemento(cs, sn,nnoselem)
    elif tipoelem == "EP-RQ8":
        pass
      #criando a matriz de rigidez do elemento de grelha
      #kel = EP_RQ8_MatrizDeRigidezDoElemento(pmat[0], pmat[1], psec[0], tipoestr, a, b)
      #Rel = EP_RQ8_MatrizDeRotacaoDoElemento(cs, sn, nnoselem)
    elif tipoelem == "EP-RQ4_ISO":
      #criando a matriz de rigidez do elemento Q4 ISO
      kel = EP_RQ4_ISO_MatrizDeRigidezDoElemento(pmat[0], pmat[1], psec[0], tipoestr, coordnos, no)
    else: 
      print("Matriz de rigidez do elemento ainda não implementada para esta estrutura")
      sys.exit()

    #Determinação do grau de liberdade do elemento para compor a matriz de rigidez global
    gle = GrausDeLiberdadeDoElemento(nnoselem,glno,no,nglno)
    

    #Deslocamento do elemento no sistema global----
    for i in range(nglel):
      if gle[0][i] != 0:
        Uel2[i][0] = Uestr[int(gle[0][i]-1)]
  
    if tipoelem != "EP-RQ4_ISO":
      #Deslocamento do elemento no sistema local
      Uel1 = np.matmul(Rel,Uel2)
    else:
      Uel1 = Uel2
    
    #Forças de extreminadade com forças equivalentes
    Fel1 = np.matmul(kel,Uel1)    
    
    #Cargas equivalente dos elementos
    for i in range(nelemscar):
      if cargaselems[i][0] == (el+1):         
         qel = cargaselems[i][0:ncarelem]
         #indentificador do sistema de coordenadas da carga no elemento
         idsist = cargaselems[i][1]
         if tipoelem == "PP2":          
           [feq, q] = PP2_VetorDeCargasEquivalentesDoElemento(q, L, idsist, cs, sn)
         elif tipoelem == "GR2":           
           feq      = GR2_VetorDeCargasEquivalentesDoElemento(q, L)
         elif tipoelem == "EP-RQ4" or tipoelem == "EP-RQ8" or tipoelem == "EP-RQ4_ISO":
           if idsist == 1:
             q[0] =  qel[0]*cs + qel[1]*sn; 
             q[1] = -qel[0]*sn + qel[1]*cs;
             q[2] =  qel[2]*cs + qel[3]*sn; 
             q[3] = -qel[2]*sn + qel[3]*cs;
             q[4] =  qel[4]*cs + qel[5]*sn; 
             q[5] = -qel[4]*sn + qel[5]*cs;
             q[6] =  qel[6]*cs + qel[7]*sn; 
             q[7] = -qel[6]*sn + qel[7]*cs;
         else:
           print("Esta força equivalante do elemento ainda não implementada para esta estrutura")
           sys.exit()
     
    #forças de extremidade 
    Fel2 = Fel1 - feq

    #Determinação dos esforços ao longo do elemento
    #Para TRELIÇA PLANA
    if tipoelem == "TP2":
       #Esforço normal
       Esf = - Fel2
       print("Esforço normal no elemento", el+1)
               
    #Para PÓRTICO_PLANO
    elif tipoelem == "PP2":
      for i in range(ns):
         x[el][i] = L*(i+0)/(ns-1)
         #Esforço normal
         print("Esforço normal no elemento", el+1)
         Esf1[el][i] = - Fel2[0][0] - q[0][0]*x[el][i]
         #Esforço cortante
         print("Esforço cortante no elemento", el+1)
         Esf2[el][i] = Fel2[1][0] - q[0][1]*x[el][i]
         #Esforço momento fletor
         print("Esforço momento fletor no elemento", el+1)
         Esf3[el][i] = - Fel2[2][0] + Fel2[1][0]*x[el][i] + q[0][1]*x[el][i]*(x[el][i]^2)/2  
    #Para GRELHA
    elif tipoelem == "GR2":
      for i in range(ns):
         x[el][i] = L*(i+0)/(ns-1)
         #Esforço cortante
         print("Esforço normal no elemento", el+1)
         Esf1[el][i] = - Fel2[0][0] - q[0][0]*x[el][i]
         #Esforço momento fletor
         print("Esforço momento fletor no elemento", el+1)
         Esf2[el][i] = - Fel2[2][0] + Fel2[0][0]*x[el][i] + q[0][0]*x[el][i]*(x[el][i]^2)/2
         #Esforço momento torçor
         print("Esforço momento torçor no elemento", el+1)
         Esf3[el][i] = - Fel2[1][0] - q[0][1]*x[el][i]
    #Para Q4
    elif tipoelem == "EP-RQ4":      
      [defor, tens] = EP_RQ4_DeformacoesTensoes(pmat[0], pmat[1], a , b, Uel1 , tipoestr)
      Deformacao[el][0] = el
      Tensao[el][0]     = el
      for k in range(3):
        Deformacao[el][k+1] = defor[k][0]
        Tensao[el][k+1]     = tens[k][0]

    elif tipoelem == "EP-RQ8":
      print("Esforço do Q8 ainda não implementada para este elemento, deve colocar a função da matriz B e determinar as deformações e tensões")
    #Para Q4_ISO
    elif tipoelem == "EP-RQ4_ISO":
      x_1=coordnos[no[0]-1,0];
      x_2=coordnos[no[1]-1,0];        
      x_3=coordnos[no[2]-1,0];
      x_4=coordnos[no[3]-1,0];         
      y_1=coordnos[no[0]-1,1];
      y_2=coordnos[no[1]-1,1];  
      y_3=coordnos[no[2]-1,1];
      y_4=coordnos[no[3]-1,1];    

      #Pontos de Gauss
      P_G=np.zeros((5,2));
      P_G[0][0] = -1/3**0.5;
      P_G[0][1] = -1/3**0.5;
      P_G[1][0] =  1/3**0.5;
      P_G[1][1] = -1/3**0.5;
      P_G[2][0] =  1/3**0.5;
      P_G[2][1] =  1/3**0.5;
      P_G[3][0] = -1/3**0.5;
      P_G[3][1] =  1/3**0.5;
      P_G[4][0] =  0;
      P_G[4][1] =  0;
      
      for i in range(5):
        xi  = P_G[i][0]
        eta = P_G[i][1]
        [JB, Ee] = EP_RQ4_ISO_DeformacoesTensoes(propgeo[0],x_1,y_1,x_2,y_2,x_3,y_3,x_4,y_4,xi,eta,tipoestr,pmat[0], pmat[1])
        #defor = np.matmul(JB,Uel1)
        Deformacao = np.matmul(JB,Uel1)
        Tensao = np.matmul(Ee,Deformacao)
        #for j in range(3):
          #Deformacao[j][i]=defor[j][0] 
      
      #Criando a matriz de tensões      
      #for i in range(5):
          #Tensao[:][i] = np.matmul(Ee*Deformacao[:][i])
       

      print("TENSÕES E DEFORMAÇÕES NO ELEMENTO:", el+1)
      print("------------------------------------------")
      print("-----------DEFORMAÇÃO----------------------  ELEMENTO", el+1)
      print(Deformacao)      
      print("------------TENSÃO-------------------------  ELEMENTO", el+1)
      print(Tensao)
      print("------------------------------------------")

    else:
      print("Esforço ainda não implementada para este elemento")
      sys.exit()
    
  status = "FIM DO PROGRAMA"
  return status, Deformacao, Tensao


# 10 - Função de dimensões do elemento Q4 e Q8 
def EP_RQ4_Dimensoes(el, coordnos, no):
  if tipoelem == "EP-RQ4" or tipoelem == "EP-RQ8":
    # Cálculo das dimensões do elemento
    c = np.zeros((2,2))
    #primeiro lado do elemento
    dx = coordnos[no[1]-1][0] - coordnos[no[0]-1][0]
    dy = coordnos[no[1]-1][1] - coordnos[no[0]-1][1]
    a  = (dx**2+dy**2)**0.5/2        
    #segundo lado do elemento
    dx_2 = coordnos[no[2]-1][0] - coordnos[no[1]-1][0]
    dy_2 = coordnos[no[2]-1][1] - coordnos[no[1]-1][1]
    b    = (dx_2**2+dy_2**2)**0.5/2
    #terceiro lado do elemento
    dx_3 = coordnos[no[3]-1][0] - coordnos[no[2]-1][0]
    dy_3 = coordnos[no[3]-1][1] - coordnos[no[2]-1][1]
    a_2  = (dx_3**2+dy_3**2)**0.5/2
    #terceiro lado do elemento
    dx_4 = coordnos[no[0]-1][0] - coordnos[no[3]-1][0]
    dy_4 = coordnos[no[0]-1][1] - coordnos[no[3]-1][1]
    b_2  = (dx_4**2+dy_4**2)**0.5/2     
    #o termo "**" significa elevar seria o sinal "^" da cálculadora
    c[0][0] = dx/(2*a)
    c[0][1] = dy/(2*a) 
    cs = dx/(2*a)
    sn = dy/(2*a)     
    if a <= 10e-8:
      print("Comprimento do elemento nulo")
      sys.exit()
    if abs(a-a_2) >= 10e-8 or abs(b-b_2) >= 10e-8:
      print("Comprimento do elemento nulo")
      sys.exit()
  elif tipoelem == "EP-RQ4_ISO":
    c = np.zeros((2,2))
    #primeiro lado do elemento
    dx = coordnos[no[1]-1][0] - coordnos[no[0]-1][0]
    dy = coordnos[no[1]-1][1] - coordnos[no[0]-1][1]
    a  = (dx**2+dy**2)**0.5/2
    #segundo lado do elemento
    dx_2 = coordnos[no[2]-1][0] - coordnos[no[1]-1][0]
    dy_2 = coordnos[no[2]-1][1] - coordnos[no[1]-1][1]
    b    = (dx_2**2+dy_2**2)**0.5/2 
    #o termo "**" significa elevar seria o sinal "^" da cálculadora
    c[0][0] = dx/(2*a)
    c[0][1] = dy/(2*a) 
    cs = dx/(2*a)
    sn = dy/(2*a) 
  else:
    print("Dimensões deste elemento não implementadas, favor verifique o elemento")
    sys.exit()  
  return cs, sn, a, b

# 11 - Função que determina os esforços do elemento Q4
def EP_RQ4_DeformacoesTensoes(E, nu, a , b, uel , tipoestr):
  #local
  x = 0
  y = 0
  B = np.zeros((3,8))
  B[0][0]= -(1/4)*(b-y)/(a*b);
  B[0][2]= (1/4)*(b-y)/(a*b);
  B[0][4]= (1/4)*(b+y)/(a*b);
  B[0][6]= -(1/4)*(b+y)/(a*b);
  B[1][1]= -(1/4)*(a-x)/(a*b);
  B[1][3]= -(1/4)*(a+x)/(a*b);
  B[1][5]= (1/4)*(a+x)/(a*b);
  B[1][7]= (1/4)*(a-x)/(a*b);
  B[2][0]= -(1/4)*(a-x)/(a*b);
  B[2][1]= -(1/4)*(b-y)/(a*b);
  B[2][2]= -(1/4)*(a+x)/(a*b);
  B[2][3]= (1/4)*(b-y)/(a*b);
  B[2][4]= (1/4)*(a+x)/(a*b);
  B[2][5]= (1/4)*(b+y)/(a*b);
  B[2][6]= (1/4)*(a-x)/(a*b);
  B[2][7]= -(1/4)*(b+y)/(a*b);
  if tipoestr == "EPD":
    E = E/(1-nu**2)
    nu = nu/(1-nu)
  
  defor = np.matmul(B,uel)
    
  Ee = np.zeros((3,3))
  Ee[0][0] = 1;
  Ee[0][1] = nu;
  Ee[1][0] = nu; 
  Ee[1][1] = 1;
  Ee[2][2] = (1-nu)*(1/2);

  Ee      = (E/(1-nu**2))*Ee;
  tens = np.matmul(Ee,defor);
  
  return defor, tens

def EP_RQ4_ISO_DeformacoesTensoes(t,x_1,y_1,x_2,y_2,x_3,y_3,x_4,y_4,xi,eta,tipoestr,E,nu):
  #Matriz de elasticidade
  if tipoestr == "EPD":
    E  = E/(1-nu**2)
    nu = nu/(1-nu)
  
  Ee = np.zeros((3,3))
  Ee[0][0] = 1;
  Ee[0][1] = nu;
  Ee[1][0] = nu; 
  Ee[1][1] = 1;
  Ee[2][2] = (1-nu)*(1/2)
  Ee       = (E/(1-nu**2))*Ee

  #Jacobiano
  B = np.zeros((3,8))
  J=(1/8)*x_1*y_2-(1/8)*x_1*y_4-(1/8)*x_2*y_1+(1/8)*x_2*y_3-(1/8)*x_3*y_2+(1/8)*x_3*y_4+(1/8)*x_4*y_1-(1/8)*x_4*y_3-(1/8)*x_2*y_4*xi-(1/8)*x_1*eta*y_2+(1/8)*x_2*eta*y_1+(1/8)*x_1*eta*y_3-(1/8)*x_2*eta*y_4+(1/8)*x_3*eta*y_4+(1/8)*x_4*eta*y_2-(1/8)*x_3*eta*y_1+(1/8)*x_2*y_3*xi-(1/8)*x_1*y_3*xi-(1/8)*x_4*eta*y_3-(1/8)*x_4*y_1*xi+(1/8)*x_4*y_2*xi+(1/8)*x_3*y_1*xi-(1/8)*x_3*y_2*xi+(1/8)*x_1*y_4*xi;
  
  B[0][0]=(((1/4)*xi-1/4)*y_1+(-(1/4)*xi-1/4)*y_2+((1/4)*xi+1/4)*y_3+(-(1/4)*xi+1/4)*y_4)*((1/4)*eta-1/4)+(-((1/4)*eta-1/4)*y_1-(-(1/4)*eta+1/4)*y_2-((1/4)*eta+1/4)*y_3-(-(1/4)*eta-1/4)*y_4)*((1/4)*xi-1/4);
  B[0][2]=(((1/4)*xi-1/4)*y_1+(-(1/4)*xi-1/4)*y_2+((1/4)*xi+1/4)*y_3+(-(1/4)*xi+1/4)*y_4)*(-(1/4)*eta+1/4)+(-((1/4)*eta-1/4)*y_1-(-(1/4)*eta+1/4)*y_2-((1/4)*eta+1/4)*y_3-(-(1/4)*eta-1/4)*y_4)*(-(1/4)*xi-1/4);
  B[0][4]=(((1/4)*xi-1/4)*y_1+(-(1/4)*xi-1/4)*y_2+((1/4)*xi+1/4)*y_3+(-(1/4)*xi+1/4)*y_4)*((1/4)*eta+1/4)+(-((1/4)*eta-1/4)*y_1-(-(1/4)*eta+1/4)*y_2-((1/4)*eta+1/4)*y_3-(-(1/4)*eta-1/4)*y_4)*((1/4)*xi+1/4);
  B[0][6]=(((1/4)*xi-1/4)*y_1+(-(1/4)*xi-1/4)*y_2+((1/4)*xi+1/4)*y_3+(-(1/4)*xi+1/4)*y_4)*(-(1/4)*eta-1/4)+(-((1/4)*eta-1/4)*y_1-(-(1/4)*eta+1/4)*y_2-((1/4)*eta+1/4)*y_3-(-(1/4)*eta-1/4)*y_4)*(-(1/4)*xi+1/4);
  B[1][1]=(-((1/4)*xi-1/4)*x_1-(-(1/4)*xi-1/4)*x_2-((1/4)*xi+1/4)*x_3-(-(1/4)*xi+1/4)*x_4)*((1/4)*eta-1/4)+(((1/4)*eta-1/4)*x_1+(-(1/4)*eta+1/4)*x_2+((1/4)*eta+1/4)*x_3+(-(1/4)*eta-1/4)*x_4)*((1/4)*xi-1/4);
  B[1][3]=(-((1/4)*xi-1/4)*x_1-(-(1/4)*xi-1/4)*x_2-((1/4)*xi+1/4)*x_3-(-(1/4)*xi+1/4)*x_4)*(-(1/4)*eta+1/4)+(((1/4)*eta-1/4)*x_1+(-(1/4)*eta+1/4)*x_2+((1/4)*eta+1/4)*x_3+(-(1/4)*eta-1/4)*x_4)*(-(1/4)*xi-1/4);
  B[1][5]=(-((1/4)*xi-1/4)*x_1-(-(1/4)*xi-1/4)*x_2-((1/4)*xi+1/4)*x_3-(-(1/4)*xi+1/4)*x_4)*((1/4)*eta+1/4)+(((1/4)*eta-1/4)*x_1+(-(1/4)*eta+1/4)*x_2+((1/4)*eta+1/4)*x_3+(-(1/4)*eta-1/4)*x_4)*((1/4)*xi+1/4);
  B[1][7]=(-((1/4)*xi-1/4)*x_1-(-(1/4)*xi-1/4)*x_2-((1/4)*xi+1/4)*x_3-(-(1/4)*xi+1/4)*x_4)*(-(1/4)*eta-1/4)+(((1/4)*eta-1/4)*x_1+(-(1/4)*eta+1/4)*x_2+((1/4)*eta+1/4)*x_3+(-(1/4)*eta-1/4)*x_4)*(-(1/4)*xi+1/4);
  B[2][0]=(-((1/4)*xi-1/4)*x_1-(-(1/4)*xi-1/4)*x_2-((1/4)*xi+1/4)*x_3-(-(1/4)*xi+1/4)*x_4)*((1/4)*eta-1/4)+(((1/4)*eta-1/4)*x_1+(-(1/4)*eta+1/4)*x_2+((1/4)*eta+1/4)*x_3+(-(1/4)*eta-1/4)*x_4)*((1/4)*xi-1/4);
  B[2][1]=(((1/4)*xi-1/4)*y_1+(-(1/4)*xi-1/4)*y_2+((1/4)*xi+1/4)*y_3+(-(1/4)*xi+1/4)*y_4)*((1/4)*eta-1/4)+(-((1/4)*eta-1/4)*y_1-(-(1/4)*eta+1/4)*y_2-((1/4)*eta+1/4)*y_3-(-(1/4)*eta-1/4)*y_4)*((1/4)*xi-1/4);
  B[2][2]=(-((1/4)*xi-1/4)*x_1-(-(1/4)*xi-1/4)*x_2-((1/4)*xi+1/4)*x_3-(-(1/4)*xi+1/4)*x_4)*(-(1/4)*eta+1/4)+(((1/4)*eta-1/4)*x_1+(-(1/4)*eta+1/4)*x_2+((1/4)*eta+1/4)*x_3+(-(1/4)*eta-1/4)*x_4)*(-(1/4)*xi-1/4);
  B[2][3]=(((1/4)*xi-1/4)*y_1+(-(1/4)*xi-1/4)*y_2+((1/4)*xi+1/4)*y_3+(-(1/4)*xi+1/4)*y_4)*(-(1/4)*eta+1/4)+(-((1/4)*eta-1/4)*y_1-(-(1/4)*eta+1/4)*y_2-((1/4)*eta+1/4)*y_3-(-(1/4)*eta-1/4)*y_4)*(-(1/4)*xi-1/4);
  B[2][4]=(-((1/4)*xi-1/4)*x_1-(-(1/4)*xi-1/4)*x_2-((1/4)*xi+1/4)*x_3-(-(1/4)*xi+1/4)*x_4)*((1/4)*eta+1/4)+(((1/4)*eta-1/4)*x_1+(-(1/4)*eta+1/4)*x_2+((1/4)*eta+1/4)*x_3+(-(1/4)*eta-1/4)*x_4)*((1/4)*xi+1/4);
  B[2][5]=(((1/4)*xi-1/4)*y_1+(-(1/4)*xi-1/4)*y_2+((1/4)*xi+1/4)*y_3+(-(1/4)*xi+1/4)*y_4)*((1/4)*eta+1/4)+(-((1/4)*eta-1/4)*y_1-(-(1/4)*eta+1/4)*y_2-((1/4)*eta+1/4)*y_3-(-(1/4)*eta-1/4)*y_4)*((1/4)*xi+1/4);
  B[2][6]=(-((1/4)*xi-1/4)*x_1-(-(1/4)*xi-1/4)*x_2-((1/4)*xi+1/4)*x_3-(-(1/4)*xi+1/4)*x_4)*(-(1/4)*eta-1/4)+(((1/4)*eta-1/4)*x_1+(-(1/4)*eta+1/4)*x_2+((1/4)*eta+1/4)*x_3+(-(1/4)*eta-1/4)*x_4)*(-(1/4)*xi+1/4);
  B[2][7]=(((1/4)*xi-1/4)*y_1+(-(1/4)*xi-1/4)*y_2+((1/4)*xi+1/4)*y_3+(-(1/4)*xi+1/4)*y_4)*(-(1/4)*eta-1/4)+(-((1/4)*eta-1/4)*y_1-(-(1/4)*eta+1/4)*y_2-((1/4)*eta+1/4)*y_3-(-(1/4)*eta-1/4)*y_4)*(-(1/4)*xi+1/4);
 
  JB=B/J;
  
  return JB, Ee

#-----------------CHAMADAS DAS FUNÇÕES PRINCIPAIS DO PROGRAMA-----------

# 1-Chamada da função de leitura da estrutura
  #1.1-definição das propriedades básicas do elemento:
  #1.2-número do elemento
  #1.3-número de elementos carregados, se for treliça deve ser zero
[nglno, ncoord, npropmat, npropgeo, nnoselem, ncarelem] = Leitura_de_dados(tipoestr, tipoelem)

# 2-Chamada da função de graus de liberdade da estrutura toda
[glno, neq] = Grau_de_liberdade(tipoestr, nnos, nglno, naps, restrsap)

# 3-Criação da matriz de rigidez da estrutura
Kestr = MatrizDeRigidezDaEstrutura(tipoestr, tipoelem, nglno, nnoselem, neq, coordnos, propelems, propmats, propgeo, glno)
print("------Matriz:--------- \n")
print(Kestr)

# 4-Chamada da função para montagem do vetor de forças externas da estrutura
Festr = VetorDeForcasDaEstrutura(tipoestr, tipoelem, nglno, nnoselem, nnoscar, nelemscar, neq, coordnos, propelems, cargasnos, cargaselems, glno, ncarelem)
print("------Vetor de forças nodal-----\n")
#print(Festr)

# 5-Chamada da função para determinação dos deslocamentos nodais
Uestr, UestrTotal = DescolamentosNodais(tipoestr, nglno, nnos, Kestr, Festr, neq, glno)
print("------VETOR DE DESLOCAMENTO NODAL------\n")
print('#################teste#################')
print(UestrTotal)

# 6-Esforços ao longo da estrutura
#[status, Deformacao, Tensao]  = EsforcosDaEstrutura(nelems, propelems, nnoselem, propmats, propgeo, coordnos, nglno, glno, tipoelem, Uestr, ncarelem, cargaselems)
#if tipoelem != "EP-RQ4_ISO":
#  print("-----Deformação nos elementos----\n")
#  print(Deformacao)
#  print("-----Tensão nos elementos--------\n")
#  print(Tensao)
#  print("\n",status)
#-----------------FIM DO PROGRAMA------


