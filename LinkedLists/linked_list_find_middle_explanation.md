# `LinkedList.find_middle()` – Die Mitte einer verketteten Liste finden

## Ziel der Übung

Die Methode

```python
find_middle()
```

soll den Wert des mittleren Nodes bestimmen, **ohne vorher die Listenlänge zu berechnen**. Dafür werden zwei unterschiedlich schnelle Referenzen verwendet. Bei einer geraden Anzahl von Nodes gilt der zweite der beiden mittleren Nodes als Ergebnis.

Beispiele:

```text
5 -> 6 -> 7
     ↑
   Mitte
```

Ergebnis:

```text
6
```

Bei einer geraden Anzahl:

```text
5 -> 6 -> 7 -> 8
          ↑
     zweite Mitte
```

Ergebnis:

```text
7
```

---

## Implementierung

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def find_middle(self):
        slow = self.head
        fast = self.head

        # slow moves one node, fast moves two nodes per iteration.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # When fast reaches the end, slow is at the middle.
        return slow.data if slow else None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        last_node = self.head

        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def __str__(self):
        elements = []
        current = self.head

        while current:
            elements.append(current.data)
            current = current.next

        return "->".join(map(str, elements))


# Test
ll = LinkedList()

ll.append(5)
ll.append(6)

print(ll.find_middle())  # Expected: 6

ll.append(7)

