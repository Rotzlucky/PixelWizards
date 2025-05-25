---
layout: lesson
title: "Quest 1: Wirke deinen ersten Python-Zauber"
lang: de
next_lesson: lessons/lesson2/
order: 1
objectives:
  - Verstehen, was die Python-Sprache ist und warum sie mächtig für die Erschaffung magischer Spiele ist
  - Deinen ersten Zauber wirken: Hallo, Magische Welt!
  - Grundlegende magische Konzepte: Print-Beschwörungen, Schriftrollen (Kommentare) und magische Behälter (Variablen)
  - Ein interaktives Begrüßungsprogramm erstellen
---

# Wirke deinen ersten Python-Zauber

<i class="fas fa-hat-wizard"></i> Sei gegrüßt, zukünftiger Spielezauberer! Bist du bereit, dein magisches Coding-Abenteuer zu beginnen? In dieser ersten Quest werden wir lernen, was die Python-Sprache ist und unseren allerersten Zauber wirken!

*Hinweis: Stelle sicher, dass du die [Vorbereitungslektion]({{ 'lessons/preparation/' | relative_url }}) abgeschlossen hast, bevor du diese Quest beginnst. Du benötigst Python und PyCharm installiert und bereit!*

## Was ist die Python-Sprache?

Python ist eine Programmiersprache - eine uralte magische Sprache, mit der du mit verzauberten Geräten sprechen und ihnen sagen kannst, was sie tun sollen. Sie ist nach der Komikertruppe "Monty Python" benannt, nicht nach der Schlange! 😄

Python ist eine der besten Sprachen für Zauberlehrlinge, weil:
- Sie leicht zu lesen und zu schreiben ist (fast wie eine menschliche Sprache!)
- Sie von Meisterzauberern bei magischen Organisationen wie NASA, Google und YouTube verwendet wird
- Sie perfekt für die Erschaffung von Spielen, Zauberportalen, magischen Helfern und mehr ist!

## Dein erster Python-Zauber: Hallo, Magische Welt!

Jetzt kommt der aufregende Teil - deinen ersten Zauber wirken! Wir beginnen mit dem klassischen "Hallo, Magische Welt!"-Zauber, den Zauberlehrlinge seit Jahrzehnten als ihren ersten Zauber verwenden.

### Schritt 1: PyCharm - Deine mächtige Zauberwerkstatt öffnen

PyCharm ist die mächtige Zauberwerkstatt, die wir in der Vorbereitungslektion eingerichtet haben.

1. Öffne PyCharm aus deinem Programme-Ordner oder Launchpad
2. Falls du noch kein Projekt geöffnet hast, erstelle ein neues Pure Python-Projekt
3. Rechtsklicke im Projekt-Panel und erstelle eine neue Python-Datei namens "hallo_welt"

### Schritt 2: Deine erste Zauberformel schreiben

Im PyCharm-Editor beschwöre folgende Zauberformel genau wie gezeigt:

```python
print("Hallo, Magische Welt!")
```

Jetzt wirke deinen Zauber, indem du rechts im Editor klickst und "hallo_welt ausführen" wählst oder den grünen Ausführen-Knopf drückst.

Du solltest im Ausgabe-Panel unten sehen:

```
Hallo, Magische Welt!
```

**GRATULATION!** Du hast gerade deinen ersten Python-Zauber gewirkt! 🎉✨

## Lass uns verstehen, was geschehen ist

Die `print()`-Beschwörung in Python ist wie ein mächtiger Zauberspruch, der Text in deiner Kristallkugel erscheinen lässt. Was auch immer du zwischen die magischen Klammern und Anführungszeichen setzt, wird manifestiert.

Lass uns noch mehr magische Formeln ausprobieren. Füge diese Zeilen zu deiner Datei hinzu:

```python
print("Hallo, Magische Welt!")
print("Mein Name ist Python-Zauberlehrling!")
print("Ich lerne, fantastische magische Spiele zu erschaffen!")
```

Führe das Programm erneut aus, um alle drei Nachrichten erscheinen zu sehen!

