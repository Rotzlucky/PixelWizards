---
layout: lesson
title: "Quest 3: Verzweigte Pfade mit Wenn-Verzauberungen"
lang: de
permalink: /de/lessons/lesson3/
previous_lesson: /de/lessons/lesson2/
next_lesson: /de/lessons/lesson4/
order: 3
objectives:
  - Die mystische Kunst der Wahrheitsmagie beherrschen (Boolesche Werte - Wahr/Falsch)
  - Vergleichsrunen zur Bewertung magischer Bedingungen einsetzen lernen
  - Wenn-, Sonst- und SonstWenn-Verzauberungen wirken, um entscheidungsfreudige Zauber zu erschaffen
  - Ein einfaches textbasiertes magisches Abenteuer mit verzweigten Pfaden erschaffen
---

# Verzweigte Pfade mit Wenn-Verzauberungen

<i class="fas fa-road-fork"></i> Sei gegrüßt, fortschreitender Lehrling! In deinen vorherigen Quests hast du gelernt, magische Essenzen zu speichern und Arithmantie zu praktizieren. Nun werden wir uns in eine der mächtigsten Formen der Zauberei vertiefen: die Kunst, Entscheidungen in deinen Zaubern zu treffen! Mit Wenn-Verzauberungen wird deine Magie verschiedene Pfade basierend auf mystischen Bedingungen wählen können.

## Wahrheitsmagie: Die Essenz der Booleschen Werte

Bevor wir entscheidungsfreudige Zauber erschaffen können, müssen wir die fundamentale Essenz der Wahrheitsmagie verstehen - Boolesche Werte. Im Reich der Python-Zauberei gibt es nur zwei Wahrheitszustände:

```python
magische_wahrheit = True
magische_falschheit = False
```

Diese mystischen Essenzen sind das Fundament aller entscheidungsfreudigen Magie!

### Beispiele der Wahrheitsmagie in Aktion

```python
hat_zauberstab = True
drache_schlaeft = False
quest_abgeschlossen = True
trank_ist_bereit = False

print("Habe ich einen Zauberstab?", hat_zauberstab)
print("Schläft der Drache?", drache_schlaeft)
```

## Vergleichsrunen: Magische Bedingungen bewerten

Vergleichsrunen ermöglichen es uns, magische Essenzen zu vergleichen und Wahrheitswerte zu bestimmen. Diese uralten Symbole besitzen große Macht:

### Die Heiligen Vergleichsrunen

```python
zauberer_level = 15
benoetigtes_level = 10
magie_kraft = 85
feind_staerke = 90

# Gleichheitsrune (==) - Sind zwei Essenzen exakt gleich?
ist_genaues_level = zauberer_level == 15
print("Zauberer ist genau Level 15:", ist_genaues_level)  # True

# Ungleichheitsrune (!=) - Sind zwei Essenzen unterschiedlich?
verschiedene_staerken = magie_kraft != feind_staerke
print("Magiekraft unterscheidet sich von Feindstärke:", verschiedene_staerken)  # True

# Größer-Als-Rune (>) - Ist die erste Essenz größer?
kann_quest_versuchen = zauberer_level > benoetigtes_level
print("Kann diese Quest versuchen:", kann_quest_versuchen)  # True

# Kleiner-Als-Rune (<) - Ist die erste Essenz kleiner?
ist_schwaecher = magie_kraft < feind_staerke
print("Zauberer ist schwächer als Feind:", ist_schwaecher)  # True

# Größer-Gleich-Rune (>=)
erfuellt_anforderung = zauberer_level >= benoetigtes_level
print("Erfüllt Level-Anforderung:", erfuellt_anforderung)  # True

# Kleiner-Gleich-Rune (<=)
innerhalb_sicherer_grenze = magie_kraft <= 100
print("Magiekraft innerhalb sicherer Grenzen:", innerhalb_sicherer_grenze)  # True
```

