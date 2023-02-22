#from ftplib import FTP
from time import sleep
import shutil
import os

origem = "C:/Users/José Filho/Downloads" # Caminho do DIR origem
destino = "D:/Downloads" # Caminho do DIR destino

while True:    
    arquivos = os.listdir(origem)
    #ftp = FTP('Insira caminho FTP')
    # Faz login no servidor FTP
    # ftp.login('usuario', 'senha')
    for arquivo in arquivos:        
        caminho_origem = os.path.join(origem, arquivo) 
        caminho_destino = os.path.join(destino, arquivo)
        try: # Tenta mover o arquivo da pasta de origem para a pasta de destino
            shutil.move(caminho_origem, caminho_destino)
            print(f'Arquivo {arquivo} movido com sucesso!')
        except:
            print(f'Não foi possível mover o arquivo {arquivo}!')
    
    # Espera um tempo antes de verificar novamente a pasta de origem
    sleep(1)

