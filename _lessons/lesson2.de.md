---
layout: lesson
title: "Quest 2: Magische Behälter und Essenzen"
lang: de
previous_lesson: lessons/lesson1/
next_lesson: lessons/lesson3/
order: 2
objectives:
  - Verschiedene Arten von magischen Essenzen verstehen (Zahlen, Text, Sammlungen)
  - Magische Behälter zur Aufbewahrung von Essenzen erschaffen und verwenden (Variablen)
  - Grundlegende Arithmantik praktizieren (mathematische Operationen)
  - Lernen, Weisheit von Benutzern durch Eingabezauber zu empfangen
---

# Magische Behälter und Essenzen

<i class="fas fa-flask-potion"></i> Sei gegrüßt, Zauberlehrling! In deiner vorherigen Quest hast du gelernt, deinen ersten Python-Zauber zu wirken. Nun werden wir tiefer in die mystischen Künste eintauchen, indem wir über magische Behälter und die verschiedenen Arten von Essenzen lernen, die sie aufbewahren können. Dieses Wissen wird wesentlich sein, während du auf deiner Reise voranschreitest, um ein Meister-Spielezauberer zu werden!

## Magische Essenzen verstehen (Datentypen)

Im Reich der Python-Zauberei fließen verschiedene Arten von magischen Essenzen durch unsere Zaubersprüche. Genau wie ein Tränkemeister die Eigenschaften verschiedener Zutaten verstehen muss, muss ein Python-Zauberer die verschiedenen Arten von Daten verstehen, mit denen wir arbeiten können.

### Zahlen: Die Essenz der Arithmantik

Zahlen sind das Fundament magischer Berechnungen. In Python arbeiten wir mit verschiedenen Arten numerischer Essenzen:

#### Ganze Zahlen (Integers)
Das sind vollständige, ungebrochene Zahlen - perfekt zum Zählen magischer Gegenstände:

```python
zauberer_level = 5
magie_punkte = 100
drachen_besiegt = 0
```

#### Dezimalzahlen (Floats)
Diese Zahlen können gebrochene magische Energie enthalten:

```python
trank_staerke = 3.5
zauber_genauigkeit = 0.95
mana_regeneration = 2.33
```

Lass uns sie in Aktion sehen:

```python
print("Zauberer Level:", zauberer_level)
print("Magie Punkte:", magie_punkte)
print("Trank Stärke:", trank_staerke, "Einheiten")
```

### Text: Die Essenz der Kommunikation (Strings)

Text-Essenzen, bekannt als Strings, besitzen die Kraft von Worten und Nachrichten:

```python
zauberer_name = "Gandalf der Codierer"
zauber_beschwörung = "print('Abrakadabra!')"
quest_beschreibung = "Hole die Verlorene Schriftrolle von Python"
```

#### String-Magie - Kombinieren von Text-Essenzen

Du kannst mehrere Text-Essenzen mit dem `+`-Operator kombinieren:

```python
begruessung = "Willkommen, " + zauberer_name + "!"
print(begruessung)

# Du kannst auch Strings direkt mit der Print-Beschwörung kombinieren
print("Der große Zauberer", zauberer_name, "beginnt die Quest:", quest_beschreibung)
```

### Boolean: Die Essenz der Wahrheit (True/False)

Boolean-Essenzen besitzen die mystische Kraft von Wahrheit und Falschheit:

```python
ist_zauberer = True
hat_zauberstab = False
quest_abgeschlossen = False
```

Diese werden sehr wichtig, wenn wir über magische Entscheidungsfindung in zukünftigen Quests lernen!

## Magische Behälter (Variablen) - Aufbewahrung deiner Essenzen

Magische Behälter, bekannt als Variablen, sind wie verzauberte Gefäße, die verschiedene Arten von Essenzen aufbewahren können. Stell sie dir vor wie beschriftete Gläser in einem Zauberer-Labor.

### Erschaffen und Benennen deiner Behälter

Wähle bedeutungsvolle Namen für deine magischen Behälter - zukünftige Zauberer (einschließlich dir selbst) werden es dir danken!

```python
# Gute magische Behälternamen
spieler_gesundheit = 100
gegner_staerke = 75
aktuelles_level = "Verzauberter Wald"
hat_heiltrank = True

# Vermeide unklare Namen wie:
# x = 100  # Was repräsentiert x?
# temp = "Wald"  # Temporär was?
```

### Behälter-Benennungsregeln in Python-Magie

