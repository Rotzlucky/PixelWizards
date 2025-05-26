---
layout: lesson
title: "Quest 4: Magische Schleifen und Wiederholungen"
lang: de
permalink: /de/lessons/lesson4/
previous_lesson: /de/lessons/lesson3/
next_lesson: /de/lessons/lesson5/
order: 4
difficulty: 3
xp: 200
objectives:
  - Die Kunst der for-Schleifen und while-Schleifen meistern
  - Mystische Muster mit Wiederholungen erschaffen
  - Ein magisches Zahlenweissagungsspiel entwickeln
  - Verstehen, wann verschiedene Schleifenarten zu verwenden sind
challenges:
  - title: "Magische Einmaleins-Tabellen"
    description: "Erstelle ein Programm, das die Einmaleins-Tabelle für jede vom Benutzer gewählte Zahl anzeigt."
    hint: "Verwende eine for-Schleife mit range() und multipliziere die Schleifenvariable mit der gewählten Zahl."
  - title: "Passwort-Schutz-Zauber"
    description: "Erstelle ein Programm, das so lange nach einem Passwort fragt, bis das richtige eingegeben wird (verwende 'zauberer123')."
    hint: "Verwende eine while-Schleife, die so lange läuft, bis die Eingabe mit dem richtigen Passwort übereinstimmt."
  - title: "Zahlen-Zauberer-Herausforderung"
    description: "Frage nach einer Zahl, zeige alle geraden Zahlen von 1 bis zu dieser Zahl und berechne ihre Summe."
    hint: "Verwende eine for-Schleife mit range() und prüfe, ob jede Zahl gerade ist, mit dem Modulus-Operator (%)."
---

# Quest 4: Magische Schleifen und Wiederholungen

<i class="fas fa-repeat"></i> Willkommen zurück, junger Zauberer! In dieser Quest lernst du einen der mächtigsten Zauber der Programmierung: **Wiederholungsmagie**. Genau wie ein Zauberer denselben Schutzspruch mehrmals um seinen Turm wirken könnte, verwenden Programmierer Schleifen, um Aktionen effizient zu wiederholen.

## Die Macht der Wiederholung

Stell dir vor, du müsstest diesen Code schreiben, um von 1 bis 10 zu zählen:

```python
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)
```

Das ist eine Menge Tipparbeit! Und was, wenn du bis 100 zählen wolltest? Oder bis 1000? Es muss einen besseren Weg geben... und den gibt es! 🪄

## Der For-Schleifen-Zauber

Die `for`-Schleife ist wie eine magische Beschwörung, die einen Zauber eine bestimmte Anzahl von Malen wiederholt:

```python
# Von 1 bis 10 zählen mit Magie!
for zahl in range(1, 11):
    print(zahl)
```

Lass uns diesen Zauber aufschlüsseln:
- `for` - startet die Wiederholungsmagie
- `zahl` - ein magischer Behälter, der jeden Wert enthält
- `range(1, 11)` - erzeugt Zahlen von 1 bis 10 (11 ist nicht enthalten)
- `:` - beginnt den Zauberblock
- Die eingerückte Zeile ist das, was wiederholt wird

### Probiere es selbst: Magisches Zählen

Erstelle eine neue Datei namens `magisches_zaehlen.py` und probiere diese Zauber:

```python
# Zauber 1: Zählen wie ein Zauberer
print("🧙‍♂️ Zählzauber aktiviert!")
for zaehlung in range(1, 6):
    print(f"Zauber Nummer {zaehlung} gewirkt!")

# Zauber 2: Magische Multiplikationstabelle
print("\n🔢 Die 5er-Einmaleins-Tabelle erscheint:")
for zahl in range(1, 11):
    ergebnis = zahl * 5
    print(f"5 × {zahl} = {ergebnis}")

# Zauber 3: Magisches Sterne-Muster
print("\n⭐ Erschaffe eine Sternenkonstellation:")
for sterne in range(1, 6):
    print("⭐" * sterne)
```

## Der While-Schleifen-Zauber

Die `while`-Schleife ist anders - sie wiederholt sich, solange eine Bedingung wahr ist. Es ist, als würde man sagen "wirf diesen Zauber weiter, solange der Drache noch wach ist":

```python
# Ein magisches Ratespiel
import random

geheime_zahl = random.randint(1, 10)
vermutung = 0

print("🔮 Ich denke an eine Zahl zwischen 1 und 10...")

while vermutung != geheime_zahl:
    vermutung = int(input("Wie lautet deine Vermutung? "))
    
    if vermutung < geheime_zahl:
        print("🔥 Zu niedrig! Die Magie wird stärker...")
    elif vermutung > geheime_zahl:
        print("❄️ Zu hoch! Die Magie wird schwächer...")
    else:
        print("✨ Richtig! Du hast den Wahrsagezauber gemeistert!")
```

## Magische Muster mit Schleifen

Lass uns einige wunderschöne magische Muster erschaffen:

```python
# Muster 1: Magische Pyramide
print("🏛️ Baue eine magische Pyramide:")
for ebene in range(1, 6):
    leerzeichen = " " * (5 - ebene)
    sterne = "⭐" * ebene
    print(leerzeichen + sterne)

# Muster 2: Magischer Diamant
print("\n💎 Beschwöre einen magischen Diamanten:")
# Obere Hälfte
for i in range(1, 5):
    leerzeichen = " " * (4 - i)
    sterne = "✨" * i
    print(leerzeichen + sterne)

# Untere Hälfte
for i in range(3, 0, -1):
    leerzeichen = " " * (4 - i)
    sterne = "✨" * i
    print(leerzeichen + sterne)
```

## Herausforderung: Das Magische Zahlenweissagungsspiel

Jetzt kombinieren wir alles, um ein episches magisches Spiel zu erschaffen! Erstelle eine Datei namens `wahrsagespiel.py`:

```python
import random

print("🔮✨ Willkommen zum Magischen Zahlenweissagungsspiel! ✨🔮")
print("Die Kristallkugel hat eine Zahl zwischen 1 und 20 gewählt...")
print("Du hast 6 Versuche, die richtige Zahl zu erraten!")

# Die magische Zahl
magische_zahl = random.randint(1, 20)
versuche = 0
max_versuche = 6
gewonnen = False

while versuche < max_versuche and not gewonnen:
    versuche += 1
    verbleibend = max_versuche - versuche + 1
    
    print(f"\n🌟 Versuch {versuche} von {max_versuche}")
    
    try:
        vermutung = int(input("Gib deine Weissagung ein: "))
        
        if vermutung == magische_zahl:
            print("🎉 UNGLAUBLICH! Du hast die Kunst der Wahrsagerei gemeistert!")
            print(f"✨ Die Kristallkugel offenbart: {magische_zahl}")
            print(f"🏆 Du hast es in {versuche} Versuchen geschafft!")
            gewonnen = True
        elif vermutung < magische_zahl:
            print("🔥 Die magische Energie wird stärker... ziele höher!")
            if verbleibend > 0:
                print(f"🔮 {verbleibend} Versuche verbleibend")
        else:
            print("❄️ Die magische Energie wird schwächer... ziele niedriger!")
            if verbleibend > 0:
                print(f"🔮 {verbleibend} Versuche verbleibend")
                
    except ValueError:
        print("⚠️ Bitte gib eine gültige Zahl ein, junger Zauberer!")
        versuche -= 1  # Ungültige Eingabe nicht als Versuch zählen

if not gewonnen:
    print(f"\n💀 Die Magie der Kristallkugel war diesmal zu stark...")
    print(f"🔮 Die geheime Zahl war: {magische_zahl}")
    print("🌟 Übe deine Wahrsagefähigkeiten und versuche es erneut!")

print("\n✨ Danke fürs Spielen des Magischen Wahrsagespiels! ✨")
```

## Fortgeschrittene Schleifenmagie

### Verschachtelte Schleifen (Schleifen in Schleifen)
```python
# Erstelle ein magisches Gitter
print("🗺️ Magische Reichskarte:")
for reihe in range(5):
    for spalte in range(5):
        if (reihe + spalte) % 2 == 0:
            print("🌟", end=" ")
        else:
            print("🌙", end=" ")
    print()  # Neue Zeile nach jeder Reihe
```

### Schleifenkontroll-Zauber
```python
# break - verlasse die Schleife sofort
# continue - springe zur nächsten Iteration

print("🔍 Suche nach magischen Artefakten:")
for truhe in range(1, 11):
    if truhe == 7:
        print(f"💎 Legendären Edelstein in Truhe {truhe} gefunden!")
        break  # Stoppe die Suche
    print(f"📦 Truhe {truhe}: Leer")

print("\n🏃‍♂️ Vermeide verfluchte Zahlen:")
for zahl in range(1, 11):
    if zahl == 4 or zahl == 7:
        print(f"⚠️ Überspringe verfluchte Zahl {zahl}")
        continue  # Überspringe diese Iteration
    print(f"✅ Sichere Zahl: {zahl}")
```

## Übungsherausforderungen

Probiere diese magischen Herausforderungen, um deine Schleifenzauber zu stärken:

### Herausforderung 1: Magische Einmaleins-Tabellen
Erstelle ein Programm, das die Einmaleins-Tabelle für jede vom Benutzer gewählte Zahl anzeigt.

### Herausforderung 2: Passwort-Schutz-Zauber
Erstelle ein Programm, das so lange nach einem Passwort fragt, bis das richtige eingegeben wird (verwende "zauberer123").

### Herausforderung 3: Magische ASCII-Kunst
Verwende Schleifen, um ein größeres magisches Muster oder Bild zu erstellen.

### Herausforderung 4: Zahlen-Zauberer
Erstelle ein Programm, das:
1. Den Benutzer nach einer Zahl fragt
2. Alle geraden Zahlen von 1 bis zu dieser Zahl anzeigt
3. Die Summe all dieser geraden Zahlen berechnet

## Was kommt als Nächstes?

In unserer nächsten Quest lernen wir über **Inventar-Schriftrollen und Sammlungen** (Listen) - magische Behälter, die mehrere Gegenstände gleichzeitig aufbewahren können! Das wird entscheidend sein für die Verwaltung von Spielerinventaren, Gegnerlisten und Spielgegenständen in unserem zukünftigen RPG.

**Übe weiter deine Schleifenmagie, junger Zauberer!** 🔄✨ 