## Magische Schriftrollen zu deinem Zauber hinzufügen

Magische Schriftrollen (Kommentare) sind Notizen, die du zu deinem Zauber hinzufügen kannst. Das verzauberte Gerät ignoriert sie, aber sie helfen anderen Zauberern zu verstehen, was dein Zauber bewirkt.

Um eine magische Schriftrolle in Python zu schreiben, verwende das `#`-Symbol:

```python
# Dies ist eine magische Schriftrolle - das Gerät wird diese Zeile ignorieren
print("Aber diese Zauberformel wird manifestiert!") # Du kannst Schriftrollen auch am Ende einer Zauberformel platzieren
```

## Magische Behälter: Magische Essenzen speichern

Magische Behälter (Variablen) sind wie verzauberte Gefäße, die magische Essenzen für dich aufbewahren können. Du kannst ihnen mystische Namen geben und magische Daten hineinlegen.

```python
zauberer_name = "Alex"
zauberer_alter = 10
print("Sei gegrüßt, mein Name ist", zauberer_name, "und ich bin", zauberer_alter, "Jahre alt!")
```

Versuche, die magischen Werte zu ändern und sieh, was in deiner Kristallkugel geschieht!

## Lass uns einen einfachen Begrüßungszauber erschaffen

Jetzt wollen wir alle magischen Konzepte zusammenfügen, um einen Zauber zu erschaffen, der den Benutzer willkommen heißt:

1. Erstelle in PyCharm eine neue Python-Datei namens "begruessung"
2. Beschwöre den folgenden Zaubercode:

```python
# Mein erster Python-Zauber
print("Willkommen in der Python-Spielezauberei!")

# Nach dem Namen des Zauberlehrlings fragen
zauberer_name = input("Wie lautet dein Zaubername? ")

# Den Zauberlehrling willkommen heißen
print("Sei gegrüßt,", zauberer_name, "! Lass uns gemeinsam magische Spiele erschaffen!")
print("Du wirst ein mächtiger Spielezauberer werden!")
```

3. Bewahre die magische Schriftrolle auf (Cmd+S auf Mac)
4. Wirke den Zauber, indem du rechtsklickst und "begruessung ausführen" wählst oder den grünen Ausführen-Knopf drückst
5. Wenn du im Ausgabe-Panel gefragt wirst, gib deinen Zaubernamen ein und drücke Enter

Fantastisch! Du hast einen Zauber erschaffen, der mit dem Benutzer interagiert!

## Probiere es selbst: Magische Herausforderungen

Bevor wir diese Quest beenden, hier sind einige verzaubernde Herausforderungen zum Ausprobieren:

1. **Personalisiere die Magie**: Ändere den Begrüßungszauber so, dass er auch nach dem magischen Alter und der Lieblingsfarbe des Zauberers fragt.

2. **Mystische Kunst**: Verwende mehrere Print-Beschwörungen, um ein einfaches magisches Symbol zu erschaffen. Zum Beispiel:

```python
print("   /\\")
print("  /  \\")
print(" /    \\")
print("/______\\")
print("  |  |")
print("  |__|")
```

3. **Geschichtenzauber**: Erschaffe einen Zauber, der nach einem Charakternamen, einem magischen Ort und einem Zaubergegenstand fragt und diese dann verwendet, um eine magische Geschichte zu beginnen.

## Was erwartet dich als Nächstes?

In der nächsten Quest werden wir mehr über magische Behälter und verschiedene Arten von magischen Essenzen in Python lernen. Wir werden beginnen, das Fundament für unser magisches Spiel zu legen, indem wir verstehen, wie man mit Zahlen und Textzaubern arbeitet und magische Entscheidungen in unserem Code trifft.

Denk daran, Zauberei zu erlernen ist wie das Erlernen einer neuen magischen Sprache oder eines Instruments - es braucht Übung! Mach dir keine Sorgen, wenn du nicht sofort alle Zaubersprüche verstehst. Je mehr du mit Python-Magie experimentierst, desto mächtiger wirst du!

**Zaubere weiter, zukünftiger Spielemagier!** 🚀✨🧙‍♂️