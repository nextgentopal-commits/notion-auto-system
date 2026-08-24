# TÜRKISCHE LITERATUR — GITHUB RESEARCH MASTER v0.9

**Stand:** 24. August 2026  
**Status:** Zehn Recherchewellen und GitHub Research Phase 2/Pass 1 abgeschlossen · Profile 01 Yunus Emre, 02 Fuzûlî, 03 Sabahattin Ali, 04 Ahmet Hamdi Tanpınar, 05 Yaşar Kemal und Emotionsprofil 06 Hüzün–Hasret–Gurbet integriert  
**Zweck:** Aufbau eines quellenkritischen Korpus für DEJÀ-VU-3: Originalwerke, Literaturgeschichte, Denkweisen, Emotionen, Biografie, soziale Bedingungen, Sprache, Form und digitale Werkzeuge.

## 1. Grundsatz

GitHub ist Fundort, nicht automatisch Primärquelle. Jede Ressource wird getrennt nach Textidentität, Edition, Herkunft, Rechten, wissenschaftlicher Belastbarkeit und Transformationsnutzen geprüft.

### Quellenklassen

| Klasse | Bedeutung | Nutzung |
|---|---|---|
| A1 | Primärtext, Faksimile oder kritische Edition | direkte Analyse nach exakter Prüfung |
| A2 | wissenschaftlich edierter Text | Analyse mit Editionsangabe |
| B1 | akademische Biografie, Katalog oder Literaturgeschichte | historische und biografische Fakten |
| B2 | wissenschaftliche Interpretation | gekennzeichnete Deutung |
| C1 | dokumentierte mündliche Variante | Traditionsanalyse, keine feste Autorschaft |
| C2 | populäre Sammlung ohne Apparat | nur als Suchhinweis |
| D | Zitatseite, unbekannter Dump oder ungeprüfte Zuschreibung | nicht als Beleg verwenden |

## 2. Erster GitHub-Fundstand

