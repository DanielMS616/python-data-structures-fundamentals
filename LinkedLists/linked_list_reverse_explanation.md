# `LinkedList.reverse()` – Eine verkettete Liste in-place umkehren

## Ziel der Übung

Die Methode

```python
reverse()
```

soll die Richtung aller `next`-Verknüpfungen einer `LinkedList` **in-place** umdrehen.

**In-place** bedeutet:

> Die vorhandenen Knoten werden weiterverwendet.  
> Es wird keine zweite Linked List mit neuen Knoten aufgebaut.

Dafür werden mehrere Referenzen gleichzeitig benötigt, damit beim Umhängen eines `next`-Links der noch nicht bearbeitete Teil der Liste erreichbar bleibt.

Beispiel:

```text
Vorher:
5 -> 6 -> 7

Nachher:
7 -> 6 -> 5
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

    def reverse(self):
        previous = None
        current = self.head

        while current:
            # Save the next node before reversing the current link.
            next_node = current.next

            current.next = previous

            # Move both references one node forward.
            previous = current
            current = next_node

        # The old last node is now the first node.
        self.head = previous

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

ll.reverse()

print(ll)
```

Erwartete Ausgabe:

```text
6->5
```

---

# 1. Wiederholung: Wie ist eine Linked List aufgebaut?

Eine einfach verkettete Liste besteht aus Knoten.

Jeder Knoten enthält:

```text
data
next
```

`data` speichert den eigentlichen Wert.

`next` zeigt auf den nächsten Knoten.

Beispiel:

```text
head
 ↓
[5] -> [6] -> [7] -> None
```

Der letzte Knoten zeigt auf:

```text
None
```

Damit wissen wir, dass die Liste dort endet.

---

# 2. Was bedeutet „in-place“?

Eine mögliche, aber hier nicht gewünschte Lösung wäre:

1. eine neue Linked List erzeugen,
2. alle Werte aus der alten Liste lesen,
3. neue Knoten in umgekehrter Reihenfolge erzeugen.

Das wäre **nicht in-place**.

Bei einer In-place-Lösung bleiben dieselben Knoten bestehen.

Wir ändern nur ihre Verbindungen:

```text
Vorher:

[5] -> [6] -> [7] -> None
```

wird zu:

```text
Nachher:

[5] <- [6] <- [7]
               ↑
              head
```

bzw. in normaler Leserichtung:

```text
head
 ↓
[7] -> [6] -> [5] -> None
```

---

# 3. Die drei wichtigen Referenzen

Für die Umkehrung verwenden wir drei Referenzen:

```python
previous
current
next_node
```

Sie haben unterschiedliche Aufgaben.

## `previous`

```python
previous = None
```

zeigt auf den Knoten, der nach dem Umdrehen hinter `current` liegen soll.

Am Anfang gibt es noch keinen vorherigen Knoten.

Deshalb:

```text
previous = None
```

---

## `current`

```python
current = self.head
```

zeigt auf den Knoten, den wir gerade bearbeiten.

Zu Beginn ist das der erste Knoten der Liste.

---

## `next_node`

```python
next_node = current.next
```

speichert den nächsten Knoten, **bevor** wir `current.next` verändern.

Das ist der wichtigste Sicherheitsmechanismus des Algorithmus.

---

# 4. Warum müssen wir `next_node` zuerst speichern?

Nehmen wir an:

```text
[5] -> [6] -> [7] -> None
```

und `current` zeigt auf:

```text
5
```

Wenn wir direkt schreiben würden:

```python
current.next = previous
```

wird aus:

```text
5 -> 6
```

sofort:

```text
5 -> None
```

Damit verlieren wir über `5` die Referenz auf:

```text
6
```

und damit auch auf den Rest der Liste.

Deshalb speichern wir vorher:

```python
next_node = current.next
```

Jetzt kennen wir `6` weiterhin, selbst nachdem wir den Link von `5` verändern.

---

# 5. Der eigentliche Umkehrschritt

Die entscheidende Zeile lautet:

```python
current.next = previous
```

Sie dreht die Richtung des aktuellen Links um.

Am Anfang gilt:

```text
previous = None
current  = 5
```

Also wird:

```python
5.next = None
```

Das ist korrekt, denn `5` soll später der letzte Knoten der umgekehrten Liste sein.

---

# 6. Danach wandern die Referenzen weiter

Nach dem Umdrehen des Links:

```python
previous = current
current = next_node
```

Wir schieben beide Referenzen einen Knoten nach vorne.

Nach dem ersten Schritt:

