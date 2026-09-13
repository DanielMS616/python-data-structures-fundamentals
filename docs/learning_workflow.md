# Lern- und Dokumentationsstandard

Diese Datei beschreibt, wie Übungen in diesem und zukünftigen Lern-Repositories strukturiert, dokumentiert und überprüft werden.

Ziel ist nicht nur, eine Aufgabe einmal korrekt zu lösen. Das Repository soll später nachvollziehbar machen:

- was die konkrete Aufgabe war,
- welche algorithmische Idee dahintersteckt,
- warum die Lösung funktioniert,
- welche Laufzeit- und Speichertrade-offs relevant sind,
- welche Randfälle und Invarianten wichtig sind,
- und wie sich der damalige Lernstand zu einer saubereren Referenzlösung entwickelt hat.

Der Standard soll dabei **gründlich, aber nicht redundant** sein.

---

## 1. Informationsarchitektur

Jede Information soll möglichst genau eine Hauptquelle besitzen.

```text
*.py
    → aktuelle Referenzimplementierung

*_explanation.md
    → übungsspezifische Herleitung und Analyse

Topic README.md
    → gemeinsame Grundlagen eines Themenbereichs

tests/
    → ausführbare Verifikation

docs/
    → übergreifende Konzepte und wiederverwendbare Muster
```

Diese Trennung verhindert, dass dieselben Inhalte an mehreren Stellen vollständig gepflegt werden müssen.

---

## 2. Pro Übung: Implementierung und Erklärung

Der Kern einer Übung besteht aus:

```text
exercise.py
exercise_explanation.md
```

Beispiel:

```text
linked_list_reverse.py
linked_list_reverse_explanation.md
```

Automatisierte Tests können thematisch gebündelt werden, zum Beispiel:

```text
tests/test_linked_lists.py
```

Es ist nicht notwendig, für jede kleine Übung eine eigene Testdatei anzulegen, solange die Zuordnung klar bleibt.

---

## 3. Die `.py`-Datei als Single Source of Truth

Die Python-Datei enthält die **aktuelle Referenzimplementierung**.

Sie ist die maßgebliche Quelle für den vollständigen Code.

Die Erklärung kopiert deshalb nicht automatisch die komplette Datei, sondern nur die Abschnitte, die für das Verständnis der konkreten Aufgabe wichtig sind.

### Codequalität

Der Code soll:

- verständliche englische Bezeichner verwenden,
- unnötige Duplikation innerhalb derselben Implementierung vermeiden,
- Type Hints einsetzen, wenn sie die Schnittstelle oder wichtige Zustände klarer machen,
- relevante Fehler- und Randfälle bewusst behandeln,
- importierbar sein, ohne unbeabsichtigten Demo-Code auszuführen.

Beispielcode für direkte Ausführung gehört deshalb bei Bedarf unter:

```python
if __name__ == "__main__":
    ...
```

### Kommentarstil

Kommentare werden gezielt eingesetzt.

Gute Kommentare erklären:

```text
Warum ist diese Zeile notwendig?
Welche algorithmische Entscheidung steckt dahinter?
Welche Invariante wird geschützt?
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

wenn der Code bereits selbsterklärend ist.

### Sprache

Für:

```text
Code
Bezeichner
kurze Code-Kommentare
```

wird Englisch bevorzugt.

Die ausführliche Lerndokumentation kann auf Deutsch bleiben.

---

## 4. Aufbau einer `_explanation.md`

Die Erklärung konzentriert sich auf das, was an **dieser konkreten Aufgabe** neu oder besonders ist.

Eine sinnvolle Standardstruktur ist:

```text
1. Ziel der Übung
2. Quick Summary
3. Relevante Implementierung
4. Schritt-für-Schritt-Erklärung
5. Warum die Lösung funktioniert / zentrale Invariante
6. Zeit- und Speicherkomplexität
7. Rand- und Fehlerfälle
8. Typvertrag, falls relevant
9. Tests
10. Design- und Skalierungsgedanken
11. Zentrale Lernidee
12. Weiterführende Links
```

Nicht jede kleine Übung benötigt jeden Abschnitt. Die Struktur dient als Leitlinie, nicht als Pflichtformular.

---

## 5. Ziel der Übung

Die ursprüngliche Aufgabe wird **sinngemäß und knapp** festgehalten.

Wichtig sind:

```text
gewünschtes Verhalten
besondere Vorgaben
relevante Zielkomplexitäten
wichtige Randbedingungen
```

Ein vollständiges Wort-für-Wort-Kopieren der Aufgabenstellung ist nicht erforderlich.

---

## 6. Quick Summary

Am Anfang der Erklärung steht möglichst eine kompakte Übersicht.

Beispiel:

```markdown
## Quick Summary

| Aspekt | Ergebnis |
| --- | --- |
| Muster | Slow / Fast Pointer |
| Laufzeit | `O(n)` |
| Zusatzspeicher | `O(1)` |
| Kernidee | Der schnelle Zeiger bewegt sich doppelt so schnell |
```

Dadurch lässt sich eine Übung später schnell wiederholen, ohne sofort die gesamte Herleitung lesen zu müssen.

---

## 7. Relevante Implementierung statt vollständiger Codekopie

Die Erklärung zeigt nur die Codeabschnitte, die für die algorithmische Idee relevant sind.

Beispiel:

```python
while current:
    next_node = current.next
    current.next = previous
    previous = current
    current = next_node
