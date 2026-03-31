# FOI Pipeline

A local pipeline for extracting structured, evidence-linked claims from Freedom of Information (FOI) documents.

---

## 🚀 What it does

This project turns unstructured FOI documents into structured data.

It:

- downloads FOI documents (PDF / DOCX)
- converts DOC/DOCX → PDF
- extracts numeric claims and surrounding context
- outputs structured datasets (`claims.csv`)
- serves documents locally for evidence review

---

## 🧠 Why this matters

FOI documents are often:

- long
- unstructured
- difficult to analyse

This pipeline converts them into:

👉 **searchable, structured, evidence-linked data**

Useful for:
- policy analysis
- journalism
- research
- auditing public data

---

## 📂 Project structure

## ⚙️ Setup

git clone https://github.com/arcmcm/foi-pipeline.git
cd foi-pipeline

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

## ▶️ Run

./run_all.sh

## 📊 Output

data/claims.csv
data/claims_full.csv
