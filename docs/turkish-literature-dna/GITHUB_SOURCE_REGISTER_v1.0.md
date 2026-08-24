# GitHub-Quellenregister v1.0

**Prüfstand:** 24. August 2026  
**Scope:** GitHub-Fundstellen zu türkischer Literatur, historischen Texten, Minderheitenschriften, Emotion/Semantik, Korpusarbeit, OCR/HTR, Transkription, Morphologie, Metrik und Digital Humanities.  
**Grundregel:** Eine Code-Lizenz deckt nicht automatisch enthaltene Texte, Bilder, Modelle oder Datensätze ab.

## Statuscodes

| Status | Bedeutung |
|---|---|
| `ADOPT_DISCOVERY` | als Katalog, Metadaten- oder Fundweg integrieren |
| `ADOPT_METHOD` | dokumentierte Methode/Schema abstrahieren; keine Datenübernahme |
| `TEST_ISOLATED` | in isolierter Umgebung technisch und rechtlich testen |
| `WATCH` | relevant, aber Reife, Wartung, Belege oder Lizenz reichen noch nicht |
| `QUARANTINE` | nur registrieren; keine Evidenz- oder Produktionsnutzung |
| `REJECT_AS_SOURCE` | nicht als literarische/faktische Quelle verwenden |

## 1. Texte, Autoren, Literatur- und Werkerschließung