Deine magischen Behälter müssen diesen uralten Regeln folgen:
- Beginne mit einem Buchstaben oder Unterstrich
- Kann Buchstaben, Zahlen und Unterstriche enthalten
- Keine Leerzeichen (verwende stattdessen Unterstriche)
- Keine Sonderzeichen wie @, #, $
- Kann keine reservierten magischen Python-Wörter verwenden

```python
# Gültige magische Behälternamen
zauberer_name = "Merlin"
zauber_level_3 = "Feuerball"
_geheimer_zauber = "Unsichtbarkeitsmantel"

# Ungültige Namen (verursachen magische Störungen!)
# 3ter_zauber = "Blitz"      # Kann nicht mit Zahl beginnen
# zauber-name = "Eis"        # Kann keine Bindestriche verwenden
# mein zauber = "Wind"       # Kann keine Leerzeichen haben
```

## Arithmantik: Mathematische Magie

Nun lass uns die Kunst der Arithmantik erkunden - die Verwendung mathematischer Operationen zur Manipulation numerischer Essenzen:

### Grundlegende Arithmantik-Operationen

```python
# Lass uns einige magische Werte einrichten
zauberer_muenzen = 50
trank_kosten = 15
zauber_buecher = 3
magie_kristalle = 7

# Addition - Essenzen kombinieren
gesamt_gold = zauberer_muenzen + 25
print("Gesamt Gold nach Quest-Belohnung:", gesamt_gold)

# Subtraktion - Essenzen ausgeben
verbleibende_muenzen = zauberer_muenzen - trank_kosten
print("Münzen nach Trank-Kauf:", verbleibende_muenzen)

# Multiplikation - Kraft verstärken
doppelte_kristalle = magie_kristalle * 2
print("Kristalle nach Verdopplungszauber:", doppelte_kristalle)

# Division - gleichmäßig teilen
kristalle_pro_gruppenmitglied = magie_kristalle / 2
print("Kristalle pro Gruppenmitglied:", kristalle_pro_gruppenmitglied)
```

### Erweiterte Arithmantik

```python
# Potenzierung - auf eine Potenz erheben (sehr mächtige Magie!)
zauber_kraft = 3 ** 2  # 3 hoch 2
print("Zauber-Kraftlevel:", zauber_kraft)

# Modulus - Rest finden (nützlich für magische Zyklen)
verbleibende_energie = 17 % 5  # 17 geteilt durch 5, Rest ist 2
print("Verbleibende Energie nach 5-Kosten-Zaubern:", verbleibende_energie)

# Ganzzahl-Division - Ganzzahl-Division
komplette_heiltränke = 23 // 4  # Wie viele komplette Tränke aus 23 Zutaten
print("Komplette Tränke, die hergestellt werden können:", komplette_heiltränke)
```

## Weisheit von Benutzern empfangen (Eingabe-Magie)

Ein weiser Zauberer muss mit anderen Wesen kommunizieren können. Der `input()`-Zauber ermöglicht es dir, Nachrichten und Weisheit von Benutzern zu empfangen:

```python
# Grundlegender Eingabezauber
zauberer_name = input("Wie lautet dein Zaubername, Lehrling? ")
print("Willkommen in der Akademie,", zauberer_name, "!")

# Denk daran: input() gibt dir immer Text-Essenz (String)
alter_text = input("Wie viele Jahre hast du Magie studiert? ")
print("Du hast eingegeben:", alter_text, "- aber das ist Text, keine Zahl!")
```

### Text in Zahlen umwandeln

Wenn du Arithmantik mit Benutzereingaben durchführen musst, musst du die Text-Essenz in numerische Essenz verwandeln:

```python
# Text in ganze Zahlen umwandeln
alter_text = input("Gib dein Alter ein: ")
alter_zahl = int(alter_text)
print("In 10 Jahren wirst du", alter_zahl + 10, "Jahre alt sein!")

# Text in Dezimalzahlen umwandeln
trank_staerke = input("Gib Trankstärke ein (Dezimal): ")
staerke_zahl = float(trank_staerke)
print("Doppelte Stärke wäre:", staerke_zahl * 2)
```

### Sichere Umwandlung mit Fehlerbehandlung

```python
try:
    magie_kraft = int(input("Gib dein Magie-Kraftlevel ein: "))
    print("Dein verstärktes Kraftlevel ist:", magie_kraft + 10)
except ValueError:
    print("Das scheint keine gültige Zahl zu sein! Bitte verwende numerische Ziffern.")
```

## Lass uns einen Magischen Charakter-Ersteller erschaffen

Nun lass uns all unser Wissen kombinieren, um einen einfachen Charakter-Erstellungszauber zu erschaffen:

```python
# Magischer Charakter-Ersteller
print("🧙‍♂️ Willkommen zum Magischen Charakter-Ersteller! 🧙‍♀️")
print("=" * 50)

# Charakter-Informationen sammeln
charakter_name = input("Wie heißt dein Charakter? ")
charakter_klasse = input("Was für ein Zauberer bist du? (Feuer/Wasser/Erde/Luft): ")

# Numerische Attribute erhalten
try:
    staerke = int(input("Gib deine Stärke ein (1-20): "))
    magie_kraft = int(input("Gib deine Magie-Kraft ein (1-20): "))
    weisheit = int(input("Gib deine Weisheit ein (1-20): "))
    
    # Abgeleitete Statistiken berechnen
    gesundheits_punkte = staerke * 5
    mana_punkte = magie_kraft * 3
    zauber_genauigkeit = weisheit * 2
    
    # Das magische Charakterblatt anzeigen
    print("\n" + "=" * 50)
    print("🌟 DEIN MAGISCHES CHARAKTERBLATT 🌟")
    print("=" * 50)
    print(f"Name: {charakter_name}")
    print(f"Klasse: {charakter_klasse} Zauberer")
    print(f"Stärke: {staerke}")
    print(f"Magie-Kraft: {magie_kraft}")
    print(f"Weisheit: {weisheit}")
    print("-" * 30)
    print("BERECHNETE STATISTIKEN:")
    print(f"Gesundheitspunkte: {gesundheits_punkte}")
    print(f"Mana-Punkte: {mana_punkte}")
    print(f"Zauber-Genauigkeit: {zauber_genauigkeit}%")
    
    # Bonus-Berechnung
    gesamt_kraft = staerke + magie_kraft + weisheit
    print(f"Gesamt-Kraftlevel: {gesamt_kraft}")
    
    if gesamt_kraft >= 45:
        print("🎉 Gratulation! Du bist ein Meister-Zauberer!")
    elif gesamt_kraft >= 30:
        print("⭐ Gut gemacht! Du bist ein Fortgeschrittener Zauberer!")
    else:
        print("🌱 Du bist ein vielversprechender Zauberlehrling!")
        
except ValueError:
    print("⚠️ Magische Störung erkannt! Bitte verwende nur Zahlen für Attribute.")
```

## Probiere es selbst: Magische Herausforderungen

Bevor wir diese Quest beenden, hier sind einige verzaubernde Herausforderungen, um deine neuen Fähigkeiten zu testen:

### Herausforderung 1: Trank-Shop-Rechner
Erschaffe einen Zauber, der:
1. Nach dem aktuellen Gold des Zauberers fragt
2. Trankpreise zeigt (Heilung: 15 Gold, Mana: 20 Gold, Stärke: 25 Gold)
3. Fragt, welchen Trank sie kaufen möchten
4. Berechnet, ob sie genug Gold haben
5. Zeigt verbleibendes Gold nach dem Kauf

### Herausforderung 2: Magischer Kreis-Rechner
Erschaffe einen Zauber, der:
1. Nach dem Radius eines magischen Kreises fragt
2. Die Fläche mit der Formel berechnet: fläche = 3,14159 * radius * radius
3. Den Umfang berechnet mit: umfang = 2 * 3,14159 * radius
4. Beide Ergebnisse mit entsprechenden magischen Beschreibungen anzeigt

### Herausforderung 3: Erfahrungspunkte-Rechner
Erschaffe einen Zauber, der:
1. Nach aktuellen Erfahrungspunkten fragt
2. Nach aus einer Quest gewonnener Erfahrung fragt
3. Neue Gesamt-Erfahrung berechnet
4. Bestimmt, ob der Zauberer ein Level aufsteigt (alle 100 XP sind ein neues Level)
5. Aktuelles Level und benötigte XP für nächstes Level zeigt

## Was erwartet dich in deiner nächsten Quest?

In Quest 3 werden wir die mystische Kunst des Treffens von Entscheidungen in unseren Zaubern mit magischen Bedingungen (if, else, elif Anweisungen) erkunden. Du wirst lernen, wie man Zauber erschafft, die verschiedene Pfade basierend auf magischen Bedingungen wählen können - wesentliches Wissen für die Erschaffung interaktiver magischer Abenteuer!

Denk daran, die Manipulation magischer Essenzen und Behälter zu meistern ist fundamental für alle fortgeschrittene Zauberei. Übe das Kombinieren verschiedener Arten von Essenzen, experimentiere mit Arithmantik, und hab keine Angst, neue magische Kombinationen auszuprobieren!

**Setze deine magische Reise fort, Zauberlehrling! Deine Kräfte werden stärker mit jedem Zauber, den du meisterst!** 🧙‍♂️✨🎮 