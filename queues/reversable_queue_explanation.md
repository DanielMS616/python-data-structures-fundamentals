# `ReversableQueue.reverse_first_k()` – Die ersten k Elemente einer Queue umkehren

## Ziel der Übung

Die Queue erhält eine Methode

```python
reverse_first_k(k)
```

mit der genau die ersten `k` Elemente umgedreht werden. Alle nachfolgenden Elemente behalten ihre Position relativ zueinander. Ein **Stack** darf als Hilfsstruktur eingesetzt werden.

Zielkomplexitäten:

```text
enqueue()         -> O(1)
dequeue()         -> O(n)
reverse_first_k() -> O(k)
```

Beispiel:

```text
Vorher:
1 -> 2 -> 3

reverse_first_k(2)

Nachher:
2 -> 1 -> 3
```

Ein anschließendes `dequeue()` soll deshalb `2` zurückgeben.

---

## Implementierung

```python
from pythonds3.basic import Stack


class ReversableQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.queue:
            return None

        # Removing index 0 shifts all remaining elements -> O(n).
        return self.queue.pop(0)

    def reverse_first_k(self, k):
        if k < 0 or k > len(self.queue):
            raise ValueError("k must be between 0 and the queue length")

        stack = Stack()

        # Store the first k elements on the stack.
        for index in range(k):
            stack.push(self.queue[index])

        # LIFO writes the elements back in reverse order.
        for index in range(k):
            self.queue[index] = stack.pop()


# Test
rq = ReversableQueue()

rq.enqueue(1)
rq.enqueue(2)
rq.enqueue(3)

rq.reverse_first_k(2)

print(rq.dequeue())  # Expected: 2
```

---

## 1. Wiederholung: Queue und Stack

Diese Aufgabe kombiniert zwei Datenstrukturen.

### Queue

Eine Queue arbeitet nach:

```text
FIFO
First In, First Out
```

Das zuerst eingefügte Element wird zuerst wieder entfernt.

Beispiel:

```text
1 -> 2 -> 3
```

Ein normales `dequeue()` entfernt:

```text
1
```

### Stack

Ein Stack arbeitet nach:

```text
LIFO
Last In, First Out
```

Das zuletzt eingefügte Element wird zuerst wieder entfernt.

Genau diese Eigenschaft eignet sich zum Umkehren einer Reihenfolge.

---

## 2. Was soll `reverse_first_k()` tun?

Angenommen:

```text
queue = [1, 2, 3, 4, 5]
```

und wir rufen auf:

```python
reverse_first_k(3)
```

Dann sollen nur die ersten drei Elemente umgekehrt werden:

```text
[3, 2, 1, 4, 5]
```

Die Elemente:

```text
4, 5
```

dürfen nicht verändert werden.

---

## 3. Warum eignet sich ein Stack zum Umkehren?

Die ersten drei Werte:

```text
1, 2, 3
```

werden in dieser Reihenfolge auf den Stack gelegt:

```python
stack.push(1)
stack.push(2)
stack.push(3)
```

Gedanklich sieht der Stack danach so aus:

```text
oben
 ↓
[3]
[2]
[1]
```

Beim Entfernen mit `pop()` erhalten wir:

```text
3
2
1
```

Der Stack liefert die Elemente also automatisch in umgekehrter Reihenfolge zurück.

---

## 4. Eingabe `k` prüfen

Zuerst wird geprüft:

```python
if k < 0 or k > len(self.queue):
    raise ValueError("k must be between 0 and the queue length")
```

Bei:

```text
queue = [1, 2, 3]
```

sind zum Beispiel diese Werte gültig:

```text
k = 0
k = 1
k = 2
k = 3
```

Ungültig wären:

```text
k = -1
k = 4
```

Eine `ValueError` macht deutlich, dass die Methode zwar korrekt aufgerufen wurde, aber der übergebene Wert nicht zulässig ist.

---

## 5. Die ersten k Elemente auf den Stack legen

Der erste wichtige Abschnitt lautet:

```python
for index in range(k):
    stack.push(self.queue[index])
```

Bei:

```text
queue = [1, 2, 3, 4, 5]
k = 3
```

erzeugt:

```python
range(3)
```

die Indizes:

```text
0, 1, 2
```

