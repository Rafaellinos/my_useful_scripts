import sys

try: 
    from pytube import YouTube
except ImportError as err:
    print("Erro ao importar YT library.\nPor favor, \
        utilize o comando pip3 install pytube3 --upgrade para instalar.")

url = sys.argv[1]
"""
Ex: https://youtu.be/4Jq1NIfTWYE
"""
print(f"Baixando vídeo da URL {url}...")
yt = YouTube(url).streams.get_highest_resolution().download()
