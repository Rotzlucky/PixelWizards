---
layout: lesson
title: "Quest 5: Erschaffe deine eigenen Zauber (Funktionen)"
lang: de
permalink: /de/lessons/lesson5/
previous_lesson: /de/lessons/lesson4/
next_lesson: /de/lessons/lesson6/
order: 5
difficulty: 3
xp: 225
objectives:
  - Lerne, deine eigenen magischen Funktionen (Zauber) zu erstellen
  - Verstehe Parameter und Rückgabewerte
  - Baue eine Sammlung wiederverwendbarer Zauberkomponenten auf
  - Erstelle eine magische Zauberbibliothek für deine Abenteuer
challenges:
  - title: "Begrüßungszauber"
    description: "Erstelle eine Funktion, die einen Namen entgegennimmt und eine personalisierte magische Begrüßung zurückgibt."
    hint: "Verwende def, um die Funktion zu erstellen, und return, um einen String mit dem Namen der Person zurückzugeben."
  - title: "Magischer Rechner"
    description: "Erstelle Funktionen für grundlegende Rechenoperationen (addieren, subtrahieren, multiplizieren, dividieren) mit magischen Zahlen."
    hint: "Jede Funktion sollte zwei Parameter entgegennehmen und das Ergebnis der Operation zurückgeben."
  - title: "Zauberkraft-Analysator"
    description: "Erstelle eine Funktion, die einen Zaubernamen und ein Kraftlevel entgegennimmt und zurückgibt, ob es ein Anfänger-, Fortgeschrittenen- oder Expertenzauber ist."
    hint: "Verwende if/elif/else-Anweisungen in deiner Funktion, um basierend auf dem Kraftlevel zu kategorisieren."
---

# Quest 5: Erschaffe deine eigenen Zauber (Funktionen)

<i class="fas fa-magic"></i> Grüße, angehender Zaubererschmied! Heute lernst du eine der wichtigsten Fähigkeiten in den magischen Künsten: **das Erschaffen eigener Zauber**. In der Programmierung nennen wir diese benutzerdefinierten Zauber **Funktionen**.

## Warum eigene Zauber erschaffen?

Stell dir vor, du bist ein Zauberer, der mehrmals denselben Schutzzauber wirken muss. Anstatt jedes Mal die gesamte Beschwörung aufzusagen, wäre es nicht einfacher, nur "Schutz!" zu sagen und den Zauber zu aktivieren? Genau das machen Funktionen!

```python
# Ohne Funktionen (wiederholende Magie)
print("🛡️ Wirke Schutzzauber...")
print("✨ Magische Barrieren erheben sich...")
print("🌟 Du bist nun geschützt!")

print("🛡️ Wirke Schutzzauber...")
print("✨ Magische Barrieren erheben sich...")
print("🌟 Du bist nun geschützt!")

# Mit Funktionen (effiziente Magie!)
def wirke_schutz():
    print("🛡️ Wirke Schutzzauber...")
    print("✨ Magische Barrieren erheben sich...")
    print("🌟 Du bist nun geschützt!")

# Jetzt können wir ihn einfach wirken
wirke_schutz()
wirke_schutz()
```

## Erschaffe deinen ersten Zauber (Funktion)

Beginnen wir mit einem einfachen Begrüßungszauber:

```python
def magische_begruessung():
    print("🧙‍♂️ Grüße, Mitmagier!")
    print("✨ Möge dein Code fehlerfrei und deine Zauber mächtig sein!")

# Um deinen Zauber zu wirken (aufzurufen):
magische_begruessung()
```

### Die Anatomie eines Zaubers

```python
def zauber_name():
    # Dein magischer Code hier
    pass
```

- `def` - sagt Python, dass du einen neuen Zauber erschaffst
- `zauber_name()` - der Name deines Zaubers (mit Klammern)
- `:` - beginnt die Zauberdefinition
- Eingerückter Code - was passiert, wenn der Zauber gewirkt wird

## Zauber mit Zutaten (Parameter)

Die meisten mächtigen Zauber brauchen Zutaten! In der Programmierung nennen wir diese **Parameter**:

```python
def personalisierte_begruessung(zauberer_name):
    print(f"🧙‍♂️ Grüße, {zauberer_name}!")
    print(f"✨ Willkommen im magischen Reich!")

# Wirke den Zauber mit verschiedenen Namen
personalisierte_begruessung("Merlin")
personalisierte_begruessung("Gandalf")
personalisierte_begruessung("Hermine")
```