Damit werden diese Werte auf den Stack gelegt:

```text
1
2
3
```

Die Queue selbst wird dabei noch nicht verändert.

---

## 6. Die Werte rückwärts zurückschreiben

Danach:

```python
for index in range(k):
    self.queue[index] = stack.pop()
```

Der Stack liefert:

```text
3
2
1
```

Diese Werte werden wieder auf die Positionen:

```text
0
1
2
```

geschrieben.

Aus:

```text
[1, 2, 3, 4, 5]
```

wird:

```text
[3, 2, 1, 4, 5]
```

Der hintere Teil der Queue bleibt unangetastet.

---

## 7. Warum verwenden wir direkten Indexzugriff?

Eine zunächst naheliegende Lösung wäre:

```python
for _ in range(k):
    stack.push(self.queue.pop(0))
```

Das wäre funktional verständlich, hätte aber ein Laufzeitproblem.

Bei einer Python-Liste kostet:

```python
pop(0)
```

```text
O(n)
```

weil alle nachfolgenden Elemente eine Position nach vorne verschoben werden müssen.

Wenn wir das `k`-mal ausführen, würde `reverse_first_k()` nicht mehr die geforderte Laufzeit `O(k)` erreichen.

Deshalb verwenden wir:

```python
self.queue[index]
```

und:

```python
self.queue[index] = ...
```

Der Zugriff auf eine bekannte Listenposition ist:

```text
O(1)
```

---

## 8. Warum sind zwei k-Schleifen trotzdem O(k)?

Wir haben zwei Schleifen:

```python
for index in range(k):
```

Die erste läuft `k`-mal.

Die zweite läuft ebenfalls `k`-mal.

Damit ergibt sich:

```text
k + k = 2k
```

In der Big-O-Notation werden konstante Faktoren ignoriert:

```text
O(2k) = O(k)
```

Deshalb ist die gesamte Methode:

```text
reverse_first_k() -> O(k)
```

---

## 9. Verwendeter Testfall

Der tatsächliche Testcode verwendet:

```python
rq.enqueue(1)
rq.enqueue(2)
rq.enqueue(3)

rq.reverse_first_k(2)
```

Vorher:

```text
[1, 2, 3]
```

Die ersten zwei Elemente:

```text
1, 2
```

werden über den Stack umgedreht.

Danach:

```text
[2, 1, 3]
```

Nun:

```python
rq.dequeue()
```

entfernt das erste Element.

Ausgabe:

```text
2
```

Genau das wird von der Aufgabe erwartet.

---

## 10. Zusätzliches Erklärbeispiel

Das folgende Beispiel gehört **nicht zum Testcode der Aufgabe**. Es dient nur dazu, das Verhalten bei einem größeren `k` zu verdeutlichen.

Ausgangslage:

```text
[10, 20, 30, 40, 50]
```

Aufruf:

```python
reverse_first_k(4)
```

Die ersten vier Werte:

```text
10, 20, 30, 40
```

werden umgekehrt.

Ergebnis:

```text
[40, 30, 20, 10, 50]
```

Das letzte Element:

```text
50
```

bleibt unverändert.

---

## 11. Laufzeit von `dequeue()`

Die Methode verwendet:

```python
self.queue.pop(0)
```

Bei einer Python-Liste liegt das erste Element an Index `0`.

Wird es entfernt, müssen alle verbleibenden Elemente nach vorne verschoben werden.

Deshalb gilt:

```text
dequeue() -> O(n)
```

Das entspricht der Vorgabe der Aufgabe.

---

## 12. Laufzeit von `enqueue()`

Die Methode verwendet:

```python
self.queue.append(item)
```

In typischen Big-O-Übungen wird das Anhängen an eine Python-Liste als:

```text
O(1)
```

behandelt.

Technisch genauer ist `list.append()` allerdings:

```text
amortisiert O(1)
```

Denn gelegentlich muss Python intern mehr Speicher für die Liste reservieren.

Die Aufgabenstellung spricht ausdrücklich von **Worst-Case O(1)**. Streng technisch erfüllt eine normale Python-Liste diese Formulierung nicht garantiert.

Für den hier vorgegebenen Lernkontext ist aber offensichtlich die übliche vereinfachte Betrachtung gemeint:

```text
append() -> O(1)
```

