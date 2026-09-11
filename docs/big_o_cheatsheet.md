# Big-O-Cheatsheet

## 1. Was beschreibt Big O?

Big O beschreibt, wie der Ressourcenbedarf eines Algorithmus wächst, wenn die Eingabegröße `n` größer wird.

Meist betrachten wir:

```text
Zeitkomplexität
Speicherkomplexität
```

Big O beschreibt **keine konkrete Zeit in Sekunden**.

Es geht um die **Wachstumsrate**.

---

## 2. Warum nicht einfach Laufzeit messen?

Messungen hängen unter anderem ab von:

```text
Hardware
Betriebssystem
Python-Version
Hintergrundprozessen
konkreter Implementierung
konkreter Eingabe
```

Benchmarking ist nützlich, wenn konkrete Implementierungen gemessen werden sollen.

Für die algorithmische Analyse abstrahieren wir dagegen von diesen Details.

---

## 3. Grundlegende Operationen

Bei der Analyse werden viele elementare Operationen näherungsweise als konstant behandelt:

```text
Variable zuweisen
Vergleich durchführen
einfache arithmetische Operation
bekannten Listenindex lesen
Referenz setzen
```

Eine Schleife selbst ist dagegen keine konstante Operation, wenn ihre Anzahl an Durchläufen von `n` abhängt.

---

## 4. Typische Komplexitätsklassen

Von günstig nach teuer:

| Big O | Name | Typische Idee |
| --- | --- | --- |
| `O(1)` | konstant | direkter Zugriff |
| `O(log n)` | logarithmisch | Suchraum wird pro Schritt stark verkleinert |
| `O(n)` | linear | jedes Element einmal ansehen |
| `O(n log n)` | log-linear | mehrere lineare Ebenen, z. B. Merge Sort |
| `O(n²)` | quadratisch | alle Paare / zwei verschachtelte Durchläufe |
| `O(2^n)` | exponentiell | Anzahl Möglichkeiten verdoppelt sich pro Schritt |
| `O(n!)` | faktoriell | alle Permutationen betrachten |

Für große Eingaben wächst:

```text
O(1)
<
O(log n)
<
O(n)
<
O(n log n)
<
O(n²)
<
O(2^n)
<
O(n!)
```

---

## 5. O(1) – konstante Zeit

Die Anzahl der notwendigen Schritte hängt nicht von `n` ab.

Beispiele:

```python
value = values[10]
```

oder:

```python
return self.max_queue[0]
```

Bei einer geeigneten Datenstruktur kann auch das Ändern einer Referenz konstant sein:

```python
self.tail.next = new_node
self.tail = new_node
```

Wichtig:

> O(1) bedeutet nicht automatisch „sehr schnell“. Es bedeutet, dass die Arbeit nicht mit `n` wächst.

Auch eine Schleife mit exakt 1000 Iterationen ist bezüglich `n`:

```text
O(1)
```

wenn 1000 nicht von der Eingabegröße abhängt.

---

## 6. O(log n) – logarithmische Zeit

Typisches Erkennungsmerkmal:

> Die verbleibende Eingabe wird bei jedem Schritt um einen konstanten Faktor reduziert.

Beispiel binäre Suche:

```text
n
n / 2
n / 4
n / 8
...
```

Bei Verdopplung der Eingabe ist oft nur ungefähr ein zusätzlicher Schritt nötig.

---

## 7. O(n) – lineare Zeit

Ein vollständiger Durchlauf:

```python
for value in values:
    print(value)
```

Die Schleife läuft `n`-mal:

```text
O(n)
```

Beispiele aus diesem Repository:

```text
Linked List durchsuchen
Linked List umkehren
Mitte mit Slow/Fast Pointer finden
```

Auch eine Schleife mit ungefähr `n / 2` Durchläufen bleibt:

```text
O(n)
```

Konstante Faktoren werden ignoriert.

---

## 8. O(n log n) – log-lineare Zeit

Ein klassisches Beispiel ist Merge Sort.

Gedanke:

```text
log n Teilungsebenen
×
n Arbeit pro Ebene
```

ergibt:

```text
O(n log n)
```

Auch das allgemeine Sortieren einer Python-Liste mit `list.sort()` wird in einer Worst-Case-Betrachtung typischerweise als:

```text
O(n log n)
```

behandelt.

---

## 9. O(n²) – quadratische Zeit

Typisches Muster:

```python
for i in range(n):
    for j in range(n):
        ...
```

Die innere Operation wird ungefähr:

```text
n × n
```

mal ausgeführt.

Also:

```text
O(n²)
```

Selection Sort und Bubble Sort sind klassische Beispiele mit quadratischer Worst-Case-Laufzeit.

---

## 10. Best, Average und Worst Case

Ein Algorithmus kann sich je nach Eingabe unterschiedlich verhalten.

Beispiel lineare Suche:

```text
Best Case:
Ziel steht direkt am Anfang.

Worst Case:
Ziel steht ganz am Ende oder existiert nicht.
```

Für Big-O-Aufgaben wird häufig der **Worst Case** betrachtet, sofern nichts anderes angegeben ist.

Bei Hash-Strukturen wie `dict` oder `set` ist dagegen häufig die **durchschnittliche** Laufzeit relevant.

---

## 11. Konstanten ignorieren

Beispiel:

```python
for value in values:
    print(value)

for value in values:
    print(value * 2)
```

Beide Schleifen laufen `n`-mal:

```text
n + n = 2n
```

Big O:

```text
O(2n)
→ O(n)
```

Der konstante Faktor `2` wird ignoriert.

---

## 12. Dominante Terme

Angenommen:

```text
n² + n + 100
```

Für große `n` dominiert:

```text
n²
```

Deshalb:

```text
O(n² + n + 100)
→ O(n²)
```

---

## 13. Sequentielle vs. verschachtelte Schleifen

### Sequentiell

```python
for i in range(n):
    ...

for j in range(n):
    ...
```

```text
n + n
→ O(n)
```

### Verschachtelt

```python
for i in range(n):
    for j in range(n):
        ...
```

```text
n × n
→ O(n²)
```

Merke:

```text
hintereinander -> addieren
ineinander     -> multiplizieren
```

Danach Konstanten und kleinere Terme vereinfachen.

---

## 14. Unterschiedliche Eingabegrößen

Nicht jede Schleife muss dieselbe Variable besitzen.

Beispiel:

```python
for left in list_a:
    ...

for right in list_b:
    ...
```

Wenn:

```text
len(list_a) = n
len(list_b) = m
```

ist die Laufzeit:

```text
O(n + m)
```

Nicht automatisch:

```text
O(n)
```

---

## 15. Amortisierte Komplexität

Manche Operationen sind nicht bei **jedem einzelnen Aufruf** konstant, aber über viele Aufrufe betrachtet.

Ein wichtiges Python-Beispiel:

```python
my_list.append(value)
```

Eine Liste muss gelegentlich ihren internen Speicher vergrößern.

Ein einzelner solcher Schritt kann mehr Arbeit benötigen.

Über viele `append()`-Operationen verteilt gilt jedoch:

```text
amortisiert O(1)
```

Das ist präziser als einfach nur `O(1)`.

---

## 16. Beispiel: MaxQueue

`enqueue()` enthält:

```python
while self.max_queue and self.max_queue[-1] < item:
    self.max_queue.pop()
```

Ein einzelnes Einfügen kann mehrere Werte entfernen.

Aber jeder Wert kann nur einmal eingefügt und höchstens einmal auf diese Weise entfernt werden.

Deshalb ist `enqueue()` über eine Operationsfolge:

```text
amortisiert O(1)
```

---

## 17. Zeit vs. zusätzlicher Speicher

Eine schnellere Lösung braucht manchmal mehr Speicher.

Beispiel Duplikate in einer Linked List:

```python
seen = set()
```

Das Set benötigt:

```text
O(n)
```

zusätzlichen Speicher.

Dafür wird die Suche nach bereits gesehenen Werten im Durchschnitt:

```text
O(1)
```

und der Gesamtalgorithmus durchschnittlich:

```text
O(n)
```

statt einer möglichen:

```text
O(n²)
```

Lösung ohne Hilfsstruktur.

---

## 18. Beispiele aus diesem Repository

| Operation | Komplexität | Warum? |
| --- | ---: | --- |
| Stack `pop()` am Listenende | `O(1)` | kein Verschieben |
| `list.pop(0)` | `O(n)` | verbleibende Elemente werden verschoben |
| Linked-List-Suche | `O(n)` | Nodes müssen nacheinander besucht werden |
| Linked-List-Append ohne `tail` | `O(n)` | Ende muss gesucht werden |
| Linked-List-Append mit `tail` | `O(1)` | direkter Zugriff auf letztes Element |
| Linked List umkehren | `O(n)` | jeder Node einmal |
| Mitte mit Slow/Fast | `O(n)` | ein Durchlauf |
| Set-Mitgliedschaft | durchschnittlich `O(1)` | Hash-Tabelle |
| PriorityQueue `dequeue()` | `O(1)` | `pop()` am Listenende |
| PriorityQueue `enqueue()` | `O(n log n)` | Liste wird sortiert |
| MaxQueue `get_max()` | `O(1)` | Maximum steht direkt vorne |
| `reverse_first_k(k)` | `O(k)` | nur erste `k` Positionen werden bearbeitet |

---

## 19. Sortieralgorithmen als Orientierung

Aus den Sortiernotizen ergeben sich gute Referenzpunkte:

```text
Selection Sort -> O(n²)
Bubble Sort    -> O(n²)
Merge Sort     -> O(n log n)
```

Bei vergleichsbasierten allgemeinen Sortierverfahren ist `O(n log n)` eine zentrale Grenze für den Worst Case.

Nicht-vergleichsbasierte Verfahren können unter zusätzlichen Annahmen andere Laufzeiten erreichen. Counting Sort ist dafür ein typisches Beispiel.

---

## 20. Big O ist nicht dasselbe wie reale Geschwindigkeit

Ein Algorithmus mit:

```text
O(n)
```

kann für kleine Eingaben real schneller sein als eine bestimmte:

```text
O(1)
```

Operation mit einem großen konstanten Aufwand.

Big O beantwortet vor allem:

> Wie verändert sich das Verhalten, wenn `n` sehr groß wird?

---

## 21. Code analysieren – Checkliste

Bei einer neuen Funktion:

```text
1. Was ist n?
2. Welche Operationen hängen von n ab?
3. Gibt es Schleifen?
4. Sind sie nacheinander oder verschachtelt?
5. Wird die Eingabe bei jedem Schritt geteilt?
6. Welche Datenstruktur-Operationen werden verwendet?
7. Haben diese Operationen selbst O(1), O(n), O(log n) ...?
8. Gibt es zusätzliche Datenstrukturen?
9. Was ist der Worst Case?
10. Welche Terme dominieren für großes n?
```

---

## 22. Wichtige Big-O-Komplexitätsklassen im Überblick

Die wichtigsten Komplexitätsklassen beschreiben, wie stark der Aufwand eines Algorithmus mit wachsender Eingabegröße zunimmt.

```text
Konstante Zeit      -> O(1)
Logarithmische Zeit -> O(log n)
Lineare Zeit        -> O(n)
Log-lineare Zeit    -> O(n log n)
Quadratische Zeit   -> O(n²)
```

---

## Kurzfassung

```text
Direkter Zugriff                    -> oft O(1)
Eingabe halbieren                   -> oft O(log n)
ein vollständiger Durchlauf         -> oft O(n)
Sortierung / Divide and Conquer     -> oft O(n log n)
zwei vollständige verschachtelte
Durchläufe                          -> oft O(n²)
```

Die wichtigste Frage lautet nicht:

> „Welche Big-O-Formel muss ich auswendig lernen?“

sondern:

> **„Welche Arbeit wächst mit meiner Eingabe und warum?“**