```

Danach wird auf die vollständige Datei verwiesen:

```markdown
Die vollständige und aktuelle Implementierung befindet sich in
[`linked_list_reverse.py`](linked_list_reverse.py).
```

Dadurch gilt:

```text
.py
= Single Source of Truth für Code

.md
= Erklärung des Codes
```

So können Code und Dokumentation nicht unbemerkt als zwei vollständige, voneinander abweichende Implementierungen weiterleben.

---

## 8. Allgemeine Grundlagen nicht unnötig wiederholen

Grundlagen, die für mehrere Übungen desselben Themas gelten, gehören in das Topic-README.

Beispiele:

```text
Was ist ein Stack?
Was bedeutet FIFO?
Wie ist ein Node aufgebaut?
Welche typischen Operationen besitzt eine Queue?
```

Die Exercise-Erklärung verweist stattdessen auf:

```text
stacks/README.md
queues/README.md
linked_lists/README.md
```

In der Exercise-Datei bleibt nur die Theorie, die für die konkrete Lösung wirklich benötigt wird.

---

## 9. Schritt-für-Schritt und Invarianten

Die Erklärung soll nicht nur beschreiben, **was** der Code macht, sondern **warum** er korrekt ist.

Besonders wertvoll sind Invarianten.

Beispiele:

```text
tail zeigt immer auf den letzten Node.

max_queue enthält nur noch mögliche Maximum-Kandidaten.

previous zeigt beim Entfernen von Duplikaten auf den letzten behaltenen Node.

Der Stack enthält genau die noch nicht geschlossenen Symbole.
```

Eine gute Erklärung beantwortet damit:

> Welche Bedingung muss während des Algorithmus immer wahr bleiben?

---

## 10. Komplexität

Zeit- und Speicherkomplexität werden nicht nur genannt, sondern kurz hergeleitet.

Beispiel:

```text
n Nodes werden einmal besucht.
Pro Node erfolgen konstante Operationen.

→ O(n)
```

Bei amortisierter Komplexität wird die technische Präzisierung ausdrücklich genannt.

Beispiel:

```text
Für die Schulaufgabe:
list.append() -> O(1)

Technisch präziser:
list.append() -> amortisiert O(1)
```

So bleibt das Lehrbuchmodell erhalten, ohne technisch ungenau zu werden.

---

## 11. Randfälle, Fehlerfälle und Robustheit

Nicht jede Aufgabe benötigt umfangreiche Fehlerbehandlung.

Relevant sind nur Fälle, die zum aktuellen Lernziel passen.

Typische Fragen:

```text
Was passiert bei einer leeren Struktur?
Was passiert bei genau einem Element?
Sind ungültige Parameter möglich?
Gibt es doppelte Werte?
Kann eine interne Invariante verletzt werden?
Gibt es versteckte Vorbedingungen?
```

Dabei wird unterschieden zwischen:

```text
notwendig für die Aufgabe
professionell sinnvoll
optionale spätere Erweiterung
```

So wird die Lösung nicht unnötig überentwickelt.

---

## 12. Typvertrag

Wenn Type Hints eine relevante Voraussetzung oder Schnittstelle sichtbar machen, wird diese kurz erklärt.

Beispiele:

```python
def find_middle(self) -> object | None:
```

zeigt:

```text
nicht leere Liste -> gespeicherter Wert
leere Liste       -> None
```

Oder:

```python
data: Hashable
```

macht sichtbar, dass eine Set-basierte Lösung nur hashbare Werte unterstützt.

Type Hints werden nicht nur als Syntax dokumentiert, sondern dort erklärt, wo sie fachliche Bedeutung besitzen.

---

## 13. Tests und Erklärbeispiele

Der ursprüngliche Lernfall darf dokumentiert werden, soll aber nicht mit zusätzlichen Beispielen vermischt werden.

Automatisierte Tests sind heute die maßgebliche ausführbare Verifikation.

Eine Explanation kann deshalb kurz festhalten:

```text
ursprünglicher Lernfall
erwartetes Ergebnis
besondere Randfälle
```

und anschließend auf die Testdatei verweisen:

```markdown
[`../tests/test_linked_lists.py`](../tests/test_linked_lists.py)
```

Zusätzliche Beispiele werden nur aufgenommen, wenn sie einen algorithmischen Punkt besser sichtbar machen.

Sie müssen klar als Erklärbeispiel erkennbar sein.

---

## 14. Topic-README

Jeder größere Themenordner erhält eine:

```text
README.md
```

Diese Datei erklärt das Thema **unabhängig von einer einzelnen Übung**.

Typische Inhalte:

```text
Definition
Visualisierung
zentrale Begriffe
Operationen
typische Laufzeiten
kleine Code-Snippets
Einsatzfälle
häufige Fehler
Muster aus den Übungen
Links zu den Exercise-Erklärungen
```

Beispiele:

```text
stacks/README.md
queues/README.md
linked_lists/README.md
```

---

## 15. Übergreifende Dokumentation

Wissen, das mehrere Themen verbindet, gehört in:

```text
docs/
```

Beispiele:

```text
Big O
ADT vs. Implementierung
Python-Collections und ihre Laufzeiten
wiederverwendbare Problemlösungsmuster
Glossar
Lern- und Dokumentationsstandard
```

Damit wird gemeinsames Wissen zentral gepflegt und nicht in mehreren Exercise-Dateien wiederholt.

---

## 16. Qualitätslinse

Bei neuen Lösungen werden – passend zum Lernstand – zusätzlich vier professionelle Qualitätsdimensionen betrachtet.

### 1. Fehlerfälle und robuste Fehlerbehandlung

```text
Welche Eingaben oder Zustände können fehlschlagen?
Wie soll die öffentliche Schnittstelle darauf reagieren?
```

### 2. Datenintegrität und Invarianten

```text
Welche internen Regeln müssen immer gelten?
Bleiben head, tail und next korrekt?
Bleiben Hilfsstrukturen synchron?
```

Bei späteren Datenbankprojekten gehört hier auch dazu:

```text
Constraints
Transaktionen
Eindeutigkeit
Referenzielle Integrität
```

### 3. Skalierung und Performance

```text
Welche Operationen dominieren die Laufzeit?
Was passiert bei deutlich größeren Datenmengen?
Welche Speicher-Laufzeit-Trade-offs existieren?
```

### 4. Betriebsreife / Production Readiness

Bei kleinen Datenstrukturübungen meist nur am Rand relevant.

Bei größeren Anwendungen zusätzlich:

```text
Konfiguration
Secrets
Logging
Monitoring
Persistenz
Fehlerbehandlung
Tests
Deployment
CI/CD
```

Diese Punkte werden **bewusst diskutiert**, aber nicht automatisch in jede kleine Übung eingebaut.

---

## 17. Notwendig vs. Best Practice vs. optional

Bei Erweiterungen soll klar unterschieden werden:

```text
Notwendig für die Aufgabe
→ erfüllt die konkrete Lernanforderung

