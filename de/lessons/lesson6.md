---
layout: lesson
title: "Quest 6: Magische Sammlungen und Listen"
lang: de
permalink: /de/lessons/lesson6/
previous_lesson: /de/lessons/lesson5/
next_lesson: /de/lessons/lesson7/
order: 6
difficulty: 3
xp: 250
objectives:
  - Meistere die Kunst des Erstellens und Verwaltens magischer Listen
  - Lerne, magische Gegenstände hinzuzufügen, zu entfernen und zu organisieren
  - Verstehe Listenmethoden und magische Operationen
  - Baue ein Inventarsystem für deine magischen Abenteuer
challenges:
  - title: "Zauber-Inventar"
    description: "Erstelle eine Liste von Zaubern und füge Funktionen hinzu, um neue Zauber hinzuzufügen, erlernte Zauber zu entfernen und alle Zauber anzuzeigen."
    hint: "Verwende append(), um Zauber hinzuzufügen, remove(), um sie zu löschen, und eine for-Schleife, um alle Zauber anzuzeigen."
  - title: "Magischer Gegenstandssortierer"
    description: "Erstelle eine Liste magischer Gegenstände mit verschiedenen Werten und sortiere sie nach Preis oder alphabetisch."
    hint: "Verwende die sort()-Methode oder die sorted()-Funktion, um deine magischen Gegenstände zu organisieren."
  - title: "Gruppen-Manager"
    description: "Erstelle ein Programm, das eine Abenteuergruppe verwaltet, dir erlaubt, Mitglieder hinzuzufügen, zu entfernen und die Gruppengröße zu überprüfen."
    hint: "Verwende eine Liste, um die Namen der Gruppenmitglieder zu speichern, und len(), um die Gruppengröße zu überprüfen."
---

# Quest 6: Magische Sammlungen und Listen

<i class="fas fa-list"></i> Willkommen zurück, junger Zauberer! Heute lernst du über einen der nützlichsten magischen Behälter in der Programmierung: **Listen**. Stell dir Listen als magische Taschen vor, die mehrere Gegenstände aufbewahren können - Zauber, Tränke, magische Kreaturen oder alles andere, was du für deine Abenteuer brauchst!

## Was sind magische Listen?

Eine Liste ist wie eine magische Schriftrolle, die viele Gegenstände in einer bestimmten Reihenfolge aufbewahren kann. Anders als die einfachen Behälter (Variablen), die du bisher verwendet hast, können Listen mehrere Werte speichern:

```python
# Eine einfache Variable hält einen Gegenstand
lieblings_zauber = "Feuerball"

# Eine Liste hält viele Gegenstände
zauber_sammlung = ["Feuerball", "Heilung", "Blitzschlag", "Schild", "Teleport"]
```

## Erstelle deine erste magische Liste

Beginnen wir mit der Erstellung einiger magischer Sammlungen:

```python
# Verschiedene Wege, Listen zu erstellen
leere_tasche = []  # Eine leere magische Tasche
traenke = ["Heiltrank", "Manatrank", "Stärketrank"]
magische_zahlen = [7, 13, 21, 42, 99]
gemischte_sammlung = ["Drache", 150, "Goldmünzen", True, 3.14]

print("🧪 Tränke:", traenke)
print("🔢 Magische Zahlen:", magische_zahlen)
print("📦 Gemischte Sammlung:", gemischte_sammlung)
```

## Zugriff auf Gegenstände in deiner magischen Sammlung

Jeder Gegenstand in einer Liste hat eine magische Adresse namens **Index**. Python beginnt bei 0 zu zählen (wie ein wahres Zauberer-Nummerierungssystem):

```python
magische_kreaturen = ["Drache", "Einhorn", "Phönix", "Greif", "Basilisk"]

# Zugriff auf Gegenstände über ihren magischen Index
print("🐉 Erste Kreatur:", magische_kreaturen[0])    # Drache
print("🦄 Zweite Kreatur:", magische_kreaturen[1])   # Einhorn
print("🔥 Dritte Kreatur:", magische_kreaturen[2])    # Phönix

# Negative Indizes zählen vom Ende (sehr magisch!)
print("🐍 Letzte Kreatur:", magische_kreaturen[-1])   # Basilisk
print("🦅 Vorletzte:", magische_kreaturen[-2])  # Greif
```

### Magisches Listen-Aufteilen

Du kannst Teile deiner Liste mit magischem Aufteilen extrahieren:

