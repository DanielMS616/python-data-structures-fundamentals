# `LinkedList.remove_duplicates()` – Duplikate aus einer verketteten Liste entfernen

## Ziel der Übung

Die Methode

```python
remove_duplicates()
```

soll eine verkettete Liste einmal durchlaufen und spätere Wiederholungen bereits gesehener Werte entfernen. **Das erste Vorkommen bleibt jeweils erhalten.**

Beispiel:

```text
Vorher:
5 -> 5 -> 6 -> 5 -> 7 -> 6

Nachher:
5 -> 6 -> 7
```

Ein `set` dient dabei als Hilfsstruktur für die bereits beobachteten Werte.

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

    def remove_duplicates(self):
        seen = set()
        current = self.head
        previous = None

        while current:
            # Skip nodes whose value has already appeared.
            if current.data in seen:
                previous.next = current.next

            else:
                seen.add(current.data)
                previous = current

            current = current.next

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
ll.append(5)
ll.append(6)
ll.append(5)
ll.append(7)
ll.append(6)

print(f"Before: {ll}")

ll.remove_duplicates()

print(f"After:  {ll}")
```

Erwartete Ausgabe:

```text
Before: 5->5->6->5->7->6
After:  5->6->7
```

---

# 1. Grundidee

Wir durchlaufen die Linked List genau einmal.

Währenddessen merken wir uns in einem `set`, welche Werte bereits vorgekommen sind:

```python
seen = set()
```

Wenn ein Wert zum ersten Mal erscheint, wird er in `seen` gespeichert.

Wenn derselbe Wert später erneut auftaucht, entfernen wir diesen Knoten aus der Liste.

---

# 2. Warum eignet sich ein `set`?

Ein Python-`set` speichert eindeutige Werte.

Zum Beispiel:

```python
seen = set()

seen.add(5)
seen.add(6)
```

Danach enthält es sinngemäß:

```text
{5, 6}
```

Wir können sehr schnell prüfen:

```python
5 in seen
```

Das liefert:

```python
True
```

und:

```python
7 in seen
```

liefert:

```python
False
```

Mit einem Set sind solche Mitgliedschaftsprüfungen im Durchschnitt:

```text
O(1)
```

Das ist der entscheidende Vorteil gegenüber einer Liste als Hilfsstruktur.

---

# 3. Die drei wichtigen Variablen

Wir verwenden:

```python
seen
current
previous
```

## `seen`

```python
seen = set()
```

Speichert alle Werte, die bereits mindestens einmal aufgetreten sind.

---

## `current`

```python
current = self.head
```

Zeigt auf den Knoten, den wir gerade untersuchen.

---

## `previous`

```python
previous = None
```

Zeigt auf den letzten Knoten, den wir **behalten** haben.

Diese Referenz brauchen wir, um einen doppelten Knoten aus der Kette herauszunehmen.

---

# 4. Erster Knoten

Nehmen wir:

```text
5 -> 5 -> 6
```

Am Anfang gilt:

```text
seen = {}
current -> erster 5-Knoten
previous = None
```

Wir prüfen:

```python
current.data in seen
```

also:

```text
5 in {}
```

Das ist:

```text
False
```

Damit ist `5` neu.

Wir führen aus:

```python
seen.add(current.data)
previous = current
```

Jetzt:

```text
seen = {5}
previous -> erster 5-Knoten
```

Der erste Wert bleibt erhalten.

---

# 5. Ein Duplikat erkennen

Als Nächstes zeigt `current` auf den zweiten `5`-Knoten.

Jetzt prüfen wir:

```python
5 in seen
```

Das ergibt:

```text
True
```

Dieser Knoten ist also ein Duplikat.

Er soll entfernt werden.

---

# 6. Wie entfernt man einen Knoten aus einer einfach verketteten Liste?

Angenommen:

```text
previous          current
   ↓                 ↓
 [5] -------------> [5] -> [6]
```

Um den zweiten `5`-Knoten zu überspringen, setzen wir:

```python
previous.next = current.next
```

Dadurch zeigt der erste `5`-Knoten direkt auf `6`:

```text
[5] -> [6]
```

Der doppelte Knoten gehört danach nicht mehr zur verketteten Liste.

Wir müssen dafür keinen neuen Knoten erzeugen.

---

# 7. Warum wird `previous` bei einem Duplikat nicht verändert?

Das ist einer der wichtigsten Punkte der Aufgabe.

Bei einem Duplikat:

```python
if current.data in seen:
    previous.next = current.next