### Fortgeschrittene Wahrheitsmagie mit Logischen Operatoren

Kombiniere mehrere Wahrheitsbedingungen mit mystischen logischen Operatoren:

```python
zauberer_gesundheit = 80
hat_heiltrank = True
feind_in_naehe = False

# UND-Operator - Beide Bedingungen müssen wahr sein
kann_sicher_erkunden = zauberer_gesundheit > 50 and not feind_in_naehe
print("Kann sicher erkunden:", kann_sicher_erkunden)  # True

# ODER-Operator - Mindestens eine Bedingung muss wahr sein
kann_kampf_ueberleben = zauberer_gesundheit > 75 or hat_heiltrank
print("Kann Kampf überleben:", kann_kampf_ueberleben)  # True

# NICHT-Operator - Kehrt den Wahrheitswert um
sicher_zu_ruhen = not feind_in_naehe
print("Sicher zu ruhen:", sicher_zu_ruhen)  # True
```

## Wenn-Verzauberungen: Deine ersten entscheidungsfreudigen Zauber

Die `if`-Verzauberung ist das Fundament aller entscheidungsfreudigen Magie. Sie erlaubt deinen Zaubern, verschiedenen Code basierend darauf auszuführen, ob eine Bedingung wahr oder falsch ist.

### Grundlegende Wenn-Verzauberungsstruktur

```python
zauberer_mana = 30

if zauberer_mana >= 25:
    print("✨ Du hast genug Mana, um einen mächtigen Zauber zu wirken!")
    print("🔥 Wirke Feuerball!")
```

### Wenn-Sonst-Verzauberungen: Zwei Pfade der Magie

```python
drachen_gesundheit = 20

if drachen_gesundheit <= 0:
    print("🎉 Sieg! Der Drache wurde besiegt!")
    print("💰 Du hast 100 Goldmünzen gefunden!")
else:
    print("⚔️ Der Drache kämpft noch!")
    print(f"🐉 Verbleibende Drachengesundheit: {drachen_gesundheit}")
```

### Wenn-SonstWenn-Sonst-Verzauberungen: Mehrere magische Pfade

```python
zauberer_erfahrung = 750

if zauberer_erfahrung >= 1000:
    zauberer_rang = "Erzmagier"
    spezielle_kraft = "Realitätsmanipulation"
elif zauberer_erfahrung >= 500:
    zauberer_rang = "Meisterzauberer"
    spezielle_kraft = "Elementarkontrolle"
elif zauberer_erfahrung >= 200:
    zauberer_rang = "Geschickter Zauberer"
    spezielle_kraft = "Verbesserte Zauber"
else:
    zauberer_rang = "Lehrling"
    spezielle_kraft = "Grundlegende Magie"

print(f"🧙‍♂️ Rang: {zauberer_rang}")
print(f"✨ Spezielle Kraft: {spezielle_kraft}")
```

## Praktische Zauberbeispiele

Lass uns unser Wissen mit einigen echten magischen Szenarien in die Praxis umsetzen:

### Beispiel 1: Magischer Gegenstandsladen

```python
# Magischer Gegenstandsladen
print("🏪 Willkommen in Merlins Magischem Emporium!")
zauberer_gold = int(input("Wie viel Gold hast du? "))

print("\n📜 Verfügbare Gegenstände:")
print("1. Heiltrank - 25 Gold")
print("2. Magische Schriftrolle - 50 Gold") 
print("3. Verzaubertes Schwert - 100 Gold")

gegenstand_wahl = input("\nWas möchtest du kaufen? (1/2/3): ")

if gegenstand_wahl == "1":
    gegenstand_name = "Heiltrank"
    gegenstand_kosten = 25
elif gegenstand_wahl == "2":
    gegenstand_name = "Magische Schriftrolle"
    gegenstand_kosten = 50
elif gegenstand_wahl == "3":
    gegenstand_name = "Verzaubertes Schwert"
    gegenstand_kosten = 100
else:
    print("❌ Dieser Gegenstand existiert nicht in unserem magischen Inventar!")
    gegenstand_kosten = 0
    gegenstand_name = None

if gegenstand_name and zauberer_gold >= gegenstand_kosten:
    verbleibendes_gold = zauberer_gold - gegenstand_kosten
    print(f"✅ Kauf erfolgreich! Du hast gekauft: {gegenstand_name}")
    print(f"💰 Verbleibendes Gold: {verbleibendes_gold}")
elif gegenstand_name and zauberer_gold < gegenstand_kosten:
    benoetigtes_gold = gegenstand_kosten - zauberer_gold
    print(f"❌ Ungenügend Gold! Du brauchst {benoetigtes_gold} mehr Gold für {gegenstand_name}")
```