```python
zauberbuch = ["Feuerball", "Heilung", "Blitz", "Schild", "Teleport", "Frost", "Fliegen"]

# Hole einen Teil der Zauber
basis_zauber = zauberbuch[0:3]      # Erste 3 Zauber
fortgeschrittene_zauber = zauberbuch[4:]    # Von Index 4 bis Ende
mittlere_zauber = zauberbuch[2:5]     # Von Index 2 bis 4

print("📚 Basiszauber:", basis_zauber)
print("🔮 Fortgeschrittene Zauber:", fortgeschrittene_zauber)
print("⚡ Mittlere Zauber:", mittlere_zauber)
```

## Gegenstände zu deiner Sammlung hinzufügen

### Der Anhängen-Zauber (Am Ende hinzufügen)

```python
inventar = ["Schwert", "Schild"]
print("🎒 Start-Inventar:", inventar)

# Neue Gegenstände am Ende hinzufügen
inventar.append("Heiltrank")
inventar.append("Magischer Ring")
print("🎒 Nach dem Einkaufen:", inventar)
```

### Der Einfügen-Zauber (An bestimmter Position hinzufügen)

```python
gruppen_mitglieder = ["Zauberer", "Krieger", "Bogenschütze"]
print("👥 Ursprüngliche Gruppe:", gruppen_mitglieder)

# Einen Heiler an Position 1 einfügen
gruppen_mitglieder.insert(1, "Heiler")
print("👥 Gruppe mit Heiler:", gruppen_mitglieder)
```

### Der Erweitern-Zauber (Mehrere Gegenstände hinzufügen)

```python
basis_zauber = ["Feuerball", "Heilung"]
neue_zauber = ["Blitz", "Schild", "Teleport"]

basis_zauber.extend(neue_zauber)
print("📖 Vollständiges Zauberbuch:", basis_zauber)
```

## Gegenstände aus deiner Sammlung entfernen

### Der Entfernen-Zauber (Nach Wert entfernen)

```python
monster_liste = ["Goblin", "Ork", "Drache", "Troll", "Goblin"]
print("👹 Monster vor dem Kampf:", monster_liste)

# Das erste Vorkommen von "Goblin" entfernen
monster_liste.remove("Goblin")
print("👹 Nach dem Besiegen eines Goblins:", monster_liste)
```

### Der Pop-Zauber (Nach Position entfernen)

```python
schatztruhe = ["Gold", "Silber", "Rubin", "Diamant", "Smaragd"]
print("💎 Schatztruhe:", schatztruhe)

# Den letzten Gegenstand entfernen und erhalten
letzter_schatz = schatztruhe.pop()
print("💎 Genommen:", letzter_schatz)
print("💎 Verbleibender Schatz:", schatztruhe)

# Gegenstand an bestimmter Position entfernen und erhalten
zweiter_schatz = schatztruhe.pop(1)
print("💎 Auch genommen:", zweiter_schatz)
print("💎 Endgültiger Schatz:", schatztruhe)
```

## Magische Listen-Operationen

### Prüfen, ob Gegenstände existieren

```python
magische_bibliothek = ["Zauberbuch", "Trankrezept", "Alte Karte", "Kristallkugel"]

# Prüfen, ob ein Gegenstand existiert
if "Kristallkugel" in magische_bibliothek:
    print("🔮 Du hast eine Kristallkugel! Du kannst die Zukunft sehen!")

if "Drachenei" not in magische_bibliothek:
    print("🥚 Du musst ein Drachenei für deine Sammlung finden!")
```

### Zählen und Messen

```python
zauber_komponenten = ["Molchauge", "Fledermausflügel", "Molchauge", "Drachenschuppe"]

# Zähle, wie viele Gegenstände
gesamt_komponenten = len(zauber_komponenten)
print(f"🧪 Gesamte Komponenten: {gesamt_komponenten}")

# Zähle bestimmte Gegenstände
molchaugen = zauber_komponenten.count("Molchauge")
print(f"👁️ Molchaugen: {molchaugen}")
```

## Organisiere deine magischen Sammlungen

### Zauber sortieren

```python
unordentliche_zauber = ["Teleport", "Feuerball", "Heilung", "Blitz", "Schild"]
print("📚 Unordentliches Zauberbuch:", unordentliche_zauber)

# Alphabetisch sortieren (verändert die ursprüngliche Liste)
unordentliche_zauber.sort()
print("📚 Organisiertes Zauberbuch:", unordentliche_zauber)

# In umgekehrter Reihenfolge sortieren
unordentliche_zauber.sort(reverse=True)
print("📚 Umgekehrt alphabetisch:", unordentliche_zauber)
```