| Repository | Inhalt | Potenzial | Vorläufige Klasse / Risiko |
|---|---|---|---|
| [Mrjavaci/Turkish-Poems](https://github.com/Mrjavaci/Turkish-Poems) | 3.370 Gedichte, 89.418 Verszeilen; Autor, Titel und Text als JSON/TXT | quantitative Motiv-, Emotions-, Rhythmus- und Wortfeldanalyse | C2/D bis Herkunft, Edition und Rechte jedes Textes geklärt sind; enthält moderne urheberrechtlich geschützte Lyrik |
| [AdilSevim/Turkish-Poetry-Language-Model](https://github.com/AdilSevim/Turkish-Poetry-Language-Model) | GPT-2/LoRA-Projekt auf Basis der Turkish-Poems-Sammlung | technische Einsicht in Strukturierung, Tokenisierung und Modellrisiken | keine literarische Quelle; Stilimitations- und Rechteproblem ausdrücklich vorhanden |
| [OttomanTextAI/OttomanTextAI](https://github.com/OttomanTextAI/OttomanTextAI) | OCR, Transkription und Modernisierung osmanisch-türkischer Drucktexte | Erschließung historischer Drucke und Vergleich Faksimile → OCR → Transkription | technischer Prototyp; OCR-Fehler und LLM-Modernisierung erfordern menschliche Kollation |
| [bilalabic/awesome-turkish-datasets](https://github.com/bilalabic/awesome-turkish-datasets) | kuratierter Katalog mit 298 türkischen Datensätzen, davon 227 Text/NLP | zentrale Discovery-Schicht für Korpora, OCR, Emotion, Dialekt, Sprache und Lizenzen | B1-artiger technischer Katalog; jeder verlinkte Datensatz muss separat geprüft werden |
| [bitig/turkbitig](https://github.com/bitig/turkbitig) | umfangreiche türkische Text- und Autorensammlung, u. a. Yunus Emre und Fuzûlî | Textsuche, Variantenvergleich, frühe Autoren- und Werkerschließung | Herkunft und Editionsapparat pro Datei unklar; zunächst C2 |
| [taniki/comp.soc-of-philosophy](https://github.com/taniki/comp.soc-of-philosophy) | Seiten- und Satzsammlungen zu Philosophen und Autoren, darunter Yunus Emre | Denkbegriffe, Netzwerk- und Rezeptionsanalyse | abgeleitete Webdaten; keine Primärquelle |
| [yunusugur/turkey-dh-atlas](https://github.com/yunusugur/turkey-dh-atlas) | Verzeichnis türkischer Digital-Humanities-Projekte | weitere Archive, Korpora, Handschriften- und Forschungsprojekte entdecken | Metadaten-/Discovery-Quelle; Zielressourcen separat validieren |
| [Alperencode/DergiPark-Data-Set](https://github.com/Alperencode/DergiPark-Data-Set) | großer Volltextbestand aus DergiPark-Artikeln | Sekundärforschung zu Autoren, Epochen, Emotionen und Literaturgeschichte | Artikelqualität, bibliografische Identität und Nutzungsrechte einzeln prüfen |
| [arch-yunus/fasl-i-fuzuli](https://github.com/arch-yunus/fasl-i-fuzuli) | Fuzûlî-Külliyat, Biografie, Transkriptionen, Kommentare und Zitatmaterial | Werkstruktur, Begriffsfelder, Poetik, Rezeption und Quellenhinweise | stark kuratiert, aber nicht automatisch kritische Edition; mehrere Zitate und Zuschreibungen benötigen Originalprüfung |
| [pgarg22/Awarded-Minds-Literary-Network](https://github.com/pgarg22/Awarded-Minds-Literary-Network) | Autorennetzwerke aus Wikipedia-/Auszeichnungsdaten | Rezeptions- und Kanonnetzwerke | Sekundärdaten; nicht für Werk- oder Biografiebelege |

## 3. Bereits sichtbare Forschungsräume

### Originalwerke und Überlieferung

- Yunus Emre: Dîvân, Risâletü'n-Nushiyye, Überlieferungsvarianten und virale Fehlzuschreibungen.
- Fuzûlî: Türkçe Dîvân, Leylâ vü Mecnûn, Şikâyetnâme, Hadîkatü's-Süedâ, Su Kasidesi.
- Şeyh Gâlib: Hüsn ü Aşk und Dîvân.
- Dede Korkut, Kutadgu Bilig, Âşık-/Tekke-/Halk-Traditionen.
- Tanzimat, Servet-i Fünun, Fecr-i Âti, Millî Edebiyat, Republik, Sozialrealismus, Moderne, İkinci Yeni, Postmoderne und Diaspora.

### Denkweisen

- mystisches Denken: Ich-Grenze, Trennung, Hingabe, Einheit;
- paradoxe Erkenntnis: zwei widersprechende Wahrheiten gleichzeitig tragen;
- materielle Kausalität: Arbeit, Armut, Besitz und Institution erzeugen privaten Schmerz;
- innere Zeit: Erinnerung verändert Dauer und Gegenwart;
- öffentliche Moral: private Entscheidung wird gesellschaftlicher Konflikt;
- institutionelle Absurdität: Regelbefolgung zeigt menschliche Kosten;
- diasporische Doppelperspektive: Verlust und zusätzliche Sicht zugleich;
- Metafiktion: Form verändert Wahrheit und Verantwortung.

### Emotionen und begriffliche Trennung

Zu untersuchen sind mindestens Hüzün, Hasret, Gurbet, Keder, Efkâr, Hicran, Sitem, Aşk, Sevda, Sabır, Tevekkül, İsyan, Onur und Aidiyet. Diese Begriffe werden nicht gleichgesetzt. Pro Werk werden Auslöser, Gegenemotion, Körperausdruck, Handlung, Beziehung, Raum, Zeit und gesellschaftlicher Preis erfasst.

### Warum Autorinnen und Autoren so denken

Die Forschung vermeidet einfache Psychobiografie. Erfasst werden:

1. historischer Bruch und politische Ordnung,
2. Sprache, Schrift und Bildungsinstitution,
3. Herkunft, Klasse, Arbeit und ökonomische Lage,
4. Exil, Gefängnis, Migration, Zensur oder Krieg,
5. religiöse, philosophische und literarische Tradition,
6. Stadt, Landschaft, Region und materielle Umwelt,
7. Beziehungen, Verluste und biografische Wendepunkte,
8. Publikationsfeld, Publikum, Patronage und Kritik,
9. formale Entscheidungen des konkreten Werks,
10. Unterschied zwischen Autor, Erzähler und Figur.

Biografie erklärt ein Werk nie vollständig. Historische Tatsache, Textbeobachtung und Interpretation bleiben getrennt.

## 4. Korpus-Schema

Für jeden Autor, jedes Werk und jede Tradition wird folgender Datensatz aufgebaut:

| Feld | Inhalt |
|---|---|
| Identität | Autor/Tradition, Titel, Sprache, Schrift, Genre, Zeit |
| Quelle | Repository, Datei, Commit, Edition/Witness, Quellenklasse |
| Rechte | Gemeinfrei, lizenziert, unklar oder geschützt |
| Historischer Kontext | Ereignisse, Institutionen, Sprach- und Gesellschaftslage |
| Biografischer Kontext | nur belegte relevante Lebensumstände |
| Menschliche Situation | Person, Wunsch, Pflicht, Wunde, Konflikt, Preis |
| Denkmodus | kausal, dialektisch, mystisch, existenziell, materiell, metakognitiv usw. |
| Perspektive | Wissensstand, moralischer Einsatz, Zeit, Körper, Sprache |
| Emotion | Hauptemotion, Gegenemotion, Intensität, Verlauf, Körperausdruck |
| Form | Gattung, Rhythmus, Syntax, Rhetorik, Stille, Bildsystem |
| Interpretation | begründete Lesart, klar von Fakten getrennt |
| DNA-Abstraktion | übertragbarer Mechanismus ohne Autorenimitation |
| Offene Fragen | Zuschreibung, Variante, Edition, Rechte, Forschungsbedarf |

## 5. Ausschlüsse

- Keine komplette Übernahme moderner geschützter Werke.
- Keine Autorennachahmung.
- Keine ungeprüften Zitate aus README-Dateien oder Gedicht-Dumps.
- Keine Gleichsetzung von Figur, Erzähler und Autor.
- Keine psychologische Diagnose aus Biografie oder Text.
- Keine Reduktion türkischer Literatur auf Melancholie, Sufismus oder Istanbul.
- Keine Verwendung religiöser, ethnischer oder migrantischer Erfahrung als Dekoration.

## 6. Nächste Recherchewellen

1. Früh- und Altanatolisch: Dede Korkut, Kutadgu Bilig, Yunus Emre, Mevlânâ-Rezeption.
2. Halk/Âşık/Tekke: Karacaoğlan, Pir Sultan Abdal, Köroğlu, Ağıt, Türkü, Cönk und Varianten.
3. Divan: Fuzûlî, Bâkî, Nef'î, Nâbî, Nedîm, Şeyh Gâlib; aruz, mazmun, patronage und Stadt.
4. Tanzimat bis Fecr-i Âti: Reform, Freiheit, Presse, Roman, Theater, neue Öffentlichkeit.
5. Republik und Sozialrealismus: Modernisierung, Dorf, Arbeit, Klasse, Gender, Institution.
6. Moderne Lyrik: Garip, İkinci Yeni, politische Lyrik, Körper, Alltag und Bildsprung.
7. Modernistischer/Postmoderner Roman: Zeit, Gedächtnis, Stadt, fragmentiertes Selbst, Dokument.
8. Frauen-, Minderheiten- und Diasporaliteratur: Mehrsprachigkeit, Zugehörigkeit, Macht und Körper.
9. Satire und Theater: Meddah, Karagöz, Ortaoyunu, Aziz Nesin, modernes Drama.
10. Digital Humanities: OCR, Handschriftenerkennung, TEI, Korpuslinguistik, Emotions- und Netzwerkmodelle.

## 7. Aktueller Befund

GitHub besitzt genügend Material, um einen großen DEJÀ-VU-3-Forschungskorpus aufzubauen, aber nicht genügend Editionssicherheit, um alles ungeprüft als Originalwerk zu übernehmen. Die stärkste Strategie ist: GitHub zur Entdeckung und technischen Erschließung nutzen; Originaltexte, Editionen und biografische Behauptungen anschließend gegen wissenschaftliche Primär- und Sekundärquellen validieren.

## 8. Recherchewellen 1–10: Ergebnisse

### Welle 1 — Frühzeit und epische Überlieferung

| Anker | GitHub-Befund | Nutzbare Mechanismen | Status |
|---|---|---|---|
| Dede Korkut | [DedeKorkutNLP](https://github.com/arch-yunus/DedeKorkutNLP) und weitere kleine Projekte | kollektives Gedächtnis, Prüfung, Ehre, Verwandtschaft, performative Gemeinschaft | das prominenteste Projekt kündigt sein digitales Korpus erst an; noch keine belastbare Textedition |
| Kutadgu Bilig | zahlreiche kapitelweise HTML-Dateien in [bitig/turkbitig](https://github.com/bitig/turkbitig) | Gerechtigkeit, Herrschaft, Vernunft, Genügsamkeit, Gespräch als Erkenntnisform | Text auffindbar, Editionsgrundlage noch offen |
| Divânu Lugâti't-Türk | hauptsächlich Sekundärhinweise und bibliografische Spuren | Sprache als Weltordnung, Dialektvergleich, Sprichwort, kulturelles Gedächtnis | GitHub liefert keine sichere Volltextbasis |
| Yunus Emre | verstreute Dîvân-Dateien und Satzsammlungen; Risâletü'n-Nushiyye kaum belastbar vorhanden | innere Opposition, ethische Veränderung, direkte Anrede, Wiederholung | starke Zuschreibungs- und Variantenprüfung erforderlich |

**Befund:** GitHub ist für frühe Werke ein Wegweiser, ersetzt aber Handschrift, Faksimile oder kritische Edition nicht.

### Welle 2 — Halk, Âşık und Tekke

Die Suche nach Karacaoğlan, Pir Sultan Abdal, Köroğlu, cönk, türkü und deyiş liefert überwiegend Zeitungsartikel, populäre Sammlungen und verstreute Textfragmente. Es wurde kein GitHub-Korpus gefunden, das Autorschaft, Variante, Aufführungskontext und Quelle konsequent gemeinsam dokumentiert.

Kanonische DNA-Felder:

- Stimme und Publikum statt stummer Seitenpoesie,
- Weg, Landschaft, Arbeit, Trennung und Tod,
- hece, durak, nakarat und musikalische Erinnerung,
- individuelles Lied innerhalb kollektiver Überlieferung,
- Dissens, Gewissen und sozialer Preis,
- Körper, Begehren und Vergänglichkeit.

**Schutzregel:** Liedtext oder deyiş niemals allein aufgrund des Stils einer historischen Person zuschreiben.

### Welle 3 — Divan

Gesucht wurden Fuzûlî, Bâkî, Nef'î, Nâbî, Nedîm und Şeyh Gâlib. GitHub ist bei Fuzûlî deutlich stärker als bei den übrigen Dichtern. Für Nef'î, Nâbî und Nedîm erscheinen überwiegend Einzeltexte, Unterrichtsmaterial und Sekundärartikel.

Starke Kandidaten:

- [arch-yunus/fasl-i-fuzuli](https://github.com/arch-yunus/fasl-i-fuzuli): umfangreiche Struktur mit Dîvân, Leylâ vü Mecnûn, Şikâyetnâme, Hadîkatü's-Süedâ, Kommentaren und Bibliografie; jede Passage bleibt editionspflichtig.
- [bitig/turkbitig](https://github.com/bitig/turkbitig): mehrere historische Autoren und Werke, aber ohne durchgehend sichtbaren kritischen Apparat.
- Fihrist- und IslamAnatolia-XML-Daten: Manuskriptmetadaten sind für Zeugen- und Katalogsuche interessant.

DNA-Felder:

- Zeichenarchitektur statt wörtlicher Symbollektüre,
- aşk, hicran, sabır, sitem und ıstırap als unterschiedliche Beziehungen,
- aruz als Bedeutungsdruck, nicht als Ornament,
- Patronage, Rang, Stadt und Gelehrsamkeit,
- tezat, istifham, hitap, tekrar, kinaye und paradox,
- sichtbares Begehren gegen unerreichbare Ordnung.

### Welle 4 — Tanzimat bis Fecr-i Âti

Suchen zu Şinasi, Namık Kemal, Tevfik Fikret und Halit Ziya liefern überwiegend Lernseiten, Zeitungsartikel, Zusammenfassungen und vereinzelte Volltextdateien unbekannter Herkunft.

DNA-Felder:

- Entstehung neuer Öffentlichkeit durch Zeitung, Theater und Roman,
- Freiheit, Gesetz, Familie und öffentliche Moral,
- Reformdruck zwischen alter Ordnung und neuer Person,
- musikalische Prosa, Atmosphäre und psychologische Innenwelt,
- Sprache als politisches und ästhetisches Entscheidungsfeld.

**Risiko:** Gegenwärtige politische Kategorien dürfen nicht ungeprüft rückwärts projiziert werden.

### Welle 5 — Republik, Modernisierung und Sozialrealismus

Suchen zu Halide Edib, Yakup Kadri, Sabahattin Ali, Yaşar Kemal, Orhan Kemal und Fakir Baykurt liefern vor allem Sekundärtexte, Buchzusammenfassungen, Autorenprofile und vereinzelt unerlaubte Textkopien. Moderne Volltexte werden nicht übernommen.

DNA-Felder:

- Modernisierung als ungleiche Erfahrung,
- Geschlecht, Bildung, Nation und Handlungsmacht,
- Dorf, Stadt, Boden, Arbeit, Eigentum und Institution,
- private Verletzung als Folge materieller Bedingungen,
- Landschaft als handelnde Kraft,
- Würde vor Elendsästhetik.

### Welle 6 — Moderne Lyrik und moderner/postmoderner Roman

Bei Nâzım Hikmet, Orhan Veli, İkinci Yeni, Tanpınar und Oğuz Atay finden sich zahlreiche Zitatdateien, Autorenprofile und unsichere Textsammlungen. Sie werden nicht als Editionsquelle genutzt.

DNA-Felder:

- freie Versbewegung: Atem, Zeilensprung, Montage und Skalenwechsel,
- alltägliche Sprache und ironische Entleerung großer Behauptungen,
- Bildsprung und semantische Instabilität,
- innere Zeit, Stadt und Erinnerung,
- fragmentiertes Selbst, Parodie, Dokument und Metafiktion,
- Form verändert Wahrheit, nicht nur Oberfläche.

**Rechteregel:** geschützte moderne Werke nur analysieren, zusammenfassen oder auf abstrakte Mechanismen reduzieren.

### Welle 7 — Frauen-, Minderheiten- und Diasporaliteratur

GitHub-Suchen nach türkischer Frauenliteratur, Deutschland-Diaspora, Armeno-Turkish, Karamanlidika und kurdisch-türkischen Korpora liefern wenig kuratierte Literaturbestände. Armeno-Turkish- und Karamanlidika-Suchen führen überwiegend zu bibliografischen Metadaten oder allgemeinen Sprachdateien.

Erforderliche externe Validierungsachsen:

- Sprache und Schrift strikt trennen,
- Selbstidentifikation und Fremdbezeichnung unterscheiden,
- Migration nicht auf Verlust reduzieren,
- Code-Switching als Beziehung und Machtoperation lesen,
- Körper, Arbeit, Aufenthalt, Familie und Generation berücksichtigen,
- keine Gemeinschaft als homogene Stimme darstellen.

### Welle 8 — Theater, Satire und mündliche Aufführung

Suchen zu Meddah, Karagöz, Ortaoyunu, Aziz Nesin und türkischem Theater ergeben vorwiegend Lehrmaterial, Einzelartikel und allgemeine Korpora. Ein sauber ediertes Aufführungskorpus wurde nicht gefunden.

DNA-Felder:

- direkte Ansprache, Rollenwechsel und Publikumstiming,
- Missverständnis und Registerkonflikt,
- Improvisation und Körperrhythmus,
- institutionelle Regel bis zum absurden menschlichen Preis durchführen,
- Satire richtet sich gegen Macht und System, nicht gegen Schwächere.

### Welle 9 — Emotion und Semantik

Gefunden:

- [StarlangSoftware/TurkishSentiNet](https://github.com/StarlangSoftware/TurkishSentiNet): türkische Sentiment-Ressource; für Polarität und semantische Nachbarschaft geeignet, nicht ausreichend für literarische Emotionsdeutung.
- [bilalabic/awesome-turkish-datasets](https://github.com/bilalabic/awesome-turkish-datasets): katalogisiert weitere Emotions-, Sentiment- und Sprachressourcen.
- ältere Turkish-Sentiment-Datensätze und TS-Corpus-Verweise in türkischen NLP-Sammlungen.

**Methodischer Befund:** Sentiment positiv/negativ kann Hüzün, Hasret, Gurbet, Keder, Efkâr, Hicran oder Sitem nicht ersetzen. Literarische Emotion benötigt Auslöser, Beziehung, Körper, Zeit, Handlung, Gegenemotion und gesellschaftlichen Kontext.

### Welle 10 — OCR, Korpuslinguistik und Digital Humanities

Starke technische Kandidaten:

| Repository | Funktion | Belastbarer Befund |
|---|---|---|
| [Ottoman-NLP/OCR-Transformer](https://github.com/Ottoman-NLP/OCR-Transformer) | Rauschenerkennung und Korrektur lateinisierter osmanischer OCR-Texte | nützlich für Korrekturpipeline; benötigt echtes Ground Truth |
| [Therad445/low-resource-arabic-script-turkic-ocr](https://github.com/Therad445/low-resource-arabic-script-turkic-ocr) | reproduzierbare OCR-Nachkorrektur für arabischschriftliche Turksprachen | besonders wertvoll wegen offen dokumentierter Grenzen: synthetisches Training überträgt sich nicht zuverlässig auf reale osmanische Seiten |
| [OttomanTextAI/OttomanTextAI](https://github.com/OttomanTextAI/OttomanTextAI) | Bildvorverarbeitung, OCR, Transkription und Modernisierung | Human-in-the-loop sinnvoll; README und Projektzustand zeigen noch Prototypcharakter |
| [ahmetax/derlemtr](https://github.com/ahmetax/derlemtr) | türkischer Korpus-/Derlemkontext | für Sprachstatistik prüfen, nicht automatisch Literaturkorpus |
| [deeplearningturkiye/turkce-yapay-zeka-kaynaklari](https://github.com/deeplearningturkiye/turkce-yapay-zeka-kaynaklari) | historisches Verzeichnis türkischer NLP-Ressourcen | Discovery; Aktualität und Links einzeln prüfen |
| [yunusugur/turkey-dh-atlas](https://github.com/yunusugur/turkey-dh-atlas) | DH-Projektatlas | wichtige Weiterleitung zu Archiven und Projekten |

**OCR-Pflichtpipeline:** Faksimile → Roh-OCR → manuelle Kollation → diplomatische Transkription → normalisierte Transkription → Modernisierung → Übersetzung. Keine Stufe darf stillschweigend die vorherige ersetzen.

## 9. Priorisierte Autoren- und Traditionsmatrix

| Cluster | Priorität 1 | Priorität 2 | Hauptfragen |
|---|---|---|---|
| Früh/ethisch | Dede Korkut, Kutadgu Bilig, Yunus Emre | Divânu Lugâti't-Türk, Ahmed Yesevî-Rezeption | Gemeinschaft, Ordnung, innere Veränderung |
| Halk/Âşık | Karacaoğlan, Pir Sultan Abdal | Köroğlu, türkü, ağıt, cönk | Weg, Körper, Dissens, Überlieferung |
| Divan | Fuzûlî, Şeyh Gâlib | Bâkî, Nef'î, Nâbî, Nedîm | Begehren, Zeichen, Rang, Sprache |
| Tanzimat/Übergang | Şinasi, Namık Kemal, Halit Ziya | Tevfik Fikret, Cenap Şahabettin | Öffentlichkeit, Reform, Innenleben |
| Republik/Sozial | Halide Edib, Sabahattin Ali, Yaşar Kemal | Yakup Kadri, Orhan Kemal, Fakir Baykurt | Modernisierung, Materialität, Würde |
| Moderne Lyrik | Nâzım Hikmet, Orhan Veli | İkinci Yeni, Attilâ İlhan | Atem, Alltag, Bild, Politik |
| Moderne Prosa | Tanpınar, Oğuz Atay | Sait Faik, Yusuf Atılgan | Zeit, Stadt, Fragment, Entfremdung |
| Plurale Literatur | Frauen-, Minderheiten- und Diasporastimmen | Karamanlidika, Armeno-Turkish, mehrsprachige Texte | Zugehörigkeit, Schrift, Körper, Macht |
| Aufführung/Satire | Meddah, Karagöz, Ortaoyunu | Nasreddin-Hoca-Tradition, Aziz Nesin | Publikum, Register, Systemabsurdität |

## 10. Integrationsstatus in DEJÀ-VU-3

### Sofort nutzbar

- Epochen- und Traditionsrouting,
- Denkmodus- und Perspektivenkarten,
- Emotionsdifferenzierung,
- Recherche- und Quellenklassen,
- OCR-Stufenmodell,
- Rechte- und Imitationsschutz,
- Autoren-/Werkprofile als Forschungsaufträge.

### Noch gesperrt

- direkte Übernahme ungeprüfter GitHub-Volltexte,
- Zuschreibungen ohne Edition oder Zeugenangabe,
- moderne Gedicht- und Romanvolltexte,
- biografische Kausalbehauptungen ohne B1/B2-Quelle,
- angebliche Originalzitate aus README-Dateien,
- automatische OCR-Modernisierung ohne Vergleich.

## 11. Nächster Arbeitsstand

Die breite GitHub-Discovery ist abgeschlossen. Der nächste Qualitätsgewinn entsteht nicht durch noch mehr unspezifische Treffer, sondern durch verifizierte Einzelprofile. Die erste Profilserie soll Yunus Emre, Fuzûlî, Sabahattin Ali, Tanpınar, Yaşar Kemal und die Begriffsgruppe Hüzün–Hasret–Gurbet abdecken.

## 12. Profil 01 — Yunus Emre

### 12.1 Profilstatus und Quellenlage

| Feld | Befund |
|---|---|
| Profilstatus | quellenkritisches Grundlagenprofil v1.0 |
| historischer Kern | ein Dichter des späten 13. und frühen 14. Jahrhunderts; die verbreitete Datierung 638/1240–41 bis 720/1320–21 beruht auf späteren Dokumenten und bleibt als Forschungsbefund, nicht als lückenlos gesicherte Biografie, zu behandeln |
| sicherster Werkanker | *Risâletü’n-Nushiyye*; der Werkabschluss wird im Text auf 707/1307–08 datiert |
| zweiter Werkkomplex | *Dîvân* beziehungsweise die unter Yunus’ Namen überlieferten Gedichte in Divanhandschriften, cönk, mecmua und mündlicher Aufführung |
| Überlieferungsproblem | kein erhaltenes Autograph und kein zu Lebzeiten angefertigter gesicherter Dîvân; späte Handschriften, Varianten, Abschreibefehler und Gedichte anderer Dichter mit dem Mahlas Yunus |
| Biografie | historische Spuren, spätere Dokumente, Menâkıb und regionale Erinnerung strikt getrennt behandeln |
| Rechte | historische Texte grundsätzlich gemeinfrei; konkrete Editionen, Übersetzungen, Kommentare, Transkriptionen und Digitalisate separat prüfen |
| DEJÀ-VU-3-Freigabe | Mechanismen, Denkbewegungen, Emotionsverläufe, Perspektiven und Formprinzipien verwendbar; keine Stimmkopie, keine ungeprüfte Zuschreibung |

### 12.2 Gesicherter Werkrahmen

#### *Risâletü’n-Nushiyye*

Die Forschung beschreibt das Werk als eine 1307 abgeschlossene, ungefähr 600 Beyt umfassende manzum-mensurische Nasihatnâme. Ein dreizehn Beyt langer aruzgebundener Eingang und eine kurze Prosapassage führen in den eigentlichen Mesnevi-Teil. Für das Profil ist entscheidend: Das Werk macht Ethik nicht zu einer Liste äußerer Gebote, sondern inszeniert den Menschen als Schauplatz widerstreitender Kräfte.

**Textbeobachtung:** innere Zustände werden personifiziert, gegeneinander gestellt und in eine Folge von Erkenntnis, Widerstand und Veränderung überführt.

**Interpretation:** Ethische Entwicklung erscheint als innerer Kampf, der Einsicht, Übung und Neuordnung verlangt; sie geschieht weder durch bloße Stimmung noch durch dekorative Frömmigkeit.

**Abstraktion:** Ein Konflikt wird stark, wenn beide Kräfte im selben Menschen wohnen und jede Handlung einen inneren Preis sichtbar macht.

#### *Dîvân* und Yunus-Tradition

Der Dîvân ist kein stabiler, autorisierter Einzeltext. Handschriften, cönk, mecmua und mündliche Aufführung bewahren unterschiedliche Fassungen. Später wurden Gedichte anderer Dichter mit dem Mahlas Yunus eingemischt. Daher wird künftig jeder verwendete Text mit Edition, Handschrift beziehungsweise Fundzeugnis und Zuschreibungsstatus erfasst.

**Textbeobachtung:** Der überlieferte Komplex verbindet aruz- und hecegebundene Formen, Beyt- und musammatartige Strukturen, direkte Anrede, Wiederholung, religiös-tasavvufische Begriffe sowie eine auf Sprechen, Erinnern und gemeinschaftliches Wiederholen angelegte Klanglichkeit.

**Interpretation:** Die Wirkung entsteht nicht allein durch angeblich „einfache Sprache“. Verständlichkeit, musikalische Wiederkehr, begriffliche Spannung und performative Nähe arbeiten zusammen.

**Abstraktion:** Große Gedanken gewinnen Reichweite, wenn sie in sprechbare Einheiten, klare Beziehungen und veränderte Wiederholungen übersetzt werden.

### 12.3 Historischer und sozialer Horizont

Yunus wird in der Forschungsüberlieferung in das Anatolien des späten 13. Jahrhunderts eingeordnet. Für DEJÀ-VU-3 gilt dabei ein Kausalitätsverbot: politische Unruhe, soziale Umbrüche, religiöse Bewegungen und sprachliche Konstellationen bilden einen möglichen Horizont, erklären aber kein einzelnes Gedicht automatisch.

Seine Entscheidung für Türkisch ist literaturhistorisch bedeutsam, darf jedoch nicht als moderne nationalpolitische Position rückprojiziert werden. Im selben kulturellen Raum hatten Arabisch und Persisch starke religiöse, gelehrte und literarische Funktionen. Türkisch wird bei Yunus zu einer tragfähigen Sprache für Erkenntnis, Unterweisung, Anrede und gemeinschaftliche Aufführung.

### 12.4 Denkarchitektur

| Ebene | Leitfrage | Yunus-Profil | DEJÀ-VU-3-Nutzung |
|---|---|---|---|
| innere Opposition | Welche Kräfte wohnen in derselben Person? | Ego, Zorn, Gier oder Hochmut stehen gegen Geduld, Vernunft, Demut und Liebe | Konflikt nicht auf Held gegen Gegner verkürzen |
| mystisches Denken | Was geschieht mit der Grenze des Ichs? | das Ich wird geprüft, relativiert und auf Beziehung beziehungsweise Einheit hin verändert | Selbstüberschreitung nur mit menschlichem und ethischem Preis |
| paradoxe Erkenntnis | Welche Gegensätze bleiben gleichzeitig wahr? | Verlieren kann Gewinnen, Erniedrigung kann Öffnung, Tod kann Erkenntnis der Vergänglichkeit werden | Paradox aus Handlung entwickeln, nicht als Rätselspruch aufsetzen |
| ethische Kausalität | Wie wird Einsicht zur Praxis? | Erkenntnis verlangt Haltung, Wiederholung, Selbstprüfung und Handeln | Konsequenz im Körper und Alltag zeigen |
| adressiertes Denken | Zu wem spricht der Text? | Selbst, Seele, Suchender, Gemeinschaft oder göttliches Gegenüber | Adressat und Verantwortung vor dem Schreiben bestimmen |
| performatives Wissen | Was verändert das Sprechen? | Wiederholung und Vortrag machen Erkenntnis gemeinschaftlich erinnerbar | Stimme, Pause und Resonanz als Bedeutungsträger einsetzen |

**Leitmodus:** DM-05 Mystisch.  
**Gegenmodus:** DM-14 Verkörpert.  
**Blind-Spot-Test:** Keine körperlose Wohlfühlspiritualität; jede Einsicht braucht Konflikt, Beziehung, Handlung oder Verzicht.

### 12.5 Emotionsarchitektur

| Emotion/Zustand | Auslöser | Gegenkraft | Körper- und Handlungsspur | Schutz vor Vereinfachung |
|---|---|---|---|---|
| Aşk | Trennung, Suche, Anrufung, Erkenntnisdrang | Angst vor Selbstverlust | gerichteter Blick, verkürzter Atem, Annäherung und Rückzug | nicht automatisch romantische Paarliebe |
| Hasret | Distanz zum ersehnten Gegenüber oder Zustand | Hoffnung auf Nähe | horchende Pause, wiederkehrende Anrede, unvollendete Bewegung | nicht mit Hüzün gleichsetzen |
| Hicran | schmerzhafte Trennung | Erinnerung oder Hingabe | stockender Atem, geringe Bewegung, Fixierung auf Abwesenheit | stärker beziehungsgebunden als allgemeine Traurigkeit |
| Sabır | andauernde Prüfung | İsyan, Erschöpfung | regulierter Atem, zurückgenommene Hände, fortgesetzte Handlung | keine Passivität oder Unterwerfung behaupten |
| Tevekkül | Grenze eigener Verfügung | Kontrollwunsch | Spannung lässt nach, Handlung bleibt bewusst | nicht als Untätigkeit darstellen |
| Korku | moralische oder existentielle Gefährdung | Vertrauen und Erkenntnis | Blick prüft, Körper hält inne, Entscheidung wird verzögert | keine pauschalen Schreckensbilder |
| Utanç / Scham | erkannte Verfehlung oder entlarvtes Ego | Annahme und Korrektur | Blickkontakt bricht, Hals und Kiefer spannen, Raum wird verkleinert | nicht mit Schuld identisch setzen |
| Umut / Hoffnung | Möglichkeit innerer Veränderung | Zweifel | Aufmerksamkeit öffnet sich, kleine Vorwärtsbewegung | kein automatisches Lächeln |

Emotionen werden in diesem Profil nicht als Behauptung über die Privatpsychologie des historischen Autors verwendet. Sie beschreiben Textfunktionen und mögliche Verkörperungen in einer neuen Szene.

### 12.6 Rhetorik, Rhythmus und Sprache

| Mechanismus | Funktion | Produktionsregel |
|---|---|---|
| Hitap | setzt Sprecher und Gegenüber in Verantwortung | Adressat eindeutig festlegen |
| Tekrar | macht Prüfung, Erinnerung oder Gebet körperlich hörbar | jede Wiederkehr verändert Druck oder Bedeutung |
| Tezat | lässt zwei aktive Wahrheiten aufeinanderprallen | keine serielle „nicht X, sondern Y“-Formel |
| İstifham | öffnet Selbstprüfung | keine leere Engagement-Frage |
| Personifikation | macht innere Kräfte handlungsfähig | Figur bleibt Mensch, keine abstrakte Allegorienparade |
| Tedric | steigert ethischen Druck stufenweise | Bruch, Pause oder Entscheidung einbauen |
| schlichte Oberfläche, tiefe Relation | verringert lexikalische Hürde, nicht gedankliche Tiefe | keine künstlich-alttürkische Wortdekoration |
| Hece/Aruz-Spannung | verbindet gesprochene Erinnerung mit gelehrter Form | Versmaß nur nach tatsächlicher Prüfung benennen |

**Rhetorische Führung:** RH-03 Hitap.  
**Unterstützung:** RH-04 Tekrar und RH-01 Tezat.  
**Formschutz:** Yunus-DNA entsteht nicht durch alte Wörter, gereimte Lebensweisheiten oder zufällige Sufi-Symbole.

### 12.7 Perspektive und menschliche Darstellung

Primäre Perspektiven sind das **angesprochene Du** und das **sich selbst prüfende Ich**. Eine Perspektive gilt erst dann als verändert, wenn sich mindestens zwei Dimensionen verschieben: Wissen, moralischer Einsatz, Zeit, Sprache, Körperverhalten oder Bildraum.

Für visuelle Umsetzungen wird keine stereotype „Derwisch“-Pose verwendet. Eine Yunus-basierte menschliche Szene zeigt den inneren Wandel konkret:

- Blickziel und Entfernung klar definieren;
- Lidspannung, Brauen, Mund, Kiefer und Schlucken zeitlich aufeinander abstimmen;
- Hände mit fünf anatomisch plausiblen Fingern und tatsächlicher Kontaktphysik zeigen;
- Atem, Schulterstand, Gewichtsverlagerung und folgende Bewegung verbinden;
- Hoffnung, Scham, Angst oder Hingabe nicht allein über Tränen darstellen;
- Kleidung, Armut, Alter oder religiöse Zeichen niemals als moralischen Kurzcode benutzen.

**Bevorzugte Handlungskette:** Absicht → Blick → Atemwechsel → Gewichtsverlagerung → Handentscheidung → Kontakt oder Loslassen → Nachbewegung.

### 12.8 DEJÀ-VU-3-DNA-Karte

```yaml
profile: YUNUS-EMRE-01
status: mechanism_release
human_situation: Eine Person erkennt, dass der bekämpfte Gegner in ihr selbst handelt.
gold:
  mechanism: LM-02 Innere Opposition
  function: Zwei ethische Kräfte bewohnen denselben Menschen.
silver:
  mechanism: RH-03 Hitap
  function: Das Ich spricht sein eigenes verborgenes Gegenüber an.
bronze:
  mechanism: RH-04 Tekrar
  function: Die wiederkehrende Formulierung verändert bei jeder Rückkehr ihre Bedeutung.
thought_mode: DM-05 Mystisch
counter_mode: DM-14 Verkörpert
perspective: BW-03 Angesprochenes Du + selbstprüfendes Ich
emotion_arc: Unruhe → Scham → Widerstand → Einsicht → kleine Handlung
body_arc: Suchblick → Kieferspannung → gehemmte Hand → Atemsenkung → bewusstes Loslassen
form: kurze sprechbare Einheiten; kontrollierte Wiederholung; klare Relation
forbidden: Autorenimitation, angebliches Yunus-Zitat, Sufi-Dekoration, körperlose Weisheit
```

### 12.9 Transformationsformel

**Person → konkrete Pflicht → innerer Gegner → angesprochenes Selbst → körperlicher Widerstand → wiederkehrende Formulierung → veränderte Entscheidung.**

Diese Formel darf auf heutige Situationen übertragen werden: Familie, Arbeit, Schuld, Besitz, Stolz, Schweigen oder Versöhnung. Der historische religiöse Kontext wird nicht als Kulisse benutzt. Eine neue Geschichte muss ihre eigene soziale Wirklichkeit und eine eigene Erkenntnis besitzen.

### 12.10 Qualitäts- und Quellenampel

| Bereich | Ampel | Begründung |
|---|---|---|
| Existenz und grobe Zeitstellung | 🟡 | starker Forschungskonsens, aber späte Dokumentation |
| *Risâletü’n-Nushiyye* als Werkanker | 🟢 | Werkdatierung und Editionsgeschichte gut dokumentiert |
| einzelne Dîvân-Gedichte | 🟡/🔴 | nur nach Editions- und Variantenprüfung |
| Tapduk-/Hacı-Bektaş-Biografie | 🟡 | als Menkıbe und Rezeptionsgeschichte nutzbar, nicht ungeprüft als Lebensfakt |
| Grab- und Herkunftsort | 🟡 | mehrere konkurrierende Erinnerungsorte |
| abstrakte Mechanismen | 🟢 | nach klarer Trennung von Quelle und neuer Transformation |
| angebliche Internetzitate | 🔴 | ohne Edition und Textzeugnis gesperrt |

### 12.11 Verwendete Kernquellen

1. [TDV İslâm Ansiklopedisi: Yûnus Emre](https://islamansiklopedisi.org.tr/yunus-emre) — biografische Forschungsfragen, Werke, Handschriften, Metrik und Editionsgeschichte; B1/B2.
2. [Türk Edebiyatı İsimler Sözlüğü: Yunus Emre](https://teis.yesevi.edu.tr/madde-detay/yunus-emre-yunus-kul-yunus-asik) — besonders wichtig für die Trennung von historischer Person, Menkıbe, folklorischer Variation und Yunus-Tradition; B1/B2.
3. Genannte kritische Editionen als nächste A2-Prüfstufe: Mustafa Tatcı, *Yunus Emre Dîvânı* und *Risâletü’n-Nushiyye*; Umay Günay/Osman Horata, *Risâletü’n-Nushiyye*; konkrete Textzitate erst nach Einsicht in die jeweilige Ausgabe.

### 12.12 Offene Prüfaufträge

- drei belastbare Textanker aus *Risâletü’n-Nushiyye* editionsgenau kollationieren;
- drei Dîvân-Gedichte über mindestens zwei Zeugen beziehungsweise eine kritische Edition vergleichen;
- Yunus Emre und Âşık Yunus textkritisch trennen;
- Türkisch–Deutsch-Übertragung in philologische, literarische und adaptive Fassung aufteilen;
- anschließend einen eigenständigen DEJÀ-VU-3-Testtext ohne Namensnennung und ohne Stimmimitation erzeugen.

**Profilentscheidung:** Yunus Emre wird ab sofort nicht als Stilvorlage, sondern als geprüfte Mechanismengruppe geführt: innere Opposition, adressierte Selbstprüfung, veränderte Wiederholung, verkörperte ethische Entscheidung und gemeinschaftlich sprechbare Form.

## 13. Profil 02 — Fuzûlî

### 13.1 Profilstatus und Quellenlage

| Feld | Befund |
|---|---|
| Profilstatus | quellenkritisches Grundlagenprofil v1.0 |
| Identität | Mehmed b. Süleyman, bekannt unter dem Mahlas Fuzûlî; Dichter und Prosaschriftsteller des 16. Jahrhunderts |
| Zeit | das häufig genannte Geburtsjahr 888/1483 ist erschlossen, nicht urkundlich zweifelsfrei; Tod 963/1556 während der Pest im Raum Bagdad/Kerbela |
| Geografie | Irakischer Kulturraum; Bagdad, Hille, Necef und Kerbela sind biografisch und literarisch relevant; der genaue Geburtsort bleibt umstritten |
| Sprachen | Türkisch, Persisch und Arabisch; Sprachwahl, Gattung und Publikum müssen pro Werk getrennt werden |
| politische Horizonte | Akkoyunlu-, Safevî- und osmanische Herrschaft; Patronage und Machtwechsel bilden reale Bedingungen, erklären aber kein Gedicht allein |
| Hauptanker | Türkischer *Dîvân*, *Leylâ vü Mecnûn*, *Hadîkatü’s-Süedâ*, fünf überlieferte Briefe einschließlich der sogenannten *Şikâyetnâme* |
| weitere Anker | *Beng ü Bâde*, *Rind ü Zâhid*, *Sıhhat u Maraz*, *Matlaʿu’l-İʿtikād*, persischer Dîvân und arabische Kasiden |
| Editionslage | zahlreiche Handschriften und historische Drucke; für den Türkischen Dîvân ist der vergleichende Text von Kenan Akyüz u. a. ein zentraler Prüfanker |
| DEJÀ-VU-3-Freigabe | Begehren, Distanz, Zeichenarchitektur, paradoxe Erkenntnis, lyrische Verdichtung und institutionelle Enttäuschung auf Mechanismenebene |

### 13.2 Historischer und materieller Horizont

Fuzûlî lebte in einem politisch wechselhaften Raum und suchte wiederholt die Anerkennung von Herrschern und Amtsträgern. Kasiden und Briefe zeigen, dass Dichtung auch innerhalb von Patronage, Versorgung, Amt und bürokratischer Abhängigkeit entstand. Die *Şikâyetnâme* wird deshalb nicht als zeitloser Internetspruch über „Bestechung“ behandelt, sondern als literarisch gestalteter Brief innerhalb einer konkreten Verwaltungs- und Patronagesituation.

Die Überlieferung, er habe sein ganzes Leben lang keinen zufriedenstellenden Patron gefunden, ist als literaturhistorische Deutung zu prüfen. Sicherer ist: Seine Texte dokumentieren wiederholte Widmungen, Erwartung, Nähe zur Macht und empfundene mangelnde Anerkennung. Daraus folgt keine einfache Psychobiografie, sondern eine produktive Spannung zwischen dichterischem Rang und materieller Abhängigkeit.

### 13.3 Gesicherter Werkrahmen

#### Türkischer *Dîvân*

Der Dîvân beginnt mit einer Prosavorrede über Dichtung und Wissen. Die vergleichende Ausgabe von Kenan Akyüz und Mitarbeitern verzeichnet 42 Kasiden, 302 Gazelen, ein Müstezâd, zwölf Musammatformen, 42 Kıtʿa und 72 Rubâʿî.

**Textbeobachtung:** konkrete Dinge öffnen mehrere Bedeutungsschichten: Natur, gesellschaftliche Beziehung, Wissensgebiet, Liebe und tasavvufische Lesbarkeit können im selben Beyt zusammenwirken.

**Interpretation:** Verdichtung entsteht nicht durch möglichst viele alte Wörter, sondern durch kontrollierte Beziehungen zwischen Zeichen. Die scheinbare Leichtigkeit an der Oberfläche kann eine präzise gebaute Tiefenstruktur tragen.

**Abstraktion:** Ein Bild wird stark, wenn es gleichzeitig eine sichtbare Handlung, eine emotionale Beziehung und eine zweite Erkenntnisebene trägt.

#### *Leylâ vü Mecnûn*

Das um 1535 entstandene Mesnevi wurde Üveys Paşa gewidmet und zählt zu den wirkungsmächtigsten türkischen Fassungen des Stoffes. Es darf weder als bloße Biografie Fuzûlîs noch ausschließlich als mystische Allegorie gelesen werden.

**Textbeobachtung:** Das Begehren verändert Mecnûns Verhältnis zu Körper, Gemeinschaft, Sprache, Landschaft und dem zunächst begehrten Gegenüber. Distanz ist keine leere Verzögerung, sondern eine formende Kraft.

**Interpretation:** Erfüllung würde den Zustand beenden, durch den der Liebende sich selbst und die Welt neu wahrnimmt. Der Schmerz wird damit nicht automatisch verherrlicht; entscheidend ist, was er erkennt, zerstört oder unmöglich macht.

**Abstraktion:** Ein Wunsch kann seinen Gegenstand überleben und zur Identität werden. Die dramatische Frage lautet dann nicht nur „Bekommt die Person, was sie will?“, sondern „Wer wäre sie ohne dieses Wollen?“

#### *Hadîkatü’s-Süedâ*

Dieses prosaische, durch Verse unterbrochene Maktelwerk gestaltet die Leiden und den Tod Husains in Kerbela und hatte starke Wirkung in schiitischen sowie alevitisch-bektaschitischen Rezeptionsräumen.

**Schutzregel:** Religiöse Trauer, Zeugenschaft und gemeinschaftliches Gedächtnis dürfen nicht als romantische Liebesästhetik oder Marketingkulisse verwendet werden.

**Abstraktion:** Übertragbar sind nur allgemeine Mechanismen wie Zeugenschaft, kollektives Erinnern und die ethische Frage, was eine Gemeinschaft nicht vergessen darf. Der sakrale Inhalt selbst bleibt kontextgebunden.

#### Briefe und *Şikâyetnâme*

Von Fuzûlî sind fünf publizierte Briefe bekannt. Der bekannteste, an Nişancı Celâlzâde Mustafa Çelebi gerichtet, wird als *Şikâyetnâme* bezeichnet.

**Textbeobachtung:** Erwartung trifft auf Verwaltungswirklichkeit; rhetorische Präzision lässt die Institution ihre eigene Absurdität offenlegen.

**Interpretation:** Sitem wird hier sozial: Die Verletzung kommt nicht nur von einer geliebten Person, sondern aus dem Missverhältnis zwischen zugesagter Anerkennung und tatsächlicher Behandlung.

**Abstraktion:** Institutionelle Satire entsteht, wenn eine Regel, ein Versprechen oder ein Verfahren bis zu seinen menschlichen Kosten verfolgt wird.

### 13.4 Registertrennung

| Register | Beziehung | Hauptemotion | Erkenntnisrisiko | Schutz |
|---|---|---|---|---|
| âşıkane Gazel | Liebender–Geliebte/Geliebter | Aşk, Hicran, Hasret, Sitem | jeden Geliebten vorschnell göttlich lesen | Werk und Beyt einzeln prüfen |
| *Leylâ vü Mecnûn* | Person–Begehren–Gemeinschaft | Sehnsucht, Trennung, Entgrenzung | Schmerz romantisieren | Verlust, Wahl und Preis mitführen |
| tasavvufische Lesart | Ich–Wahrheit/Einheit | Hingabe, Unruhe, Erkenntnis | universelle Wellness-Spiritualität | religiös-intellektuellen Kontext bewahren |
| *Hadîkatü’s-Süedâ* | Zeuge–Leid–Gemeinschaft | Yas, Keder, Treue | sakrale Trauer ästhetisch ausschlachten | keine kommerzielle Transformation |
| *Şikâyetnâme* | Dichter–Institution | Sitem, gekränkte Würde, Ironie | bloßen Meme-Satz extrahieren | Briefsituation und Machtverhältnis erhalten |
| Kaside | Dichter–Patron | Hoffnung, Lob, Erwartung, Ambivalenz | Lob mit privater Überzeugung gleichsetzen | Gattung und Patronage beachten |

### 13.5 Denkarchitektur

| Ebene | Operation | Fuzûlî-Profil | DEJÀ-VU-3-Nutzung |
|---|---|---|---|
| Zeichenarchitektur | Sichtbares öffnet Unsichtbares | Gegenstand, Naturbild und Beziehung tragen mehrere Ebenen | ein Bild, maximal drei notwendige Bedeutungsschichten |
| paradoxe Erkenntnis | Gegensätze bleiben wirksam | Nähe kann Distanz vertiefen; Schmerz kann Wissen erzeugen | Widerspruch aus Handlung statt Spruchform |
| Begehren als Motor | Mangel organisiert Wahrnehmung | das Unerreichte verändert Identität und Sprache | Wunsch, Hindernis, Preis und Gegenemotion abbilden |
| relationale Wahrheit | Bedeutung liegt zwischen Zeichen | Geliebter, Rivale, Bote, Träne, Wunde und Raum definieren einander | Symbol niemals isoliert einsetzen |
| Wissen und Dichtung | Gefühl wird durch Form präzisiert | Gelehrsamkeit trägt die Konstruktion, ohne Lyrik zu ersetzen | Recherche unter der Oberfläche, Mensch im Vordergrund |
| materielle Gegenkraft | Kunst trifft Institution | Patronage und Bürokratie begrenzen dichterische Autonomie | soziale Ursache in private Emotion einschreiben |

**Leitmodus:** DM-06 Paradoxal.  
**Gegenmodus:** DM-09 Materiell-sozial.  
**Blind-Spot-Test:** Schmerz ist weder automatisch Wahrheit noch künstlerischer Adel; sichtbar werden müssen Ursache, Preis, Wahl und mögliche Selbsttäuschung.

### 13.6 Emotionsarchitektur

| Zustand | Beziehung und Auslöser | Gegenemotion | Körper-/Handlungsspur | Abgrenzung |
|---|---|---|---|---|
| Aşk | starke Ausrichtung auf Person, Wahrheit oder Ideal | Furcht vor Verlust des Selbst | Blick haftet, Atem beschleunigt oder hält, Körper orientiert sich zum Gegenüber | Register nicht vorab festlegen |
| Hicran | vollzogene oder dauerhafte Trennung | Hoffnung auf Wiederbegegnung | verlangsamte Bewegung, Mundspannung, Hand stoppt vor Kontakt | stärkerer Trennungsriss als allgemeine Trauer |
| Hasret | Entfernung und fortdauernder Wunsch | Imagination von Nähe | Aufmerksamkeit sucht Spuren, Körper wiederholt Wege oder Rituale | kann Zukunft enthalten |
| Sitem | Beziehung verletzt eine Erwartung, ohne dass Bindung endet | Stolz, Liebe oder Hoffnung | kontrollierte Stimme, präzise Geste, zurückgehaltene Hand | keine reine Wut; Adressat bleibt wichtig |
| Istırap | anhaltender Schmerz mit Bedeutungsdruck | Erkenntnis oder Erschöpfung | Atemrhythmus bricht, Schlaf und Routine werden schwer | nicht verherrlichen |
| Keder | schwerer, anhaltender Gram | Pflicht oder Erinnerung | niedrige Initiation, langsame Aufmerksamkeit, mechanische Tätigkeit | nicht identisch mit Hüzün |
| Onur | Anspruch auf angemessene Behandlung | Abhängigkeit | aufrechtere Haltung bei kontrolliertem Gesicht; Hände begrenzen Kontakt | nicht mit Hochmut verwechseln |
| İsyan | Grenze des Erträglichen oder der Ordnung | Bindung, Angst, Sabır | Atemdruck, genaue Bewegung, Stimme gewinnt Kante | Faust und Schrei nicht zwingend |

Emotionen beschreiben Funktionen im Werk und mögliche neue Verkörperungen. Sie sind keine Diagnose des historischen Autors.

### 13.7 Rhetorik, Klang und Form

| Mechanismus | Wirkung | Produktionsregel |
|---|---|---|
| Tezat | hält Lust und Schmerz, Nähe und Ferne gleichzeitig aktiv | beide Seiten müssen reale Folgen besitzen |
| Paradox | macht Erkenntnis aus unauflösbarer Spannung | kein dekoratives Rätsel |
| Hitap | bindet Klage, Bitte oder Vorwurf an ein Gegenüber | Beziehung und Machtgefälle definieren |
| İstifham | verwandelt Aussage in Prüfung des Anderen und des Selbst | keine TikTok-Scheinfrage |
| Tekrar/Redif | lässt dieselbe Beziehung mit verändertem Druck zurückkehren | Bedeutung muss sich pro Wiederkehr verschieben |
| Mübalağa | vergrößert die emotionale Wirklichkeit | körperlich oder relational erden |
| Kinaye/Ironie | legt institutionelle oder soziale Doppeldeutigkeit frei | nicht gegen Schwächere richten |
| Mazmun-Netz | verbindet kulturell lesbare Zeichen | Zeichenbeziehung erklären, keine Symbolinventur |
| Aruz und Klang | erzeugen Erwartung, Druck, Rückkehr und musikalische Erinnerbarkeit | konkretes Gedicht vor metrischer Behauptung scannen |

**Rhetorische Führung:** RH-09 Paradox.  
**Unterstützung:** RH-01 Tezat und RH-03 Hitap.  
**Formschutz:** Keine Pseudo-Divan-Dichtung aus Rosen, Nachtigallen, Wein und Wunden ohne notwendige Relation.

### 13.8 Perspektive und menschliche Darstellung

Die stärkste Perspektive ist das **unmittelbare Ich**, das ein abwesendes oder unerreichbares **Du** anspricht. Als Gegenperspektive dient das **abwesende Gegenüber**, dessen Nichtanwesenheit Handlung, Raum und Sprache organisiert.

Eine Fuzûlî-basierte Szene zeigt keinen dekorativ leidenden „orientalischen Dichter“. Sie zeigt eine konkrete Person in einer konkreten Beziehung:

- Blick richtet sich auf eine reale Spur, Tür, Nachricht, Hand oder leeren Platz;
- Augenfeuchtigkeit nur bei plausibler Lichtquelle und Physiologie;
- Lid-, Brauen-, Mund- und Kieferspannung gehören zum selben Moment;
- Hand nähert sich, hält inne, faltet, schreibt, löscht oder gibt etwas zurück;
- Brustkorb, Hals und Schultern zeigen den Atemdruck;
- Gewichtsverlagerung entscheidet zwischen Annäherung und Rückzug;
- Schmerz verändert eine Handlung, nicht nur das Gesicht.

**Bevorzugte Bewegungskette:** Spur erkennen → Blick fixiert → Atem stoppt → Hand beginnt → Erinnerung oder Stolz hemmt → Kontakt bleibt aus → Körper trägt die Entscheidung weiter.

### 13.9 DEJÀ-VU-3-DNA-Karte

```yaml
profile: FUZULI-02
status: mechanism_release
human_situation: Eine Person hält an einem Wunsch fest, obwohl sie erkennt, dass genau dieser Wunsch sie verändert und bindet.
gold:
  mechanism: LM-03 Zeichenarchitektur
  function: Eine sichtbare Spur trägt Beziehung, Verlust und Erkenntnis zugleich.
silver:
  mechanism: RH-09 Paradox
  function: Das Unerreichte verletzt die Person und erhält gleichzeitig ihr inneres Bild.
bronze:
  mechanism: RH-03 Hitap
  function: Das abwesende Gegenüber bleibt durch direkte Ansprache handlungswirksam.
thought_mode: DM-06 Paradoxal
counter_mode: DM-09 Materiell-sozial
perspective: BW-01 unmittelbares Ich + BW-12 abwesende Person
emotion_arc: Begehren → Hoffnung → Hicran → Sitem → Erkenntnis ohne sichere Erlösung
body_arc: Fixierter Blick → Atemstopp → beginnende Handbewegung → Hemmung → Rückzug oder bewusstes Ablegen
form: verdichtete Relation; veränderte Wiederkehr; klare Gegenkraft; Schluss öffnet den Anfang neu
forbidden: Autorenimitation, ungeprüftes Zitat, Schmerzromantik, beliebige Sufi-Deutung, Symbolhäufung
```

### 13.10 Transformationsformeln

**Liebes-/Beziehungsformel:** Person → unerreichbares Gegenüber → konkrete Spur → Hoffnung → gescheiterter Kontakt → Sitem → Erkenntnis über den eigenen Wunsch.

**Soziale Formel:** zugesagte Anerkennung → institutionelles Verfahren → wiederholte Verzögerung → kontrollierte Beschwerde → Regel offenbart menschlichen Preis.

**Zeichenformel:** sichtbares Detail → erste Beziehung → widersprechende zweite Bedeutung → Körperreaktion → Entscheidung verändert das Detail.

Diese Formeln dürfen auf heutige Beziehungen, Familie, Arbeit, Bürokratie, Status, digitale Nähe oder Erinnerung übertragen werden. Sie erzeugen keine Fuzûlî-Kopie, sondern neue menschliche Situationen.

### 13.11 Qualitäts- und Quellenampel

| Bereich | Ampel | Begründung |
|---|---|---|
| Name, Epoche und mehrsprachiges Werk | 🟢 | durch akademische Nachschlagewerke und Werküberlieferung belastbar |
| genaues Geburtsjahr und Geburtsort | 🟡 | erschlossen beziehungsweise umstritten |
| Tod 1556 während der Pest | 🟢/🟡 | stark überliefert; genaue Grabbehauptungen vorsichtig behandeln |
| Türkischer *Dîvân* | 🟢 | breiter Handschriftenbestand und vergleichende Edition vorhanden |
| *Leylâ vü Mecnûn* | 🟢 | amtliche Editionen und starke Forschungslage |
| *Sohbetü’l-Esmâr* | 🟡/🔴 | Zuschreibung nicht abschließend gesichert |
| genaue religiöse Zugehörigkeit | 🟡 | Forschungsdebatte; nicht vereinfachen |
| *Şikâyetnâme*-Internetzitate | 🔴 bis Editionsprüfung | virale Verkürzung ersetzt keinen Brieftext |
| Mechanismenübertragung | 🟢 | bei Registertrennung und ohne Stimmimitation |

### 13.12 Verwendete Kernquellen

1. [TDV İslâm Ansiklopedisi: Fuzûlî](https://islamansiklopedisi.org.tr/fuzuli) — Biografie, Debatten, Werk- und Editionsgeschichte, Mehrschichtigkeit und Rezeption; B1/B2.
2. [Türk Edebiyatı İsimler Sözlüğü: Fuzûlî](https://teis.yesevi.edu.tr/madde-detay/fuzuli-mdbir//yumni-osmanzade-seyhzade-mehmed) — historische Kontexte, Patronage, Werkbestand und poetologische Einordnung; B1/B2.
3. [T.C. Kültür ve Turizm Bakanlığı: Fuzûlî – Leylâ ve Mecnûn](https://ekitap.ktb.gov.tr/TR-78423/fuzuli---leyla-ve-mecnun.html) — amtlicher Zugang zu Einleitung und Text; A2-Prüfpfad.
4. [Türkiye Yazma Eserler Kurumu: Leylâ vü Mecnûn](https://ekitap.yek.gov.tr/Uploads/ProductsFiles/d42e8ffd-92e1-466b-8ce7-7d7e80811fc0.pdf) — aktuelle wissenschaftliche Editionsressource; A2-Prüfpfad.
5. Kenan Akyüz u. a., *Fuzûlî Divanı*, Ankara 1990 — zentraler vergleichender Dîvân-Text; vor exakten Zitaten direkt konsultieren.

### 13.13 Offene Prüfaufträge

- drei Gazelen aus der Akyüz-Ausgabe einschließlich aruz, redif und Varianten kollationieren;
- einen Abschnitt aus *Leylâ vü Mecnûn* philologisch, literarisch und adaptiv getrennt übertragen;
- das verbreitete *Şikâyetnâme*-Zitat gegen vollständigen Brief und Edition prüfen;
- *Hadîkatü’s-Süedâ* ausschließlich als religiös-historischen Werkraum vertiefen;
- anschließend einen eigenständigen DEJÀ-VU-3-Testtext mit Sitem und institutioneller Gegenkraft erstellen.

**Profilentscheidung:** Fuzûlî wird als geprüfte Mechanismengruppe geführt: Begehren als Wahrnehmungsmotor, Hicran als Beziehungsriss, Sitem als gebundener Vorwurf, mehrschichtige Zeichenarchitektur, paradoxe Erkenntnis und die materielle Gegenkraft von Patronage und Institution.

## 14. GitHub Research Phase 2 — gezielte Quellen-, Rechte- und Editionsprüfung

### 14.1 Auftrag und Prüfregel

Phase 2 ersetzt die breite Treffermenge durch eine entscheidungsfähige Ampel. Geprüft werden Repository, konkrete Datei, Commit, behauptete Herkunft, Edition beziehungsweise Textzeuge, Lizenz, enthaltene Fremdtexte und zulässige DEJÀ-VU-3-Nutzung.

**Wichtig:** Eine Softwarelizenz des Repositorys lizenziert nicht automatisch darin enthaltene literarische Texte, Editionen, Übersetzungen, Bilder oder Kommentare. Für jede Inhaltsschicht bleibt eine eigene Rechte- und Herkunftsprüfung erforderlich.

| Ampel | Bedeutung | Nutzung |
|---|---|---|
| 🟢 | Identität, Herkunft und Lizenz für den konkreten Zweck belastbar | gemäß Lizenz und Quellenklasse nutzbar |
| 🟡 | technisch oder bibliografisch nützlich, aber Editions-/Rechtekette teilweise offen | nur Discovery, Methode oder nach zusätzlicher Prüfung |
| 🔴 | geschützter Volltext, fehlende Herkunft, falsche Zuschreibung oder unklare Rechte | nicht übernehmen und nicht zum Training/Imitieren verwenden |

### 14.2 Ergebnis der gezielten Suchachsen

| Suchachse | GitHub-Befund | Entscheidung |
|---|---|---|
| Yunus Emre | Treffer konzentrieren sich weiterhin auf DergiPark-Dumps, Unterrichtsdaten und verstreute Texte; kein neu entdeckter, sauber dokumentierter A1/A2-Dîvân oder vollständiger editionskritischer *Risâletü’n-Nushiyye*-Datensatz | 🟡 Discovery; Textzitate nur aus externer kritischer Edition |
| Fuzûlî | *arch-yunus/fasl-i-fuzuli* bietet ein großes digitales Külliyat mit Texten, Kommentaren, Wörterbuch, JSON und Werkzeugen | 🟡 starkes Navigations- und Analysehilfsmittel, aber keine automatische kritische Edition |
| Sabahattin Ali | mehrere Repositories enthalten den vollständigen Text von *Kürk Mantolu Madonna* oder große Textsegmente; Herkunft und Rechtekette sind teilweise nicht ausgewiesen | 🔴 Volltexte sperren; nur rechtmäßige Metadaten und wissenschaftliche Sekundäranalyse |
| Tanpınar | Treffer bestehen überwiegend aus Zeitungsarchiven, Notizen, Zusammenfassungen und vereinzelten Datendumps; kein belastbarer literarischer Forschungskorpus | 🟡/🔴 nicht als Werktext verwenden |
| Yaşar Kemal | kein kuratierter GitHub-Korpus mit überprüfbarer Rechte- und Editionskette gefunden | 🔴 für Volltext; externe B1/B2-Quellen für Profil |
| Hüzün–Hasret–Gurbet | Polaritätslexika und allgemeine Wortlisten existieren, aber kein ausreichend kontextualisiertes literarisches Emotionskorpus dieser Begriffsgruppe | 🟡 lexikalische Nachbarschaft, keine literarische Emotionsentscheidung |
| Osmanische OCR/TEI | mehrere reproduzierbare OCR- und Nachkorrekturprojekte, aber weiterhin kaum durchgängig verknüpfte Faksimile–Ground-Truth–TEI–Editionsketten | 🟡 technische Pipeline freigegeben, Textautorität nicht |
| Karamanlidika/Armeno-Turkish | kombinierte Suche liefert keinen belastbaren kuratierten GitHub-Literaturkorpus | 🟡 externe Archive und Kataloge erforderlich |
| Deutschland-Diaspora | Treffer überwiegend generische Sprachdaten, Zeitungsarchive und irrelevante Dateien | 🟡 GitHub derzeit schwach; externe Literatur- und Migrationsforschung |
| Meddah/Karagöz/Ortaoyunu | überwiegend Presseartikel, Lernmaterial und vereinzelte Erwähnungen; kein ediertes Aufführungskorpus | 🟡 Aufführungsmechanismen nur aus Fachquellen validieren |

### 14.3 Repository-Ampel

| Repository | geprüfter Befund | Lizenz-/Rechterisiko | Ampel | Freigabe |
|---|---|---|---|---|
| [arch-yunus/fasl-i-fuzuli](https://github.com/arch-yunus/fasl-i-fuzuli) | 2026 angelegtes digitales Külliyat; README, Transkriptionen, Kommentare, Zitate, JSON und Python-Werkzeuge; Repository-Metadaten nennen MIT | MIT deckt den Code ab; Herkunft einzelner Texte, Übersetzungen und zugeschriebener Sekundärzitate muss separat geprüft werden | 🟡 | Navigation, Dateistruktur, Suchwerkzeuge und Forschungsfragen; kein Zitat ohne A2-Abgleich |
| [bsenurbas/ai-yazar-tespit](https://github.com/bsenurbas/ai-yazar-tespit) | enthält vollständige moderne literarische Texte als Rohdaten, darunter *Kürk Mantolu Madonna* | keine Repository-Lizenz sichtbar; literarische Volltexte mit ungeklärter Rechtekette | 🔴 | weder Textübernahme noch Training noch Stilprofil daraus |
| [Kon-tiki-ship/tasvir-bankasi-turkish-literary-annotation-pipeline](https://github.com/Kon-tiki-ship/tasvir-bankasi-turkish-literary-annotation-pipeline) | literarische Annotations- und Probe-Dateien, darunter Sabahattin-Ali-bezogene Datensätze | Annotation kann geschützte Textsegmente enthalten; Herkunft, Umfang und Lizenz pro Datei prüfen | 🟡/🔴 | Annotationsschema eventuell nutzbar; Inhaltsdaten bis Rechteprüfung gesperrt |
| [Ottoman-NLP/OCR-Transformer](https://github.com/Ottoman-NLP/OCR-Transformer) | Pipeline zur Erkennung und Korrektur von OCR-Rauschen in lateinisierten osmanischen Texten | Modell- und Codefreigabe ersetzt kein Ground Truth und keine Textrechte | 🟡 | technische Versuchspipeline; Ausgabe immer manuell kollationieren |
| [Therad445/low-resource-arabic-script-turkic-ocr](https://github.com/Therad445/low-resource-arabic-script-turkic-ocr) | reproduzierbare Nachkorrektur; dokumentiert selbst die schwache Übertragung synthetischen Trainings auf reale osmanische Seiten | kein Produktionsbeweis; Datenherkunft und Lizenz je Bestandteil prüfen | 🟡 | besonders als Fehler- und Grenzmodell wertvoll |
| [OttomanTextAI/OttomanTextAI](https://github.com/OttomanTextAI/OttomanTextAI) | Vorverarbeitung, OCR, Transkription und Modernisierung in einer Pipeline | LLM-Modernisierung kann Bedeutung und Textidentität verändern | 🟡 | Human-in-the-loop; jede Stufe getrennt speichern |
| [StarlangSoftware/TurkishSentiNet](https://github.com/StarlangSoftware/TurkishSentiNet) | HisNet mit rund 76.825 manuell als positiv, negativ oder neutral annotierten Synsets; Repository-Metadaten nennen GPL-3.0 | Polarität ist keine differenzierte literarische Emotion; Lizenzpflichten für Code/Daten beachten | 🟢/🟡 | semantische Nachbarschaft und Polarität; keine Entscheidung über Hüzün, Hasret oder Gurbet |
| [arch-yunus/DedeKorkutNLP](https://github.com/arch-yunus/DedeKorkutNLP) | NLP-Projekt mit MIT-Metadaten und programmatischer Vision | angekündigte beziehungsweise technische Korpusfunktion ist keine ausgewiesene kritische Dede-Korkut-Edition | 🟡 | Architekturideen; Originaltext nur aus gesicherter Edition |
| [Alperencode/DergiPark-Data-Set](https://github.com/Alperencode/DergiPark-Data-Set) | große Artikelsammlung mit relevanten Sekundärtreffern | Artikelidentität, Version, Rechte und Extraktionsqualität einzeln prüfen | 🟡 | Fundstellen entdecken, anschließend Originalartikel beziehen |
| [bitig/turkbitig](https://github.com/bitig/turkbitig) | umfangreiche historische Textsammlung | Editionsapparat und Quellenkette nicht durchgängig sichtbar | 🟡 | Suche und Variantenhinweise; kein automatischer A1/A2-Status |

### 14.4 Rechte- und Lizenzmatrix

| Situation | Entscheidung |
|---|---|
| gemeinfreier Autor + moderne Edition | Autor ist gemeinfrei, Edition/Kommentar kann geschützt sein; nur geprüfte Textgrundlage verwenden |
| MIT/GPL-Repository + fremder Roman | Softwarelizenz legalisiert den Romantext nicht |
| Annotation + kurze Textsegmente | Umfang, Zweck, Quelle, Lizenz und mögliche Reproduzierbarkeit prüfen |
| README-Zitat + berühmter Name | bis Abgleich mit Edition oder Originalquelle Klasse D |
| OCR-Ausgabe eines Faksimiles | Ausgabe bleibt Hypothese; Faksimile und Korrekturprotokoll erforderlich |
| modernisierte osmanische Fassung | als Bearbeitung kennzeichnen; niemals als Originaltext ausgeben |
| wissenschaftlicher Artikel-Dump | nur Suchindex; zitierfähige Originalpublikation mit Metadaten beschaffen |

### 14.5 Fehlzuschreibungs- und Risikoregister

1. **README-Autoritäten:** Das Fuzûlî-Külliyat führt zahlreiche lange Aussagen unter bekannten Namen an. Ohne genaue Werk-, Seiten- und Editionsangabe bleiben diese Aussagen ungeprüft und dürfen nicht als Zitate in DEJÀ-VU-3 gelangen.
2. **Moderne Volltextdaten:** Das Auffinden eines Romans in einem öffentlichen Repository bedeutet weder Gemeinfreiheit noch Nutzungserlaubnis.
3. **Yunus-Variation:** Texte mit dem Mahlas Yunus können Yunus Emre, Âşık Yunus oder späteren Yunus-Traditionen angehören.
4. **Maktel und religiöse Texte:** Textidentität, Konfessionsgeschichte, Edition und gemeinschaftliche Funktion müssen vor jeder Interpretation getrennt werden.
5. **Sentimentverkürzung:** Positiv/negativ/neutral darf keine literarische Emotionskarte ersetzen.
6. **OCR-Scheinpräzision:** Flüssige Modernisierung kann philologisch falsch sein, selbst wenn sie sprachlich überzeugend wirkt.

### 14.6 Neue Integrationsfreigaben

#### Sofort freigegeben

- Repository-Ampel als Pflichtfeld jedes Werkprofils;
- getrennte Lizenzprüfung für Code, Datensatz, Originaltext, Edition, Übersetzung und Bild;
- Commit-URL als unveränderlicher GitHub-Fundnachweis;
- rote Sperre für moderne Volltexte ohne nachvollziehbare Rechtekette;
- Nutzung von HisNet ausschließlich als lexikalische Hilfsschicht;
- OCR-Projekte als technische Werkzeuge innerhalb der bestehenden Human-in-the-loop-Pipeline;
- Annotationsschemata getrennt von möglicherweise geschützten Inhaltsdaten bewerten.

#### Weiterhin gesperrt

- jede direkte Verwendung der gefundenen Sabahattin-Ali-Volltexte;
- Training oder Stilklassifikation mit ungeklärten modernen Romanbeständen;
- Übernahme von Fuzûlî-README-Zitaten ohne Editionsabgleich;
- automatische Freigabe eines Textes aufgrund einer Repository-Lizenz;
- Behauptung, GitHub habe einen vollständigen Diaspora-, Minderheiten- oder Theaterkorpus geliefert;
- Gleichsetzung von Polarität und literarischer Emotion.

### 14.7 Konsequenz für die nächsten Profile

**Sabahattin Ali:** Das Profil wird nicht aus den gefundenen Volltext-Dumps gebaut. Verwendet werden bibliografisch gesicherte Ausgaben, autoritative Biografie und wissenschaftliche Werkforschung; GitHub liefert lediglich ein dokumentiertes Negativbeispiel für Rechte- und Korpusrisiken.

**Tanpınar und Yaşar Kemal:** GitHub reicht für Werkprofile nicht aus. Externe B1/B2-Quellen und rechtmäßig zugängliche Textausschnitte sind zwingend.

**Hüzün–Hasret–Gurbet:** HisNet und ähnliche Ressourcen können Wortfelder vorbereiten. Die endgültige Trennung entsteht nur durch geprüfte Werke, Beziehungen, Situationen, Körperhandlungen, Zeit und sozialen Kontext.

### 14.8 Phase-2-Entscheidung

GitHub bleibt ein leistungsfähiger Discovery- und Technikraum, ist aber für die nächsten modernen Autoren nicht die primäre Werkquelle. Der größte Qualitätsgewinn dieser Phase ist die klare Sperrlogik: Öffentliche Auffindbarkeit, technische Lizenz und literarisches Nutzungsrecht werden ab sofort als drei verschiedene Fragen behandelt.

**Nächster Arbeitsschritt:** Profil 03 Sabahattin Ali aus autoritativen externen Quellen aufbauen; parallel keine weiteren unspezifischen GitHub-Suchen durchführen. Eine weitere GitHub-Prüfung wird erst bei einer konkreten Repository-, Werk- oder Datensatzfrage ausgelöst.

## 15. Profil 03 — Sabahattin Ali

### 15.1 Profilstatus und Quellenlage

| Feld | Befund |
|---|---|
| Profilstatus | quellenkritisches Grundlagenprofil v1.0 |
| Identität | Sabahattin Ali; Erzähler, Romancier, Lyriker, Lehrer, Übersetzer und Publizist |
| Zeit | geboren am 25. Februar 1907 in Eğridere/Ardino; gestorben am 1. April 1948; Einzelheiten des Todes nur mit ausgewiesener Quellenlage behandeln |
| Hauptwerke | *Kuyucaklı Yusuf*, *İçimizdeki Şeytan*, *Kürk Mantolu Madonna*; Erzählbände von *Değirmen* bis *Sırça Köşk* |
| biografische Relevanz | Lehrtätigkeit, Deutschlandaufenthalt, Haft, Publizistik und institutioneller Druck sind belegte Horizonte, aber keine automatische Erklärung einzelner Figuren |
| GitHub-Lage | mehrere unlizenzierte oder in ihrer Rechtekette ungeklärte Volltexte; vereinzelte Annotations-, Zusammenfassungs- und Klassifikationsprojekte; kein belastbares A1/A2-Werkkorpus |
| Rechte | Werke und Briefe sind nicht aufgrund öffentlicher Auffindbarkeit frei nutzbar; Editionen, Übersetzungen und digitale Textkopien separat prüfen |
| DEJÀ-VU-3-Freigabe | soziale Kausalität, verborgene Innenwelt, Selbsttäuschung, Würde, Raumdruck, Perspektivwechsel und verkörperte Hemmung auf Mechanismenebene |

### 15.2 GitHub-Dateiprüfung

| Fund | konkreter Nachweis | Befund | Ampel / Nutzung |
|---|---|---|---|
| bsenurbas/ai-yazar-tespit | [Kürk Mantolu Madonna, Commit f4157b8](https://github.com/bsenurbas/ai-yazar-tespit/blob/f4157b8e744604031407cd4f8989ba9f77d9b582/data/raw_turkish/sabahattin_ali/kurk_mantolu_madonna.txt) | vollständiger moderner Romantext als Rohdatum; keine tragfähige Rechtekette | 🔴 keine Übernahme, Analysepipeline, Stilklassifikation oder Trainingsnutzung |
| KerimYasin/DOGALDIL | [Romantext, Commit 451fe0a](https://github.com/KerimYasin/DOGALDIL/blob/451fe0aad44f7815e259b5a93ee0c145124d83bf/data/raw/kurk_mantolu_madonna.txt) | weitere Volltextkopie ohne Editions- und Rechtebeleg | 🔴 gesperrt |
| Kon-tiki-ship/tasvir-bankasi-turkish-literary-annotation-pipeline | [Two-regime probe, Commit 2074730](https://github.com/Kon-tiki-ship/tasvir-bankasi-turkish-literary-annotation-pipeline/blob/20747300ffbe349359c2e6407dcd39fe683e94a9/data/two_regime_probe_v0.1/sabahattin_ali_kurk_mantolu_madonna.two_regime_probe_v0.1.jsonl) | Annotationsidee ist methodisch interessant; enthaltene Segmente und deren Herkunft bleiben einzeln zu prüfen | 🟡 Schema abstrahierbar, Inhaltsdaten gesperrt |
| Kon-tiki-ship/tasvir-bankasi-turkish-literary-annotation-pipeline | [Gold-smoke probe, Commit 2074730](https://github.com/Kon-tiki-ship/tasvir-bankasi-turkish-literary-annotation-pipeline/blob/20747300ffbe349359c2e6407dcd39fe683e94a9/data/gold_smoke_v0.1/sabahattin_ali_kurk_mantolu_madonna.gold_smoke_v0.1.jsonl) | literarische Annotation mit möglichem geschütztem Ausgangsmaterial | 🟡/🔴 nur Feldlogik untersuchen, keine Textsegmente übernehmen |
| ufukcankurt/myLibrary | Buchzusammenfassungen zu *Kürk Mantolu Madonna* und *Canım Aliye, Ruhum Filiz* | persönliche oder abgeleitete Zusammenfassungen ohne wissenschaftlichen Apparat | C2/D; nur Suchhinweis |
| tfritzy/typerace.io | Zitatschnipsel unter dem Autorennamen | Textidentität und Edition nicht ausgewiesen | 🔴 bis Editionsabgleich |
| Zeitungsarchiv-Repositories | Artikel über Leben, Tod und Rezeption | nützlich für Rezeptions- und Pressespuren, nicht automatisch für Tatsachenbehauptungen | 🟡 Originalartikel und Kontext separat prüfen |

**GitHub-Entscheidung:** Für Sabahattin Ali dient GitHub als Rechtewarnsystem, Commit-gebundener Fundnachweis und Quelle für abstrakte Annotationsarchitektur. Es liefert gegenwärtig keine freigegebene Werkbasis.

### 15.3 Historischer und biografischer Horizont

Die autoritative biografische Erschließung verortet Sabahattin Ali zwischen spätem Osmanischem Reich und früher Republik. Familienbedingte Ortswechsel, Lehrerausbildung, Unterrichtstätigkeit, ein staatlich organisierter Deutschlandaufenthalt, Gefängniserfahrungen, Übersetzungsarbeit und oppositionelle Publizistik gehören zum belegbaren Horizont. Seine Arbeit für *Markopaşa* und Nachfolgepublikationen, Prozesse, Haftzeiten und wirtschaftlicher Druck zeigen, dass Schreiben, Staat, Beruf und materielle Existenz nicht getrennte Welten waren.

Für DEJÀ-VU-3 gilt dennoch: Eine Haftbiografie erklärt keine Erzählung automatisch; eine Figur ist kein Selbstporträt; politische Haltung ersetzt keine Textanalyse. Verwendet wird eine Dreiteilung:

1. **Fakt:** datierbares Ereignis, Publikation oder institutionelle Lage.
2. **Textbeobachtung:** konkrete Erzähloperation, Beziehung, Raum- oder Sprachhandlung.
3. **Interpretation:** begründete Verbindung, als solche gekennzeichnet.

Die Umstände seines Todes sind historisch und politisch belastet. Das Profil übernimmt keine vereinfachte Täter-, Motiv- oder Staatskausalität aus journalistischen GitHub-Dumps; jede Detailbehauptung benötigt eigenständige historische Prüfung.

### 15.4 Gesicherter Werkrahmen

#### Kuyucaklı Yusuf

Der Roman verbindet eine persönliche Bindungs- und Verlustgeschichte mit der Machtordnung einer westanatolischen Kleinstadt. Forschung zu Sprache und Raum zeigt Status, Geschlecht und Ökonomie als miteinander arbeitende Ungleichheitsachsen. Bürokratie, lokale Notabeln, Besitz und gesellschaftliche Reputation wirken unmittelbar auf private Möglichkeiten.

**Textbeobachtung:** Räume sind keine Kulisse. Dorf, Stadt, Amt, Haus, Straße und Natur verändern Schutz, Sichtbarkeit, Bewegung und Handlungsmacht. Früh gesetzte körperliche und biografische Details tragen spätere Konsequenzen.

**Interpretation:** Der Konflikt entsteht nicht bloß aus einem „wilden Außenseiter“ gegen eine verdorbene Stadt, sondern aus einer Person, deren begrenzte Sprache und soziale Stellung auf ein eng gekoppeltes Machtfeld treffen.

**Abstraktion:** Private Tragik wird präzise, wenn Besitz, Amt, Geschlecht, Ruf und Raum als konkrete Ursachen mitlaufen.

#### İçimizdeki Şeytan

Der Roman verbindet inneren Konflikt mit einer Kritik an intellektuellen Milieus und sozialen Abhängigkeiten. Die titelgebende innere Macht wird nicht als übernatürliche Entschuldigung übernommen.

**Textbeobachtung:** Ömer verschiebt Verantwortung auf eine angeblich fremde Kraft in sich. Parasızlık, Bindung, Gruppendruck, Begehren und moralische Unentschiedenheit verändern seine Handlungen. Die Entwicklung bleibt unvollständig und hält die Spannung über den Schluss hinaus offen.

**Interpretation:** Der „Teufel“ funktioniert als Sprache der Selbstentlastung: Er benennt einen realen inneren Konflikt, kann aber zugleich die eigene Entscheidung unsichtbar machen.

**Abstraktion:** Eine Figur wird glaubwürdig, wenn ihre Ausrede psychologisch verständlich ist und dennoch reale Kosten für andere erzeugt.

#### Kürk Mantolu Madonna

Der Roman erschien zunächst 1940–1941 als Zeitungsfortsetzung und 1943 als Buch. Seine soziale Wirklichkeit ist zurückgenommener als in den beiden früheren Romanen, aber nicht abwesend. Arbeit, Familie, Geschlechterrollen, ökonomische Abhängigkeit, Erinnerung und mangelnde Kommunikation formen die private Geschichte.

**Textbeobachtung:** Eine äußerlich unscheinbare Person wird zunächst durch den begrenzten Blick eines anderen Menschen gesehen. Erst eine vermittelte Innenerzählung verändert ihre moralische und emotionale Lesbarkeit. Die Beziehung zwischen Raif und Maria ist zugleich durch Begehren, Rollenprüfung, Eigenständigkeit, Verletzbarkeit, räumliche Distanz und ungleiches Wissen geprägt.

**Interpretation:** Der Roman ist nicht nur eine „traurige Liebesgeschichte“. Er untersucht, wie eine Gesellschaft stille Menschen falsch liest und wie eine Person ihr Inneres schützen kann, bis dieser Schutz zur Isolation wird.

**Abstraktion:** Ein Perspektivwechsel besitzt ethische Kraft, wenn neue Information das frühere Urteil über eine Person revidiert.

#### Erzählungen, Lyrik und Briefe

Die Erzählungen bewegen sich von ereignisorientierter Beobachtung zu stärker verdichteten, teilweise kritisch-realistischen Momentaufnahmen. Arbeit, Gefängnis, Dorf, Stadt, Armut, marginalisierte Begabung, institutionelle Willkür und beschädigte Würde treten wiederholt auf. Dialog, gesprochene Sprache, kurze Szenen und abrupte Schlüsse tragen den sozialen Druck.

Lyrik und private Briefe dürfen nicht als direkte psychologische Schlüssel zu Romanfiguren benutzt werden. Briefe sind historische Dokumente einer konkreten Beziehung und konkrete Ausgaben bleiben urheber- und editionsrechtlich zu prüfen.

### 15.5 Denkarchitektur

| Ebene | Operation | Sabahattin-Ali-Profil | DEJÀ-VU-3-Nutzung |
|---|---|---|---|
| materielle Kausalität | soziale Ordnung erzeugt private Folgen | Geld, Arbeit, Amt, Ruf, Geschlecht und Besitz begrenzen Entscheidung | emotionale Szene mit mindestens einer konkreten materiellen Ursache bauen |
| verborgene Innenwelt | äußere Lesbarkeit widerspricht innerer Erfahrung | unscheinbare oder schweigende Personen werden systematisch unterschätzt | Urteil zunächst begrenzen, später durch Perspektivwechsel revidieren |
| Selbstentlastung | innerer Konflikt wird zur Ausrede | Verantwortung wird an Milieu, Schwäche oder den „inneren Teufel“ abgegeben | Motiv verständlich machen, Verantwortung nicht aufheben |
| Raum als Macht | Ort verteilt Schutz und Risiko | Haus, Amt, Straße, Dorf, Stadt und Natur erlauben verschiedene Körperhaltungen | Raumgrenze muss eine Handlung verändern |
| kritischer Realismus | Einzelfall legt System frei | persönliche Verletzung zeigt gesellschaftliche Struktur | System über menschliche Kosten statt Thesenrede zeigen |
| Würde | Person widersteht ihrer Reduktion | Schweigen, Rückzug oder Aufbegehren können Schutz und Verlust zugleich sein | Würde nicht mit Stolz oder Passivität gleichsetzen |

**Leitmodus:** DM-09 Materiell-sozial.  
**Gegenmodus:** DM-08 Phänomenologisch.  
**Blind-Spot-Test:** Keine Elendsästhetik, kein romantischer Außenseiterkult, keine Gleichsetzung von Schweigen und Tiefe. Ursache, Wahl, Preis und Wirkung auf andere müssen sichtbar bleiben.

### 15.6 Emotionsarchitektur

| Zustand | Auslöser und Beziehung | Gegenkraft | Körper- und Handlungsspur | Abgrenzung |
|---|---|---|---|---|
| Yalnızlık | fehlende Resonanz trotz sozialer Nähe | vorsichtige Bindung | Blick bleibt bei einer Aufgabe, Körper verkleinert seinen Raum, Sprechen wird funktional | nicht mit bloßem Alleinsein gleichsetzen |
| Yabancılaşma | Arbeit, Rolle oder Milieu trennt Person von eigenem Erleben | Erinnerung oder Beziehung | mechanische Routine, zeitverzögerte Reaktion, reduzierte Eigeninitiative | keine klinische Diagnose |
| Utanç | soziale Entwertung oder erkannte Verfehlung | Würde und Annahme | Blickkontakt bricht, Hals spannt, Hände verdecken oder ordnen | Scham ist nicht Schuld |
| Sitem | verletzte Erwartung bei fortbestehender Bindung | Hoffnung oder Onur | kontrollierte Stimme, präziser Satz, gestoppte Annäherung | keine reine Aggression |
| İsyan | erlebte Ungerechtigkeit überschreitet eine Grenze | Angst, Pflicht oder Abhängigkeit | Atem gewinnt Druck, Schwerpunkt verlagert sich vor, Handlung wird plötzlich genau | Schrei oder Faust nicht erforderlich |
| Onur | Anspruch auf menschliche Behandlung | materielle Abhängigkeit | Haltung richtet sich auf, Hände setzen eine Grenze, Blick wird stabil | nicht mit Hochmut verwechseln |
| Aşk / Sevgi | Anerkennung einer bislang ungesehenen Person | Angst vor Abhängigkeit oder Verlust | Aufmerksamkeit wird detaillierter, Atemrhythmus synchronisiert sich kurz, Berührung bleibt verhandelbar | keine automatische Erlösung |
| Umutsuzluk | wiederholte Blockade und verlorene Zukunft | Pflicht, Erinnerung oder kleine Solidarität | verlangsamte Initiation, flacherer Atem, Routine ersetzt Wunsch | nicht als dauerhafte Autorenpsychologie behaupten |

### 15.7 Erzähltechnik, Rhetorik und Sprache

| Mechanismus | Wirkung | Produktionsregel |
|---|---|---|
| begrenzter Erstblick | lässt Leserinnen und Leser an einem Fehlurteil teilnehmen | nur zeigen, was die beobachtende Figur wirklich wissen kann |
| vermittelte Innenerzählung | revidiert äußere Identität | neue Information muss mindestens zwei frühere Details umdeuten |
| soziale Detailkausalität | bindet Gefühl an Welt | Geld, Arbeitszeit, Raumrecht oder Ruf konkret benennen |
| Dialog und Register | macht Klasse, Nähe und Macht hörbar | keine Dialektkarikatur; Funktion vor Folklore |
| kontrollierte Ironie | entlarvt Selbstbild oder Institution | Ironie gegen Macht, Ausrede oder Pose richten |
| entworfene Stille | Schweigen wird Handlung | festlegen, wer schweigt, was geschützt wird und wer den Preis trägt |
| abrupter oder offener Schluss | verweigert bequeme moralische Schließung | Schluss muss eine frühere Szene neu beleuchten |
| Raumkontrast | übersetzt gesellschaftliche Ordnung in Bewegung | mindestens eine Tür, Distanz, Sitzordnung oder Wegentscheidung funktional einsetzen |

**Rhetorische Führung:** RH-12 Entworfene Stille.  
**Unterstützung:** RH-07 Ironie und RH-01 Tezat.  
**Formschutz:** Keine imitationistische „schlichte Traurigkeit“, keine künstliche Armutssprache und kein schweigender Mann als automatischer Tiefencode.

### 15.8 Perspektive, menschliche Anatomie und Gesichtsausdruck

Die zentrale visuelle Aufgabe ist der Widerspruch zwischen öffentlicher Rolle und innerer Reaktion. Emotion muss im Gesicht lesbar sein, ohne zur Maske zu werden. Dafür werden nicht einzelne Symbole, sondern gekoppelte Muskel-, Atem- und Handlungsverläufe gebaut.

**Gesichtskette bei unterdrückter Kränkung:** Blick trifft den Auslöser → oberes Lid spannt sich leicht → innere Braue reagiert minimal → Kiefer fixiert → Mundwinkel verlieren Symmetrie → Schlucken verzögert die Antwort.  
**Gesichtskette bei vorsichtiger Nähe:** Blickdauer wächst → Lidspannung sinkt → Lippen öffnen sich vor dem Satz → Atem wird tiefer → Kopf neigt sich nur wenig → Hand bleibt sichtbar und nicht greifend.  
**Gesichtskette bei erkannter Selbsttäuschung:** Blick löst sich vom Gegenüber → Stirnspannung konzentriert sich → Unterlippe wird kurz gehalten → Ausatmung verlängert sich → Hände beenden eine Ausweichhandlung → Blick kehrt mit veränderter Verantwortung zurück.

Anatomische Pflichtfelder:

- korrekte Schädel-, Hals- und Schulterausrichtung;
- Blickziel, Fokusdistanz und Lichtreflex physiologisch konsistent;
- fünf plausible Finger, Gelenkachsen, Druckstellen und tatsächlicher Objektkontakt;
- Brustkorb, Schlüsselbein und Schultern folgen demselben Atemzustand;
- Schwerpunkt, Becken, Knie und Fußkontakt tragen die beabsichtigte Bewegung;
- Mimik, Hand und Körper dürfen sich widersprechen, müssen aber zeitlich erklärbar sein;
- Tränen nur, wenn Flüssigkeit, Lidreaktion, Atem und Licht gemeinsam plausibel sind.

Bevorzugte Handlungskette: soziale Herabsetzung → funktionales Gesicht bleibt bestehen → Blick weicht um Millimeter aus → Hand ordnet ein Objekt zu genau → Atem wird gehalten → Entscheidung zwischen Schweigen, Grenze und Widerspruch → Nachbewegung zeigt den Preis.

### 15.9 DEJÀ-VU-3-DNA-Karte

```yaml
profile: SABAHATTIN-ALI-03
status: mechanism_release
human_situation: Eine übersehene Person wird nach ihrer sozialen Funktion beurteilt; eine verborgene Erfahrung zwingt das Gegenüber, dieses Urteil zu revidieren.
gold:
  mechanism: LM-05 Materielle Kausalität
  function: Arbeit, Geld, Status und Raum erzeugen die private Verletzung mit.
silver:
  mechanism: BW-04 Begrenzter Beobachter
  function: Das erste Urteil bleibt an sichtbare Rolle und unvollständiges Wissen gebunden.
bronze:
  mechanism: RH-12 Entworfene Stille
  function: Schweigen schützt die Person und vergrößert gleichzeitig ihre Isolation.
thought_mode: DM-09 Materiell-sozial
counter_mode: DM-08 Phänomenologisch
perspective: äußerer Beobachter → vermittelte Innenperspektive → revidierter Beobachter
emotion_arc: Unsichtbarkeit → Vorsicht → mögliche Bindung → Entblößung → Verlust oder Grenze → verspätetes Verstehen
body_arc: verkleinerter Raum → mechanische Handlung → verlängerter Blick → gehemmte Hand → kurze Öffnung → bewusster Rückzug oder Widerspruch
form: soziale Details; begrenztes Wissen; Dialogregister; entworfene Stille; Schluss revidiert den Anfang
forbidden: Autorenimitation, Volltextnutzung, tragische-Liebesgeschichte-Reduktion, Armutsästhetik, Figur-gleich-Autor, schweigender-Mann-Klischee
```

### 15.10 Transformationsformeln

**Unsichtbarkeitsformel:** funktionale Rolle → vorschnelles Urteil → irritierendes Detail → verborgene Geschichte → revidierter Blick → konkrete Wiedergutmachung oder bleibender Schaden.

**Verantwortungsformel:** Wunsch → materielle und soziale Blockade → verständliche Ausrede → Handlung verletzt eine andere Person → Ausrede verliert Schutzfunktion → unvollständige, aber reale Verantwortungsübernahme.

**Raumformel:** Person sucht Schutz → Raum besitzt soziale Regeln → Körper passt sich an → Grenze wird überschritten → kleine Gegenhandlung → Raum und Beziehung sind danach verändert.

**Würdeformel:** wiederholte Herabsetzung → funktionale Selbstkontrolle → sichtbarer Mikroriss → genaue Grenze statt Explosion → materieller Preis → Selbstachtung ohne sichere Belohnung.

### 15.11 Qualitäts-, Quellen- und Rechteampel

| Bereich | Ampel | Begründung |
|---|---|---|
| Identität, Lebensdaten, Berufe und Werkverzeichnis | 🟢 | durch akademische Autorenlexika und bibliografische Forschung belastbar |
| institutionelle Konflikte und Haftstationen | 🟢/🟡 | grundsätzlich dokumentiert; genaue Motive und Kausalbehauptungen quellengebunden halten |
| Details des Todes | 🟡 | politisch belastete und teils widersprechende Überlieferung; keine GitHub-Zeitung als Endbeleg |
| drei Romane als Werkanker | 🟢 | bibliografisch und forschungsgeschichtlich gut erschlossen |
| psychobiografische Gleichsetzung mit Figuren | 🔴 | methodisch gesperrt |
| GitHub-Volltexte | 🔴 | öffentliche Auffindbarkeit ohne ausreichende Rechte- und Editionskette |
| GitHub-Annotationsschemata | 🟡 | abstrakte Struktur prüfbar; Inhaltsdaten separat sperren |
| Mechanismenübertragung | 🟢 | bei eigener Situation, eigener Stimme und klarer Ursachenstruktur |
| kurze Originalzitate | 🟡 | nur aus rechtmäßig zugänglicher, genau genannter Ausgabe und im notwendigen Umfang |
| Briefe als „wahres Ich“ | 🔴 | Dokument, Adressat, Situation und Edition müssen erhalten bleiben |

### 15.12 Verwendete Kernquellen

- [Türk Edebiyatı İsimler Sözlüğü: Sabahattin Ali](https://teis.yesevi.edu.tr/madde-detay/sabahattin-ali) — Lebensstationen, Werkverzeichnis, Erzählentwicklung und Romanprofile; B1/B2.
- [Kuyucaklı Yusuf’ta Toplumsal Eşitsizlik Bildiren Dil Birimleri](https://dergipark.org.tr/tr/pub/turcology/article/1488071) — Status, Geschlecht, Ökonomie und Sprachform; B2.
- [Sabahattin Ali’nin Kuyucaklı Yusuf Romanında Mekânın Poetiği](https://dergipark.org.tr/tr/download/article-file/635013) — Raum-Person-Beziehung und soziale Kritik; B2.
- [Kuyucaklı Yusuf’ta kadınların toplumsal konumu](https://dergipark.org.tr/tr/pub/insanveinsan/article/521714) — patriarchale Hierarchie und Genderdimension; B2.
- [İçimizdeki Şeytan’ın Greimas’ın Eyleyenler Modeline Göre Çözümlenmesi](https://dergipark.org.tr/tr/download/article-file/3039596) — Verantwortung, materielle Gegenkräfte, Figuren- und Handlungsrelationen; B2.
- [Yozlaşma Karşısında Bireyin Çığlığı: Kürk Mantolu Madonna](https://dergipark.org.tr/tr/pub/eeder/article/1412025) — Individuum, Umwelt und soziale Verletzbarkeit; B2.
- [Kürk Mantolu Madonna und Geschlechternormen](https://dergipark.org.tr/tr/pub/asya/article/936565) — Maria Puder, Eigenständigkeit und soziale Geschlechterordnung; B2.

### 15.13 Offene Prüfaufträge

1. Bibliografisch gesicherte Ausgaben der drei Romane erfassen und die verwendeten Seitenbereiche dokumentieren.
2. Je Roman drei kurze Textanker auswählen und strikt in Textbeobachtung, Interpretation und DNA-Abstraktion trennen.
3. Die Fassungs- und Modernisierungsunterschiede von *İçimizdeki Şeytan* prüfen; moderne sprachliche Eingriffe nicht mit dem historischen Text verwechseln.
4. Die Erzählungen *Kanal*, *Kağnı*, *Ses*, *Çilli* und *Sırça Köşk* als getrennte Arbeits-, Raum- und Würdeprofile erschließen.
5. GitHub-Annotationsschema ohne fremde Textdaten in ein neutrales DEJÀ-VU-3-Schema überführen.
6. Einen eigenständigen Testtext bauen: moderne Arbeitssituation, begrenzter Beobachter, entworfene Stille, anatomisch lesbare Mikromimik und reale materielle Konsequenz.

**Profilentscheidung:** Sabahattin Ali wird als geprüfte Mechanismengruppe geführt: materielle Kausalität, verborgene Innenwelt, begrenztes Wissen, Verantwortung gegen Selbstentlastung, Raum als soziale Macht, entworfene Stille und Würde unter institutionellem Druck. GitHub bleibt dabei Discovery-, Risiko- und Methodenschicht, nicht Werkquelle.

## 16. Profil 04 — Ahmet Hamdi Tanpınar

### 16.1 Profilstatus und Quellenlage

| Feld | Befund |
|---|---|
| Profilstatus | quellenkritisches Grundlagenprofil v1.0 |
| Identität | Ahmet Hamdi Tanpınar; Dichter, Erzähler, Romancier, Essayist, Literaturhistoriker, Hochschullehrer und zeitweise Abgeordneter |
| Lebensdaten | 23. Juni 1901, İstanbul–24. Januar 1962, İstanbul |
| Hauptanker | *Huzur*, *Saatleri Ayarlama Enstitüsü*, *Beş Şehir*, *Mahur Beste*, *Sahnenin Dışındakiler*, *Abdullah Efendi’nin Rüyaları*, ausgewählte Gedichte |
| Forschungsschwerpunkte | innere Zeit, Erinnerung, Stadt, kulturelle Kontinuität und Bruch, Modernisierung, Musik, Traum, Identität, Ironie und Institution |
| GitHub-Lage | überwiegend Werklisten, Lern- und Testdaten, Zitatschnipsel, Tweets und bibliografische Nennungen; kein überprüftes editionskritisches Werkkorpus gefunden |
| Rechte | Tod 1962 bedeutet nicht automatisch weltweite Gemeinfreiheit; türkische, deutsche und plattformspezifische Schutzfristen sowie Rechte moderner Editionen und Übersetzungen prüfen |
| DEJÀ-VU-3-Freigabe | innere Zeit, veränderte Erinnerung, Stadt als Gedächtnisraum, unzuverlässige Selbstordnung, institutionelle Absurdität und ironische Modernisierungskritik auf Mechanismenebene |

### 16.2 GitHub-Prüfung

| GitHub-Fund | Inhalt | Quellenwert | Ampel / Entscheidung |
|---|---|---|---|
| [lys-edebiyat/data](https://github.com/lys-edebiyat/data/blob/master/lys-edebiyat/csv/oyun-data.csv) | CSV-Werkliste mit Tanpınar-Titeln | bibliografische Lern- oder Discovery-Daten ohne Editionsapparat | 🟡 Titelhinweis; Titel und Gattung extern bestätigen |
| [kurtulusutkucenik/LibraryProject](https://github.com/kurtulusutkucenik/LibraryProject/blob/main/book.c) | *Huzur* und *Saatleri Ayarlama Enstitüsü* als Einträge eines C-Testprojekts | technisches Beispieldatum, keine Literaturquelle | 🔴 nicht für Werk-, Inhalts- oder Rechtebehauptungen |
| [BenKosSoft/deepTwitter](https://github.com/BenKosSoft/deepTwitter/blob/master/tweets.txt) | Tweet-Dump mit Tanpınar-Nennung und ungesichertem Gedichtfragment | Identität, Orthografie, Kontext und Rechte ungeklärt | 🔴 keine Zitate oder Emotionsanalyse |
| generische Buchdatenbanken und SQL-Testdaten | Titel, Preis, Genre oder Kurzbeschreibung | Produkt- und Testdaten, teils vereinfachte Inhaltsangaben | D; keine Forschung |
| Zeitungs- und Social-Media-Dumps | Rezeption, Festivalnennungen, paraphrasierte Aussagen | höchstens Rezeptionsspur | 🟡 Originalpublikation suchen; keine Autorenzuschreibung aus Dump |
| unspezifische NLP- und Klassifikationskorpora | Autor- oder Titelnamen in Kategorien | möglicherweise für Named-Entity- oder Katalogtests brauchbar | 🟡 technische Schicht; keine Werkinterpretation |

**GitHub-Befund:** Für Tanpınar ist GitHub aktuell schwächer als bei Fuzûlî und technisch weniger ergiebig als bei Sabahattin Ali. Der Fundraum bestätigt Werkidentitäten nur vorläufig und zeigt vor allem, wie leicht kanonische Literatur in kontextlose Titel-, Tweet- und Trainingszeilen zerfällt.

**Neue Sperrregel:** Ein Name-Titel-Paar ist keine Werkquelle. Ein Gedichtfragment in einem Tweet-Korpus ist weder Zitatbeleg noch editionsfähiger Text. Eine automatische Emotionsanalyse solcher Zeilen bleibt gesperrt.

### 16.3 Historischer und biografischer Horizont

Tanpınars Kindheit war durch die dienstbedingten Ortswechsel seines Vaters geprägt; zu seinen Lebensräumen gehörten unter anderem İstanbul, Sinop, Siirt, Kerkük und Antalya. Er studierte am Darülfünun bei Yahya Kemal und weiteren prägenden Gelehrten, unterrichtete in verschiedenen Städten und wurde 1939 Professor für Neue Türkische Literatur an der Universität İstanbul. Seine Tätigkeiten als Lehrer, Kunst- und Literaturhistoriker, Ästhetikdozent und Abgeordneter verbanden literarische Arbeit mit Institution, Bildung und Kulturpolitik. Diese Stationen sind als belegte Horizonte nutzbar, nicht als automatische Schlüssel zu einzelnen Figuren.

Für seine ästhetische Entwicklung sind türkische Literaturtraditionen, französische Dichtung und Prosa, bildende Kunst, klassische Musik sowie philosophische Zeit- und Erinnerungskonzepte wichtig. Bergson, Bachelard, Valéry, Proust, Yahya Kemal und Ahmet Haşim gehören zu den nachweisbaren Bezugspunkten. Einfluss bedeutet jedoch keine Ableitungsgleichung: Ein Werk wird nicht auf einen Philosophen, eine Verlusterfahrung oder den Gegensatz „Ost gegen West“ reduziert.

Der Übergang vom späten Osmanischen Reich zur Republik bildet einen realen historischen Druckraum. Tanpınars Texte untersuchen Kontinuität und Abbruch, doch sie liefern keine einfache Parole für Tradition oder Modernisierung. Besonders wichtig ist die Frage, wie eine Gesellschaft ihre Zeit ordnet, ihre Vergangenheit erzählt und neue Institutionen legitimiert.

### 16.4 Werkrahmen

#### Huzur

*Huzur* erschien 1948 als Fortsetzung und 1949 als Buch. Der Roman umfasst vier nach zentralen Figuren benannte Teile und verdichtet seine Gegenwart auf ungefähr vierundzwanzig Stunden unmittelbar vor Beginn des Zweiten Weltkriegs. Erinnerungen, Gespräche, Spaziergänge, Musik und historische Räume erweitern diese kurze Gegenwart in mehrere Zeitschichten.

**Fakt:** İstanbul, Osmanische Kultur, Musik, Krankheit, Liebe und drohender Krieg gehören zur nachweisbaren Werkarchitektur.

**Textbeobachtung:** Gegenwärtige Wahrnehmung löst Erinnerung aus; Räume und Klänge verändern die Dauer einer Szene. Private Liebe steht nicht außerhalb der Geschichte. Das Wissen um Krankheit und Krieg verändert selbst Momente möglicher Nähe.

**Interpretation:** „Huzur“ funktioniert weniger als erreichter Zustand denn als gefährdete Ordnung. Eine Person versucht, Vergangenheit, Begehren, Kultur und Gegenwart zu einer lebbaren Einheit zu verbinden, während äußere Geschichte und innere Widersprüche diese Einheit aufbrechen.

**Abstraktion:** Eine kurze äußere Zeit kann eine lange innere Zeit tragen. Spannung entsteht, wenn Erinnerung die Gegenwart nicht erklärt, sondern gleichzeitig vertieft und belastet.

#### Saatleri Ayarlama Enstitüsü

Der 1961 veröffentlichte Roman ist als Erinnerungserzählung Hayri İrdals gestaltet. Eine Institution, deren gesellschaftliche Notwendigkeit erst sprachlich erzeugt wird, organisiert Zeit, Personal, Regeln und öffentliches Ansehen. Forschung hebt die ironische und absurde Kritik an Modernisierung, Bürokratie und legitimierenden Diskursen hervor.

**Textbeobachtung:** Hayri erzählt rückblickend und bleibt an seiner eigenen Beteiligung gebunden. Die Institution wirkt immer realer, je mehr Sprache, Titel, Verfahren und gesellschaftliche Zustimmung sie erzeugt. Funktion und Behauptung treten auseinander.

**Interpretation:** Die Satire richtet sich weder schlicht gegen Uhren noch gegen Modernität. Sie zeigt, wie Menschen eine institutionelle Fiktion mitbauen, weil sie Ordnung, Einkommen, Status oder Zukunft verspricht.

**Abstraktion:** Institutionelle Absurdität entsteht, wenn ein unnötiges System durch perfekte Begriffe, Rollen und Abläufe notwendig erscheint und reale menschliche Abhängigkeit produziert.

#### Beş Şehir

*Beş Şehir* versammelt essayistische Stadtporträts zu Ankara, Erzurum, Konya, Bursa und İstanbul. Die Texte entstanden schrittweise; die Erstausgabe erschien 1946, die zweite Fassung 1960 wurde überarbeitet und erweitert.

**Textbeobachtung:** Architektur, Musik, Landschaft, Alltag, historische Figuren und persönliche Erinnerung bilden keine getrennten Inventare. Ein Ort wird über überlagerte Zeiten wahrgenommen.

**Interpretation:** Die Stadt ist ein Gedächtnisraum, aber kein unveränderliches Museum. Erinnerung wählt, verbindet und wertet; sie kann Kontinuität ermöglichen und zugleich Verlust sichtbar machen.

**Abstraktion:** Raum wird literarisch stark, wenn mindestens drei Ebenen miteinander handeln: gegenwärtige Bewegung, materielle Spur und erinnerte beziehungsweise historische Beziehung.

#### Mahur Beste und Sahnenin Dışındakiler

*Mahur Beste* verbindet Familien-, Kultur- und Beziehungsgeschichte; der ergänzende Brief an Behçet Bey lässt den Autor mit einer eigenen Figur in Dialog treten. *Sahnenin Dışındakiler* richtet den Blick auf das besetzte İstanbul und auf Menschen, die sich gegenüber dem als „eigentliche Bühne“ verstandenen Anatolien außerhalb des historischen Zentrums erleben.

**Abstraktion:** Eine Figur kann historisch randständig sein und dennoch eine zentrale Wahrnehmungsposition besitzen. Unabgeschlossenheit kann als Form sichtbar machen, dass weder Biografie noch Geschichte vollständig geordnet werden können.

#### Abdullah Efendi’nin Rüyaları, Gedichte und Traumlogik

In den Erzählungen und Gedichten verbinden sich Wahrnehmung, Traum, Doppelung, Bild, Musik und innere Zeit. Die Traumebene darf nicht als beliebiger Surrealismus verwendet werden. Sie braucht einen konkreten Wahrnehmungsauslöser, eine Beziehung zum Wachzustand und eine nachfolgende Veränderung der Figur.

Bei Gedichten wie *Bursa’da Zaman* sind Zeit, Raum, kulturelles Gedächtnis und Bildsystem gemeinsam zu prüfen. Einzelne berühmte Zeilen bleiben ohne genaue Ausgabe und Gedichtkontext für direkte Übernahme gesperrt.

### 16.5 Denkarchitektur

| Ebene | Leitfrage | Tanpınar-Profil | DEJÀ-VU-3-Nutzung |
|---|---|---|---|
| innere Zeit | Warum dauert dieselbe Minute für Menschen verschieden? | Erinnerung, Erwartung und Wahrnehmung dehnen die äußere Zeit | äußere Uhrzeit und erlebte Dauer getrennt führen |
| Kontinuität und Bruch | Was bleibt beim Wandel erhalten? | kulturelle Formen überleben verändert oder werden institutionell abgebrochen | weder Fortschritts- noch Verfallserzählung automatisch bevorzugen |
| Stadtgedächtnis | Wer und was erinnert im Raum? | Architektur, Klang, Weg, Landschaft und Person tragen verschiedene Zeiten | Ort muss Handlung und Erinnerung gleichzeitig verändern |
| modernes Selbst | Welche Rollen passen nicht zusammen? | Person bewegt sich zwischen geerbten Formen, neuen Institutionen und privaten Wünschen | Konflikt in Körper, Sprache und Entscheidung zeigen |
| institutionelle Absurdität | Wie wird eine Behauptung gesellschaftlich real? | Titel, Verfahren, Expertenstatus und Wiederholung erzeugen Legitimität | Regel bis zu ihren menschlichen Kosten verfolgen |
| ironische Distanz | Was erkennt der Erzähler an sich selbst nicht? | Rückblick kann Selbsterklärung und Selbsttäuschung zugleich sein | Leserwissen darf das Figurenwissen übersteigen |
| Musik und Komposition | Wie kehrt Bedeutung verändert wieder? | Klang, Rhythmus und Motiv verbinden Erinnerungsschichten | Leitmotiv nur verwenden, wenn jede Rückkehr neue Zeit trägt |

**Leitmodus:** DM-15 Geschichtete Zeit.  
**Gegenmodus:** DM-02 Systemisch.  
**Blind-Spot-Test:** Keine dekorativen Rückblenden, keine automatische İstanbul-Melancholie und keine abstrakte Kulturklage. Jede Zeitschicht braucht Auslöser, Wahrnehmung, Beziehung und gegenwärtige Folge.

### 16.6 Emotionsarchitektur

| Emotion/Zustand | Auslöser | Gegenkraft | Körper- und Handlungsspur | Schutz vor Vereinfachung |
|---|---|---|---|---|
| Hüzün | Bewusstsein von Verlust und Fortdauer im selben Raum | ästhetische oder menschliche Verbundenheit | Blick verweilt an einer Spur, Atem wird länger, Bewegung verlangsamt sich ohne Stillstand | nicht allgemeine Traurigkeit und nicht automatisch „İstanbul-Gefühl“ |
| Hasret | Entfernung zu einer Person, Zeit oder Möglichkeit | Vorstellung künftiger Nähe | Körper richtet sich zu einem Weg oder Klang aus, Hand beginnt eine Kontaktbewegung | kann Zukunft enthalten; nicht mit Hüzün gleichsetzen |
| Keder | schwerer, anhaltender Gram | Pflicht oder Rhythmus des Alltags | Initiation sinkt, Routine wird mühsam, Blick verliert Wechsel | nicht als schöne Atmosphäre verwenden |
| Huzursuzluk | widersprechende Wünsche, drohende Geschichte oder unsichere Ordnung | vorläufige Form, Musik, Gespräch | Blick springt zwischen Details, Atemrhythmus wechselt, Hände beginnen und unterbrechen | keine Diagnose; situative Funktion |
| Korku | Krankheit, Krieg, Verlust oder Entlarvung | Bindung, Pflicht, Selbstkontrolle | Fokus verengt oder sucht Ausgänge, Brustkorb hält Atem, Gewicht bleibt rückwärts | weite Augen nicht zwingend |
| Aşk | Beziehung wird zum Versuch einer inneren Ordnung | Eigenständigkeit des Gegenübers und historische Realität | Aufmerksamkeit vertieft sich, Distanz wird bewusst verhandelt, Berührung bleibt fragil | Liebe nicht als Heilung aller Brüche |
| Aidiyet | Person erkennt sich in Sprache, Ort, Musik oder Gemeinschaft | Erfahrung von Fremdheit und Veränderung | Haltung öffnet sich kurz, bekannte Bewegung kehrt zurück, Stimme findet Rhythmus | keine homogene nationale Essenz |
| İronik rahatlık | Person profitiert von einer absurden Ordnung | aufkommende Selbsterkenntnis | höfliches Gesicht, kleine Verzögerung, Blick umgeht Widerspruch, Hände führen Verfahren fort | Komik darf Verantwortung nicht löschen |

**Emotionsregel:** Tanpınars Mechanismen erlauben gleichzeitig Zugehörigkeit und Fremdheit, Freude und Vorahnung, Erinnerung und Verlust. Der Widerspruch muss aus einer Situation entstehen, nicht aus poetischen Gegensatzpaaren allein.

### 16.7 Erzähltechnik, Rhetorik und Form

| Mechanismus | Funktion | Produktionsregel |
|---|---|---|
| geschichtete Gegenwart | mehrere Zeiten wirken im selben Moment | jede Erinnerung braucht einen sensorischen oder relationalen Auslöser |
| Leitmotiv | Klang, Objekt oder Weg kehrt verändert wieder | mindestens zwei Rückkehrpunkte mit neuer Bedeutung |
| semantische Rückkehr | Schluss verändert den Anfang | keine beliebige Twist-Auflösung |
| begrenzte Rückschau | Erzähler ordnet und verdeckt zugleich | Selbstrechtfertigung und Faktenspuren auseinanderhalten |
| Ironie | Realität widerlegt die institutionelle Behauptung | System sprechen und handeln lassen; keine Autorenthese als Pointe |
| absurde Folgerichtigkeit | falsche Prämisse erzeugt perfekte Abläufe | menschlichen Nutzen, Preis und Mitwirkung zeigen |
| Musikalisierung | Wiederholung und Variation ordnen Zeit | Klangfunktion beschreiben, keine bloße Musiknamensliste |
| Traumübergang | Wahrnehmungsordnung verschiebt sich | Körper, Raum oder Entscheidung müssen nach dem Traum verändert sein |

**Rhetorische Führung:** RH-15 Semantische Rückkehr.  
**Unterstützung:** RH-10 Leitmotiv und RH-08 Ironie.  
**Formschutz:** Keine Proust-Kopie, keine Tanpınar-Stimmimitation, keine willkürliche Satzverlängerung und keine Ansammlung von Uhren, Nebel, Musik und alten Häusern ohne Handlung.

### 16.8 Perspektive, Anatomie und sichtbare Emotion

Tanpınar-basierte Visualisierung zeigt Zeit nicht durch eine große Uhr im Bild, sondern durch eine Person, deren Gegenwart von einer Spur verändert wird. Gesicht, Atem, Hände, Gewicht und Raum müssen denselben zeitlichen Übergang tragen.

**Erinnerung setzt ein:** Blick stoppt an einem konkreten Detail → Pupillen- und Fokusgeometrie bleiben auf reale Distanz ausgerichtet → obere Lider entspannen minimal → Stirn reagiert asymmetrisch → Einatmung bricht vorzeitig ab → Hand verliert für einen Moment ihre aktuelle Aufgabe.

**Gegenwart kehrt zurück:** Geräusch oder Ansprache erreicht die Person → Augen fokussieren neu → Kiefer löst oder fixiert sich → Gewicht verlagert sich zum aktuellen Gegenüber → Hand beendet, verändert oder verweigert die begonnene Bewegung.

**Unterdrückte Zukunftsangst:** Blick hält scheinbar höflichen Kontakt → unteres Lid spannt → Schlucken verzögert den Satz → Schultern bleiben kontrolliert, während der Brustkorb flacher atmet → Finger korrigieren wiederholt einen Gegenstand.

**Institutionelle Mitwirkung trotz Zweifel:** Mund trägt ein soziales Halblächeln → Augen beteiligen sich nicht vollständig → Kopf nickt geringfügig → Schreibhand oder Stempelbewegung bleibt routiniert → Füße und Becken orientieren sich bereits zum Ausgang.

Anatomische Pflicht:

- ein eindeutig bestimmtes Blickziel und plausible Fokusdistanz;
- Mikroexpressionen zeitlich statt als starre Emotionsmaske;
- fünf anatomisch plausible Finger mit korrekter Griff- und Kontaktphysik;
- Atembewegung in Brustkorb, Hals, Schlüsselbein und Schulterstand konsistent;
- Körpergewicht und Fußkontakt folgen der Entscheidung zwischen Bleiben und Gehen;
- Erinnerung wird nicht durch transparentes Doppelgesicht oder schwebende Geister standardisiert;
- Alter, Haut, Haar und Haltung bleiben individuell und werden nicht als Weisheits- oder Verfallscode benutzt.

Bevorzugte Bewegungskette: Gegenwartsaufgabe → sensorische Spur → Fokusbindung → Atemunterbrechung → kurze Entkopplung der Hand → Erinnerung verändert Bedeutung → neues Blickziel → heutige Entscheidung.

### 16.9 DEJÀ-VU-3-DNA-Karte

```yaml
profile: AHMET-HAMDI-TANPINAR-04
status: mechanism_release
human_situation: Eine Person will eine gegenwärtige Entscheidung treffen, doch ein Klang oder Ort öffnet eine frühere Zeit, die ihre Verantwortung neu ordnet.
gold:
  mechanism: LM-06 Innere Zeit
  function: Äußere Minuten und erlebte Dauer laufen auseinander.
silver:
  mechanism: LM-12 Institutionelle Absurdität
  function: Eine künstliche Ordnung verspricht Zukunft und bindet die Person an ein Verfahren.
bronze:
  mechanism: RH-15 Semantische Rückkehr
  function: Die letzte Handlung verändert die Bedeutung der ersten Wahrnehmung.
thought_mode: DM-15 Geschichtete Zeit
counter_mode: DM-02 Systemisch
perspective: BW-02 rückblickendes Ich + BW-08 Institution
emotion_arc: vorläufige Ordnung → Erinnerung → Hüzün oder Hasret → widersprüchliche Zugehörigkeit → Entscheidungsdruck → unvollständige Kontinuität
body_arc: aktuelle Routine → Blickstopp → Atembruch → gehemmte Hand → neue Fokussierung → Gewichtsverlagerung → veränderte Handlung
form: kurze äußere Zeit; geschichtete Erinnerung; Leitmotiv; ironische Gegenkraft; Ende verändert Anfang
forbidden: Autorenimitation, ungeprüftes Zitat, Istanbul-Klischee, Uhren-Symbolinventur, nostalgische Verklärung, körperlose Erinnerung
```

### 16.10 Transformationsformeln

**Innere-Zeit-Formel:** aktuelle Pflicht → sensorische Spur → erinnerte Beziehung → Gegenwart dauert anders → äußere Unterbrechung → Entscheidung trägt beide Zeiten.

**Stadtgedächtnis-Formel:** heutiger Weg → materielle Spur → fremde oder eigene Erinnerung → widersprechende Stadtdeutung → körperliche Richtungsänderung → neue Verantwortung gegenüber dem Ort.

**Institutionsformel:** unbelegter Bedarf → überzeugender Begriff → Rolle und Verfahren → gesellschaftlicher Nutzen für Beteiligte → Zweifel wird mit mehr Organisation beantwortet → Regel offenbart ihren menschlichen Preis.

**Kontinuitätsformel:** geerbte Form → Bruch → Versuch der Wiederholung → notwendige Veränderung → Verlust eines Anteils → Fortsetzung ohne Identitätskopie.

**Hüzün-Formel:** sichtbare Fortdauer → Bewusstsein des Verlorenen → kurze Verbundenheit → keine Rückkehrmöglichkeit → gegenwärtige kleine Handlung statt dekorativer Trauer.

### 16.11 Qualitäts-, Quellen- und Rechteampel

| Bereich | Ampel | Begründung |
|---|---|---|
| Identität, Lebensdaten und berufliche Stationen | 🟢 | TEİS und TDV bieten belastbare biografische Grunddaten |
| Werkidentität und Publikationschronologie | 🟢/🟡 | zentrale Werke gut dokumentiert; Fortsetzungs-, Buch- und postume Fassungen getrennt halten |
| Beş Şehir-Fassungen | 🟢 | Erstausgabe 1946 und überarbeitete Ausgabe 1960 wissenschaftlich dokumentiert |
| Huzur-Grundarchitektur | 🟢 | Kapitel-, Zeit- und Rezeptionsstruktur belastbar erschlossen |
| Tanpınars Privatpsychologie aus Figuren | 🔴 | Autor, Erzähler und Figur bleiben getrennt |
| GitHub-Werklisten | 🟡 | Discovery, keine Edition |
| GitHub-Tweet- und Zitatsammlungen | 🔴 | kein Textbeleg und keine Zuschreibungsgrundlage |
| moderne Romanvolltexte auf GitHub | 🔴 | ohne konkrete Rechte- und Editionskette gesperrt |
| institutionelle Ironie als Mechanismus | 🟢 | auf abstrakter Ebene übertragbar |
| innere Zeit und Stadtgedächtnis | 🟢 | bei eigener Situation und ohne Stilkopie übertragbar |
| Hüzün als pauschale Markenästhetik | 🔴 | Begriff braucht Auslöser, Zeit, Beziehung, Gegenemotion und Handlung |

### 16.12 Verwendete Kernquellen

- [Türk Edebiyatı İsimler Sözlüğü: Ahmet Hamdi Tanpınar](https://teis.yesevi.edu.tr/madde-detay/ahmet-hamdi-tanpinar) — Biografie, Werkchronologie, ästhetische und wissenschaftliche Bezugspunkte; B1/B2.
- [TDV İslâm Ansiklopedisi: Tanpınar, Ahmet Hamdi](https://islamansiklopedisi.org.tr/tanpinar-ahmet-hamdi) — Lebenslauf, akademische Laufbahn und Werküberblick; B1.
- [TDV İslâm Ansiklopedisi: Huzur](https://islamansiklopedisi.org.tr/huzur--tanpinar) — Aufbau, Zeit, Figuren und Rezeption; B1/B2.
- [TDV İslâm Ansiklopedisi: Beş Şehir](https://islamansiklopedisi.org.tr/bes-sehir) — Entstehung, Fassungen und Stadtmonografie; B1/B2.
- [Modernite’nin Söylemsel Araçlarını İfşa Eden Bir Roman: Saatleri Ayarlama Enstitüsü](https://dergipark.org.tr/tr/pub/sosbilder/article/1115708) — Institution, Diskurs, Zeit und Ironie; B2.
- [Saatleri Ayarlama Enstitüsü’nde Toplumsal-Kurumsal Eleştiri ve İroni](https://dergipark.org.tr/tr/pub/fsmiadeti/article/86150) — Wertewandel, Institution und ironische Kritik; B2.
- [Bursa’da Zaman Şiirinde Zaman ve Mekân Algısı](https://dergipark.org.tr/en/pub/akademikincelemeler/article/418347) — Zeit, Raum, Erinnerung und kulturelles Gedächtnis; B2.
- [Beş Şehir’in Hafıza Mekânları](https://dergipark.org.tr/en/download/article-file/203827) — Stadt, Transformation und Gedächtnisraum; B2.

### 16.13 Offene Prüfaufträge

1. Editionsmatrix für *Huzur*, *Saatleri Ayarlama Enstitüsü* und die beiden Fassungen von *Beş Şehir* anlegen.
2. Je Werk drei kurze Textanker aus rechtmäßig zugänglichen Ausgaben prüfen; keine GitHub-Zeilen verwenden.
3. *Mahur Beste* einschließlich „Behçet Bey’e Mektup“ auf Figuren-Autor-Dialog und Unabgeschlossenheit untersuchen.
4. *Bursa’da Zaman* metrisch, klanglich und bildlogisch vollständig analysieren; berühmte Einzelzeilen erst danach freigeben.
5. Hüzün, Hasret, Keder und Huzursuzluk werkbezogen gegeneinander testen.
6. Ein neutrales GitHub-Metadatenschema entwickeln, das Titel, Autor, Ausgabe, Rechte, Zitatstatus und Commit trennt.
7. DEJÀ-VU-3-Testszene erstellen: heutige Behörde, künstlicher Zeitstandard, erinnerungsauslösender Klang, sichtbare Mikromimik und eine Handlung, die den Anfang neu deutet.

**Profilentscheidung:** Ahmet Hamdi Tanpınar wird nicht als Stimme oder nostalgische İstanbul-Ästhetik integriert. Freigegeben sind innere Zeit, geschichtete Erinnerung, Stadt als Gedächtnisraum, Kontinuität unter Veränderung, begrenzte Rückschau, institutionelle Absurdität, Ironie und semantische Rückkehr. GitHub bleibt Discovery- und Fehlzuschreibungsfilter; Werktext und Zitate benötigen externe Editionsprüfung.

## 17. Profil 05 — Yaşar Kemal

### 17.1 Profilstatus und Quellenlage

| Feld | Befund |
|---|---|
| Profilstatus | quellenkritisches Grundlagenprofil v1.0 |
| Identität | Kemal Sadık Göğceli, bekannt als Yaşar Kemal; Romancier, Erzähler, Journalist, Interviewautor und Sammler mündlicher Überlieferung |
| Lebensdaten | Geburt Ende Oktober 1923 nach eigener Angabe und TEİS; abweichende Jahresangaben in der Überlieferung; gestorben am 28. Februar 2015 in İstanbul |
| Hauptanker | *İnce Memed*-Tetralogie, *Dağın Öte Yüzü*, *Akçasazın Ağaları*, *Hüyükteki Nar Ağacı*, *Teneke*, *Ağrıdağı Efsanesi*, *Binboğalar Efsanesi*, *Bir Ada Hikâyesi*, Reportagen und *Ağıtlar* |
| Forschungsräume | Çukurova, Landbesitz, Arbeit, Mechanisierung, Aga- und Staatsmacht, Widerstand, Migration, mündliche Erinnerung, Naturzerstörung, Gemeinschaft und Würde |
| GitHub-Lage | keine belastbare wissenschaftliche Werkedition; überwiegend Rezension-Scraping, Quizdaten, Zeitungssammlungen, Metadaten und mutmaßlich unzulässige Digitalisate |
| Rechte | Autor 2015 verstorben; Werke eindeutig geschützt. Volltexte, Übersetzungen, Hörtexte, Comics und Digitalisate dürfen nicht aus GitHub übernommen werden |
| DEJÀ-VU-3-Freigabe | Landschaft als materielle Kraft, soziale Kausalität, kollektive Legendenbildung, mündliche Resonanz, Würde unter Druck, Veränderung durch Technik und Widerstand gegen Herrschaft |

### 17.2 GitHub-Prüfung

| GitHub-Fund | Inhalt | Risiko | Ampel / Nutzung |
|---|---|---|---|
| [afyildizz/temel_tensoflow2_egitimi](https://github.com/afyildizz/temel_tensoflow2_egitimi/blob/master/yorum_alma.ipynb) | Notebook mit Links zu Online-Produktrezensionen zu *İnce Memed* | Leserkommentare statt Werktext; Plattformdaten und Nutzungsrechte beachten | 🟡 geeignet als technisches Scraping-Beispiel, nicht als Literaturquelle |
| [warezturkey/icerikler](https://github.com/warezturkey/icerikler/blob/master/yerel-kahramanlar-2) | Dateiliste mit einer Zeitungs-/Comicadaption von *Ağrıdağı Efsanesi* | geschütztes Werk und geschützte Adaption; Rechtekette nicht ausgewiesen | 🔴 weder herunterladen noch übernehmen oder analysieren |
| bahadiri/Millionaire | Quiz- und Antwortdaten mit Autorennennungen | vereinfachte oder fehleranfällige Wissensdaten | D; keine Biografie- oder Werkbehauptung |
| generische Zeitungs-Gists | vermischte Artikel, Nachrufe, politische und kulturelle Nennungen | Artikelgrenzen, Metadaten und Rechte teils unklar | 🟡 nur Fundhinweis; Originalpublikation beschaffen |
| zemberek-nlp-Testressourcen | zufällige Namensnennungen in Satzgrenzentests | technisch sinnvoll, literarisch bedeutungslos | 🟢 für Tokenisierungstest, 🔴 für Literaturprofil |
| unspezifische Datensätze zu „Yasar Kemal“ | häufig Namensgleichheiten oder irrelevante Personen | Entity-Verwechslung | 🔴 Identität zuerst auflösen |

**GitHub-Entscheidung:** GitHub ist bei Yaşar Kemal ein technischer und rechtlicher Warnraum. Es liefert weder eine freigegebene Textbasis noch ein hinreichend kuratiertes Werk-, Folklore- oder Emotionskorpus.

**Neue Schutzregel:** Adaptionen werden getrennt vom Roman geprüft. Die Nennung Yaşar Kemals neben einer PDF-, Comic- oder Zeitungsdatei erlaubt weder die Nutzung des Textes noch der Bilder. Leserrezensionen beschreiben Rezeption, nicht Werkidentität.

### 17.3 Historischer, sprachlicher und materieller Horizont

Yaşar Kemals Kindheit und Jugend sind mit dem ländlichen Çukurova-Raum, Mehrsprachigkeit und unterschiedlichen Arbeitsformen verbunden. TEİS dokumentiert Türkisch im Dorf- und Kürdisch im Familienkontext. Diese Mehrsprachigkeit ist als konkrete soziale Erfahrung zu verstehen, nicht als exotische Autorenmarke.

Er arbeitete unter anderem als Landarbeiter, Arbeiteraufseher, Traktorfahrer, Wasserwächter in Reisfeldern, Aushilfslehrer, Bibliothekskraft und Briefschreiber. Später wurde er Journalist und prägte eine literarisch verdichtete Form der Reportage. Diese Tätigkeiten bilden einen belastbaren Erfahrungshorizont für Arbeit, Boden, Krankheit, Bürokratie und technische Veränderung. Sie erklären jedoch keine Figur automatisch.

Seine frühen Folklorearbeiten führten 1943 zur Sammlung *Ağıtlar*. Mündliche Kultur, Erzählen, Lied, Klage, Legende und kollektive Variation bleiben deshalb eigenständige Werk- und Forschungsräume. Ein von ihm gesammelter Ağıt ist nicht automatisch seine eigene Dichtung; Informantin oder Informant, Aufführungssituation, Ort, Variante und Editionsform müssen erhalten bleiben.

Der Übergang von arbeitsintensiver Landwirtschaft zu Mechanisierung verändert in den Çukurova-Werken nicht nur Technik. Er verändert Besitz, Beschäftigung, Migration, Abhängigkeit, Natur und menschliche Beziehungen. Diese Verbindung von materiellem Wandel und emotionaler Erfahrung ist für DEJÀ-VU-3 zentral.

### 17.4 Werkrahmen

#### İnce Memed

Der erste Band erschien 1955; die vier Bände entstanden über mehrere Jahrzehnte. Im Zentrum steht Memeds Weg vom ausgebeuteten Dorfjungen zur gesellschaftlich verschieden gedeuteten Widerstandsfigur. Das Ağa-System, Landbesitz, Gewalt, patriarchale Ordnung, Bürokratie und die Lebensbedingungen der Dörfer erzeugen den Konflikt mit.

**Textbeobachtung:** Memed wird nicht allein durch individuelle Tapferkeit zur Legende. Er entsteht in Erzählungen, Hoffnungen, Ängsten und Übertreibungen anderer Menschen. Seine Gegner sind nicht austauschbare Bösewichte; Herrschaft erneuert sich durch Besitz, Verwandtschaft, Amt und Gewalt.

**Interpretation:** Der Roman fragt, wie Widerstand notwendig werden kann und zugleich neue Gewalt erzeugt. Die Tötung eines Unterdrückers beendet das System nicht automatisch. Die Gemeinschaft braucht ein Bild von Memed, doch dieses Bild kann den Menschen hinter der Legende verschlucken.

**Abstraktion:** Eine Widerstandsfigur wird stark, wenn individuelle Entscheidung, materielle Zwangslage, kollektive Hoffnung und moralischer Preis gleichzeitig sichtbar bleiben.

#### Dağın Öte Yüzü

Die Trilogie verbindet Dorfleben, saisonale Arbeit, Armut, Migration, Naturbedingungen und gemeinschaftliche Imagination. Mythos und Heiligenbildung entstehen nicht als dekoratives „Volksglauben“-Element, sondern innerhalb von Angst, Hoffnung, Herrschaft und Überlebensdruck.

**Textbeobachtung:** Die Gemeinschaft erzeugt Erzählungen, um eine kaum erträgliche Lage deutbar und handhabbar zu machen. Wiederholung und kollektive Bestätigung verändern, was als wirklich gilt.

**Interpretation:** Mythos kann Schutz, Zusammenhalt und Handlungskraft erzeugen; er kann aber auch Verantwortung verschieben und neue Macht bilden.

**Abstraktion:** Kollektive Imagination braucht eine materielle Ursache und einen sozialen Preis. Sie ist weder bloße Lüge noch automatisch höhere Wahrheit.

#### Akçasazın Ağaları und Hüyükteki Nar Ağacı

*Demirciler Çarşısı Cinayeti* und *Yusufçuk Yusuf* zeigen die Veränderung alter Herrschaftsformen unter Kapitalisierung und Industrialisierung. *Hüyükteki Nar Ağacı* richtet den Blick auf Arbeitslosigkeit und die Folgen landwirtschaftlicher Mechanisierung.

**Textbeobachtung:** Maschinen, Märkte, Landtitel und neue wirtschaftliche Rollen verändern alte Beziehungen. Die neue Ordnung beseitigt Gewalt und Abhängigkeit nicht; sie verteilt sie anders.

**Interpretation:** Yaşar Kemals Veränderungslogik ist weder Maschinenfeindlichkeit noch Verklärung der alten Ağa-Welt. Entscheidend ist, wer vom Wandel profitiert, wer verdrängt wird und wie sich Natur und Arbeit gemeinsam verändern.

**Abstraktion:** Technischer Fortschritt wird erzählerisch konkret, wenn Maschine → Besitzverschiebung → Arbeitsverlust → Familienkonflikt → Körperfolge → Entscheidung abgebildet wird.

#### Teneke

Der Roman verbindet Reisproduktion, Gesundheit, lokale Macht und Verwaltung. Wirtschaftliches Interesse wirkt über Wasser, Boden, Insekten, Krankheit, Genehmigung und Amt unmittelbar auf Körper.

**Abstraktion:** Ein ökologischer Konflikt wird stark, wenn Umweltveränderung, Profit, Verwaltungsentscheidung und körperliches Risiko kausal verbunden sind.

#### Efsane, Ağıt und mündliche Tradition

*Üç Anadolu Efsanesi*, *Ağrıdağı Efsanesi* und *Binboğalar Efsanesi* greifen auf mündliche, historische und neu komponierte Erzählformen zurück. Dabei müssen überlieferte Tradition, schriftstellerische Bearbeitung und eigenständige Neuschöpfung getrennt werden.

**Schutz:** Keine traditionelle Gemeinschaft wird zur homogenen Stimme erklärt. Efsane ist keine beliebige Fantasy, Ağıt keine allgemeine traurige Stimmung und Mehrsprachigkeit keine Folkloredekoration.

#### Bir Ada Hikâyesi

Die Tetralogie verbindet Krieg, Vertreibung, Bevölkerungsaustausch, Erinnerung und den schwierigen Aufbau einer neuen Gemeinschaft. Menschen tragen unterschiedliche Sprachen, Verluste, Schuldverhältnisse und Hoffnungen auf eine fiktive Insel.

**Abstraktion:** Neue Zugehörigkeit entsteht nicht durch das Vergessen früherer Gewalt, sondern durch geteilte Arbeit, Konflikt, Erinnerung und wiederholte Entscheidung.

### 17.5 Denkarchitektur

| Ebene | Operation | Yaşar-Kemal-Profil | DEJÀ-VU-3-Nutzung |
|---|---|---|---|
| materielle Kausalität | Besitz und Arbeit erzeugen private Folgen | Land, Wasser, Maschine, Markt, Ağa und Amt formen Beziehungen | jede Emotion an mindestens eine reale Bedingung binden |
| Landschaft als Kraftfeld | Natur ermöglicht und begrenzt Handlung | Hitze, Ebene, Berg, Wasser, Pflanze und Tier reagieren auf Arbeit und Macht | Landschaft muss Handlung verändern, nicht illustrieren |
| kollektive Erinnerung | Gemeinschaft erzählt Figuren und Ereignisse weiter | Ağıt, Efsane, Gerücht und Zeugnis erzeugen soziale Wirklichkeit | Varianten und Sprecherpositionen sichtbar halten |
| Widerstand | Unterdrückung erzeugt Gegenhandlung | Aufbegehren kann Würde schaffen und Gewalt fortsetzen | Ursache, Ziel, Preis und Wirkung auf Dritte führen |
| Veränderung | Technik und Kapital ordnen Beziehungen neu | Mechanisierung ersetzt alte Abhängigkeit teilweise durch neue | kein linearer Fortschritts- oder Verfallsmythos |
| Würde | Person widersetzt sich ihrer Reduktion | Arbeitende, Frauen, Kinder, Vertriebene und alte Menschen besitzen Handlungsmacht | keine Elendsästhetik und kein Retterblick |
| Mythopoetik | reale Erfahrung wird kollektiv vergrößert | Person oder Ereignis gewinnt durch Wiedererzählen epische Dimension | Vergrößerung auf menschliche Folge zurückführen |

**Leitmodus:** DM-09 Materiell-sozial.  
**Gegenmodus:** DM-10 Narrativ.  
**Blind-Spot-Test:** Das System darf den Menschen nicht verschlucken und die Legende darf die materielle Ursache nicht ersetzen. Keine romantisierte Armut, kein edler Bandit als automatische Lösung und keine Naturmystik ohne Arbeit, Besitz und Körper.

### 17.6 Emotionsarchitektur

| Emotion/Zustand | Auslöser | Gegenkraft | Körper- und Handlungsspur | Abgrenzung |
|---|---|---|---|---|
| İsyan | wiederholte Gewalt, Enteignung oder Erniedrigung | Angst, Bindung, Verantwortung | Atemdruck steigt, Gewicht geht nach vorn, Hand greift Werkzeug oder setzt Grenze | nicht automatisch Waffe oder Schrei |
| Korku | Ağa, Amt, Hunger, Krankheit, Verfolgung oder Naturgefahr | Gemeinschaft, Wissen, Fluchtweg | Blick prüft Gelände und Personen, Atem wird flach, Körper schützt andere | keine großen Augen als Standard |
| Onur | Anspruch auf gerechte Behandlung | ökonomische Abhängigkeit | Haltung richtet sich trotz Erschöpfung auf, Stimme wird genauer, Hände verweigern eine Geste | nicht Hochmut |
| Umut | Möglichkeit gemeinsamer Veränderung | Erfahrung wiederholten Scheiterns | Aufmerksamkeit öffnet sich, kleine kollektive Bewegung beginnt, Arbeit wird neu verteilt | kein obligatorisches Lächeln |
| Yas | Tod innerhalb einer Beziehung und Gemeinschaft | Erinnern, Sprechen, Ritual | Stimme verändert Atem und Rhythmus, Hände halten oder lösen Kontakt, Routine stockt | Ağıt nicht als anonyme Trauermusik |
| Öfke | konkrete Grenzverletzung | Sorge um Folgen | Kiefer und Hals spannen, Bewegung wird präzise, Abstand verändert sich | Aggression nicht mit Widerstand gleichsetzen |
| Çaresizlik | blockierte Wege und fehlende Ressourcen | kollektive Erfindung oder Solidarität | Blick sucht keine Option mehr, Arbeit wird mechanisch, Schultern verlieren Initiation | keine Charaktereigenschaft der Armen |
| Aidiyet | geteilte Arbeit, Sprache, Erinnerung und Schutz | Vertreibung oder Ausschluss | Körper findet Rhythmus mit anderen, Blick verteilt Aufmerksamkeit, Stimme antwortet | Gemeinschaft nicht homogenisieren |
| Hasret / Gurbet | Entfernung von Ort, Menschen oder Lebensform | neue Bindung und zusätzliche Sicht | Person reagiert auf Geruch, Wetter oder Klang; Hand wiederholt vertraute Arbeit | Gurbet enthält soziale Fremdheit, nicht nur Sehnsucht |

### 17.7 Erzähltechnik, Sprache und mündliche Energie

| Mechanismus | Wirkung | Produktionsregel |
|---|---|---|
| epische Natur-Mensch-Verflechtung | vergrößert Konflikt, ohne Materialität zu verlieren | Wetter, Boden, Arbeit und Macht kausal verbinden |
| Tekrar | erzeugt mündliche Erinnerung und wachsenden Druck | jede Wiederholung verändert Sprecher, Wissen oder Einsatz |
| kollektive Variation | zeigt, wie eine Legende entsteht | mindestens zwei abweichende Gemeinschaftsstimmen |
| Aufzählung | macht Fülle, Arbeit oder Zerstörung körperlich erfahrbar | Auswahl funktional halten; keine dekorative Pflanzenliste |
| direkte Rede und Register | verteilt soziale Macht | Dialekt nur quellen- und situationsgebunden, keine Karikatur |
| Zeugenschaft | verbindet beobachtete Realität und moralische Position | Beobachtergrenze und mögliche Auswahl benennen |
| Vergrößerung | macht menschliche Erfahrung episch | Überhöhung durch eine konkrete Körper- oder Arbeitsfolge erden |
| semantische Rückkehr | Gerücht oder Bild kommt verändert zurück | Schluss zeigt, was die Gemeinschaft aus dem Menschen gemacht hat |

**Rhetorische Führung:** RH-13 Zeugenschaft.  
**Unterstützung:** RH-04 Tekrar und RH-10 Leitmotiv.  
**Formschutz:** Keine imitierte Yaşar-Kemal-Satzmelodie, keine künstlichen regionalen Redewendungen, keine Naturinventur und keine austauschbare „anatolische“ Bildsprache.

### 17.8 Perspektive, Anatomie und sichtbare Emotion

Eine Yaşar-Kemal-basierte Szene zeigt Menschen in einer materiellen Tätigkeit: gehen, säen, ernten, Wasser lenken, Last tragen, warten, verstecken, reparieren, pflegen oder eine Grenze verteidigen. Das Gesicht reagiert innerhalb dieser Handlung.

**Unterdrückter Widerstand:** Blick bleibt zunächst auf der Arbeit → Kiefer fixiert → Nasenflügel und Atemdruck verändern sich leicht → Finger schließen präziser um Werkzeug oder Stoff → Schwerpunkt richtet sich auf → Blick wechselt zur Machtperson → Handlung stoppt oder wird bewusst anders fortgesetzt.

**Kollektive Angst:** einzelne Person scannt Gelände → zweite Person folgt dem Blick → Atemrhythmen verkürzen sich unterschiedlich → Hände sichern Kind, Last oder Ausgang → Körper bilden keinen dekorativen Block, sondern unterschiedliche Schutzaufgaben.

**Würde nach Erschöpfung:** Brustkorb hebt sich gegen flachen Atem → Nacken richtet sich ohne Heldenpose → Blick hält Kontakt → Mund bleibt angespannt, aber sprechfähig → Hände zeigen Arbeitsspuren und setzen eine reale Grenze.

**Hoffnung ohne Kitsch:** Aufmerksamkeit wechselt von Gefahr zu einer machbaren Aufgabe → Brauen- und Lidspannung sinken geringfügig → Gewicht verlagert sich nach vorn → eine Hand beginnt Arbeit, die andere lädt zur Beteiligung ein → kein automatisches Lächeln.

Anatomische Pflichtfelder:

- Hände mit fünf plausiblen Fingern, Arbeitskonsistenz, Druckstellen und korrektem Werkzeugkontakt;
- Wirbelsäule, Schultergürtel, Becken, Knie und Füße tragen Last und Gelände physikalisch glaubwürdig;
- Hitze, Staub, Regen, Wind und Erschöpfung wirken konsistent auf Haut, Haar, Kleidung und Atmung;
- Blickziel und Entfernung bleiben eindeutig; keine Pupillen als Moralcode;
- Verletzung, Behinderung, Alter und Armut werden nicht als Symbol für Reinheit oder Schuld verwendet;
- Landschaftsmaßstab darf die Person klein zeigen, aber nicht ihrer Handlungsmacht berauben;
- maximal zwei zentrale Personen im DEJÀ-VU-3-Bild; Gemeinschaft kann über Spuren, Stimmen, Wege oder Hintergrundhandlung anwesend sein.

Bevorzugte Handlungskette: materielle Aufgabe → Umweltwiderstand → Macht greift ein → Blick erkennt Grenze → Atem- und Griffwechsel → Entscheidung → Kontakt mit Boden, Wasser, Werkzeug oder Person → Landschaft trägt die Folge weiter.

### 17.9 DEJÀ-VU-3-DNA-Karte

```yaml
profile: YASAR-KEMAL-05
status: mechanism_release
human_situation: Eine arbeitende Person erkennt, dass eine neue Maschine nicht nur ihre Tätigkeit ersetzt, sondern Besitz, Familie und Zukunft neu verteilt.
gold:
  mechanism: LM-05 Materielle Kausalität
  function: Land, Technik, Eigentum und Arbeit erzeugen den privaten Konflikt.
silver:
  mechanism: LM-01 Kollektive Erinnerung
  function: Die Gemeinschaft erzählt Verlust und Widerstand in konkurrierenden Fassungen.
bronze:
  mechanism: RH-13 Zeugenschaft
  function: Eine begrenzte beobachtende Stimme hält Körper, Arbeit und Macht zusammen.
thought_mode: DM-09 Materiell-sozial
counter_mode: DM-10 Narrativ
perspective: BW-14 Körper + BW-09 variierender Chor
emotion_arc: Erschöpfung → Angst → Erniedrigung → İsyan → kollektive Hoffnung → Preis ohne garantierte Erlösung
body_arc: Arbeitsrhythmus → Umweltwiderstand → kontrollierte Spannung → Griffwechsel → aufgerichtete Grenze → gemeinsame Handlung → Nacherschöpfung
form: materielle Detailkette; Landschaft als Kraft; veränderte Wiederholung; mehrere Gemeinschaftsstimmen; Schluss prüft die Legende
forbidden: Autorenimitation, Volltextnutzung, Armutsromantik, edler-Bandit-Klischee, homogene Dorfstimme, Naturdekoration, erfundener Dialekt
```

### 17.10 Transformationsformeln

**Landschaftsformel:** konkrete Arbeit → Boden/Wasser/Wetter antwortet → Besitzregel greift ein → Körper trägt Folge → Entscheidung verändert Raum und Beziehung.

**Widerstandsformel:** wiederholte Erniedrigung → materieller Verlust → verständliche Angst → kleine Grenzüberschreitung → Gemeinschaft erzählt sie weiter → Person wird zur Figur → Legende fordert einen neuen Preis.

**Mechanisierungsformel:** neue Technik → Produktivität steigt → Arbeit verschwindet oder wandert → Besitz konzentriert sich → Familie verliert Handlungsspielraum → Gegenorganisation oder Migration.

**Ağıt-Formel:** konkreter Verlust → benannte Beziehung → Stimme und Atem organisieren Erinnerung → Gemeinschaft antwortet verschieden → Handlung bewahrt, verändert oder bestreitet das Erinnerte.

**Neue-Zugehörigkeit-Formel:** Vertreibung → Ankunft ohne Sicherheit → geteilte Arbeit → Konflikt der Erinnerungen → gegenseitiger Schutz → Zugehörigkeit als wiederholte Praxis.

### 17.11 Qualitäts-, Quellen- und Rechteampel

| Bereich | Ampel | Begründung |
|---|---|---|
| Name, Lebenszeit und Grundbiografie | 🟢/🟡 | gut dokumentiert; Geburtsjahr in Quellen abweichend |
| berufliche und sprachliche Horizonte | 🟢 | TEİS und Verlagsbiografie bieten belastbare Grundlinien |
| Werkchronologie | 🟢 | bibliografisch breit dokumentiert |
| autobiografische Details als Werkerklärung | 🟡/🔴 | nur als belegter Horizont; keine Figur-Autor-Gleichsetzung |
| mündliche Sammlungen | 🟡 | Quelle, Informant, Variante und Herausgabe pro Text prüfen |
| GitHub-Rezensionsdaten | 🟡 | Rezeptions- und Technikschicht, keine Werkquelle |
| GitHub-PDFs, Comics und Volltexte | 🔴 | geschützt und ohne belastbare Rechtekette |
| Landschafts- und Materialmechanismen | 🟢 | abstrakt und situationsgebunden übertragbar |
| Dialekt- oder Stimmenimitation | 🔴 | keine stilistische Kopie oder erfundene Regionalität |
| ökologische und soziale Transformation | 🟢 | wenn Natur, Arbeit, Macht und Körper gemeinsam modelliert werden |
| Widerstand als reine Heldengeschichte | 🔴 | Preis, Gewaltfolge und kollektive Wirkung erforderlich |

### 17.12 Verwendete Kernquellen

- [Türk Edebiyatı İsimler Sözlüğü: Yaşar Kemal](https://teis.yesevi.edu.tr/madde-detay/yasar-kemal) — Biografie, Mehrsprachigkeit, Arbeit, Folklore, Werkchronologie und Poetik; B1/B2.
- [Yapı Kredi Yayınları: Yaşar Kemal](https://www.yapikrediyayinlari.com.tr/yazarlar/yasar-kemal-2) — Verlagsbibliografie und biografischer Überblick; B1-artige Verlagsquelle.
- [Yapı Kredi Yayınları: İnce Memed 1](https://www.yapikrediyayinlari.com.tr/ince-memed-1.aspx) — aktuelle Ausgabe, ISBN und Werkbeschreibung; bibliografischer Prüfpfad.
- [Yaşar Kemal’in Romanlarının soziologische Struktur aus feministischer Perspektive](https://dergipark.org.tr/en/download/article-file/960907) — Patriarchat, Land, Bürokratie und weibliche Handlungsmacht; B2.
- [İstanbul’un Kentleşme Deneyiminin Edebiyatçı Tanıklığı: Yaşar Kemal](https://dergipark.org.tr/tr/download/article-file/3546023) — Mechanisierung, Kapitalisierung, Migration, Natur und Veränderung; B2.
- [Türkiye’de Köy Romanını Yeniden Yorumlamak](https://dergipark.org.tr/en/download/article-file/1306957) — Landbesitz, kapitalistische Transformation und Widerstand; B2.
- [Gülizarlan Ninesi üzerine ekofeministische Untersuchung](https://dergipark.org.tr/en/download/article-file/2281024) — Naturzerstörung, Macht, Frauen und Kinder; B2.
- [Yaşar Kemal’in Romanlarında Dağlar](https://dergipark.org.tr/tr/download/article-file/5577069) — Raum, Gesellschaft und Landschaft; B2, Aktualitäts- und Methodenprüfung fortsetzen.

### 17.13 Offene Prüfaufträge

1. Editionsmatrix für die vier *İnce Memed*-Bände samt Erstveröffentlichung, Verlag und verwendbarer Textgrundlage erstellen.
2. *Ağıtlar* hinsichtlich Informanten, Regionen, Varianten und editorischer Eingriffe prüfen.
3. *Dağın Öte Yüzü* auf kollektive Mythenbildung, Geschlecht und materielle Angst werkgenau untersuchen.
4. *Teneke* als Umwelt–Verwaltung–Gesundheits-Kausalmodell profilieren.
5. *Akçasazın Ağaları* und *Hüyükteki Nar Ağacı* für Mechanisierung, Besitzwechsel und Arbeitsmigration vergleichen.
6. *Bir Ada Hikâyesi* mit historischer Forschung zu Vertreibung und Bevölkerungsaustausch gegenprüfen; keine Gemeinschaftserfahrung vereinheitlichen.
7. GitHub-Suchroutine um automatische Warnfelder für Volltext, Scan, Comicadaption, Rezension und Namensgleichheit erweitern.
8. Eigenständigen DEJÀ-VU-3-Testtext erstellen: Landarbeiterin, neue Maschine, bedrohte Würde, zwei widersprechende Dorfstimmen, anatomisch präzise Grenzhandlung.

**Profilentscheidung:** Yaşar Kemal wird als Mechanismengruppe integriert: materielle Kausalität, Landschaft als handelndes Kraftfeld, kollektive Erinnerung, mündliche Variation, Wandel von Arbeit und Besitz, Würde und Widerstand mit realem Preis. Gesperrt bleiben Autorenimitation, Dialektkopie, romantisierte Armut, homogene Dorfstimmen und sämtliche ungeklärten GitHub-Volltexte oder Adaptionen.

## 18. Profil 06 — Hüzün–Hasret–Gurbet

### 18.1 Profilstatus, Zweck und methodische Grenze

| Feld | Befund |
|---|---|
| Profilstatus | quellenkritisches Emotions- und Situationsprofil v1.0 |
| Gegenstand | drei verwandte, aber nicht austauschbare Begriffe der türkischen Literatur- und Aufführungstraditionen |
| GitHub-Lage | Wortlisten, Polaritätslexika und Zufallskorpora vorhanden; kein hinreichend kontextualisiertes literarisches Hüzün–Hasret–Gurbet-Korpus gefunden |
| Arbeitsregel | Begriff, Auslöser, Gegenüber, Zeit, Raum, Körper, Handlung und gesellschaftliche Ursache gemeinsam prüfen |
| Interpretationsgrenze | keine Behauptung eines einheitlichen „türkischen Gefühls“; Bedeutung bleibt werk-, epochen-, gattungs- und situationsabhängig |
| DEJÀ-VU-3-Freigabe | differenzierte Emotionsverläufe, Körperketten, Perspektiven, räumliche Ursachen und Transformationsformeln |

Die folgenden Definitionen sind **operationale literarische Abstraktionen**, keine endgültigen Wörterbuchdefinitionen. Ein konkretes Werk kann sie verschieben, verbinden oder bewusst unterlaufen. Tatsache, Textbeobachtung, Interpretation und kreative Übertragung bleiben getrennt.

### 18.2 GitHub-Ressourcenampel

| Ressource | Befund | Ampel | Zulässige Nutzung |
|---|---|---|---|
| [StarlangSoftware/TurkishSentiNet](https://github.com/StarlangSoftware/TurkishSentiNet) | türkisches HisNet mit Polaritätsannotation und semantischen Nachbarschaften | 🟢/🟡 | lexikalische Hilfsschicht; keine literarische Emotionsentscheidung |
| [TurkishSentiNet-C](https://github.com/StarlangSoftware/TurkishSentiNet-C) / [TurkishSentiNet-Py](https://github.com/StarlangSoftware/TurkishSentiNet-Py) | Implementierungen für technische Verarbeitung | 🟡 | reproduzierbare Abfragen; Daten- und Lizenzpflichten getrennt prüfen |
| [all-words-in-all-languages: Turkish.txt](https://github.com/eymenefealtun/all-words-in-all-languages/blob/main/Turkish/Turkish.txt) | Wortformen zu *gurbet* und *hasret*, aber ohne literarischen Kontext | 🟡/🔴 | Suchformen entdecken; keine Semantik oder Quellenbehauptung |
| [TezFlask: TumKelimeKokleri.txt](https://github.com/ayseelgoren/TezFlask/blob/master/TumKelimeKokleri.txt) | Wortstammliste ohne Werk-, Beziehungs- und Emotionskontext | 🟡/🔴 | Tokenisierungshilfe, nicht Interpretation |
| zufällige Nachrichten-/Klassifikationsdatensätze | einzelne Treffer ohne kontrollierten literarischen Kontext | 🔴 | nicht in das Literaturkorpus übernehmen |

**GitHub-Entscheidung:** Polarität beantwortet höchstens, ob ein Ausdruck tendenziell positiv, negativ oder neutral markiert wird. Sie beantwortet nicht, ob eine Figur Hüzün, Hasret, Gurbet, Keder, Hicran oder Efkâr erlebt. Diese Entscheidung benötigt Werk, Beziehung, Situation, Zeit, Körper und soziale Ursache.

### 18.3 Kerntrennung

| Begriff | Operativer Kern | Objekt/Beziehung | Zeit und Raum | typische Gegenkraft | Nicht gleichsetzen mit |
|---|---|---|---|---|---|
| **Hüzün** | affektives Feld wahrgenommenen Verlusts, beschädigter Kontinuität oder Vergänglichkeit | kann klar benannt oder diffus über Person, Stadt, Zeit, Gemeinschaft oder Selbst verteilt sein | Vergangenheit wirkt in die Gegenwart; Raum kann Spuren tragen | Hoffnung, Sinn, Nähe, Solidarität, Schönheit | Depression, Keder, Melancholie oder bloße Traurigkeit |
| **Hasret** | gerichtetes Vermissen und Begehren von Nähe | abwesende Person, Heimat, Zeit, Zustand, Sprache oder Möglichkeit | Distanz bleibt als Vektor spürbar; Zukunft kann Wiederkehr imaginieren | Hoffnung auf Kontakt, Angst vor endgültigem Verlust | Hicran, allgemeine Trauer oder romantische Liebe |
| **Gurbet** | soziale und räumliche Lage des Fortseins, Fremdseins oder Nicht-Zugehörens | Herkunftsort, Zurückgebliebene, neue Umgebung, Arbeit, Institution und Sprache | Entfernung, Migration, Exil, Reise oder langes Dazwischen | Aidiyet, neue Bindung, Rückkehr, Anpassung, Widerstand | eine Emotion; Gurbet kann Hasret und Hüzün auslösen, muss es aber nicht |

**Minimaltest:** Hüzün beantwortet vor allem „Welche Verlust- oder Vergänglichkeitsstimmung färbt die Gegenwart?“. Hasret beantwortet „Wohin oder zu wem zieht die fehlende Nähe?“. Gurbet beantwortet „Unter welchen räumlichen und sozialen Bedingungen lebt die Person fern oder fremd?“

### 18.4 Historische und gattungsspezifische Register

| Register | Hüzün | Hasret | Gurbet | Schutzregel |
|---|---|---|---|---|
| Divan | Teil eines differenzierten Feldes aus gam, keder, melâl, hicran und weiteren Begriffen | auf Geliebte, Ort, frühere Nähe oder metaphysisches Gegenüber gerichtet | Fremde, Entfernung, garip-Sein; weltliche und tasavvufische Lesarten möglich | einzelnen Beyt und Mazmun-Zusammenhang prüfen |
| Tasavvuf | kann Erkenntnis der eigenen Begrenztheit und Ausrichtung auf Wahrheit markieren | Nähe zum göttlichen Gegenüber oder verlorener Einheit, werkabhängig | Welt- oder Ichferne kann metaphorisch werden | keine Wellness-Spiritualität und keine universelle Sufi-Deutung |
| Halk/Âşık/Türkü | gemeinschaftlich singbare Trauer- und Erinnerungslage | Zurückgelassene, Heimat, Geliebte, Familie | Weg, Militärdienst, Arbeit, Migration; *gurbet havası* als kulturell spezifische Form | Variante, Aufführung, Region und Informant dokumentieren |
| moderne Lyrik und Stadt | beschädigte Zeit, Erinnerung, Öffentlichkeit oder Selbstverhältnis | verlorene Zeit, Person, Stadt oder mögliche Zukunft | Entfremdung kann räumlich, sozial und sprachlich werden | nicht jede urbane Melancholie als Hüzün etikettieren |
| Arbeitsmigration/Diaspora | Einsamkeit und Verlust können mit Würde, Hoffnung und Solidarität koexistieren | Familie, Sprache, Herkunft und versäumtes Leben | Aufenthaltsrecht, Arbeit, Ausbeutung, Wohnen, Registerwechsel und Generation | Migration nicht auf Verlust reduzieren; neue Zugehörigkeit mitführen |

### 18.5 Kausalitätsarchitektur

Die Begriffe werden nicht aus einem traurigen Gesicht rückwärts erraten. Die Pflichtkette lautet:

**materielle oder relationale Situation → benannte Bindung → räumliche Distanz → Zeitrichtung → Gegenemotion → Körperreaktion → Handlung → sozialer Preis oder neue Zugehörigkeit.**

Beispiele der Trennung:

- Eine Arbeiterin lebt in Gurbet, empfindet Hasret nach ihrem Kind und trägt Hüzün über verpasste Lebenszeit. Drei Ebenen, nicht drei Synonyme.
- Ein Mann kann in Gurbet neugierig, stolz und erleichtert sein, ohne Hasret im aktuellen Moment.
- Eine Person kann Hasret nach einer früheren Zukunft empfinden, obwohl kein geografischer Gurbet-Raum vorliegt.
- Hüzün kann aus kollektivem Gedächtnis entstehen, ohne ein einziges abwesendes Gegenüber zu besitzen.

### 18.6 Körper- und Handlungsarchitektur

| Ebene | Hüzün | Hasret | Gurbet |
|---|---|---|---|
| Blick | verweilt auf Spur, Oberfläche oder wiederkehrendem Detail | sucht Eingang, Weg, Nachricht, Stimme oder erwartete Bewegung | kartiert Regeln, Personen, Schilder und sichere Ausgänge |
| Lider/Brauen | leicht verringerte Öffnung; Brauenbewegung abhängig von Erinnerung und Gegenkraft | Aufmerksamkeit erhöht; innere Brauen können kurz ansteigen, dann halten | wechselnde Wachsamkeit; keine festgeschriebene Trauermimik |
| Mund/Kiefer | reduzierte Mundbewegung, gelegentliches Pressen oder unvollendetes Sprechen | Lippen bereiten Namen oder Antwort vor; Kiefer hält Kontaktimpuls zurück | Artikulation und Register werden kontrolliert; Kiefer kann bei Missverständnis spannen |
| Atem | längeres Ausatmen, Pause vor neuer Handlung | kurzer Atemstopp beim vermeintlichen Signal; Einatmung richtet Körper aus | Atem wird bei institutioneller oder sprachlicher Unsicherheit reguliert |
| Hände | berühren, ordnen, falten oder bewahren eine Spur | beginnen Kontakt, schreiben, wählen, öffnen und stoppen | sichern Dokumente/Gegenstände, lernen Abläufe, arbeiten oder markieren Grenze |
| Körperachse | Initiation kann sinken, Beziehung zur Welt bleibt bestehen | Orientierung zieht zum abwesenden Objekt; Gewicht beginnt vor Kontakt | Körper passt Distanz, Stimme und Bewegungsradius an unbekannte Regeln an |
| Handlung | erinnern, bewahren, teilen, weiterarbeiten oder loslassen | Nachricht senden, Route wiederholen, warten, reisen oder Kontakt verweigern | übersetzen, arbeiten, navigieren, dazugehören, widerstehen oder neue Bindung bauen |

Anatomische Pflicht: Blickziel, Lidspannung, Brauen, Mund, Kiefer, Schlucken, Hals, Brustkorb, Schulterstand, Hände, Gewichtsverlagerung und Folgebewegung müssen denselben Moment erzählen. Tränen sind optional und niemals der alleinige Emotionsbeleg.

### 18.7 Gesichtsketten

**Hüzün:** Spur wird erkannt → Blick bleibt einen Moment zu lang → Unterlider verlieren etwas Spannung → Mund schließt unvollständig → langer Ausatem → Hand ordnet den Gegenstand statt ihn wegzuwerfen → Körper setzt die Pflicht langsamer fort.

**Hasret:** erwartetes Signal → Kopf und Augen orientieren sich gleichzeitig → Einatmung stoppt → Lippen bereiten Anrede vor → Hand beginnt Kontakt → Erkennen der Abwesenheit → Finger lösen sich zeitversetzt → Blick bleibt auf möglicher Rückkehrroute.

**Gurbet:** unbekannte Regel oder Sprache → Blick prüft Menschen und Zeichen → Kiefer stabilisiert Stimme → Hand sichert Dokument oder Werkzeug → Gewicht bleibt flucht- und handlungsbereit → kleine soziale Korrektur → Körper entscheidet zwischen Anpassung, Grenze und Annäherung.

Mischgefühle erhalten lesbare Übergänge. Ein Lächeln kann Hasret begleiten; Stolz kann Gurbet strukturieren; Hüzün kann mit Hoffnung zugleich im Gesicht stehen. Mikroausdruck, Atem und Handlung müssen die Gegenemotion sichtbar halten.

### 18.8 Rhetorik, Klang und Form

| Routing | Führung | Unterstützung | Produktionsregel |
|---|---|---|---|
| Hüzün | RH-10 Leitmotiv | RH-06 Ellipse | dasselbe Detail kehrt verändert zurück; Auslassung trägt verlorene Kontinuität |
| Hasret | RH-03 Hitap | RH-04 Tekrar | das abwesende Du bleibt adressierbar; jede Wiederkehr verschiebt Hoffnung oder Distanz |
| Gurbet | RH-13 Zeugenschaft | RH-08 Registerwechsel | konkrete Arbeit, Sprache, Behörde, Wohnung und Weg machen Fremdheit materiell |

Formschutz: Keine automatische Nacht-, Regen-, Fenster-, Bahnhof- oder Schwarzweißästhetik. Ein Bild oder Leitmotiv ist nur zulässig, wenn es eine konkrete Beziehung und Handlung verändert.

### 18.9 Perspektiven- und Bildrouting

| Begriff | Primärperspektive | Gegenperspektive | Bildfrage |
|---|---|---|---|
| Hüzün | BW-02 rückblickendes Ich | BW-15 Objektperspektive/Spur | Was hat der Raum behalten, was die Person nicht mehr halten kann? |
| Hasret | BW-12 abwesende Person | BW-03 angesprochenes Du | Wie organisiert Nichtanwesenheit Blick, Atem und nächste Handlung? |
| Gurbet | BW-10 diasporische Doppelperspektive | BW-14 Körper | Welche Regel sieht die Person doppelt, und was kostet diese zusätzliche Sicht? |

Für Bilddarstellungen gilt: kulturelle Zugehörigkeit wird nicht durch Kostüm, Kopftuch, Koffer, Schnurrbart oder „orientalisches“ Licht behauptet. Ort, Beruf, Generation, Sprache und soziale Beziehung benötigen konkrete Belege. Hände besitzen fünf plausible Finger, Kontaktphysik und eine funktionale Aufgabe; Gesicht und Körper widersprechen einander nur, wenn die Szene diesen Widerspruch begründet.

### 18.10 DEJÀ-VU-3-DNA-Routing

```yaml
cluster: HUZUN-HASRET-GURBET-06
status: mechanism_release
router:
  huzun:
    human_situation: Eine vertraute Spur macht beschädigte Kontinuität gegenwärtig.
    mechanism: LM-01 Kollektive oder persönliche Erinnerung
    rhetoric: RH-10 Leitmotiv
    thought_mode: DM-04 Temporal
    body_arc: Verweilen → langer Ausatem → bewahrende oder lösende Handlung
  hasret:
    human_situation: Ein abwesendes Gegenüber bleibt als Richtung handlungswirksam.
    mechanism: LM-04 Innere Zeit
    rhetoric: RH-03 Hitap + RH-04 Tekrar
    thought_mode: DM-06 Paradoxal
    body_arc: Suchorientierung → Kontaktimpuls → Hemmung → erneute Ausrichtung
  gurbet:
    human_situation: Eine Person lebt unter fremden räumlichen, sprachlichen oder institutionellen Regeln.
    mechanism: LM-05 Materielle Kausalität
    rhetoric: RH-13 Zeugenschaft
    thought_mode: DM-09 Materiell-sozial
    body_arc: Kartieren → Selbstregulation → Arbeit/Grenze → neue oder verweigerte Bindung
forbidden: Synonymisierung, Nationalgefühl-Essentialismus, Sentimentersatz, trauriges-Gesicht-Kurzcode, Migrationsromantik, kulturelle Dekoration
```

### 18.11 Transformationsformeln

**Hüzün-Formel:** vertrauter Gegenstand → frühere Kontinuität → gegenwärtiger Bruch → Gegenemotion bleibt aktiv → Körper verlangsamt → kleine bewahrende oder lösende Handlung.

**Hasret-Formel:** benanntes Gegenüber → räumliche oder zeitliche Distanz → konkrete Spur → imaginierter Kontakt → Körper beginnt Antwort → Kontakt scheitert oder verändert sich → Wunsch erhält neue Richtung.

**Gurbet-Formel:** Herkunftsbindung → materielle Ursache des Fortseins → unbekannte Regel → Arbeit/Sprache/Körper passen sich an → Preis der Anpassung → neue Beziehung oder Grenze → doppelte Zugehörigkeit ohne einfache Erlösung.

**Dreifachformel:** Gurbet als Lage → Hasret als gerichtete Bindung → Hüzün als zeitliche Färbung → Handlung baut Aidiyet, Rückkehr oder bewusste Distanz.

### 18.12 Qualitäts- und Anti-Kollaps-Test

| Prüffrage | Bestehensbedingung |
|---|---|
| Ist Gurbet eine Emotion? | Nein; zuerst räumlich-soziale Lage bestimmen |
| Besitzt Hasret ein Gegenüber? | Person, Ort, Zeit, Sprache, Zustand oder Möglichkeit ist konkret benannt |
| Hat Hüzün eine Zeitstruktur? | Verlust, Vergänglichkeit oder beschädigte Kontinuität wirkt in der Gegenwart |
| Bleibt eine Gegenemotion aktiv? | Hoffnung, Stolz, Pflicht, Erleichterung, Neugier, Liebe oder Widerstand verändert die Darstellung |
| Ist der Körper kausal? | mindestens Blick, Atem, Spannung und Handlung bilden eine plausible Kette |
| Ist der soziale Preis sichtbar? | Arbeit, Entfernung, Sprache, Institution, Familie oder Zugehörigkeit hat konkrete Folge |
| Funktioniert die Szene ohne Emotionswort? | Begriff bleibt über Beziehung, Körper und Handlung identifizierbar |
| Vermeidet die Darstellung Essentialismus? | keine Behauptung, alle türkischen Figuren oder Werke fühlten gleich |

Automatische Sperre bei: bloßem traurigem Gesicht, beliebiger Träne, generischem Kofferbild, Polaritätslabel als Diagnose, Gleichsetzung mit Depression, romantisierter Migration oder fehlendem Gegenüber bei behaupteter Hasret.

### 18.13 Verwendete Kernquellen

- [Klâsik Türk Edebiyatında Gurbet und Nevres-i Kadîm](https://dergipark.org.tr/tr/download/article-file/414635) — Gurbet, Trennung und Divan-/tasavvufische Register; B2.
- [Divan Şiirinde Gurbet ve Gariplik Üzerine](https://dergipark.org.tr/en/download/article-file/3172962) — Liebender als *garip*, Trennung und Hoffnung auf Begegnung; B2.
- [Tevfik Fikret’in Şiirlerinde Hüzün](https://dergipark.org.tr/en/download/article-file/2317151) — differenziertes Wortfeld um Hüzün, elem, keder, gam, melâl, matem und yeis; B2.
- [Türk Halk Müziğinde Gurbet Kavramının Tezahürü Olarak İstanbul](https://dergipark.org.tr/tr/download/article-file/5052441) — Migration, Zurückbleibende, İstanbul, Text und Melodie; B2.
- [Kemalettin Kamu und Gültekin Sâmanoğlu: Gurbet](https://dergipark.org.tr/tr/download/article-file/630596) — Koexistenz von Gurbet, Hasret, Hüzün, Hilflosigkeit und Einsamkeit; B2.
- [Balkanlardan Göç Eden Divan Şairlerinin Şiirlerinde Gurbet](https://dergipark.org.tr/en/download/article-file/4827064) — Migration, Heimatbindung, Hüzün und Selbstpositionierung; B2.
- [Köln Bülbülü Yüksel Özkasap’ın Türkülerinde Göç](https://dergipark.org.tr/tr/download/article-file/6109976) — Arbeitsmigration, Einsamkeit, Fremdheit, Ausbeutung und Zugehörigkeit; B2.
- [Gurbet Havaları üzerine Untersuchung](https://dergipark.org.tr/en/download/article-file/3799105) — Zugehörigkeit, Entfernung, Sehnsucht und kulturell spezifische Aufführungsform; B2.
- [Hüzün Metafiziği: İsmail Hakkı Bursevî](https://dergipark.org.tr/tr/download/article-file/5306563) — registergebundene tasavvufische Deutung von Hüzün; B2, nicht verallgemeinern.
- [Erzincan Türkülerinde Gurbet](https://dergipark.org.tr/en/download/article-file/68523) — Gurbet in regionaler Volksliedüberlieferung und Variantenbildung; B2/C1-Prüfpfad.

### 18.14 Offene Prüfaufträge und Profilentscheidung

1. Mindestens zwölf Werkstellen aus Divan, Halk/Türkü, moderner Lyrik, Roman und Diaspora nach demselben Schema annotieren.
2. Hüzün gegen Keder, Gam, Melâl und Efkâr werkbezogen abgrenzen.
3. Hasret gegen Özlem und Hicran anhand konkreter Beziehungen und Zeitrichtungen prüfen.
4. Gurbet-Profile nach Ursache differenzieren: Arbeit, Exil, Militärdienst, Bildung, Heirat, Flucht und freiwillige Mobilität.
5. GitHub-Suchschema als strukturierte Annotation ohne geschützte Textsegmente veröffentlichungsfähig vorbereiten.
6. Drei DEJÀ-VU-3-Testbilder erstellen, bei denen der Begriff ohne Beschriftung aus Körper, Raum und Handlung erkennbar bleibt.
7. Profil 07 Nâzım Hikmet mit GitHub-Repository-Ampel, autoritativer Biografie und Rechteprüfung beginnen.

**Profilentscheidung:** Hüzün, Hasret und Gurbet sind ab sofort als getrennte, kombinierbare Routingebenen integriert. Hüzün steuert ein zeitlich gefärbtes affektives Feld, Hasret eine gerichtete Beziehung zur Abwesenheit und Gurbet eine materielle, räumliche und soziale Lage. Freigegeben sind ihre kausalen, rhetorischen, perspektivischen und anatomischen Mechanismen. Gesperrt bleiben Synonymisierung, Sentimentersatz, kultureller Essentialismus, Migrationsromantik und jede Darstellung, die Emotion nur über Tränen oder Dekoration behauptet.
