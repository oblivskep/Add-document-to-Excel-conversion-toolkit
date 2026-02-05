# 📄 Document → Excel / CSV Conversion Toolkit

This repository contains small, reliable utilities and workflows to convert messy documents and raw text into clean, structured CSV or Excel files.

The focus is on **practical delivery**: turning unstructured data into spreadsheets that are immediately usable.

---

## 🧩 Text → CSV

Convert messy text files (copied lists, emails, logs, raw text) into clean CSV files.

### Example input
`examples/input.txt`

```
John Smith    john@example.com    +1 555-1111
Ana Pérez     ana@acme.com        +54 11 5555-2222
Mike Lee      mike@demo.org       +44 20 7777 8888
```

### Run

```bash
python text_to_csv.py examples/input.txt examples/output.csv --header name,email,phone
```

### Output
A clean CSV file with normalized columns, ready to open in Excel or LibreOffice.

---

## 📄 PDF → Excel

Extract tables from PDF documents and deliver them as CSV or Excel files.

On this system, PDF table extraction is performed using **Tabula (Java CLI)** to ensure stability and compatibility.

### Run

```bash
java -jar tabula.jar -o examples/output.csv examples/input.pdf
```

Then open `examples/output.csv` in LibreOffice and **Save As → `.xlsx`**.

### Notes
- Works best with **text-based PDFs** containing tables
- Scanned/image-only PDFs may require **OCR** before conversion (handled as an add-on)
- Each table is exported cleanly and can be further formatted if needed

---

## ⚙️ What this toolkit is useful for

- Converting PDFs into Excel or CSV
- Turning copied or exported text into spreadsheets
- Cleaning and structuring raw data
- Preparing data for reports, analysis, or import into other systems

---

## 📋 Requirements

- Python 3.8+ (for text conversion tools)
- Java Runtime Environment (for PDF table extraction via Tabula)
- LibreOffice / Excel for final formatting