### Zahlen sortieren

```python
magische_level = [15, 3, 42, 7, 23, 1, 99]
print("📊 Zufällige Level:", magische_level)

# Zahlen sortieren
magische_level.sort()
print("📊 Sortierte Level:", magische_level)

# Eine sortierte Kopie erstellen (lässt das Original unverändert)
level_kopie = sorted(magische_level, reverse=True)
print("📊 Höchste zu niedrigste:", level_kopie)
print("📊 Original noch sortiert:", magische_level)
```

## Durch magische Sammlungen schleifen

### Die For-Schleife mit Listen

```python
magische_artefakte = ["Excalibur", "Heiliger Gral", "Elderstab", "Der Eine Ring"]

print("🏛️ Untersuche magische Artefakte:")
for artefakt in magische_artefakte:
    print(f"✨ Gefunden: {artefakt}")

# Mit Indexnummern
print("\n📋 Katalog der Artefakte:")
for index, artefakt in enumerate(magische_artefakte):
    print(f"{index + 1}. {artefakt}")
```

### Jeden Gegenstand verarbeiten

```python
trank_preise = [25, 50, 75, 100, 150]
print("💰 Ursprüngliche Preise:", trank_preise)

# Rabatt auf alle Tränke anwenden
rabattierte_preise = []
for preis in trank_preise:
    neuer_preis = preis * 0.8  # 20% Rabatt
    rabattierte_preise.append(neuer_preis)

print("💰 Rabattierte Preise:", rabattierte_preise)
```

## Fortgeschrittene Listen-Magie

### Listen-Verständnis (Fortgeschrittene Zaubererschaffung)

```python
# Erstelle eine Liste quadrierter magischer Zahlen
magische_zahlen = [1, 2, 3, 4, 5]
quadrierte_zahlen = [zahl ** 2 for zahl in magische_zahlen]
print("🔢 Quadrierte Zahlen:", quadrierte_zahlen)

# Filtere Zauber nach Länge
alle_zauber = ["Feuer", "Heilung", "Blitzschlag", "Schild", "Teleportation"]
kurze_zauber = [zauber for zauber in alle_zauber if len(zauber) <= 5]
print("⚡ Kurze Zauber:", kurze_zauber)
```

### Verschachtelte Listen (Listen in Listen)

```python
# Ein magisches Gitter/Karte
magische_karte = [
    ["🌲", "🌲", "🏰", "🌲"],
    ["🌲", "🗡️", "🌲", "🐉"],
    ["🌊", "🌊", "🌲", "🌲"],
    ["🏔️", "🏔️", "🏔️", "💎"]
]

print("🗺️ Magische Reichskarte:")
for reihe in magische_karte:
    print(" ".join(reihe))

# Zugriff auf bestimmte Orte
burg_ort = magische_karte[0][2]
drachen_ort = magische_karte[1][3]
print(f"\n🏰 Burg gefunden: {burg_ort}")
print(f"🐉 Drache gefunden: {drachen_ort}")
```

## Herausforderung: Das ultimative magische Inventarsystem

Erstelle eine Datei namens `magisches_inventar.py` und baue ein vollständiges Inventarverwaltungssystem:

```python
class MagischesInventar:
    def __init__(self):
        self.gegenstaende = []
        self.gold = 100
        
    def inventar_anzeigen(self):
        """Zeigt alle Gegenstände im Inventar an."""
        print("\n🎒 === MAGISCHES INVENTAR ===")
        if not self.gegenstaende:
            print("📦 Dein Inventar ist leer!")
        else:
            for i, gegenstand in enumerate(self.gegenstaende, 1):
                print(f"{i}. {gegenstand}")
        print(f"💰 Gold: {self.gold}")
        print("=" * 30)
    
    def gegenstand_hinzufuegen(self, gegenstand):
        """Fügt einen Gegenstand zum Inventar hinzu."""
        self.gegenstaende.append(gegenstand)
        print(f"✅ {gegenstand} zu deinem Inventar hinzugefügt!")
    
    def gegenstand_entfernen(self, gegenstand_name):
        """Entfernt einen Gegenstand aus dem Inventar."""
        if gegenstand_name in self.gegenstaende:
            self.gegenstaende.remove(gegenstand_name)
            print(f"❌ {gegenstand_name} aus deinem Inventar entfernt!")
        else:
            print(f"⚠️ {gegenstand_name} nicht in deinem Inventar gefunden!")
    
    def gegenstand_verwenden(self, gegenstand_name):
        """Verwendet einen Gegenstand (entfernt ihn aus dem Inventar)."""
        if gegenstand_name in self.gegenstaende:
            self.gegenstaende.remove(gegenstand_name)
            print(f"✨ Du hast {gegenstand_name} verwendet!")
            
            # Spezielle Effekte für verschiedene Gegenstände
            if "Heiltrank" in gegenstand_name:
                print("💚 Du fühlst dich erfrischt und geheilt!")
            elif "Manatrank" in gegenstand_name:
                print("💙 Deine magische Energie ist wiederhergestellt!")
            elif "Stärketrank" in gegenstand_name:
                print("💪 Du fühlst dich unglaublich stark!")
        else:
            print(f"⚠️ Du hast keinen {gegenstand_name}!")
    
    def inventar_sortieren(self):
        """Sortiert das Inventar alphabetisch."""
        self.gegenstaende.sort()
        print("📚 Inventar alphabetisch sortiert!")
    
    def gegenstand_typ_zaehlen(self, gegenstand_typ):
        """Zählt, wie viele Gegenstände ein bestimmtes Wort enthalten."""
        anzahl = sum(1 for gegenstand in self.gegenstaende if gegenstand_typ.lower() in gegenstand.lower())
        return anzahl
    
    def gegenstaende_finden(self, suchbegriff):
        """Findet alle Gegenstände, die einen Suchbegriff enthalten."""
        gefundene_gegenstaende = [gegenstand for gegenstand in self.gegenstaende if suchbegriff.lower() in gegenstand.lower()]
        return gefundene_gegenstaende

def magischer_laden(inventar):
    """Ein magischer Laden, wo du Gegenstände kaufen kannst."""
    laden_gegenstaende = {
        "Heiltrank": 25,
        "Manatrank": 30,
        "Stärketrank": 50,
        "Magisches Schwert": 200,
        "Schutzschild": 150,
        "Feuerball-Schriftrolle": 75,
        "Heilkraut": 10,
        "Drachenschuppe": 300
    }
    
    print("\n🏪 === MAGISCHER LADEN ===")
    print("Willkommen in Merlins Magischem Emporium!")
    print("Verfügbare Gegenstände:")
    
    for gegenstand, preis in laden_gegenstaende.items():
        print(f"💰 {gegenstand}: {preis} Gold")
    
    while True:
        wahl = input("\nWas möchtest du kaufen? (oder 'exit' zum Verlassen): ")
        
        if wahl.lower() == 'exit':
            break
        
        if wahl in laden_gegenstaende:
            preis = laden_gegenstaende[wahl]
            if inventar.gold >= preis:
                inventar.gold -= preis
                inventar.gegenstand_hinzufuegen(wahl)
                print(f"💰 {preis} Gold ausgegeben. Verbleibt: {inventar.gold}")
            else:
                print(f"💸 Nicht genug Gold! Du brauchst {preis}, hast aber nur {inventar.gold}")
        else:
            print("❓ Gegenstand nicht im Laden verfügbar!")

def main():
    """Hauptspielschleife für das magische Inventarsystem."""
    inventar = MagischesInventar()
    
    # Starte mit einigen Grundgegenständen
    inventar.gegenstand_hinzufuegen("Holzstab")
    inventar.gegenstand_hinzufuegen("Heiltrank")
    inventar.gegenstand_hinzufuegen("Zauberbuch")
    
    print("🧙‍♂️ Willkommen zu deinem magischen Abenteuer!")
    print("Du beginnst deine Reise mit einer Grundausstattung.")
    
    while True:
        print("\n🔮 Was möchtest du tun?")
        print("1. Inventar anzeigen")
        print("2. Gegenstand hinzufügen")
        print("3. Gegenstand entfernen")
        print("4. Gegenstand verwenden")
        print("5. Inventar sortieren")
        print("6. Gegenstände suchen")
        print("7. Laden besuchen")
        print("8. Gegenstandsstatistiken")
        print("9. Abenteuer beenden")
        
        wahl = input("\nGib deine Wahl ein (1-9): ")
        
        if wahl == "1":
            inventar.inventar_anzeigen()
            
        elif wahl == "2":
            gegenstand = input("Gegenstandsname zum Hinzufügen eingeben: ")
            inventar.gegenstand_hinzufuegen(gegenstand)
            
        elif wahl == "3":
            gegenstand = input("Gegenstandsname zum Entfernen eingeben: ")
            inventar.gegenstand_entfernen(gegenstand)
            
        elif wahl == "4":
            gegenstand = input("Gegenstandsname zum Verwenden eingeben: ")
            inventar.gegenstand_verwenden(gegenstand)
            
        elif wahl == "5":
            inventar.inventar_sortieren()
            
        elif wahl == "6":
            suche = input("Suche nach Gegenständen mit: ")
            gefunden = inventar.gegenstaende_finden(suche)
            if gefunden:
                print(f"🔍 Gefundene Gegenstände: {gefunden}")
            else:
                print("🔍 Keine Gegenstände gefunden!")
                
        elif wahl == "7":
            magischer_laden(inventar)
            
        elif wahl == "8":
            traenke = inventar.gegenstand_typ_zaehlen("Trank")
            waffen = inventar.gegenstand_typ_zaehlen("Schwert")
            gesamt_gegenstaende = len(inventar.gegenstaende)
            
            print(f"\n📊 Inventarstatistiken:")
            print(f"🧪 Tränke: {traenke}")
            print(f"⚔️ Waffen: {waffen}")
            print(f"📦 Gesamte Gegenstände: {gesamt_gegenstaende}")
            
        elif wahl == "9":
            print("✨ Danke fürs Spielen!")
            print("🧙‍♂️ Mögen deine Abenteuer legendär sein!")
            break
            
        else:
            print("❓ Ungültige Wahl! Bitte versuche es nochmal.")

if __name__ == "__main__":
    main()
```