### Mehrere Zutaten

```python
def erstelle_trank(zutat1, zutat2, magie_level):
    print(f"🧪 Braue Trank mit {zutat1} und {zutat2}")
    print(f"⚡ Magie-Level: {magie_level}")
    
    if magie_level > 5:
        print("💥 MÄCHTIGER Trank erschaffen!")
    else:
        print("✨ Einfacher Trank erschaffen!")

# Probiere verschiedene Kombinationen
erstelle_trank("Drachenschuppe", "Einhornhaar", 8)
erstelle_trank("Pilz", "Wasser", 3)
```

## Zauber, die dir etwas zurückgeben (Rückgabewerte)

Manche Zauber tun nicht nur etwas - sie geben dir etwas zurück! Wie ein Zauber, der magische Kraft berechnet:

```python
def berechne_zauberkraft(basis_kraft, zauberer_level):
    gesamt_kraft = basis_kraft * zauberer_level
    return gesamt_kraft

# Verwende das Ergebnis des Zaubers
meine_kraft = berechne_zauberkraft(10, 5)
print(f"🔥 Deine Zauberkraft ist: {meine_kraft}")

# Oder verwende es direkt
if berechne_zauberkraft(15, 3) > 40:
    print("💪 Du bist bereit für fortgeschrittene Magie!")
```

### Ein magischer Rechner

```python
def magisches_addieren(zahl1, zahl2):
    ergebnis = zahl1 + zahl2
    print(f"✨ {zahl1} + {zahl2} = {ergebnis}")
    return ergebnis

def magisches_multiplizieren(zahl1, zahl2):
    ergebnis = zahl1 * zahl2
    print(f"🌟 {zahl1} × {zahl2} = {ergebnis}")
    return ergebnis

# Teste deinen magischen Rechner
summe = magisches_addieren(25, 17)
produkt = magisches_multiplizieren(6, 7)
```

## Baue deine Zauberbibliothek auf

Lass uns eine Sammlung nützlicher Zauber erstellen:

```python
# Zauberbibliothek: magische_zauber.py

def wirke_feuerball(schaden):
    """Ein Zauber, der einen Feuerball mit angegebenem Schaden erschafft."""
    print(f"🔥 FEUERBALL! Verursacht {schaden} Schaden!")
    return schaden

def heile_zauberer(aktuelle_gesundheit, heilkraft):
    """Ein Zauber, der einen Zauberer heilt."""
    neue_gesundheit = aktuelle_gesundheit + heilkraft
    print(f"💚 Heilende Magie fließt durch dich!")
    print(f"❤️ Gesundheit: {aktuelle_gesundheit} → {neue_gesundheit}")
    return neue_gesundheit

def pruefe_zauber_erfolg(fertigkeits_level, zauber_schwierigkeit):
    """Bestimmt, ob ein Zauberwirken erfolgreich ist."""
    erfolgs_chance = fertigkeits_level - zauber_schwierigkeit
    
    if erfolgs_chance >= 3:
        print("✨ PERFEKTER WURF! Zauber gelingt großartig!")
        return "perfekt"
    elif erfolgs_chance >= 0:
        print("👍 Guter Wurf! Zauber gelingt!")
        return "erfolg"
    else:
        print("💥 Zauber verpufft... Versuche es nochmal!")
        return "fehlschlag"

def generiere_zauberer_name(vorname):
    """Erstellt einen magischen Zauberernamen."""
    magische_titel = ["der Weise", "der Tapfere", "der Mystische", "der Mächtige"]
    import random
    titel = random.choice(magische_titel)
    zauberer_name = f"{vorname} {titel}"
    print(f"🎭 Dein Zaubername ist: {zauberer_name}")
    return zauberer_name

# Teste deine Zauberbibliothek
print("🧙‍♂️ Teste die Zauberbibliothek!")
print("=" * 40)

# Teste Kampfzauber
verursachter_schaden = wirke_feuerball(25)

# Teste Heilung
neue_lp = heile_zauberer(50, 30)

# Teste Zaubererfolg
ergebnis = pruefe_zauber_erfolg(7, 4)

# Generiere einen Zauberernamen
mein_zauberer_name = generiere_zauberer_name("Alex")
```

## Fortgeschrittene Zaubererschaffung

### Standard-Zutaten (Standard-Parameter)

