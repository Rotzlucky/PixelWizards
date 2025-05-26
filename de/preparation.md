---
layout: lesson
title: "Vorbereitung"
lang: de
permalink: /de/preparation/
next_lesson: /de/lessons/lesson1/
order: 0
objectives:
  - Python auf deinem Mac installieren
  - PyCharm IDE herunterladen und einrichten
  - Testen, dass alles korrekt funktioniert
  - Mit der PyCharm-Oberfläche vertraut werden
---

# Deinen Mac für Python-Programmierung vorbereiten

Bevor wir unsere aufregende Reise in die Spieleprogrammierung beginnen, müssen wir die richtigen Programme auf deinem Computer installieren. Stell dir vor, als würdest du deine Kunstmaterialien vor dem Malen eines Meisterwerks vorbereiten!

Wir werden zwei wichtige Programme installieren:
1. **Python** - Das ist die Programmiersprache, die wir verwenden werden, um Spiele zu erstellen
2. **PyCharm** - Das ist ein spezieller Texteditor, der extra für das Schreiben von Python-Code entwickelt wurde

Mach dir keine Sorgen, wenn das am Anfang kompliziert erscheint - wir gehen jeden Schritt sorgfältig durch, und wenn einmal alles eingerichtet ist, musst du das nie wieder machen!

## Teil 1: Python installieren

Python ist die Programmiersprache, die wir in all unseren Lektionen verwenden werden. Lass uns sie auf deinem Mac installieren.

### Schritt 1: Python herunterladen

