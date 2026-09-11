# Lern- und Dokumentationsstandard

Diese Datei beschreibt, wie Übungen in diesem und zukünftigen Lern-Repositories dokumentiert werden.

Ziel ist nicht nur, eine Aufgabe einmal zu lösen, sondern den damaligen Wissensstand später wiederherstellen zu können.

---

## 1. Pro Übung zwei Dateien

Jede Übung erhält:

```text
exercise.py
exercise_explanation.md
```

Beispiel:

```text
linked_list_reverse.py
linked_list_reverse_explanation.md
```

---

## 2. Die `.py`-Datei

Die Python-Datei enthält den sauberen Referenzcode.

### Kommentarstil

Kommentare werden gezielt verwendet.

Gute Kommentare erklären:

```text
Warum ist diese Zeile notwendig?
Welche algorithmische Entscheidung steckt dahinter?
Welche Stelle ist leicht falsch zu verstehen?
Welche Laufzeitentscheidung ist wichtig?
```

Beispiel:

```python
# Save the next node before reversing the current link.
next_node = current.next
```

Nicht nötig:

```python
# Return the item.
return item
```

wenn der Code bereits vollständig selbsterklärend ist.

### Sprache

Für Code, Bezeichner und kurze Code-Kommentare wird Englisch bevorzugt.

Die ausführliche Lerndokumentation ist auf Deutsch.

---

## 3. Die `_explanation.md`

Die Erklärung soll eigenständig verständlich sein.

Sie enthält möglichst:

```text
1. sinngemäß zusammengefasstes Übungsziel
2. überarbeitete Lösung
3. Grundkonzept / Wiederholung
4. Schritt-für-Schritt-Erklärung
5. tatsächlichen Testcode
6. zusätzliche Erklärbeispiele – klar als solche markiert
7. Laufzeitkomplexität
8. Speicherkomplexität
9. Rand- und Fehlerfälle
10. Design- und Skalierungsgedanken
11. zentrale Lernidee
```

---

## 4. Testcode und Erklärbeispiele trennen

Ein zusätzlicher Erklärfall darf nicht so aussehen, als gehöre er zum tatsächlichen Test.

Darum ausdrücklich:

```markdown
## Verwendeter Testfall
```

und:

```markdown
## Zusätzliches Erklärbeispiel
```

So bleibt später klar, was wirklich ausgeführt wurde.

---

## 5. Topic-README

Jeder Themenordner erhält eine:

```text
README.md
```

Diese Datei erklärt das Thema **unabhängig von einer konkreten Aufgabenstellung**.

Beispiele:

```text
Stack/README.md
queue/README.md
LinkedLists/README.md
```

Sie enthält:

```text
Definition
Visualisierung
Operationen
Laufzeiten
kleine Code-Snippets
typische Einsatzfälle
Fehlerquellen
Muster aus den Übungen
Links zu den Aufgaben
```

---

## 6. Übergreifende Dokumentation

Wissen, das mehrere Themen verbindet, gehört in:

```text
docs/
```

Beispiele:

```text
Big O
ADT vs. Implementierung
Python-Laufzeiten
Problemlösungsmuster
Glossar
```

Damit wird Wissen nicht in mehreren Exercise-Dateien unnötig dupliziert.

---

## 7. Qualitätslinse

Bei neuen Lösungen werden – passend zum Lernstand – zusätzlich diese Fragen betrachtet:

### Korrektheit

```text
Löst der Code die Aufgabe?
```

### Fehler- und Randfälle

```text
leere Struktur?
ein Element?
ungültige Parameter?
mehrere gleiche Werte?
```

### Datenintegrität / Invarianten

```text
Bleiben head, tail und next korrekt?
Bleiben Hilfsstrukturen synchron?
```

### Skalierung

```text
Was passiert bei 10 Elementen?
Was bei 10.000?
```

### Komplexität

```text
Welche Operation ist O(1), O(n), O(n log n) ...?
```

### Betriebsreife

Bei kleinen Datenstrukturübungen meist nicht relevant.

Bei größeren Backend- oder Webprojekten zusätzlich:

```text
Fehlerbehandlung
Datenbank-Constraints
Persistenz
Konfiguration
Secrets
Logging
Tests
Deployment
```

Diese Themen werden nicht blind eingebaut, sondern als nächste professionelle Ebene bewusst diskutiert.

---

## 8. Lehrbuchmodell vs. technische Präzision

Schulaufgaben vereinfachen manchmal bewusst.

Beispiel:

```text
list.append() -> O(1)
```

Für die Übung ist das häufig die erwartete Aussage.

Technisch präziser:

```text
list.append() -> amortisiert O(1)
```

Beides soll im Repository sauber auseinandergehalten werden:

```text
Für die Aufgabe:
...

Technische Präzisierung:
...
```

So wird der Lernstoff nicht unnötig verkompliziert, aber späteres Wissen überschreibt die ursprüngliche Erklärung nicht.

---

## 9. Wissensstand nicht verlieren

Git selbst ist Teil des Lernsystems.

Wenn eine frühere Erklärung später verbessert wird:

```text
alter Stand -> Git-Historie
neuer Stand -> aktueller Commit
```

Dadurch muss altes Verständnis nicht aus Angst vor Wissensverlust künstlich unverändert bleiben.

Sinnvoll ist aber, Änderungen nachvollziehbar zu machen und nicht stillschweigend das ursprüngliche Lernziel zu verändern.

---


## 10. Zielbild

Ein gutes Lern-Repository beantwortet später drei verschiedene Fragen:

```text
Was ist das Konzept?
→ Topic-README

Wie habe ich diese konkrete Aufgabe gelöst?
→ *_explanation.md

Wie sieht der saubere Code aus?
→ *.py
```

Und übergreifend:

```text
Welche Muster und Regeln verbinden die Aufgaben?
→ docs/
```

So wird aus einer Sammlung von Übungen ein persönliches technisches Nachschlagewerk.
