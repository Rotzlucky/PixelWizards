---
layout: lesson
title: "Lektion 1: Dein erstes Python-Programm"
lang: de
next_lesson: lesson2.html
objectives:
  - Verstehen, was Python ist und warum es großartig für die Erstellung von Spielen ist
  - Python auf deinem Computer einrichten
  - Dein allererstes Python-Programm schreiben
  - Über Print-Anweisungen, Kommentare und Variablen lernen
---

# Dein erstes Python-Programm

Hallo, zukünftiger Spieleentwickler! Bist du bereit, dein Coding-Abenteuer zu beginnen? In dieser ersten Lektion werden wir lernen, was Python ist, es auf deinem Computer einrichten und unser allererstes Programm schreiben!

## Was ist Python?

Python ist eine Programmiersprache - eine spezielle Sprache, mit der du mit Computern sprechen und ihnen sagen kannst, was sie tun sollen. Sie ist nach der Komikertruppe "Monty Python" benannt, nicht nach der Schlange! 😄

Python ist eine der besten Sprachen für Anfänger, weil:
- Sie leicht zu lesen und zu schreiben ist (fast wie Englisch!)
- Sie von professionellen Programmierern bei NASA, Google und YouTube verwendet wird
- Sie perfekt für die Erstellung von Spielen, Websites, Robotern und mehr ist!

## Python einrichten

Bevor wir mit dem Programmieren beginnen können, müssen wir Python auf deinem Computer installieren. Bitte einen Erwachsenen um Hilfe bei diesem Teil, falls nötig.

### Schritt 1: Python herunterladen

1. Gehe zu [python.org/downloads](https://www.python.org/downloads/)
2. Klicke auf den großen "Download Python"-Button
3. Führe den Installer aus, der heruntergeladen wird

### Schritt 2: Python installieren

Während der Installation:
1. Stelle sicher, dass du das Kästchen "Add Python to PATH" ankreuzt
2. Klicke auf "Install Now"
3. Warte, bis die Installation abgeschlossen ist

### Schritt 3: Deine Installation testen

Lass uns sicherstellen, dass Python korrekt installiert ist:

1. Öffne die "Eingabeaufforderung" (Windows) oder das "Terminal" (Mac/Linux)
2. Tippe `python --version` ein und drücke Enter
3. Du solltest etwas wie `Python 3.9.5` sehen (die Zahlen können unterschiedlich sein)

Gut gemacht! Python ist jetzt auf deinem Computer installiert!

## Dein erstes Python-Programm: Hello, World!

Jetzt kommt der spannende Teil - dein erstes Programm schreiben! Wir beginnen mit dem klassischen "Hello, World!"-Programm, das Programmierer seit Jahrzehnten als ihr erstes Programm verwenden.

### Schritt 1: IDLE öffnen

IDLE ist ein einfaches Programm, das mit Python mitgeliefert wird und mit dem du Python-Code schreiben und ausführen kannst.

1. Suche auf deinem Computer nach "IDLE" und öffne es
2. Du siehst ein Fenster namens "Python Shell" mit etwas Text und einer Eingabeaufforderung (`>>>`)

### Schritt 2: Deine erste Codezeile schreiben

Tippe an der Eingabeaufforderung (`>>>`) Folgendes genau wie gezeigt ein und drücke Enter:

```python
print("Hello, World!")
```

Du solltest sehen:

```
Hello, World!
```

**HERZLICHEN GLÜCKWUNSCH!** Du hast gerade dein erstes Python-Programm geschrieben! 🎉

## Lass uns verstehen, was passiert ist

Die `print()`-Funktion in Python ist wie ein magischer Zauberspruch, der Text auf dem Bildschirm erscheinen lässt. Was auch immer du zwischen die Klammern und Anführungszeichen setzt, wird angezeigt.

Lass uns noch mehr ausprobieren:

```python
print("Mein Name ist Python-Programmierer!")
print("Ich lerne, tolle Spiele zu machen!")
```

## Kommentare zu deinem Code hinzufügen

Kommentare sind Notizen, die du zu deinem Code hinzufügen kannst. Der Computer ignoriert sie, aber sie helfen Menschen zu verstehen, was dein Code tut.

Um einen Kommentar in Python zu schreiben, verwende das `#`-Symbol:

```python
# Dies ist ein Kommentar - der Computer wird diese Zeile ignorieren
print("Aber diese Zeile wird angezeigt!") # Du kannst Kommentare auch am Ende einer Zeile platzieren
```

## Variablen: Informationen speichern

Variablen sind wie magische Behälter, die Informationen für dich aufbewahren können. Du kannst ihnen Namen geben und Daten hineinlegen.

```python
spieler_name = "Alex"
spieler_alter = 10
print("Hallo, mein Name ist", spieler_name, "und ich bin", spieler_alter, "Jahre alt!")
```

Versuche, die Werte zu ändern und sieh, was passiert!

## Lass uns ein einfaches Begrüßungsprogramm erstellen

Jetzt wollen wir alles zusammenfügen, um ein Programm zu erstellen, das den Benutzer begrüßt:

1. Klicke in IDLE auf "File" und dann auf "New File"
2. Tippe den folgenden Code ein:

```python
# Mein erstes Python-Programm
print("Willkommen zur Python-Spieleprogrammierung!")

# Nach dem Namen des Spielers fragen
spieler_name = input("Wie heißt du? ")

# Den Spieler begrüßen
print("Hallo,", spieler_name, "! Lass uns gemeinsam Spiele erstellen!")
print("Du wirst ein toller Spieleentwickler werden!")
```

3. Speichere die Datei, indem du auf "File" und dann auf "Save As..." klickst und nenne sie `begruessung.py`
4. Führe das Programm aus, indem du auf "Run" und dann auf "Run Module" klickst (oder F5 drückst)
5. Wenn du gefragt wirst, gib deinen Namen ein und drücke Enter

Fantastisch! Du hast ein Programm erstellt, das mit dem Benutzer interagiert!

## Probier es selbst aus: Herausforderungen

Bevor wir diese Lektion beenden, hier sind einige lustige Herausforderungen zum Ausprobieren:

1. **Personalisiere es**: Ändere das Begrüßungsprogramm so, dass es auch nach dem Alter und der Lieblingsfarbe des Benutzers fragt.

2. **ASCII-Kunst**: Verwende mehrere Print-Anweisungen, um ein einfaches Bild zu erstellen. Zum Beispiel:

```python
print("   /\\")
print("  /  \\")
print(" /    \\")
print("/______\\")
print("  |  |")
print("  |__|")
```

3. **Geschichtenanfang**: Erstelle ein Programm, das nach einem Charakternamen, einem Ort und einem Gegenstand fragt und diese dann verwendet, um eine Geschichte zu beginnen.

## Was kommt als Nächstes?

In der nächsten Lektion werden wir mehr über Variablen und verschiedene Arten von Daten in Python lernen. Wir werden beginnen, das Fundament für unser Spiel zu legen, indem wir verstehen, wie man mit Zahlen und Text arbeitet und Entscheidungen in unserem Code trifft.

Denk daran, Programmieren zu lernen ist wie eine neue Sprache oder ein Instrument zu lernen - es braucht Übung! Mach dir keine Sorgen, wenn du nicht sofort alles verstehst. Je mehr du mit Python spielst, desto besser wirst du!

**Programmiere weiter, zukünftiger Spieleentwickler!** 🚀