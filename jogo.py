  import forca
  import adivinhacao
  
  def escolhe_jogo():
      print("*********************************")
      print("*******Escolha o eu jogo!********")
      
      print("(1) Forca (2) adivimhação")
      
      jogo = int(input("Qual jogo"))
      
      if(jogo == 1):
          print("Jogando forca")
          forca.jogar()
       elif(jogo == 2):
           print("Jogando  adivinhação")
           adivinhacao.jogar()
           
        if(_name_ == "_name_"):
            escolhe_jogo()
         