Diese Feinheit ist wichtig zu kennen, muss die Schul-Lösung aber nicht unnötig verkomplizieren.

---

## 13. Gesamte Laufzeiten

Für die in der Aufgabe erwartete Betrachtung:

```text
enqueue()         -> O(1)
dequeue()         -> O(n)
reverse_first_k() -> O(k)
```

Technische Präzisierung:

```text
list.append() -> amortisiert O(1)
```

---

## 14. Speicherkomplexität von `reverse_first_k()`

Der Stack speichert genau die ersten `k` Elemente.

Deshalb benötigt die Methode zusätzlichen Speicher von:

```text
O(k)
```

Es wird keine vollständige Kopie der Queue erstellt.

---

## 15. Sonderfall: k = 0

Bei:

```python
reverse_first_k(0)
```

läuft keine der beiden Schleifen.

Die Queue bleibt unverändert.

Das ist korrekt.

---

## 16. Sonderfall: k = 1

Ein einzelnes Element umzukehren verändert nichts.

Beispiel:

```text
[1, 2, 3]
```

bleibt nach:

```python
reverse_first_k(1)
```

```text
[1, 2, 3]
```

---

## 17. Sonderfall: k entspricht der gesamten Queue-Länge

Bei:

```text
queue = [1, 2, 3]
```

und:

```python
reverse_first_k(3)
```

wird die gesamte Queue umgekehrt:

```text
[3, 2, 1]
```

Auch dieser Fall funktioniert ohne Sonderlogik.

---

## 18. Fehlerfälle

Zwei problematische Werte werden ausdrücklich abgefangen:

```text
k < 0
k > len(queue)
```

Beispiel:

```python
reverse_first_k(10)
```

bei nur drei Elementen ist nicht sinnvoll.

Die Methode löst deshalb eine:

```python
ValueError
```

aus.

Das ist robuster, als einen ungültigen Aufruf stillschweigend zu ignorieren.

---

## 19. Design- und Skalierungsgedanke

Diese Aufgabe zeigt sehr gut, dass eine funktionierende Lösung nicht automatisch auch die geforderte Laufzeit besitzt.

Zum Beispiel wäre:

```python
pop(0)
```

ein naheliegender Weg, Elemente vorne aus der Queue zu nehmen.

Innerhalb von `reverse_first_k()` wäre das jedoch ungünstig, weil jede Entfernung:

```text
O(n)
```

kostet.

Stattdessen nutzen wir direkten Indexzugriff:

```text
O(1)
```

und kombinieren ihn mit einem Stack.

Die entscheidende Frage lautet also:

> Welche Operationen meiner gewählten Datenstruktur sind günstig und welche sind teuer?

Dieses Denken wird später auch bei Datenbanken, Caches und Backend-Systemen wichtig.

---

## 20. Warum die Klasse `ReversableQueue` heißt

Im Startercode lautet der Klassenname:

```python
ReversableQueue
```

Wir behalten diesen Namen bei, damit die Lösung zur Aufgabenstellung passt.

Im Englischen wäre die üblichere Schreibweise allerdings:

```python
ReversibleQueue
```

Für eine eigene Anwendung würde man eher diese Schreibweise wählen.

Für die Schulaufgabe sollte der vorgegebene Name nicht ohne Grund geändert werden.

---

## Zusammenfassung

Die Methode kombiniert eine Queue mit einem Stack.

Die ersten `k` Elemente werden auf den Stack gelegt:

```python
for index in range(k):
    stack.push(self.queue[index])
```

Anschließend werden sie durch LIFO in umgekehrter Reihenfolge zurückgeschrieben:

```python
for index in range(k):
    self.queue[index] = stack.pop()
```

Dadurch bleibt der Rest der Queue unverändert.

Für die erwartete Betrachtung ergeben sich:

```text
enqueue()         -> O(1)
dequeue()         -> O(n)
reverse_first_k() -> O(k)
```

Der zusätzliche Speicher für die Umkehrung beträgt:

```text
O(k)
```

Die zentrale Erkenntnis lautet:

> **Durch die Kombination aus direktem Listenindex und dem LIFO-Prinzip eines Stacks lassen sich genau die ersten k Elemente in O(k) umkehren, ohne den restlichen Teil der Queue zu verändern.**