Professionelle Best Practice
→ verbessert Wartbarkeit, Robustheit oder Nachvollziehbarkeit

Optional / spätere Erweiterung
→ sinnvoll in größeren oder produktiven Systemen
```

Diese Trennung verhindert, dass kleine Lernaufgaben unnötig überkomplex werden.

---

## 18. Automatisierte Qualitätssicherung

Sobald ein Repository über einzelne Experimente hinausgeht, sollte ein kleines reproduzierbares Quality Gate vorhanden sein.

In diesem Repository:

```bash
ruff check .
python -m pytest -q
```

GitHub Actions führt dieselben Checks automatisch bei Pushes und Pull Requests aus.

Das Ziel ist nicht möglichst viel Tooling, sondern:

```text
wiederholbare Verifikation
+
frühes Erkennen von Regressionen
+
klare Qualitätsgrenze
```

---

## 19. Wissensstand und Git-Historie

Git ist Teil des Lernsystems.

Wenn eine frühere Lösung später verbessert wird:

```text
alter Stand
→ Git-Historie

aktueller sauberer Stand
→ aktueller Commit
```

Dadurch muss veralteter Code nicht künstlich erhalten bleiben, nur um den Lernweg nicht zu verlieren.

Wichtig ist aber:

> Spätere Erkenntnisse dürfen das ursprüngliche Lernziel nicht stillschweigend umdeuten.

Historischer Lernstand und aktuelle Referenzlösung dürfen voneinander unterschieden werden.

---

## 20. Eigenständige Übungsdateien und bewusste Wiederholung

In Lern-Repositories kann Wiederholung didaktisch sinnvoll sein.

Beispiel:

```text
mehrere Linked-List-Übungen
→ jeweils eigene Node- und LinkedList-Klasse
```

Das kann akzeptabel sein, wenn jede Übung dadurch unabhängig gelesen und ausgeführt werden kann.

In produktivem Code würde gemeinsame Logik normalerweise stärker extrahiert.

Die Entscheidung soll bewusst getroffen und dokumentiert werden, statt jede Wiederholung automatisch als Fehler zu behandeln.

---

## 21. Zielbild

Ein gutes Lern-Repository beantwortet später mehrere unterschiedliche Fragen:

```text
Was ist das Konzept?
→ Topic README

Wie wurde diese konkrete Aufgabe gelöst?
→ *_explanation.md

Wie sieht die aktuelle Referenzimplementierung aus?
→ *.py

Funktioniert sie noch?
→ tests/

Welche Muster verbinden mehrere Aufgaben?
→ docs/

Welche Qualitätschecks gelten für das Repository?
→ Ruff + pytest + CI
```

Damit wird aus einer Sammlung gelöster Übungen ein:

```text
persönliches technisches Nachschlagewerk
+
reproduzierbares Lernartefakt
+
sauberes öffentliches Portfolio-Beispiel
```