```text
previous -> 5
current  -> 6
```

Der bereits umgedrehte Teil ist:

```text
[5] -> None
```

Der noch nicht bearbeitete Teil beginnt bei:

```text
[6] -> [7] -> None
```

---

# 7. Komplettes Beispiel mit `5 -> 6 -> 7`

Ausgangszustand:

```text
previous
   ↓
  None

current
  ↓
 [5] -> [6] -> [7] -> None
```

---

## Iteration 1

Zuerst:

```python
next_node = current.next
```

Damit:

```text
next_node -> 6
```

Dann:

```python
current.next = previous
```

Aus:

```text
5 -> 6
```

wird:

```text
5 -> None
```

Danach:

```python
previous = current
current = next_node
```

Jetzt:

```text
previous -> 5
current  -> 6
```

---

## Iteration 2

`next_node` speichert:

```text
7
```

Dann wird:

```text
6 -> 5
```

Danach:

```text
previous -> 6
current  -> 7
```

Der bereits umgekehrte Teil ist jetzt:

```text
6 -> 5 -> None
```

---

## Iteration 3

`next_node` ist:

```text
None
```

Dann wird:

```text
7 -> 6
```

Danach:

```text
previous -> 7
current  -> None
```

Jetzt endet die Schleife.

---

# 8. Warum wird `self.head = previous` gesetzt?

Nach der letzten Schleifenrunde zeigt:

```python
previous
```

auf den alten letzten Knoten.

Bei:

```text
5 -> 6 -> 7
```

ist das:

```text
7
```

Dieser Knoten muss jetzt der neue Anfang der Liste werden:

```python
self.head = previous
```

Danach:

```text
head
 ↓
[7] -> [6] -> [5] -> None
```

Die Liste ist vollständig umgekehrt.

---

# 9. Warum entsteht keine zirkuläre Liste?

Die Aufgabe warnt ausdrücklich davor, versehentlich eine zirkuläre Liste zu erzeugen.

Das könnte passieren, wenn Referenzen falsch gesetzt werden und beispielsweise:

```text
5 -> 6
↑    ↓
└────┘
```

entsteht.

Unser Algorithmus verhindert das dadurch, dass jeder Link kontrolliert genau einmal umgedreht wird.

Besonders wichtig ist der erste Schritt:

```python
previous = None
```

Dadurch wird beim alten ersten Knoten:

```python
current.next = previous
```

zu:

```text
old_head.next = None
```

Der alte erste Knoten wird damit korrekt zum neuen letzten Knoten.

---

# 10. Laufzeitkomplexität

Wir durchlaufen jeden Knoten genau einmal:

```python
while current:
```

Bei `n` Knoten läuft die Schleife `n`-mal.

Pro Knoten führen wir nur konstante Operationen aus:

```python
next_node = current.next
current.next = previous
previous = current
current = next_node
```

Damit ergibt sich insgesamt:

```text
O(n)
```

---

# 11. Speicherkomplexität

Die Methode erzeugt keine neue Liste und keine neuen Knoten.

Wir verwenden nur drei zusätzliche Referenzen:

```python
previous
current
next_node
```

Unabhängig davon, ob die Linked List 5 oder 5 Millionen Knoten enthält, bleiben es dieselben drei Referenzen.

Deshalb beträgt der zusätzliche Speicherbedarf:

```text
O(1)
```

Das ist ein wichtiger Vorteil der In-place-Lösung.

---

# 12. Sonderfall: Leere Liste

Bei einer leeren Liste gilt:

```python
self.head = None
```

Dann:

```python
current = self.head
```

ergibt ebenfalls:

```text
None
```

Die Schleife:

```python
while current:
```

wird kein einziges Mal ausgeführt.

Am Ende:

```python
self.head = previous
```

wobei `previous` ebenfalls `None` ist.

Die Liste bleibt korrekt leer.

Wir brauchen dafür keine zusätzliche Sonderbehandlung.

---

# 13. Sonderfall: Nur ein Knoten

Ausgangslage:

```text
head
 ↓
[5] -> None
```

Dann:

```text
previous = None
current = 5
```

In der Schleife:

```text
next_node = None
5.next = None
previous = 5
current = None
```

Danach:

```python
self.head = previous
```

Der Head zeigt weiterhin auf `5`.

Die Liste bleibt:

```text
[5] -> None
```

Auch dieser Randfall funktioniert automatisch.

---

# 14. Was ist der gefährlichste Fehler bei dieser Aufgabe?

