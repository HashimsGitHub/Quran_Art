<div align="center">

﷽

# ⚜️ Quran's Art Gallery ⚜️

### *Verses Visualized*

---



[![Live Site](https://img.shields.io/badge/🌐%20Live%20Site-quran--art.cloud-d4af37?style=for-the-badge&labelColor=0a0601)](https://www.quran-art.cloud/)
&nbsp;
[![AI Art](https://img.shields.io/badge/🕌%20AI%20Art-Inspired%20by%20The%20Holy%20Quran-b47c2e?style=for-the-badge&labelColor=0a0601)](https://www.quran-art.cloud/)

</div>

---

## ✦ About

**Quran Art** is a devotional web gallery that unites the timeless beauty of Quranic scripture with the transformative power of AI-generated imagery. Each piece pairs a sacred verse with a visual meditation — rendered in the spirit of the illuminated Topkapi manuscripts — accompanied by the classical English translation of **Abdullah Yusuf Ali**.

> *"God is the Light of the heavens and the earth."*
> — Sūra 24: Nūr (The Light), Verse 35

The result is an experience of reverence: scripture made visible, contemplation made accessible.

---

## 🖼️ Gallery : AI-Generated Artwork

Each image is uniquely crafted to reflect the imagery and emotion of its corresponding verse

---

## ✨ Features

- **Gold-Framed Carousel** — An elegant, auto-advancing gallery inspired by illuminated manuscript aesthetics
- **Sacred Typography** — Arabesque overlays and royal ornamentation evoking classical Islamic calligraphy
- **Classical Translation** — Verse text drawn from Abdullah Yusuf Ali's revered English translation
- **Quran Search Engine** — Search the English Quran translation by keyword and browse matching verses
- **Hadith Search Engine** — Search across multiple English Hadith collections directly in the browser
- **AI Scholar** — A Botpress-powered conversational assistant grounded in the Quran and Hadith knowledge sources configured for this project
- **Fully Responsive** — Designed for desktop, laptop, tablet, and mobile devices
- **Keyboard & Touch Navigation** — Swipe, click, or use arrow keys to move between revelations

---

---

## 🔎 Search the Quran and Hadith

The gallery includes two dedicated search experiences:

- **Quran Search Engine** — Search the English translation of the Holy Quran by keyword and browse matching verses.
- **Hadith Search Engine** — Search the English Hadith collections, including Sahih al-Bukhari, Sahih Muslim, Sunan Abu Dawud, Jami At Tirmidhi, and more.

The Hadith search page downloads and prepares all English SQLite collections from Azure Blob Storage when it opens, then searches them locally in the browser. Search terms are not sent to a server. The first visit may take a little longer while the collections are loaded.

---

## 🤖 AI Scholar — Quran & Hadith Chatbot

The site also includes **AI Scholar**, an embedded conversational assistant powered by **Botpress**.

AI Scholar is configured to answer using the Quran and Hadith knowledge sources prepared for this project. The assistant is instructed to remain grounded in those sources and to avoid inventing unsupported Quran verses, Hadith references, narrations, grades, or interpretations.

### How it works

1. Quran and Hadith source data is prepared as structured knowledge documents.
2. Those documents are uploaded into the Botpress Knowledge Base.
3. When a user asks a question, Botpress retrieves relevant Quran and Hadith passages.
4. The language model generates a response using the retrieved knowledge.
5. If the available sources do not contain sufficient evidence, the assistant is instructed to say so rather than answer from unsupported information.

This provides a **RAG-style (Retrieval-Augmented Generation)** experience: the AI response is generated from retrieved source material instead of functioning as an unrestricted general-purpose chatbot.

### Grounding rules

The AI Scholar is instructed to:

- Answer only from the configured Quran and Hadith knowledge sources
- Distinguish Quran evidence from Hadith evidence
- Provide Surah and verse references where available
- Provide Hadith collection, Hadith number, section, and grade where available
- Never invent a Hadith grade if one is not present in the source data
- Clearly identify summaries rather than presenting them as direct quotations
- State when the available knowledge is insufficient to answer a question
- Avoid unsupported fatwas, theological conclusions, and external scholarly opinions

### Website integration

The chatbot is embedded in a dedicated `ai-scholar.html` page using the Botpress Webchat embed:

```html
<script src="https://cdn.botpress.cloud/webchat/v3.7/inject.js"></script>
<script src="https://files.bpcontent.cloud/2026/09/13/02/20260913024652-1WDUCY7V.js" defer></script>
```

The AI Scholar page follows the same black-and-gold Quran Art visual theme and includes responsive desktop, laptop, and mobile styling.

### Hadith data source

English Hadith database archives are taken from:

https://github.com/IsmailHosenIsmailJames/compressed_hadith_sqlite/tree/master

The browser Hadith search implementation uses standard SQLite text matching for broad WebAssembly compatibility.

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Markup | HTML5 |
| Styling | CSS3 (custom properties, gradients, backdrop filters) |
| Carousel | [Swiper.js v11](https://swiperjs.com/) |
| Quran Search | JavaScript + Quran JSON dataset |
| Hadith Search | sql.js + SQLite databases loaded in the browser |
| AI Chatbot | Botpress Webchat + Knowledge Base / RAG |
| Knowledge Sources | Quran and English Hadith collections |
| Data / Images | Azure Blob Storage |
| Deployment | Custom domain — `quran-art.cloud` |

---

Visit the live site at **[www.quran-art.cloud](https://www.quran-art.cloud/)**.

---

## 📜 Credits & Acknowledgements

- **Quranic Translation** — *The Holy Quran: Text, Translation and Commentary* by Abdullah Yusuf Ali
- **Visual Inspiration** — The illuminated manuscripts of the Topkapi Palace Museum, Istanbul
- **AI Imagery** — Generated with reverence and care to honour the sacred source material
- **AI Scholar** — Conversational interface powered by Botpress and grounded in the project's Quran and Hadith knowledge sources

---

<div align="center">

---

🕌 &nbsp; AI Art &nbsp; · &nbsp; ⚜️ Inspired by the Verses of The Holy Quran ⚜️ &nbsp; · &nbsp; 📜 Copyright © 2026 Hashim Hilal

</div>