```

bleibt `previous` auf dem letzten gültigen Knoten stehen.

Das ist notwendig, damit auch mehrere Duplikate direkt hintereinander korrekt entfernt werden.

Beispiel:

```text
5 -> 5 -> 5 -> 6
```

Nach dem ersten `5` zeigt:

```text
previous -> erster 5-Knoten
```

Der zweite `5`-Knoten wird entfernt.

`previous` bleibt trotzdem auf dem ersten `5`.

Dann wird auch der dritte `5`-Knoten entfernt.

Erst bei `6`, einem neuen Wert, wandert `previous` weiter.

---

# 8. Warum funktioniert das mit mehreren aufeinanderfolgenden Duplikaten?

Ausgangslage:

```text
5 -> 5 -> 5 -> 6
```

Nach dem ersten Knoten:

```text
seen = {5}
previous -> erstes 5
```

Beim zweiten `5`:

```python
previous.next = current.next
```

Ergebnis:

```text
5 -> 5 -> 6
```

Beim dritten `5` wieder:

```python
previous.next = current.next
```

Ergebnis:

```text
5 -> 6
```

Da `previous` währenddessen nicht weitergerückt ist, können beliebig viele direkt folgende Duplikate entfernt werden.

---

# 9. Warum wird `previous` bei einem neuen Wert aktualisiert?

Wenn ein Wert noch nicht vorkam:

```python
else:
    seen.add(current.data)
    previous = current
```

Dann soll dieser Knoten erhalten bleiben.

Er wird deshalb zum neuen letzten gültigen Knoten.

Beispiel:

```text
5 -> 6
```

Nach `5`:

```text
previous -> 5
```

Bei `6`:

```text
6 not in seen
```

also:

```python
previous = current
```

Danach:

```text
previous -> 6
```

---

# 10. Warum können wir am Ende immer `current = current.next` ausführen?

Am Ende jeder Schleifenrunde:

```python
current = current.next
```

Bei einem normalen Knoten gehen wir einfach zum nächsten.

Auch bei einem entfernten Duplikat funktioniert das:

Der lokale Name `current` zeigt noch auf den entfernten Knoten, und dessen `next`-Referenz zeigt weiterhin auf den ursprünglichen Nachfolger.

Dadurch können wir die Liste korrekt weiter durchlaufen.

---

# 11. Komplettes Beispiel

Ausgangsliste:

```text
5 -> 5 -> 6 -> 5 -> 7 -> 6
```

### Erster Wert: `5`

```text
seen = {5}

Liste:
5 -> 5 -> 6 -> 5 -> 7 -> 6
```

Der erste `5` bleibt.

### Zweiter Wert: `5`

Bereits in `seen`.

Knoten entfernen:

```text
5 -> 6 -> 5 -> 7 -> 6
```

### Wert: `6`

Noch nicht gesehen:

```text
seen = {5, 6}
```

`6` bleibt.

### Nächster Wert: `5`

Bereits gesehen.

Entfernen:

```text
5 -> 6 -> 7 -> 6
```

### Wert: `7`

Neu:

```text
seen = {5, 6, 7}
```

`7` bleibt.

### Letzter Wert: `6`

Bereits gesehen.

Entfernen:

```text
5 -> 6 -> 7
```

Fertiges Ergebnis:

```text
5 -> 6 -> 7
```

---

# 12. Laufzeitkomplexität

Sei `n` die Anzahl der Knoten.

Die Schleife:

```python
while current:
```

besucht jeden Knoten genau einmal.

Die Operationen:

```python
current.data in seen
seen.add(...)
```

sind bei einem Set im Durchschnitt:

```text
O(1)
```

Auch das Umhängen einer Referenz:

```python
previous.next = current.next
```

ist:

```text
O(1)
```

Damit ergibt sich insgesamt im durchschnittlichen Fall:

```text
O(n)
```

---

# 13. Speicherkomplexität

Im schlimmsten Fall enthält die Liste nur unterschiedliche Werte:

```text
1 -> 2 -> 3 -> 4 -> 5 -> ...
```

Dann landen alle `n` Werte im Set:

```python
seen
```

Der zusätzliche Speicherbedarf beträgt deshalb:

```text
O(n)
```

Wir tauschen also zusätzlichen Speicher gegen eine schnelle Duplikatprüfung.

---

# 14. Was wäre eine Lösung ohne Set?

Man könnte für jeden Knoten alle vorherigen Knoten durchsuchen und prüfen, ob der Wert schon vorkam.

Das würde ungefähr bedeuten:

```text
für jeden Knoten:
    viele andere Knoten durchsuchen