print(ll.find_middle())  # Expected: 6
```

---

# 1. Grundidee: Zwei Zeiger mit unterschiedlicher Geschwindigkeit

Die zentrale Idee dieser Aufgabe ist das sogenannte:

```text
slow-and-fast-pointer principle
```

Wir verwenden zwei Referenzen:

```python
slow = self.head
fast = self.head
```

Beide starten am ersten Knoten.

Aber sie bewegen sich unterschiedlich schnell:

```text
slow -> 1 Knoten pro Schleifenrunde
fast -> 2 Knoten pro Schleifenrunde
```

Wenn `fast` das Ende der Liste erreicht, hat `slow` ungefähr nur die halbe Strecke zurückgelegt.

Damit befindet sich `slow` genau in der Mitte.

---

# 2. Warum funktioniert das mathematisch?

Angenommen, die Liste hat `n` Knoten.

Wenn `fast` pro Schleifenrunde zwei Schritte macht, benötigt es ungefähr:

```text
n / 2
```

Schleifenrunden, um das Ende zu erreichen.

In denselben Schleifenrunden bewegt sich `slow` immer nur einen Schritt.

Also legt `slow` ungefähr:

```text
n / 2
```

Knoten zurück.

Genau dort liegt die Mitte.

---

# 3. Beispiel mit ungerader Anzahl

Nehmen wir:

```text
5 -> 6 -> 7 -> 8 -> 9
```

Start:

```text
slow -> 5
fast -> 5
```

Nach der ersten Schleifenrunde:

```text
slow -> 6
fast -> 7
```

Nach der zweiten:

```text
slow -> 7
fast -> 9
```

Danach kann `fast` nicht mehr zwei Schritte weitergehen.

Die Schleife endet.

`slow` zeigt auf:

```text
7
```

Das ist die Mitte.

---

# 4. Beispiel mit gerader Anzahl

Nehmen wir:

```text
5 -> 6 -> 7 -> 8
```

Start:

```text
slow -> 5
fast -> 5
```

Nach der ersten Runde:

```text
slow -> 6
fast -> 7
```

Nach der zweiten Runde:

```text
slow -> 7
fast -> None
```

Die Schleife endet.

`slow` zeigt auf:

```text
7
```

Bei vier Elementen wären die beiden mittleren Werte:

```text
6 und 7
```

Die Aufgabe verlangt ausdrücklich den **zweiten mittleren Knoten**.

Genau diesen liefert die gewählte Schleifenlogik automatisch.

---

# 5. Warum lautet die Schleifenbedingung so?

```python
while fast and fast.next:
```

Wir prüfen zwei Dinge:

```python
fast
```

und:

```python
fast.next
```

Der Grund ist diese Zeile:

```python
fast = fast.next.next
```

`fast` springt immer zwei Knoten weiter.

Dafür muss sowohl:

- der aktuelle `fast`-Knoten existieren,
- als auch sein nächster Knoten.

existieren.

Wenn einer davon fehlt, können wir nicht sicher zwei Schritte weitergehen.

Die Bedingung schützt uns deshalb vor einem Fehler wie:

```text
AttributeError: 'NoneType' object has no attribute 'next'
```

---

# 6. Was passiert bei zwei Knoten?

Liste:

```text
5 -> 6
```

Start:

```text
slow -> 5
fast -> 5
```

Die Schleifenbedingung ist wahr:

```text
fast exists
fast.next exists
```

Dann:

```python
slow = slow.next
```

macht:

```text
slow -> 6
```

und:

```python
fast = fast.next.next
```

macht:

```text
fast -> None
```

Die Schleife endet.

Ergebnis:

```text
6
```

Das ist genau der **zweite mittlere Knoten**.

---

# 7. Was passiert bei drei Knoten?

Liste:

```text
5 -> 6 -> 7
```

Start:

```text
slow -> 5
fast -> 5
```

Nach einer Runde:

```text
slow -> 6
fast -> 7
```

Jetzt ist:

```text
fast.next = None
```

also endet die Schleife.

Ergebnis:

```text
6
```

Das ist die echte Mitte.

---

# 8. Randfall: Leere Liste

Bei einer leeren Liste:

```python
self.head = None
```

setzen wir:

```python
slow = None
fast = None
```

Die Schleife läuft nicht.

Am Ende:

```python
return slow.data if slow else None
```

Da `slow` `None` ist, wird zurückgegeben:

```text
None
```

Damit ist der leere Fall sauber behandelt.

---

# 9. Randfall: Nur ein Knoten

Liste:

```text
5
```

Dann:

```text
slow -> 5
fast -> 5
```

Aber:

```text
fast.next = None
```

Die Schleife läuft nicht.

`slow` zeigt weiterhin auf `5`.

Ergebnis:

```text
5
```

Auch dafür brauchen wir keine Sonderbehandlung.

---

# 10. Warum bestimmen wir nicht zuerst die Länge?

Eine naheliegende Lösung wäre:

1. durch die gesamte Liste laufen und die Knoten zählen,
2. die Mitte berechnen,
3. nochmals vom Head bis zur Mitte laufen.

Zum Beispiel:

```text
Länge bestimmen -> O(n)
zur Mitte laufen -> O(n)
```

In Big-O wäre das zwar ebenfalls:

```text
O(n)
```

aber wir würden die Liste zweimal durchlaufen.

Die Aufgabe verlangt ausdrücklich eine Lösung ohne vorherige Längenbestimmung.

Der Slow/Fast-Ansatz benötigt nur einen Durchlauf.

---

# 11. Laufzeitkomplexität

Der `fast`-Zeiger bewegt sich doppelt so schnell wie `slow`.

Trotzdem bleibt die Laufzeit:

```text
O(n)
```

Warum?

Weil die Anzahl der Schleifenrunden proportional zur Anzahl der Knoten wächst.

Genauer läuft die Schleife ungefähr:

```text
n / 2
```

Mal.

Bei Big-O werden konstante Faktoren ignoriert:

```text
O(n / 2) -> O(n)
```

---

# 12. Speicherkomplexität

Wir verwenden nur zwei zusätzliche Referenzen:

```python
slow
fast
```

Es wird:

- keine zusätzliche Liste,
- kein Set,
- kein Stack,
- keine Kopie der Linked List

erstellt.

Der zusätzliche Speicherbedarf beträgt deshalb:

```text
O(1)
```

Das ist ein großer Vorteil dieser Lösung.

---

# 13. Warum ist das besser als Werte zu speichern?

Eine andere Möglichkeit wäre, alle Werte zuerst in einer Python-Liste zu speichern:

```python
values = []
```

und danach den mittleren Index zu wählen.

Das würde funktionieren, hätte aber zusätzlichen Speicherbedarf:

```text
O(n)
```

Die Slow/Fast-Lösung braucht dagegen:

```text
O(1)
```

zusätzlichen Speicher.

---

# 14. Wichtiger Designgedanke: Zeiger statt Zusatzdaten

Diese Aufgabe zeigt einen wichtigen allgemeinen Algorithmus-Gedanken:

> Manchmal kann man Informationen über die Position in einer Struktur gewinnen, ohne zusätzliche Daten zu speichern.

Durch zwei unterschiedlich schnelle Zeiger erhalten wir indirekt die Mitte der Liste.

Dieses Muster wird häufig eingesetzt.

---

# 15. Weitere Anwendungen von Slow/Fast Pointers

Das gleiche Prinzip kann unter anderem verwendet werden für:

- Mitte einer Linked List finden,
- Zyklen in Linked Lists erkennen,
- Startpunkt eines Zyklus finden,
- bestimmte Abstände zwischen Knoten untersuchen.

Das Verfahren wird oft auch als:

```text
Tortoise and Hare
```

bezeichnet:

```text
Tortoise = slow
Hare     = fast
```

also Schildkröte und Hase.

---

# 16. Fehlerfälle und Robustheit

Für eine normale, korrekt aufgebaute einfach verkettete Liste funktioniert die Methode sauber.

Ein interessanter Sonderfall wäre jedoch eine **zirkuläre Linked List**.

Zum Beispiel:

```text
5 -> 6 -> 7
     ↑    |
     └────┘