1. Öffne deinen Webbrowser (Safari, Chrome oder Firefox)
2. Gehe zu [python.org/downloads](https://www.python.org/downloads/)
3. Du siehst einen großen gelben Button mit "Download Python 3.x.x" (die Zahlen können anders sein - das ist okay!)

*[Screenshot-Platzhalter: Python.org Download-Seite mit dem gelben Download-Button]*

4. Klicke auf diesen gelben Download-Button
5. Eine Datei wird heruntergeladen - sie heißt etwa "python-3.x.x-macosx10.9.pkg"
6. Warte, bis der Download fertig ist (du siehst ihn in deinem Downloads-Ordner oder unten im Browser)

*[Screenshot-Platzhalter: Download-Fortschritt im Browser]*

### Schritt 2: Python installieren

1. Finde die heruntergeladene Datei (wahrscheinlich in deinem Downloads-Ordner)
2. Doppelklicke auf die Datei, um das Installationsprogramm zu starten

*[Screenshot-Platzhalter: Python-Installationsdatei im Downloads-Ordner]*

3. Du siehst einen Willkommensbildschirm für das Python-Installationsprogramm - klicke "Fortfahren"

*[Screenshot-Platzhalter: Python-Installer Willkommensbildschirm]*

4. Auf dem nächsten Bildschirm lies die wichtigen Informationen und klicke "Fortfahren"
5. Du siehst die Software-Lizenzvereinbarung - klicke "Fortfahren" und dann "Akzeptieren"
6. Wähle aus, wo Python installiert werden soll (der Standardort ist in Ordnung) und klicke "Fortfahren"
7. Klicke "Installieren" - du musst möglicherweise das Passwort deines Macs eingeben

*[Screenshot-Platzhalter: Python-Installationsort-Bildschirm]*

8. Warte, bis die Installation abgeschlossen ist - das kann ein paar Minuten dauern
9. Wenn du "Die Installation war erfolgreich" siehst, klicke "Schließen"

*[Screenshot-Platzhalter: Erfolgreiche Installation-Bildschirm]*

### Schritt 3: Python-Installation überprüfen

Lass uns sicherstellen, dass Python korrekt installiert wurde:

1. Öffne die "Terminal"-App auf deinem Mac:
   - Drücke `Command + Leertaste`, um die Spotlight-Suche zu öffnen
   - Tippe "Terminal" und drücke Enter

*[Screenshot-Platzhalter: Spotlight-Suche zeigt Terminal]*

2. Im Terminal-Fenster tippe genau: `python3 --version`
3. Drücke Enter
4. Du solltest etwas wie "Python 3.x.x" erscheinen sehen

*[Screenshot-Platzhalter: Terminal zeigt Python-Version]*

Wenn du die Python-Versionsnummer siehst, herzlichen Glückwunsch! Python ist erfolgreich installiert.

## Teil 2: PyCharm installieren

PyCharm ist ein mächtiges Programm, das das Schreiben von Python-Code viel einfacher macht. Es ist wie ein intelligenter Assistent, der dir beim Programmieren hilft!

### Schritt 1: PyCharm herunterladen

1. Gehe zu [jetbrains.com/pycharm/download](https://www.jetbrains.com/pycharm/download/)
2. Stelle sicher, dass "macOS" oben ausgewählt ist
3. Du siehst zwei Versionen: "Professional" und "Community"
4. Klicke "Download" unter **Community** (ist kostenlos und perfekt zum Lernen!)

*[Screenshot-Platzhalter: PyCharm Download-Seite zeigt Community Edition]*

5. Der Download beginnt - es ist eine große Datei (etwa 500MB), also kann es eine Weile dauern
6. Warte, bis "pycharm-community-2023.x.x.dmg" fertig heruntergeladen ist

*[Screenshot-Platzhalter: Download-Fortschritt für PyCharm]*

### Schritt 2: PyCharm installieren

1. Finde die heruntergeladene PyCharm-Datei in deinem Downloads-Ordner
2. Doppelklicke auf die ".dmg"-Datei

*[Screenshot-Platzhalter: PyCharm DMG-Datei in Downloads]*

3. Ein neues Fenster öffnet sich und zeigt die PyCharm-Anwendung und einen Programme-Ordner
4. Ziehe das PyCharm-Symbol auf das Programme-Ordner-Symbol

*[Screenshot-Platzhalter: PyCharm in den Programme-Ordner ziehen]*

5. Warte, bis das Kopieren abgeschlossen ist
6. Schließe das Installer-Fenster
7. Du findest PyCharm jetzt in deinem Programme-Ordner oder Launchpad

### Schritt 3: PyCharm zum ersten Mal einrichten

1. Öffne PyCharm aus deinem Programme-Ordner oder Launchpad
2. Das erste Mal könntest du eine Sicherheitswarnung sehen - klicke "Öffnen"

*[Screenshot-Platzhalter: Sicherheitswarnung-Dialog]*

3. PyCharm fragt nach dem Import von Einstellungen - wähle "Einstellungen nicht importieren" und klicke "OK"

*[Screenshot-Platzhalter: Einstellungen importieren-Dialog]*

4. Akzeptiere die Benutzervereinbarung, indem du "Akzeptieren" klickst
5. Wähle, ob du Nutzungsstatistiken senden möchtest (beide Optionen sind in Ordnung) und klicke "Fortfahren"

*[Screenshot-Platzhalter: Nutzungsstatistiken-Dialog]*

6. PyCharm zeigt dir einen Willkommensbildschirm mit Themes - wähle das, was dir gefällt (du kannst das später ändern)

*[Screenshot-Platzhalter: Theme-Auswahl-Bildschirm]*

7. Du könntest Bildschirme über Plugins sehen - du kannst diese überspringen, indem du "Übrige überspringen und Standards setzen" klickst

*[Screenshot-Platzhalter: Plugin-Konfiguration-Bildschirme]*

### Schritt 4: Python in PyCharm konfigurieren

Jetzt müssen wir PyCharm sagen, wo es das gerade installierte Python finden kann:

1. Auf dem PyCharm-Willkommensbildschirm klicke "Neues Projekt"

*[Screenshot-Platzhalter: PyCharm-Willkommensbildschirm mit Neues Projekt-Button]*

2. Du siehst einen "Neues Projekt"-Dialog
3. Stelle sicher, dass "Pure Python" links ausgewählt ist
4. Wähle einen Ort für dein Projekt (der Standard ist in Ordnung)
5. Erweitere den "Python Interpreter"-Bereich, indem du auf den Pfeil klickst
6. Stelle sicher, dass "Interpreter hinzufügen" ausgewählt ist
7. Wähle "System Interpreter" aus der Dropdown-Liste
8. Klicke den "..."-Button neben dem Interpreter-Pfad

*[Screenshot-Platzhalter: Neues Projekt-Dialog mit Interpreter-Einstellungen]*

9. Navigiere zu `/usr/bin/python3` oder `/usr/local/bin/python3` (PyCharm könnte es automatisch finden)
10. Klicke "OK", um den Interpreter auszuwählen
11. Klicke "Erstellen", um dein erstes Projekt zu erstellen

*[Screenshot-Platzhalter: Interpreter-Auswahl-Dialog]*

### Schritt 5: Testen, dass alles funktioniert

Lass uns ein einfaches Programm erstellen, um zu testen, dass alles korrekt eingerichtet ist:

1. PyCharm öffnet sich mit deinem neuen Projekt
2. Rechtsklicke im Projekt-Panel links und wähle "Neu" → "Python-Datei"

*[Screenshot-Platzhalter: Rechtsklick-Menü zeigt Neue Python-Datei-Option]*

3. Benenne deine Datei "test" und drücke Enter
4. PyCharm erstellt eine neue Datei und öffnet sie im Editor
5. Tippe den folgenden Code genau wie gezeigt:

```python
print("Hallo, Welt! Python und PyCharm funktionieren!")
```

*[Screenshot-Platzhalter: PyCharm-Editor mit dem Test-Code]*

6. Rechtsklicke im Editor und wähle "test ausführen"

*[Screenshot-Platzhalter: Rechtsklick-Menü zeigt Ausführen-Option]*

7. Du solltest ein Panel unten sehen, das die Ausgabe zeigt: "Hallo, Welt! Python und PyCharm funktionieren!"

*[Screenshot-Platzhalter: Ausgabe-Panel zeigt das Ergebnis]*

## Teil 3: Mit PyCharm vertraut werden

Jetzt, da alles funktioniert, lass uns schnell die PyCharm-Oberfläche kennenlernen:

### Hauptbereiche von PyCharm

*[Screenshot-Platzhalter: PyCharm-Oberfläche mit beschrifteten Bereichen]*

1. **Projekt-Panel** (linke Seite): Zeigt alle deine Dateien und Ordner
2. **Editor** (Mitte): Wo du deinen Code schreibst
3. **Ausgabe-Panel** (unten): Zeigt die Ergebnisse, wenn du deine Programme ausführst
4. **Menüleiste** (oben): Enthält alle Befehle und Optionen

### Wichtige Buttons und Funktionen

- **Grüner Play-Button**: Führt dein aktuelles Programm aus
- **Roter Quadrat-Button**: Stoppt ein laufendes Programm
- **Datei-Menü**: Neue Dateien erstellen, bestehende öffnen, deine Arbeit speichern
- **Ausführen-Menü**: Verschiedene Wege, deine Programme auszuführen und zu testen

### Nützliche Tastenkombinationen

- `Cmd + S`: Aktuelle Datei speichern
- `Cmd + R`: Aktuelles Programm ausführen
- `Cmd + Z`: Letzte Änderung rückgängig machen
- `Cmd + Shift + Z`: Wiederholen

## Fehlerbehebung bei häufigen Problemen

### Wenn Python nicht korrekt installiert wird:
- Stelle sicher, dass du die richtige Version für Mac heruntergeladen hast
- Versuche, deinen Computer neu zu starten und das Installationsprogramm erneut auszuführen
- Überprüfe, dass du genug Speicherplatz auf deiner Festplatte hast

### Wenn PyCharm Python nicht finden kann:
- In PyCharm gehe zu "PyCharm" → "Einstellungen" → "Projekt" → "Python Interpreter"
- Klicke das Zahnrad-Symbol und wähle "Hinzufügen"
- Wähle "System Interpreter" und durchsuche, um Python zu finden

### Wenn du Berechtigungsfehler bekommst:
- Du musst möglicherweise dein Mac-Passwort bei der Installation eingeben
- Stelle sicher, dass du als Administrator auf deinem Mac angemeldet bist

## Du bist bereit, mit dem Programmieren zu beginnen!

Herzlichen Glückwunsch! Du hast jetzt alles eingerichtet, um Python-Programmierung zu lernen. In unserer nächsten Lektion werden wir unser erstes Python-Programm schreiben und unsere Reise zur Erstellung fantastischer Spiele beginnen!

Denk daran:
- **Python** ist die Programmiersprache, die wir verwenden werden
- **PyCharm** ist unser Code-Editor, der das Programmieren einfacher macht
- Du kannst immer zu diesem Setup-Leitfaden zurückkehren, wenn du Hilfe brauchst

Bereit für dein erstes Programmierabenteuer? Lass uns zu [Quest 1: Wirke deinen ersten Python-Zauber]({{ '/de/lessons/lesson1/' | relative_url }}) gehen! 