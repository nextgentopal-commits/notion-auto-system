# 01 DIGITAL PRODUCTS

## Ziel
Digitale Produkte mit minimalen Fixkosten testen und verkaufen.

## Geeignete Formate
- PDFs
- Kurzgeschichten
- Sammlungen
- Hörbücher
- Vorlagen
- Premium-Content

## Kern-Funnel
Content -> Interesse -> Produktseite -> Zahlung -> Download -> Wiederkauf

## GitHub-Funde / Kandidaten

### 1. Sellf — Favorit für den langfristigen Ausbau
Self-hosted Plattform für digitale Produkte mit Stripe, Supabase und Next.js.

**Stärken**
- Einmalzahlungen und wiederkehrende Zahlungen
- digitale Downloads, Kurse, Memberships und SaaS-Abos
- Coupons, Order Bumps, One-Time-Offers und Funnels
- Waitlists / Pre-Launch
- Webhooks für n8n, Make, Zapier und eigene Automationen
- Analytics / Revenue Dashboard
- Content Protection
- GDPR-/EU-Funktionen laut Projektbeschreibung
- eigener Stripe-Account, keine Plattform-Umsatzbeteiligung

**Schwächen / Aufwand**
- technisch deutlich komplexer
- Supabase, Stripe, Hosting und Environment-Variablen notwendig
- steuerliche Abwicklung bleibt beim Betreiber

**Eignung**
- MVP: 7/10
- langfristige Plattform: 10/10
- Membership-Ausbau: 10/10
- Automatisierung: 10/10

### 2. TishCommerce — Favorit für einen einfachen MVP
Database-free Next.js-Shop speziell für virtuelle Produkte.

**Stärken**
- digitale Downloads als Kernfunktion
- Stripe und PayPal
- keine Datenbank notwendig
- Produkte über JSON-Konfiguration verwaltbar
- sichere, zahlungsgeprüfte Downloadlinks
- kostenlose Produkte / Lead Magnets
- Newsletter-Anbindung
- Vercel-/Netlify-/Cloudflare-Deployment möglich
- geringere technische Komplexität als Sellf

**Schwächen / Grenzen**
- primär kleiner Download-Shop
- weniger geeignet für komplexe Membership-/Abo-Modelle
- stärkerer Ausbau würde später Migration oder Erweiterung erfordern

**Eignung**
- MVP: 10/10
- langfristige Plattform: 7/10
- Membership-Ausbau: 5/10
- Automatisierung: 6/10

### 3. Streamlit + Stripe Beispielprojekt — Lern-/Prototyping-Kandidat
Python-/Streamlit-Demo zum Verkauf digitaler Produkte über Stripe.

**Stärken**
- sehr einfaches Konzept
- gut zum Lernen und Verstehen des Zahlungsflusses
- Python-basiert

**Schwächen**
- eher Tutorial / Demo als Produktionsplattform
- kaum integrierte Shop-, Membership- oder Funnel-Funktionen
- nicht als Kernsystem vorgesehen

**Eignung**
- Lernen: 9/10
- MVP-Verkauf: 5/10
- langfristige Plattform: 2/10

## Entscheidungsmatrix
| Kriterium | Sellf | TishCommerce | Streamlit + Stripe |
|---|---:|---:|---:|
| Einfacher Start | 7 | 10 | 8 |
| Digitale Downloads | 10 | 10 | 6 |
| Stripe | 10 | 10 | 10 |
| PayPal | nicht Kernfokus | 10 | 0 |
| Membership / Abo | 10 | 5 | 0 |
| Funnels / Upsells | 10 | 4 | 0 |
| Automatisierbarkeit | 10 | 6 | 4 |
| Langfristige Skalierung | 10 | 7 | 2 |
| Technische Einfachheit | 6 | 9 | 8 |

## Aktuelle Empfehlung

**Kurzfristig testen:** TishCommerce

Begründung: Für den ersten realen Verkauf eines PDFs oder einer Geschichte ist der technische Aufwand niedriger. Ein Produkt kann als MVP mit Stripe oder PayPal und automatischem Download getestet werden.

**Langfristiges Zielsystem:** Sellf

Begründung: Sellf deckt zusätzlich Memberships, wiederkehrende Zahlungen, Funnels, Webhooks und Automatisierung ab. Damit kann später aus einem einzelnen digitalen Produkt ein vollständiges Creator-Commerce-System entstehen.

## Testkriterien
- niedrige Startkosten
- einfacher Checkout
- digitaler Download
- Stripe und möglichst PayPal
- Hosting-Kosten
- Aufwand für Einrichtung und Wartung
- DSGVO-/Steuerprüfung vor Livegang
- Automatisierbarkeit
- spätere Membership-Fähigkeit

## Nächster Test
1. Ein bestehendes digitales Produkt als MVP festlegen.
2. TishCommerce technisch auf Deployment- und Zahlungsanforderungen prüfen.
3. Parallel Sellf als langfristige Zielarchitektur dokumentieren.
4. Noch kein Live-Zahlungssystem aktivieren, bevor Steuer-/Impressums-/DSGVO-Punkte für Deutschland geprüft sind.