Der kritischste Fehler wäre, den nächsten Knoten nicht zu speichern.

Zum Beispiel:

```python
current.next = previous
current = current.next
```

Das funktioniert nicht.

Warum?

Nach:

```python
current.next = previous
```

zeigt `current.next` bereits **rückwärts**.

Wir würden also nicht mehr zum ursprünglichen nächsten Knoten laufen.

Die Verbindung zum unbearbeiteten Rest der Liste wäre verloren.

Deshalb ist:

```python
next_node = current.next
```

vor dem Umdrehen so wichtig.

---

# 15. Warum verwenden wir keine neue Liste?

Eine einfachere gedankliche Lösung könnte sein:

```text
alte Liste lesen
Werte speichern
neue Liste rückwärts aufbauen
```

Das würde zusätzliche Datenstrukturen oder neue Knoten benötigen.

Die Aufgabe fordert aber ausdrücklich:

```text
in-place
```

Darum verändern wir nur die vorhandenen `next`-Referenzen.

Das spart zusätzlichen Speicher und trainiert gleichzeitig das Verständnis von Referenzen.

---

# 16. Design- und Skalierungsgedanke

Diese Aufgabe zeigt einen sehr wichtigen Unterschied zwischen:

```text
Daten kopieren
```

und:

```text
bestehende Struktur verändern
```

Die In-place-Lösung benötigt:

```text
O(1)
```

zusätzlichen Speicher.

Eine Lösung, die alle Knoten oder Werte kopiert, könnte dagegen:

```text
O(n)
```

zusätzlichen Speicher benötigen.

Bei kleinen Listen ist der Unterschied kaum relevant.

Bei sehr großen Datenstrukturen kann er aber wichtig werden.

---

# 17. Fehlerfälle und Datenintegrität

Hier geht es weniger um ungültige Benutzereingaben und mehr um die **Integrität der Datenstruktur**.

Beim Verändern von Referenzen müssen wir sicherstellen, dass:

- kein Knoten verloren geht,
- kein Link versehentlich auf sich selbst zeigt,
- keine zirkuläre Struktur entsteht,
- der neue `head` korrekt gesetzt wird,
- der alte `head` am Ende auf `None` zeigt.

Das ist ein gutes Beispiel dafür, dass „Fehlerfälle“ bei Datenstrukturen nicht immer Formulareingaben oder Exceptions sind.

Manchmal besteht Robustheit vor allem darin, die internen Zustände korrekt zu erhalten.

---

# 18. Hinweis zur `append()`-Methode in dieser Aufgabe

Die hier gegebene `append()`-Methode sucht das Listenende jedes Mal mit:

```python
while last_node.next:
    last_node = last_node.next
```

Deshalb ist dieses `append()`:

```text
O(n)
```

Das ist für die aktuelle Reverse-Aufgabe vollkommen in Ordnung.

In der vorherigen Übung haben wir bereits gesehen, wie man mit einem zusätzlichen:

```python
self.tail
```

das Anhängen auf:

```text
O(1)
```

verbessern kann.

Die beiden Aufgaben verfolgen also unterschiedliche Lernziele:

```text
vorherige Aufgabe -> schnelles Anhängen mit tail
diese Aufgabe     -> Links in-place umkehren
```

---

# 19. Zentrale Lernidee

Der Algorithmus funktioniert durch drei Referenzen:

```text
previous
current
next_node
```

Für jeden Knoten passiert immer dieselbe Reihenfolge:

```text
1. nächsten Knoten sichern
2. aktuellen Link umdrehen
3. previous weiterschieben
4. current weiterschieben
```

Kurz:

```python
next_node = current.next
current.next = previous
previous = current
current = next_node
```

Diese Reihenfolge ist entscheidend.

Wird sie verändert, kann man den restlichen Teil der Liste verlieren oder falsche Verknüpfungen erzeugen.

---

# Zusammenfassung

Eine Linked List:

```text
5 -> 6 -> 7 -> None
```

wird durch das Umdrehen ihrer `next`-Referenzen zu:

```text
7 -> 6 -> 5 -> None
```

Wir benötigen dafür keine neue Liste.

Die Methode verwendet nur:

```python
previous
current
next_node
```

und arbeitet dadurch mit:

```text
Laufzeit:             O(n)
zusätzlicher Speicher: O(1)
```

Die wichtigste Erkenntnis lautet:

> **Beim In-place-Umkehren einer Linked List muss der ursprüngliche nächste Knoten immer zuerst gespeichert werden, bevor die aktuelle `next`-Referenz umgedreht wird.**