### Beispiel 2: Magisches Kampfsystem

```python
# Einfacher magischer Kampf
import random

zauberer_gesundheit = 100
drachen_gesundheit = 80

print("🐉 Ein wilder Drache erscheint!")
print(f"🧙‍♂️ Deine Gesundheit: {zauberer_gesundheit}")
print(f"🐉 Drachengesundheit: {drachen_gesundheit}")

while zauberer_gesundheit > 0 and drachen_gesundheit > 0:
    print("\n⚔️ Wähle deine Aktion:")
    print("1. Feuerball wirken (hoher Schaden, hohe Manakosten)")
    print("2. Eissplitter wirken (mittlerer Schaden, mittlere Manakosten)")  
    print("3. Heiltrank verwenden (Gesundheit wiederherstellen)")
    
    aktion = input("Gib deine Wahl ein (1/2/3): ")
    
    if aktion == "1":
        schaden = random.randint(20, 30)
        drachen_gesundheit -= schaden
        print(f"🔥 Feuerball trifft für {schaden} Schaden!")
    elif aktion == "2":
        schaden = random.randint(15, 25)
        drachen_gesundheit -= schaden
        print(f"❄️ Eissplitter trifft für {schaden} Schaden!")
    elif aktion == "3":
        heilung = random.randint(15, 25)
        zauberer_gesundheit += heilung
        if zauberer_gesundheit > 100:
            zauberer_gesundheit = 100
        print(f"💚 Du heilst um {heilung} Gesundheit!")
    else:
        print("❌ Ungültige Aktion! Du verlierst deinen Zug!")
    
    # Drachenzug
    if drachen_gesundheit > 0:
        drachen_schaden = random.randint(10, 20)
        zauberer_gesundheit -= drachen_schaden
        print(f"🐉 Drache greift für {drachen_schaden} Schaden an!")
    
    print(f"🧙‍♂️ Deine Gesundheit: {zauberer_gesundheit}")
    print(f"🐉 Drachengesundheit: {drachen_gesundheit}")

# Gewinner bestimmen
if zauberer_gesundheit <= 0:
    print("\n💀 Du wurdest besiegt! Der Drache gewinnt!")
    print("🔄 Kehre zur Akademie zurück, um mehr zu trainieren!")
else:
    print("\n🎉 Sieg! Du hast den Drachen besiegt!")
    print("💰 Du hast 150 Gold und 200 Erfahrungspunkte erhalten!")
```

## Lass uns ein magisches Abenteuerspiel erschaffen

Jetzt kombinieren wir all unser Wissen, um ein interaktives textbasiertes Abenteuer zu erschaffen:

