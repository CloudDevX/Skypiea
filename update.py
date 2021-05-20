#This is the Update file for the Skypiea launcher
if Version != "0.0.1":   
    Max = 13
    Taches.append(r'os.mkdir(CHEMIN+r"\launcher")')
    Taches.append(r'Options = open(CHEMIN+r"\launcher\options.txt", "w")')
    Taches.append(r'Options.write("0.0.1")')
    Taches.append(r'Options.close()')
    Taches.append(r'os.mkdir(CHEMIN+r"\mods")')
    Taches.append(r'os.mkdir(CHEMIN+r"\assets")')
    Taches.append(r'os.mkdir(CHEMIN+r"\assets\panorama")')
    Taches.append(r'Download("https://raw.githubusercontent.com/CloudDevX/Skypiea/main/Panorama/panorama_0.png", r"\assets\panorama\panorama_0.png")')
    Taches.append(r'Download("https://raw.githubusercontent.com/CloudDevX/Skypiea/main/Panorama/panorama_1.png", r"\assets\panorama\panorama_1.png")')
    Taches.append(r'Download("https://raw.githubusercontent.com/CloudDevX/Skypiea/main/Panorama/panorama_2.png", r"\assets\panorama\panorama_2.png")')
    #10
    Taches.append(r'Download("https://raw.githubusercontent.com/CloudDevX/Skypiea/main/Panorama/panorama_3.png", r"\assets\panorama\panorama_3.png")')
    Taches.append(r'Download("https://raw.githubusercontent.com/CloudDevX/Skypiea/main/Panorama/panorama_4.png", r"\assets\panorama\panorama_4.png")')
    Taches.append(r'Download("https://raw.githubusercontent.com/CloudDevX/Skypiea/main/Panorama/panorama_5.png", r"\assets\panorama\panorama_5.png")')

else:
    Loading = Max