```python
def erstelle_magischen_schild(staerke=5, dauer=10):
    print(f"🛡️ Erstelle magischen Schild...")
    print(f"💪 Stärke: {staerke}")
    print(f"⏰ Dauer: {dauer} Sekunden")

# Diese funktionieren alle!
erstelle_magischen_schild()                    # Verwendet Standards
erstelle_magischen_schild(8)                   # Benutzerdefinierte Stärke
erstelle_magischen_schild(staerke=12)          # Benannter Parameter
erstelle_magischen_schild(7, 15)              # Beide benutzerdefiniert
```

### Zauber mit mehreren Rückgabewerten

```python
def analysiere_magische_kreatur(kreatur_name, level):
    """Analysiert eine magische Kreatur und gibt mehrere Statistiken zurück."""
    gesundheit = level * 20
    magie_kraft = level * 15
    gefahr_level = "Niedrig" if level < 5 else "Hoch" if level > 8 else "Mittel"
    
    return gesundheit, magie_kraft, gefahr_level

# Entpacke die Ergebnisse
lp, mp, gefahr = analysiere_magische_kreatur("Drache", 10)
print(f"🐉 Drachen-Analyse:")
print(f"❤️ Gesundheit: {lp}")
print(f"⚡ Magiekraft: {mp}")
print(f"⚠️ Gefahrenlevel: {gefahr}")
```

## Herausforderung: Die ultimative Zaubererschaffungs-Werkstatt

Erstelle eine Datei namens `zauber_werkstatt.py` und baue deine eigene magische Zaubersammlung:

```python
import random

def willkommens_nachricht():
    """Zeigt eine Willkommensnachricht für die Zauberwerkstatt an."""
    print("🏰 Willkommen in der Zaubererschaffungs-Werkstatt! 🏰")
    print("✨ Hier kannst du magische Zauber erstellen und testen!")
    print("=" * 50)

def wuerfle_magischen_wuerfel(seiten=6):
    """Würfelt einen magischen Würfel mit angegebener Seitenzahl."""
    ergebnis = random.randint(1, seiten)
    print(f"🎲 Würfle magischen {seiten}-seitigen Würfel... Ergebnis: {ergebnis}")
    return ergebnis

def braue_zufalls_trank():
    """Braut einen zufälligen magischen Trank."""
    zutaten = ["Drachenschuppe", "Einhornhaar", "Phönixfeder", 
              "Mondsteinstaub", "Trolltränen", "Feenflügel"]
    farben = ["rot", "blau", "grün", "lila", "golden", "silbern"]
    
    zutat = random.choice(zutaten)
    farbe = random.choice(farben)
    potenz = random.randint(1, 10)
    
    print(f"🧪 Braue Trank mit {zutat}...")
    print(f"✨ Der Trank leuchtet {farbe}!")
    print(f"💪 Potenz-Level: {potenz}/10")
    
    return {"zutat": zutat, "farbe": farbe, "potenz": potenz}

def berechne_abenteuer_erfolg(gruppen_groesse, durchschnitts_level, quest_schwierigkeit):
    """Berechnet die Erfolgschance eines magischen Abenteuers."""
    basis_chance = (gruppen_groesse * 10) + (durchschnitts_level * 5)
    schwierigkeits_abzug = quest_schwierigkeit * 15
    erfolgs_chance = max(0, min(100, basis_chance - schwierigkeits_abzug))
    
    print(f"🗺️ Abenteuer-Analyse:")
    print(f"👥 Gruppengröße: {gruppen_groesse}")
    print(f"📊 Durchschnittslevel: {durchschnitts_level}")
    print(f"⚔️ Quest-Schwierigkeit: {quest_schwierigkeit}")
    print(f"🎯 Erfolgschance: {erfolgs_chance}%")
    
    if erfolgs_chance >= 80:
        print("🏆 Ausgezeichnet! Diese Quest sollte einfach sein!")
    elif erfolgs_chance >= 60:
        print("👍 Gute Erfolgschance!")
    elif erfolgs_chance >= 40:
        print("⚠️ Riskant, aber möglich!")
    else:
        print("💀 Sehr gefährlich! Erwäge mehr Vorbereitung!")
    
    return erfolgs_chance

def magischer_zahlen_generator(min_wert=1, max_wert=100, anzahl=1):
    """Generiert magische Zahlen für Zauber und Tränke."""
    zahlen = []
    for i in range(anzahl):
        zahl = random.randint(min_wert, max_wert)
        zahlen.append(zahl)
    
    print(f"🔢 {anzahl} magische Zahl(en) generiert: {zahlen}")
    return zahlen if anzahl > 1 else zahlen[0]

# Hauptprogramm der Zauberwerkstatt
def starte_zauber_werkstatt():
    willkommens_nachricht()
    
    while True:
        print("\n🔮 Wähle deine magische Aktion:")
        print("1. Magischen Würfel würfeln")
        print("2. Zufallstrank brauen")
        print("3. Abenteuererfolg berechnen")
        print("4. Magische Zahlen generieren")
        print("5. Werkstatt verlassen")
        
        wahl = input("\nGib deine Wahl ein (1-5): ")
        
        if wahl == "1":
            seiten = int(input("Wie viele Seiten soll dein magischer Würfel haben? "))
            wuerfle_magischen_wuerfel(seiten)
            
        elif wahl == "2":
            trank = braue_zufalls_trank()
            
        elif wahl == "3":
            gruppe = int(input("Gruppengröße: "))
            level = int(input("Durchschnittliches Gruppenlevel: "))
            schwierigkeit = int(input("Quest-Schwierigkeit (1-10): "))
            berechne_abenteuer_erfolg(gruppe, level, schwierigkeit)
            
        elif wahl == "4":
            anzahl = int(input("Wie viele Zahlen sollen generiert werden? "))
            magischer_zahlen_generator(anzahl=anzahl)
            
        elif wahl == "5":
            print("✨ Danke für deinen Besuch in der Zauberwerkstatt!")
            print("🧙‍♂️ Mögen deine Funktionen fehlerfrei und deine Magie stark sein!")
            break
            
        else:
            print("⚠️ Ungültige Wahl! Bitte versuche es nochmal.")

# Starte die Werkstatt
if __name__ == "__main__":
    starte_zauber_werkstatt()
```