```python
# Das Verzauberte Wald-Abenteuer
print("🌲 Willkommen zum Verzauberten Wald-Abenteuer! 🌲")
print("=" * 50)

# Charaktererstellung
zauberer_name = input("Wie lautet der Name deines Zauberers? ")
print(f"\nWillkommen, {zauberer_name}! Deine magische Reise beginnt...")

# Startwerte
gesundheit = 100
mana = 50
gold = 20
hat_schluessel = False

print(f"\n📊 Startwerte:")
print(f"❤️ Gesundheit: {gesundheit}")
print(f"💙 Mana: {mana}")
print(f"💰 Gold: {gold}")

# Das Abenteuer beginnt
print(f"\n🌟 {zauberer_name}, du befindest dich am Rand eines verzauberten Waldes.")
print("Drei mystische Pfade erstrecken sich vor dir, jeder führt zu verschiedenen Abenteuern.")

while True:
    print("\n🛤️ Wähle deinen Pfad:")
    print("1. 🏰 Der Alte Turm (benötigt magischen Schlüssel)")
    print("2. 🕳️ Die Geheimnisvolle Höhle")
    print("3. 🌸 Die Feenlichtung")
    print("4. 🏪 Den Waldhändler besuchen")
    print("5. 🚪 Den Wald verlassen")
    
    wahl = input("\nGib deine Wahl ein (1-5): ")
    
    if wahl == "1":
        if hat_schluessel:
            print("🗝️ Du verwendest deinen magischen Schlüssel, um den Turm zu öffnen!")
            print("✨ Drinnen entdeckst du ein altes Zauberbuch!")
            print("📚 Dein magisches Wissen wächst enorm!")
            mana += 30
            print(f"💙 Mana erhöht auf: {mana}")
            print("🎉 Gratulation! Du hast die größte Herausforderung gemeistert!")
            break
        else:
            print("🔒 Die Turmtür ist mit mächtiger Magie verschlossen.")
            print("🗝️ Du brauchst einen magischen Schlüssel, um einzutreten.")
    
    elif wahl == "2":
        print("🕳️ Du betrittst die dunkle, geheimnisvolle Höhle...")
        print("👹 Ein Kobold springt heraus und fordert dich zum Kampf heraus!")
        
        if mana >= 20:
            print("⚡ Du wirkst Blitzschlag!")
            mana -= 20
            gold += 15
            print("🎉 Sieg! Der Kobold lässt 15 Goldmünzen fallen!")
            print(f"💰 Gold: {gold}, 💙 Mana: {mana}")
        else:
            print("💔 Du hast nicht genug Mana zum Kämpfen!")
            gesundheit -= 15
            print(f"💔 Du verlierst 15 Gesundheit. Gesundheit: {gesundheit}")
            
            if gesundheit <= 0:
                print("💀 Dein Abenteuer endet hier. Trainiere mehr, bevor du zurückkehrst!")
                break
    
    elif wahl == "3":
        print("🌸 Du betrittst eine wunderschöne Lichtung voller freundlicher Feen.")
        print("🧚‍♀️ Die Feen bieten an, dir zu helfen!")
        
        fee_wahl = input("Ihre Hilfe annehmen? (ja/nein): ").lower()
        
        if fee_wahl == "ja":
            print("✨ Die Feen wirken einen Heilzauber auf dich!")
            gesundheit += 25
            if gesundheit > 100:
                gesundheit = 100
            print("🗝️ Sie geben dir auch einen magischen Schlüssel!")
            hat_schluessel = True
            print(f"❤️ Gesundheit wiederhergestellt auf: {gesundheit}")
        else:
            print("🧚‍♀️ Die Feen respektieren deine Wahl und winken zum Abschied.")
    
    elif wahl == "4":
        print("🏪 Du triffst einen freundlichen Waldhändler.")
        print("🧙‍♂️ 'Willkommen, junger Zauberer! Ich habe magische Waren!'")
        print("💊 Heiltrank - 15 Gold (stellt 30 Gesundheit wieder her)")
        print("🔮 Manakristall - 20 Gold (stellt 25 Mana wieder her)")
        
        if gold >= 15:
            kauf_wahl = input("Was möchtest du kaufen? (gesundheit/mana/nichts): ").lower()
            
            if kauf_wahl == "gesundheit" and gold >= 15:
                gold -= 15
                gesundheit += 30
                if gesundheit > 100:
                    gesundheit = 100
                print(f"💊 Heiltrank konsumiert! Gesundheit: {gesundheit}, Gold: {gold}")
            elif kauf_wahl == "mana" and gold >= 20:
                gold -= 20
                mana += 25
                print(f"🔮 Manakristall verwendet! Mana: {mana}, Gold: {gold}")
            elif kauf_wahl == "mana" and gold < 20:
                print("💰 Du hast nicht genug Gold für einen Manakristall!")
            else:
                print("🤝 Danke für deinen Besuch!")
        else:
            print("💰 Du hast nicht genug Gold, um etwas zu kaufen.")
    
    elif wahl == "5":
        print(f"🚪 {zauberer_name} verlässt den verzauberten Wald.")
        print("🌟 Danke fürs Spielen des Verzauberten Wald-Abenteuers!")
        break
    
    else:
        print("❌ Ungültige Wahl! Bitte wähle 1-5.")

print("\n📊 Endwerte:")
print(f"❤️ Gesundheit: {gesundheit}")
print(f"💙 Mana: {mana}")
print(f"💰 Gold: {gold}")
print(f"🗝️ Hat Schlüssel: {hat_schluessel}")
```