| Repository | Inhalt / Nutzen | Lizenzanzeige | Entscheidung / Grenze |
|---|---|---|---|
| [Mrjavaci/Turkish-Poems](https://github.com/Mrjavaci/Turkish-Poems) | großer Gedicht-Dump für quantitative Experimente | keine | `QUARANTINE`; Herkunft, Edition und Rechte pro Text offen; moderne geschützte Lyrik |
| [bitig/turkbitig](https://github.com/bitig/turkbitig) | umfangreiche historische türkische Text-/Autorenstruktur | keine | `ADOPT_DISCOVERY`; Datei für Datei gegen Edition prüfen |
| [arch-yunus/fasl-i-fuzuli](https://github.com/arch-yunus/fasl-i-fuzuli) | Fuzûlî-Külliyat, Kommentare, Werkstruktur, CLI | MIT (Repository) | `ADOPT_DISCOVERY`; sehr jung, Textzuschreibungen/Editionen separat prüfen |
| [aliok/yunusEmreNlp](https://github.com/aliok/yunusEmreNlp) | NLP-Experiment mit Yunus-Emre-Gedichten | Apache-Hinweis; archiviert | `ADOPT_METHOD`; Textbasis nicht automatisch ediert |
| [common-repository/yunus-emre-divani](https://github.com/common-repository/yunus-emre-divani) | WordPress-Plugin-Spiegel | keine | `REJECT_AS_SOURCE`; Spiegel ohne Editionsapparat |
| [arch-yunus/DedeKorkutNLP](https://github.com/arch-yunus/DedeKorkutNLP) | angekündigte Cyber-Sage/NLP-Struktur | MIT | `WATCH`; kein belastbares ediertes Dede-Korkut-Korpus nachgewiesen |
| [GITenberg/Turkish-fairy-tales-and-folk-tales...](https://github.com/GITenberg/Turkish-fairy-tales-and-folk-tales-collected-by-Dr-Ignacz-Kunos-Translated-from-the-Hungarian__64807) | Gutenberg-Ausgabe englischer Übersetzungen von Kúnos-Sammlungen | NOASSERTION | `ADOPT_DISCOVERY`; historische Sammlung/Übersetzung, kein türkischer Originaltext und keine feste orale Autorschaft |
| [mseroglu/turkish-books-dataset](https://github.com/mseroglu/turkish-books-dataset) | Metadaten zu 82.324 türkischsprachigen Büchern | keine | `ADOPT_DISCOVERY`; bibliografische Identität extern bestätigen |
| [lys-edebiyat/data](https://github.com/lys-edebiyat/data) | Schul-/App-Daten zu Literatur | keine | `QUARANTINE`; Orientierung, keine Fachquelle |
| [kurtulusutkucenik/LibraryProject](https://github.com/kurtulusutkucenik/LibraryProject) | generisches Bibliotheksprojekt | MIT | `REJECT_AS_SOURCE`; kein belastbarer Literaturkorpus |
| [warezturkey/icerikler](https://github.com/warezturkey/icerikler) | ungeklärte Inhalte | keine | `REJECT_AS_SOURCE`; Herkunft/Rechte ungeklärt |
| [Alperencode/DergiPark-Data-Set](https://github.com/Alperencode/DergiPark-Data-Set) | großer DergiPark-Datensatz | keine | `QUARANTINE`; Artikelidentität, Qualität, Volltextrechte einzeln prüfen |
| [taniki/comp.soc-of-philosophy](https://github.com/taniki/comp.soc-of-philosophy) | abgeleitete Seiten-/Satzdaten zu Denkern/Autoren | keine | `ADOPT_METHOD`; Rezeptions-/Netzwerkhinweis, kein Primärbeleg |
| [pgarg22/Awarded-Minds-Literary-Network](https://github.com/pgarg22/Awarded-Minds-Literary-Network) | Wikipedia-/Auszeichnungsnetzwerke | keine | `ADOPT_METHOD`; Sekundärdaten, nicht für Werk- oder Biografiebelege |
| [turkitext/turkitext.github.io](https://github.com/turkitext/turkitext.github.io) | Einstieg zu klassifizierten Turki-Texten | GPL-3.0 | `ADOPT_DISCOVERY`; Türkisch/Turkic und Einzelrechte trennen |

## 2. Annotation, Stilometrie und literarische Analyse

| Repository | Inhalt / Nutzen | Lizenzanzeige | Entscheidung / Grenze |
|---|---|---|---|
| [Kon-tiki-ship/tasvir-bankasi-turkish-literary-annotation-pipeline](https://github.com/Kon-tiki-ship/tasvir-bankasi-turkish-literary-annotation-pipeline) | Rechteprüfung, Szenen-/State-/Description-Schema, Validatoren, DOI | Code PolyForm Noncommercial; Daten CC BY-NC 4.0 | `ADOPT_METHOD`; kommerzielle Nutzung blockiert; Vollkorpus separat/gated |
| [gulcu/AuthorshipAttribution](https://github.com/gulcu/AuthorshipAttribution) | Stilometrie türkischer Romane | keine | `ADOPT_METHOD`; Korpus-/Volltextrechte ungeklärt, keine Autorimitation |
| [volkanagun/AuthorshipDataset](https://github.com/volkanagun/AuthorshipDataset) | XML-/Reader-Verweis mit DOI | keine im Repo | `ADOPT_DISCOVERY`; DOI-Datensatz und Rechte separat prüfen |
| [seydakaba/turkish-poetry-analysis](https://github.com/seydakaba/turkish-poetry-analysis) | Topic Modeling türkischer Gedichte | keine | `ADOPT_METHOD`; Themenmodell ersetzt keine Edition/Interpretation |
| [bkucukertem/Themes-Analysis-of-Turkish-Poems](https://github.com/bkucukertem/Themes-Analysis-of-Turkish-Poems) | MATLAB-Themenanalyse | keine | `WATCH`; Datenherkunft/Methodik prüfen |
| [bsenurbas/ai-yazar-tespit](https://github.com/bsenurbas/ai-yazar-tespit) | Autor-/KI-Erkennung | keine | `WATCH`; Validität und Trainingsdaten offen |
| [AdilSevim/Turkish-Poetry-Language-Model](https://github.com/AdilSevim/Turkish-Poetry-Language-Model) | Modell auf Turkish-Poems-Basis | MIT (Code) | `REJECT_AS_SOURCE`; Rechte-/Stilimitationrisiko, nur technische Risikoanalyse |
| [mcemilg/fuzuli](https://github.com/mcemilg/fuzuli) | Encoder-Decoder für alte Gedichtstile | Apache-2.0 (Code) | `REJECT_AS_SOURCE`; Stilvorhersage/-erzeugung ist keine philologische Quelle |
| [KerimYasin/DOGALDIL](https://github.com/KerimYasin/DOGALDIL) | junges NLP-Projekt ohne klare Beschreibung | keine | `WATCH` |
| [ayseelgoren/TezFlask](https://github.com/ayseelgoren/TezFlask) | Wortstamm-Frequenz | keine | `ADOPT_METHOD`; begrenzter statistischer Hilfswert |

## 3. Armeno-Turkish, Karamanlidika, Manuskriptmetadaten und TEI

| Repository | Inhalt / Nutzen | Lizenzanzeige | Entscheidung / Grenze |
|---|---|---|---|
| [comp-int-hum/Armeno-Turkish-Collection](https://github.com/comp-int-hum/Armeno-Turkish-Collection) | Findworkflow für armenischschriftliches Türkisch; FastText-Testwert im README | keine | `ADOPT_METHOD`; Fundwahrscheinlichkeit ist keine Werkidentität oder Rechtefreigabe |
| [halesirin/hathitrust_armeno_turkish](https://github.com/halesirin/hathitrust_armeno_turkish) | HathiTrust-MARC-Filter und human gelabelte Findmethode | keine | `ADOPT_METHOD`; Katalogfehler/OCR sichtbar halten; HathiTrust-Rechte pro Werk |
| [erkinalp/karamanlidika](https://github.com/erkinalp/karamanlidika) | Werkzeuge zu Karamanlı-Türkisch | LGPL-3.0 | `TEST_ISOLATED`; Sprache, griechische Schrift, Religion und Druckkontext trennen |
| [miguelpaflis/Karamanlidika-Translator](https://github.com/miguelpaflis/Karamanlidika-Translator) | moderne Transliteration in griechische Schrift | keine | `WATCH`; sehr klein/jung, keine historische Edition |
| [soas-library/fihrist-mss](https://github.com/soas-library/fihrist-mss) | TEI-Manuskriptmetadaten für Fihrist | keine | `ADOPT_DISCOVERY`; Katalogmetadaten, keine Volltextedition |
| [tillgrallert/kanun-i-esasi](https://github.com/tillgrallert/kanun-i-esasi) | TEI-XML-Editionen der osmanischen Verfassung in mehreren Sprachen | keine | `ADOPT_METHOD`; historisch-politischer Text, kein Literaturbeleg; Editions-/Dateirechte prüfen |
| [yunusugur/turkey-dh-atlas](https://github.com/yunusugur/turkey-dh-atlas) | DH-Projektatlas/CollectionBuilder-Bestand | MIT/CC BY-SA für Framework-Inhalte | `ADOPT_DISCOVERY`; Objektlizenzen bleiben individuell |

## 4. Osmanische OCR, HTR, Transkription und Text Mining

| Repository | Funktion | Lizenzanzeige | Entscheidung / Grenze |
|---|---|---|---|
| [Ottoman-NLP/OCR-Transformer](https://github.com/Ottoman-NLP/OCR-Transformer) | Rauschenerkennung/-korrektur lateinisierter OCR-Texte | GPL-3.0 | `TEST_ISOLATED`; synthetische Fehler/Accuracy gegen echtes Ground Truth prüfen |
| [Therad445/low-resource-arabic-script-turkic-ocr](https://github.com/Therad445/low-resource-arabic-script-turkic-ocr) | reproduzierbare OCR-Nachkorrektur; dokumentiert Synthetic-to-real-Lücke | MIT | `ADOPT_METHOD`; gerade wegen negativer Real-OCR-Ergebnisse wertvoll; nicht produktionsreif behaupten |
| [OttomanTextAI/OttomanTextAI](https://github.com/OttomanTextAI/OttomanTextAI) | mobile Vorverarbeitung → OCR → Transkription → LLM-Simplifizierung | keine | `WATCH`; Human-in-the-loop behalten, Modernisierung niemals als Original ausgeben |
| [Koras0ff/OttomanOCR-search](https://github.com/Koras0ff/OttomanOCR-search) | OCR-Ausgabe zu 28 gedruckten osmanischen Werken | Apache-2.0 | `TEST_ISOLATED`; Modelloutput ist keine kollationierte Edition; Werkrechte/Scans separat |
| [Koras0ff/OtaHTR-search](https://github.com/Koras0ff/OtaHTR-search) | Stichwortsuche in osmanischen Handschriften | CC0-1.0 | `ADOPT_DISCOVERY`; Treffer gegen Faksimile/Witness prüfen |
| [MemduhG/OttomanData](https://github.com/MemduhG/OttomanData) | OCR-Daten für osmanische Dokumente | keine | `QUARANTINE`; Datenherkunft, Ground Truth und Rechte offen |
| [seccily/ottoman-text-line-segmentation-dataset](https://github.com/seccily/ottoman-text-line-segmentation-dataset) | 150 Seiten; manuelle/automatische Zeilensegmentierung | MIT | `TEST_ISOLATED`; automatische Labels enthalten dokumentierte Fehlsegmente |
| [hmzdot/alamet](https://github.com/hmzdot/alamet) | Ottoman OCR | keine | `WATCH`; Benchmarks/Provenienz prüfen |
| [Fbilalyy/ottoman_ocr](https://github.com/Fbilalyy/ottoman_ocr) | Deep-Learning-OCR für Handschriften | keine | `WATCH`; sehr kleine Repo, Datennachweis nötig |
| [mahmutkoc/ottoman-ocr](https://github.com/mahmutkoc/ottoman-ocr) | OCR-Prototyp | keine | `WATCH` |
| [Baki-Projesi/Scribe](https://github.com/Baki-Projesi/Scribe) | standardisierte Transkriptionsentscheidungen, Bild/Text-Vergleich | keine | `ADOPT_METHOD`; ältere Work-in-progress-Software, Entscheidungsprovenienz ist Goldmechanismus |
| [cdliai/ottoman-ner](https://github.com/cdliai/ottoman-ner) | Ottoman-Turkish NER Toolkit | MIT | `TEST_ISOLATED`; Modell-/Datensatzgüte, Zeichen-/Transkriptionsstandard prüfen |
| [cdliai/ottominer](https://github.com/cdliai/ottominer) | junges Ottoman Text-Mining Toolkit | keine | `WATCH`; README/License unvollständig |
| [sb-b/OttTur_resources_for_nlp](https://github.com/sb-b/OttTur_resources_for_nlp) | NER-/NLP-Ressourcen und Notebooks | CC0-1.0 | `ADOPT_DISCOVERY`; moderne Modelle nicht ungeprüft auf Osmanisch übertragen |
| [osmandemiroz/ottoman-turkish-pos-tagger](https://github.com/osmandemiroz/ottoman-turkish-pos-tagger) | POS-Tagger auf UD Ottoman Turkish-DUDU | MIT-Code / CC BY-SA-Datenhinweis | `TEST_ISOLATED`; duale Lizenzen und OOV-Fehlerbericht erhalten |
| [bilirkesi/ottoman-agent-pipeline](https://github.com/bilirkesi/ottoman-agent-pipeline) | Multi-Agent-Transliteration mit externem Modell | MIT | `WATCH`; sehr jung, Datenfluss/Secrets/Kosten/Halluzinationen prüfen |
| [jzxjxzh/selase](https://github.com/jzxjxzh/selase) | osmanisch-türkisches Wörterbuch-Frontend | keine | `QUARANTINE`; Wörterbuchdatenquelle/Rechte fehlen |
| [deeppaz/lugat](https://github.com/deeppaz/lugat) | Devellioğlu-Wörterbuch-Frontend | keine; archiviert | `REJECT_AS_SOURCE`; Wörterbuch urheberrechtlich geschützt/keine Datenlizenz |

## 5. Metrik, Aruz und Prosodie

| Repository | Funktion | Lizenzanzeige | Entscheidung / Grenze |
|---|---|---|---|
| [emreozcan/taktisyen](https://github.com/emreozcan/taktisyen) | Silbifizierung und Aruz-Analyse | MIT; archiviert | `ADOPT_METHOD`; automatisches Ergebnis durch manuelles taktîʿ prüfen |
| [Koras0ff/ottoman-aruz-predictor](https://github.com/Koras0ff/ottoman-aruz-predictor) | Aruz-Vorhersage per Edit-Distance | Apache-2.0 | `TEST_ISOLATED`; README fehlt, Muster-/Fehlerprüfung erforderlich |
| [ell-shad/Bahrmetr](https://github.com/ell-shad/Bahrmetr) | Aruz-Meter für aserbaidschanische/türkische Gedichte | MIT | `WATCH`; jung, Sprach-/Musterabdeckung testen |

## 6. Emotion, Semantik und Sprachwerkzeuge

| Repository | Funktion | Lizenzanzeige | Entscheidung / Grenze |
|---|---|---|---|
| [StarlangSoftware/TurkishSentiNet](https://github.com/StarlangSoftware/TurkishSentiNet) | HisNet-Polaritätslexikon | GPL-3.0 / README nennt Apache für Paketbestandteile | `TEST_ISOLATED`; Lizenzdateien priorisieren; Polarität ≠ Literaturgefühl |
| [StarlangSoftware/TurkishSentiNet-Py](https://github.com/StarlangSoftware/TurkishSentiNet-Py) | Python-Port | GPL-3.0 | `TEST_ISOLATED`; gleiche semantische Grenze |
| [StarlangSoftware/TurkishSentiNet-C](https://github.com/StarlangSoftware/TurkishSentiNet-C) | C-Port | keine Metadatenlizenz | `WATCH` |
| [swnettr/SWNetTR](https://github.com/swnettr/SWNetTR) | türkisches Sentimentlexikon | keine | `QUARANTINE`; Publikation/Lizenz separat prüfen |
| [verdeerosso/affective-turkish](https://github.com/verdeerosso/affective-turkish) | regel-/lexikonbasierte Affektanalyse | keine | `ADOPT_METHOD`; alt, nicht literaturspezifisch |
| [yyakupatli/NAYALex-nayalex_tr](https://github.com/yyakupatli/NAYALex-nayalex_tr) | türkisches Emotionslexikon | keine | `WATCH`; Herkunft/Annotation/Lizenz prüfen |
| [rabia-tintin/turkish-plutchik-emotion-dataset](https://github.com/rabia-tintin/turkish-plutchik-emotion-dataset) | 136.000 Sätze, Plutchik-Labels/Intensität; Paper/DOI im README | keine Repo-Lizenz | `ADOPT_DISCOVERY`; Paper/Datensatz prüfen; Plutchik-Klassen ersetzen Hüzün/Hasret/Gurbet nicht |
| [StarlangSoftware/TurkishWordNet](https://github.com/StarlangSoftware/TurkishWordNet) | KeNet/WordNet | GPL-3.0; README-Paketinfo beachten | `TEST_ISOLATED`; semantische Beziehungen, keine Werkdeutung |
| [StarlangSoftware/TurkishMorphologicalAnalysis](https://github.com/StarlangSoftware/TurkishMorphologicalAnalysis) | Morphologie | GPL-3.0 | `TEST_ISOLATED` |
| [ahmetaa/zemberek-nlp](https://github.com/ahmetaa/zemberek-nlp) | Tokenisierung, Morphologie, Normalisierung | NOASSERTION; README nennt Apache-2.0 | `TEST_ISOLATED`; langsamer Wartungsmodus, Lizenzdatei prüfen |
| [coltekin/TRmorph](https://github.com/coltekin/TRmorph) | finite-state Morphologie | MIT | `ADOPT_METHOD`; modernes Türkisch, historische Register separat |
| [google-research/turkish-morphology](https://github.com/google-research/turkish-morphology) | zweistufiger Morphologieanalysator | Apache-2.0; archiviert | `ADOPT_METHOD`; keine aktive Weiterentwicklung |
| [ahmetax/derlemtr](https://github.com/ahmetax/derlemtr) | türkische Corpus-Erstellung | MIT | `ADOPT_METHOD`; Korpusrechte bleiben extern |

## 7. Discovery-Kataloge

| Repository | Nutzen | Entscheidung |
|---|---|---|
| [bilalabic/awesome-turkish-datasets](https://github.com/bilalabic/awesome-turkish-datasets) | 298 nach eigener Methodik geprüfte Datensätze; Rechte/Zugang getrennt | `ADOPT_DISCOVERY`; jeden Zieldatensatz erneut prüfen |
| [agmmnn/turkish-nlp-resources](https://github.com/agmmnn/turkish-nlp-resources) | kuratierte NLP-Ressourcenliste | `ADOPT_DISCOVERY`; Linkalter/Lizenzen einzeln |
| [yusufusta/awesome-turkish-nlp](https://github.com/yusufusta/awesome-turkish-nlp) | Open-Source-NLP-Liste | `ADOPT_DISCOVERY`; ältere Pflege |
| [deeplearningturkiye/turkce-yapay-zeka-kaynaklari](https://github.com/deeplearningturkiye/turkce-yapay-zeka-kaynaklari) | historisch große türkische KI-Ressourcenliste | `ADOPT_DISCOVERY`; Aktualität jedes Links prüfen |
| [ulughann/awesome-turkic](https://github.com/ulughann/awesome-turkic) | Turksprachen-Ressourcen | `WATCH`; sehr klein, Türkisch nicht mit Turkic gleichsetzen |
| [eymenefealtun/all-words-in-all-languages](https://github.com/eymenefealtun/all-words-in-all-languages) | allgemeine Wortlisten | `REJECT_AS_SOURCE`; Herkunft/Lizenz/Sprachqualität unklar |
| [BenKosSoft/deepTwitter](https://github.com/BenKosSoft/deepTwitter) | alte Twitter-Extraktion | `REJECT_AS_SOURCE`; Plattform-/Rechte-/Relevanzproblem |
| [afyildizz/temel_tensoflow2_egitimi](https://github.com/afyildizz/temel_tensoflow2_egitimi) | allgemeine TensorFlow-Lehre | `REJECT_AS_SOURCE`; nicht literaturspezifisch |

## 8. Integrationsentscheidung

In DÉJÀ-VU-3 integriert werden:

1. Fund- und Katalogpfade,
2. Quellen-/Rechtefelder,
3. methodische Mechanismen,
4. OCR-/Transkriptions-/Editionsgates,
5. Metrik-, Morphologie-, Semantik- und Netzwerkhilfen,
6. explizite Fehlermodi und Negativbefunde.

Nicht integriert werden ungeprüfte Volltexte, Modellgewichte, geschützte Wörterbuchdaten, Quote-Dumps, Stilerzeugungsmodelle oder Inhalte mit ungeklärter Herkunft. `TEST_ISOLATED` ist keine Installations- oder Produktionsfreigabe.