```

Im Worst Case wäre das:

```text
O(n²)
```

Mit dem Set erreichen wir stattdessen durchschnittlich:

```text
O(n)
```

Das ist ein klassischer Trade-off:

> Mehr Speicher kann verwendet werden, um Laufzeit zu sparen.

---

# 15. Randfall: Leere Liste

Wenn:

```python
self.head = None
```

dann gilt:

```python
current = self.head
```

also:

```text
current = None
```

Die Schleife:

```python
while current:
```

wird nicht ausgeführt.

Die Methode endet einfach.

Das ist korrekt.

---

# 16. Randfall: Nur ein Knoten

Bei:

```text
5
```

wird `5` einmal in `seen` eingetragen.

Es gibt keinen zweiten Knoten.

Die Liste bleibt:

```text
5
```

Auch dafür ist keine Sonderbehandlung nötig.

---

# 17. Randfall: Alle Werte gleich

Beispiel:

```text
5 -> 5 -> 5 -> 5
```

Der erste `5`-Knoten bleibt.

Alle weiteren werden entfernt.

Ergebnis:

```text
5
```

Gerade hier zeigt sich, warum `previous` bei einem Duplikat nicht weiterbewegt werden darf.

---

# 18. Randfall: Keine Duplikate

Beispiel:

```text
1 -> 2 -> 3
```

Jeder Wert wird einmal in `seen` eingetragen.

Kein Knoten wird entfernt.

Die Liste bleibt unverändert:

```text
1 -> 2 -> 3
```

---

# 19. Wichtiger Robustheitsaspekt: Werte müssen hashbar sein

Da wir ein Python-Set verwenden:

```python
seen = set()
```

müssen die gespeicherten Werte **hashbar** sein.

Typische Werte wie:

```python
5
"hello"
(1, 2)
```

sind hashbar und funktionieren.

Eine veränderbare Liste wie:

```python
[1, 2]
```

ist dagegen nicht hashbar.

Bei:

```python
seen.add([1, 2])
```

würde Python einen `TypeError` auslösen.

Für diese Schulaufgabe ist es sehr wahrscheinlich vorgesehen, einfache Werte wie Zahlen oder Strings zu speichern.

In einer allgemeineren Datenstruktur müsste man jedoch bewusst festlegen, welche Datentypen unterstützt werden sollen.

---

# 20. Datenintegrität beim Entfernen

Bei Linked Lists bedeutet Löschen normalerweise nicht, dass wir den Knoten manuell aus dem Speicher entfernen.

Wir ändern die Verknüpfung:

```python
previous.next = current.next
```

Dadurch ist der doppelte Knoten von der Liste aus nicht mehr erreichbar.

Python kann den Speicher später automatisch durch den Garbage Collector freigeben, sobald keine Referenz mehr darauf existiert.

Das Entscheidende ist deshalb die korrekte Pflege der `next`-Referenzen.

---

# 21. Hinweis zu `tail`

Diese konkrete `LinkedList` besitzt nur:

```python
self.head
```

und kein:

```python
self.tail
```

Deshalb müssen wir beim Entfernen von Duplikaten keinen Tail-Zeiger aktualisieren.

Wenn wir diese Methode jedoch mit unserer vorherigen `LinkedList`-Variante kombinieren würden, die ein `tail`-Attribut für `append()` in `O(1)` besitzt, müssten wir einen zusätzlichen Fall bedenken:

> Wird der letzte Knoten als Duplikat entfernt, muss `tail` anschließend auf den neuen letzten Knoten zeigen.

Das ist ein gutes Beispiel dafür, wie neue Optimierungen auch zusätzliche Invarianten erzeugen, die andere Methoden berücksichtigen müssen.

---

# 22. Design- und Skalierungsgedanke

Die Aufgabe zeigt wieder einen wichtigen Software-Engineering-Trade-off:

```text
ohne Set:
weniger zusätzlicher Speicher
aber möglicherweise O(n²)
```

gegen:

```text
mit Set:
O(n) zusätzlicher Speicher
aber durchschnittlich O(n) Laufzeit
```

Bei kleinen Datenmengen ist beides wahrscheinlich schnell genug.

Bei großen Listen wird der Unterschied jedoch erheblich.

---

# 23. Zentrale Lernidee

Der Algorithmus kombiniert zwei Datenstrukturen:

## Linked List

Die eigentlichen Knoten werden durch ihre `next`-Referenzen verbunden.

## Set

Merkt sich effizient, welche Werte bereits vorgekommen sind.

Wenn ein Wert doppelt vorkommt, überspringen wir den entsprechenden Knoten mit:

```python
previous.next = current.next
```

Dabei bleibt `previous` bewusst stehen, damit auch direkt aufeinanderfolgende Duplikate korrekt entfernt werden.

---

# Zusammenfassung

Die Methode verwendet:

```python
seen = set()
current = self.head
previous = None
```

Bei einem neuen Wert:

```python
seen.add(current.data)
previous = current
```

Bei einem Duplikat:

```python
previous.next = current.next
```

Damit bleibt immer nur das erste Vorkommen eines Wertes erhalten.

Die durchschnittliche Laufzeit beträgt:

```text
O(n)
```

Der zusätzliche Speicherbedarf beträgt:

```text
O(n)
```

Die wichtigste Erkenntnis lautet:

> **Ein Set ermöglicht eine schnelle Prüfung bereits gesehener Werte, während `previous.next = current.next` den doppelten Knoten direkt aus der Linked List überspringt.**