```

Dann gibt es kein echtes Ende mit:

```text
None
```

Die Schleife:

```python
while fast and fast.next:
```

könnte deshalb endlos weiterlaufen.

Für diese Schulaufgabe ist das kein Problem, weil eine normale nicht-zirkuläre Linked List vorausgesetzt wird.

In einer allgemeineren Datenstruktur müsste man jedoch entscheiden, ob Zyklen:

- ausgeschlossen,
- validiert,
- oder bewusst unterstützt

werden sollen.

Das ist ein gutes Beispiel für eine versteckte Annahme einer Funktion.

---

# 17. Zusammenhang mit Datenintegrität

Die Methode verändert die Liste selbst nicht.

Sie liest nur:

```python
next
```

und verschiebt lokale Referenzen.

Das bedeutet:

- keine Knoten werden gelöscht,
- keine `next`-Referenz wird verändert,
- `head` bleibt unverändert.

Das Risiko, die Datenstruktur versehentlich zu beschädigen, ist deshalb deutlich geringer als bei `reverse()` oder `remove_duplicates()`.

---

# 18. Hinweis zu `append()`

Die `append()`-Methode dieser Aufgabe sucht weiterhin jedes Mal das Listenende:

```python
while last_node.next:
    last_node = last_node.next
```

Damit ist:

```text
append() -> O(n)
```

Das gehört nicht zum Lernziel dieser Aufgabe.

Aus einer vorherigen Übung wissen wir bereits, dass ein zusätzlicher:

```python
self.tail
```

das Anhängen auf:

```text
O(1)
```

verbessern kann.

---

# 19. Zentrale Lernidee

Der entscheidende Code lautet:

```python
slow = self.head
fast = self.head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```

Dabei gilt:

```text
slow -> 1 Schritt
fast -> 2 Schritte
```

Wenn `fast` das Ende erreicht, hat `slow` nur ungefähr die halbe Strecke zurückgelegt.

Damit steht `slow` genau in der Mitte.

Bei einer geraden Anzahl von Knoten landet `slow` automatisch auf dem zweiten mittleren Knoten.

---

# Zusammenfassung

Die Methode verwendet zwei unterschiedlich schnelle Referenzen:

```python
slow
fast
```

Beide starten beim `head`.

Pro Schleifenrunde gilt:

```python
slow = slow.next
fast = fast.next.next
```

Dadurch erreicht `fast` das Ende doppelt so schnell.

Wenn das passiert, befindet sich `slow` in der Mitte.

Die Methode hat:

```text
Laufzeit:              O(n)
zusätzlicher Speicher: O(1)
```

und benötigt keine vorherige Berechnung der Listenlänge.

Die zentrale Erkenntnis lautet:

> **Wenn sich ein Zeiger doppelt so schnell durch eine Linked List bewegt wie ein anderer, befindet sich der langsamere Zeiger in der Mitte, sobald der schnelle Zeiger das Ende erreicht.**