## Arbeiten mit mehreren Listen

Manchmal musst du mit mehreren verwandten Listen arbeiten:

```python
# Parallele Listen (verwandte Daten in separaten Listen)
helden_namen = ["Aragorn", "Legolas", "Gimli", "Gandalf"]
helden_level = [25, 22, 24, 50]
helden_klassen = ["Waldläufer", "Bogenschütze", "Krieger", "Zauberer"]

print("🏆 Helden-Gruppenstatus:")
for i in range(len(helden_namen)):
    name = helden_namen[i]
    level = helden_level[i]
    helden_klasse = helden_klassen[i]
    print(f"⚔️ {name} - Level {level} {helden_klasse}")

# Zip verwenden, um Listen zu kombinieren
print("\n🏆 Mit Zip-Magie:")
for name, level, helden_klasse in zip(helden_namen, helden_level, helden_klassen):
    print(f"⚔️ {name} - Level {level} {helden_klasse}")
```

## Quest abgeschlossen! 🎉

Glückwunsch, Meister der magischen Sammlungen! Du hast gelernt:

- ✅ Magische Listen zu erstellen und zu verwalten
- ✅ Gegenstände zu deinen Sammlungen hinzuzufügen und zu entfernen
- ✅ Auf Gegenstände über ihre magischen Indizes zuzugreifen
- ✅ Dein magisches Inventar zu sortieren und zu organisieren
- ✅ Effizient durch Sammlungen zu schleifen
- ✅ Komplexe Inventarverwaltungssysteme zu bauen

Listen sind unglaublich mächtige Werkzeuge, die du in fast jedem magischen Programm verwenden wirst, das du erstellst. Sie sind perfekt zum Speichern von Zaubersammlungen, Verwalten von Gruppenmitgliedern, Verfolgen von Inventar und Organisieren jeder Art von Daten in deinen Abenteuern!

In deiner nächsten Quest lernst du über **Wörterbücher** - noch mächtigere magische Behälter, die Schlüssel-Wert-Paare speichern können, wie ein magisches Adressbuch für deine Zauber und Gegenstände!

### Übungsherausforderungen

Versuche diese zusätzlichen Herausforderungen, um deine Listen-Magie zu meistern:

1. **Magisches Rezeptbuch**: Erstelle ein Programm, das Rezepte als Listen von Zutaten speichert und dir erlaubt, nach Rezepten anhand von Zutaten zu suchen.

2. **Abenteuergruppen-Optimierer**: Erstelle ein System, das verschiedene Heldentypen verwaltet und die beste Gruppenzusammensetzung für verschiedene Quest-Typen vorschlägt.

3. **Zauber-Combo-Ersteller**: Baue ein Programm, das eine Liste von Basiszaubern nimmt und alle möglichen Kombinationen für mächtige Combo-Zauber erstellt.

Übe weiter mit Listen, und bald wirst du magische Sammlungen verwalten wie ein wahrer Zaubermeister! 🧙‍♂️📚✨ 