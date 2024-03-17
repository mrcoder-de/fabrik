# Du willst selber ausprobieren?

So geht das:
1. such dir ein Prompt aus z.B. Vorhersagen extrahieren (extract predictions)
1. such dir ein passende Text aus z.B. https://www.handelsblatt.com/politik/deutschland/kuenstliche-intelligenz-wie-ki-die-welt-veraendern-wird-das-sagen-oekonomen-und-studien/29222364.html
1. probier das mit einem LLM aus z.B. Mixtral8x7b hier: https://labs.perplexity.ai/

Einfach folgendes Copy & Pasten:

```
# IDENTITÄT und ZWECK

Sie verdauen den Input vollständig und extrahieren die darin enthaltenen
Vorhersagen.

Treten Sie einen Schritt zurück und überlegen Sie Schritt für Schritt, wie Sie
die bestmöglichen Ergebnisse erzielen können, indem Sie die folgenden Schritte
befolgen.

# SCHRITTE

* Extrahieren Sie alle Vorhersagen, die im Inhalt enthalten sind.

* Extrahieren Sie für jede Vorhersage die folgenden Informationen:

* Die spezifische Vorhersage in weniger als 15 Wörtern.

* Das Datum, bis zu dem die Vorhersage eintreten soll.
* Das für die Vorhersage angegebene Vertrauensniveau.
* Wie wir wissen, ob sie wahr ist oder nicht.

# AUSGABEANWEISUNGEN

* Geben Sie nur gültigen Markdown ohne Fett- oder Kursivdruck aus.

* Geben Sie die Vorhersagen als aufgereihte Liste aus.

* Erstellen Sie unter der Liste eine Vorhersagetabelle, die folgende Spalten enthält: Vorhersage, Konfidenz, Datum, Wie
  zu verifizieren.

* Begrenzen Sie jeden Aufzählungspunkt auf maximal 15 Wörter.

* Geben Sie keine Warnungen oder Anmerkungen an; geben Sie nur die geforderten Abschnitte aus.

* Achten Sie darauf, dass Sie bei der Erstellung Ihrer Ausgabe ALLE diese Anweisungen befolgen.

# EINGABE

Künstliche Intelligenz : Wie KI die Welt verändern wird: Das sagen Ökonomen und Studien
8–9 minutes

Die Ökonomen analysieren die ökonomischen Chancen von KI.

Berlin. Jobängste? Neue Heilmittel? Sonderkonjunktur? Das Handelsblatt hat ungezählte Studien gesichtet und mit Deutschlands führenden Ökonomen über die Frage gesprochen, wie KI die Bereiche Arbeitswelt, Forschung und Wirtschaftswachstum in den kommenden Jahren und Jahrzehnten verändern wird.

Ob in Banken, Anwaltskanzleien oder Kreativbüros: Die jüngsten Fortschritte im Bereich KI lösen in Branchen Jobängste aus, die sich bislang nicht betroffen fühlten. Die sogenannten „white collar worker“ – Arbeiter mit weißen Kragen – fragen sich, ob sie noch gebraucht werden, wenn Algorithmen auch intellektuelle Arbeit übernehmen können. Tatsächlich aber ist diese Frage noch weitestgehend unerforscht. Belastbare Zahlen sind rar.

Expertinnen und Experten sprechen meist von einem Nullsummenspiel: Jobs gingen verloren, gleichzeitig aber entstehen neue - wie bei allen technologischen Revolutionen der vergangenen Jahrzehnte auch.

So prognostizierte das World Economic Forum (WEF) zuletzt, dass etwas mehr als jeder zehnte Job weltweit innerhalb von fünf Jahren von einer KI übernommen werden könnte. Die meisten befragten Arbeitgeber erwarten jedoch, dass durch den KI-Einsatz mehr Stellen entstehen als wegfallen werden.

Und in Deutschland? Laut dem kürzlich Arbeitsminister Hubertus Heil (SPD) übergebenen Arbeitswelt-Bericht gehen durch die Digitalisierung hierzulande zwar 3,6 Millionen Jobs bis 2040 verloren. Ebenso viele, sagen die 13 Expertinnen und Experten des Gremiums, würden aber auch neu entstehen.

Ökonomen blicken deswegen optimistisch bis euphorisch auf die Chancen, die KI für den Arbeitsmarkt bietet. „Durch KI können viele Routinetätigkeiten ersetzt werden“, sagt die Vorsitzende der Wirtschaftsweisen, Monika Schnitzer. So könne beispielsweise das Erstellen von Schriftstücken bei Strafverfahren wie Verkehrsdelikten durch KI erleichtert und könnten dadurch die Verfahren erheblich beschleunigt werden.
KI könnte Wegfall von Arbeitskräften teilweise auffangen

Die Herausforderung: Gerade kleineren Unternehmen und den öffentlichen Verwaltungen fällt es nach wie vor schwer, auf digitalisierte Prozesse umzustellen. Von daher sei in diesen Bereichen fraglich, ob sie zeitnah KI-Methoden anwenden würden, meint die Chefin des Sachverständigenrats.

Wenn das allerdings gelingt, habe KI für den Arbeitsmarkt großes Potenzial. „Ich halte es für durchaus möglich, dass durch KI der Wegfall von Arbeitskräften durch den demografischen Wandel teilweise kompensiert werden kann“, erklärt sie. Laut einer Studie des Instituts für Arbeitsmarkt- und Berufsforschung gehen dem deutschen Arbeitsmarkt bis 2035 allein durch die älter werdende Bevölkerung immerhin sieben Millionen Menschen verloren.

Dieser Text ist Teil des großen Handelsblatt-Spezials zur Künstlichen Intelligenz. Sie interessieren sich für dieses Thema? Alle Texte, die im Rahmen unserer Themenwoche schon erschienen sind, finden Sie hier.

Die Folgen könnten vor allem dann am besten aufgefangen werden, wenn KI auch für komplexere Aufgaben eingesetzt werden kann. Vor allem das Sprachprogramm ChatGPT speist bei Ökonomen diese Hoffnung. Die KI kann Texte in Sekundenschnelle analysieren und schreiben. „Solche Technologien können vielleicht auch bei Nicht-Routinetätigkeiten eingesetzt werden“, sagt Simon Jäger, Chef des Bonner Instituts zur Zukunft der Arbeit (IZA).

Ob ein Einsatz in der Breite gelingt, hängt nicht nur von technischen, sondern auch von gesellschaftlichen Fragen ab. „Bisher haben wir wenig Leitplanken gesetzt und so dafür gesorgt, dass technologischer Fortschritt mit dazu beigetragen hat, dass sich der Niedriglohnsektor mit vielen einfachen Tätigkeiten, die häufig standardisiert sind, vergrößert hat“, erklärt Jäger.

Ein Beispiel seien Taxifahrer: „Mit Apps für Navigationshilfen oder Übersetzungen ist die Einstiegsschwelle für Fahrdienstleistungen inzwischen viel niedriger, deswegen gibt es so was wie Uber.“ Gleichzeitig seien dort aber prekäre Arbeitsbedingungen entstanden.

Der Deutsche Gewerkschaftsbund (DGB) sieht deswegen in der Weiterbildung der Arbeitskräfte die wichtigste Aufgabe von Unternehmen, um ihre Beschäftigten auf die Umwälzungen vorzubereiten.  Es gehe darum, Beschäftigte in den Betrieben mitzunehmen und nicht den Menschen, sondern Prozesse zu optimieren, sagte DGB-Chefin Yasmin Fahimi vor Kurzem dem Handelsblatt.
Wissenschaft wird produktiver

In der Wissenschaft vermelden Forscher beinahe im Wochentakt Durchbrüche, die ohne KI undenkbar gewesen wären. Im Oktober gelang es der Google-Tochterfirma Deepmind, nach mehr als 50 Jahren einen schnelleren Weg für die Multiplikation von Matrizen zu finden. Der kürzere Rechenweg könnte künftig Zeit und Energie sparen. Deepmind half auch dabei, die bislang größte Datenbank an menschlichen Proteinen zu erstellen.

Weltweit hoffen Forscher, Mediziner und Regierungen deswegen darauf, mithilfe von KI Antworten auf die großen Probleme der Menschheit zu finden. Es geht um die Erforschung neuer Modelle, Materialien und Medikamente – mit teils gewaltigen Ressourcen.

US-Präsident Joe Biden etwa setzt mit einer zwölf Milliarden Dollar schweren „Moonshot”-Initiative auf KI in der Medizin. Sie soll die Todesfälle durch Krebs binnen 25 Jahren um mindestens 50 Prozent senken. Andere wiederum warnen vor Risiken - etwa die Weltgesundheitsorganisation WHO, die vor Ausbrüchen von künstlichen, durch KI hergestellten Erregern warnt.

„KI wird auch die Wissenschaft umkrempeln“, sagt Jens Südekum, Mitglied im unabhängigen Beirat beim Bundeswirtschaftsministerium. Einfache Datenauswertungen, Programmierarbeiten oder Visualisierungen könnten automatisiert werden. KI könne Wissenschaftlern in allen Forschungsbereichen Teile ihrer Arbeit abnehmen und sie dadurch „viel produktiver“ machen. Wissenschaftler würden deshalb aber nicht überflüssig.

Das sieht auch die Wirtschaftsweisen-Vorsitzende Schnitzer so. Durch maschinelles Lernen könnten Zusammenhänge in großen Datenmengen analysiert werden. „Man lernt aber nicht, was der Grund für diese Zusammenhänge ist“, sagt Schnitzer.
Chance für mehr Wachstum

Ökonomen erhoffen sich durch KI einen gewaltigen Schub beim Wirtschaftswachstum. Smarte Auswertungen von Energiesystemen können die Verbräuche reduzieren, Leitsysteme für Straße und Schiene können den Verkehr schneller fließen lassen, die Industrie kann Ressourcen genauer einsetzen. Der gleiche Einsatz kann zu höheren Outputs führen.

In der Summe rechnen Wirtschaftswissenschaftler damit, dass KI großes Potenzial hat, die Produktivität der Volkswirtschaften weltweit zu erhöhen. „Erste Projektionen deuten darauf hin, dass KI zu massivem Produktivitätswachstum führen wird“, sagt Ökonom Südekum. Er hält langfristig einen Zuwachs der globalen Wirtschaftsleistung durch KI um sieben Prozent für denkbar. „Das ist ein riesiges Potenzial.“

Gerade für Deutschland ist das eine große Chance. „Denn demografiebedingt schrumpft das deutsche Wachstumspotenzial in den kommenden Jahren erheblich, einfach, weil an allen Ecken und Enden Arbeitskräfte fehlen“, sagt Südekum. Wo immer es möglich sei, sollten diese Lücken auch durch KI geschlossen werden.
```