## Zauber-Dokumentation (Docstrings)

Gute Zauberer dokumentieren ihre Zauber! Verwende Docstrings, um zu erklären, was deine Funktionen tun:

```python
def wirke_blitzschlag(ziel, kraft_level):
    """
    Wirkt einen Blitzschlag auf das angegebene Ziel.
    
    Parameter:
    ziel (str): Der Name des Ziels
    kraft_level (int): Die Kraft des Blitzes (1-10)
    
    Rückgabe:
    int: Der verursachte Schaden
    """
    schaden = kraft_level * 15
    print(f"⚡ Blitz trifft {ziel} und verursacht {schaden} Schaden!")
    return schaden
```

## Quest abgeschlossen! 🎉

Glückwunsch, Zaubererschmied! Du hast gelernt:

- ✅ Eigene Funktionen (Zauber) zu erstellen
- ✅ Parameter zu verwenden, um flexible Zauber zu machen
- ✅ Werte von deinen Funktionen zurückzugeben
- ✅ Eine Bibliothek wiederverwendbarer magischer Komponenten aufzubauen
- ✅ Deine Zauber ordentlich zu dokumentieren

Funktionen sind eines der mächtigsten Werkzeuge in der Programmierung. Sie helfen dir, deinen Code zu organisieren, Wiederholungen zu vermeiden und wiederverwendbare magische Komponenten zu erstellen, die du in all deinen zukünftigen Abenteuern verwenden kannst!

In deiner nächsten Quest lernst du über **Listen und magische Sammlungen** - perfekt, um deine wachsende Sammlung von Zaubern und magischen Gegenständen zu verwalten!

### Übungsherausforderungen

Versuche diese zusätzlichen Herausforderungen, um deine Zaubererschaffungs-Fähigkeiten zu meistern:

1. **Wetterzauber**: Erstelle eine Funktion, die eine Temperatur entgegennimmt und zurückgibt, ob du einen Wärmezauber, Kühlzauber oder gar keinen Zauber brauchst.

2. **Magischer Gegenstandsladen**: Erstelle Funktionen, um Preise zu berechnen, Rabatte anzuwenden und zu bestimmen, ob sich ein Kunde magische Gegenstände leisten kann.

3. **Zauberkombination**: Erstelle eine Funktion, die zwei Zaubernamen entgegennimmt und sie zu einem neuen, mächtigeren Zaubernamen kombiniert.

Übe weiter, und bald wirst du Zauber erschaffen wie ein wahrer Zaubermeister! 🧙‍♂️✨ 