## Probiere es selbst: Magische Herausforderungen

Bevor wir diese Quest abschließen, hier sind einige bezaubernde Herausforderungen, um deine neuen Wenn-Verzauberungsfähigkeiten zu meistern:

### Herausforderung 1: Magisches Wettersystem
Erschaffe einen Zauber, der:
1. Nach dem aktuellen Wetter fragt (sonnig/regnerisch/stürmisch)
2. Angemessene magische Ausrüstung basierend auf dem Wetter empfiehlt
3. Zaubereffektivität basierend auf Bedingungen berechnet
4. Verschiedene magische Aktivitäten für jeden Wettertyp vorschlägt

### Herausforderung 2: Zaubererakademie-Notenbuch
Erschaffe einen Zauber, der:
1. Nach drei magischen Fachbereichspunkten fragt (0-100)
2. Die durchschnittliche magische Begabung berechnet
3. Eine magische Note zuweist (A, B, C, D, F)
4. Angemessene Ermutigung oder Verbesserungsvorschläge gibt
5. Bestimmt, ob der Zauberer zum nächsten Level aufsteigt

### Herausforderung 3: Magische Kreaturbegegnung
Erschaffe einen Zauber, der:
1. Zufällig verschiedene magische Kreaturen antrifft
2. Verschiedene Interaktionswahlmöglichkeiten für jede Kreatur anbietet
3. Wenn-Anweisungen verwendet, um Ergebnisse zu bestimmen
4. Den Ruf bei verschiedenen magischen Wesen verfolgt
5. Spezielle Begegnungen basierend auf Rufstufen freischaltet

## Was erwartet dich in deiner nächsten Quest?

In Quest 4 werden wir die mystische Kunst magischer Schleifen und Wiederholungen meistern! Du wirst lernen, wie man zyklische Zauber mit For-Schleifen und While-Schleifen erschafft, die deiner Magie erlauben, Aktionen zu wiederholen und mächtige Muster zu erschaffen. Dieses Wissen wird essentiell für die Erschaffung dynamischer magischer Erfahrungen und automatisierter Zauberwirkung!

Denk daran, die Macht der Entscheidungsfindung durch Wenn-Verzauberungen ist eine der fundamentalsten Fähigkeiten in der gesamten Zauberei. Übe das Erschaffen von Zaubern mit mehreren verzweigten Pfaden, experimentiere mit komplexen logischen Bedingungen, und hab keine Angst davor, Wenn-Anweisungen innerhalb anderer Wenn-Anweisungen zu verschachteln für wahrhaft anspruchsvolle magische Entscheidungsfindung!

**Deine magische Macht wächst mit jeder Verzauberung, die du meisterst, edler Zauberer!** 🧙‍♂️✨🎮 