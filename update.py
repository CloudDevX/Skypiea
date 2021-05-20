#This is the Update file for the Skypiea launcher
if Version != "0.0.1":   
    Max = 7
    Taches.append(r'os.mkdir(CHEMIN+r"\launcher")')
    Taches.append(r'Options = open(CHEMIN+r"\launcher\options.txt", "w")')
    Taches.append(r'Options.write("0.0.1")')
    Taches.append(r'Options.close()')
    Taches.append(r'os.mkdir(CHEMIN+r"\mods")')
    Taches.append(r'os.mkdir(CHEMIN+r"\assets")')
    Taches.append(r'os.mkdir(CHEMIN+r"\assets\panorama")')
