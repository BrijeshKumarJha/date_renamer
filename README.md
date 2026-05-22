# 📅 Smart Date-Based File Renamer

A Python-based automation utility that intelligently renames files by prepending their OS-level Creation or Modification dates in the ISO 8601 standard format (`YYYY-MM-DD`). 

##  The Problem it Solves
When organizing files like invoices, logs, or reports, operating systems sort files alphabetically by default. This ruins the chronological order if file names don't start with a properly formatted date. This tool extracts the raw Unix timestamps from the file's metadata and prepends a sort-friendly date, ensuring your files are always perfectly ordered by time.

##  Features
* **Dual Date Extraction:** Gives the user the option to use either the Creation Date (`st_ctime`) or the Modification Date (`st_mtime`).
* **ISO 8601 Formatting:** Converts raw timestamps to `YYYY-MM-DD` so that default OS alphabetical sorting automatically acts as perfect chronological sorting.
* **Safe Renaming:** Preserves original file extensions and strictly ignores directories.
* **Robust Error Handling:** Fallbacks to default dates if an invalid choice is made, and prevents crashes on invalid directory inputs.

##  Example Output

**Before (Chronologically messy when sorted by name):**
```text
date_dummy_data/
├── project_brief.pdf     (Created: May 11, 2026)
├── old_invoice.jpg       (Created: May 15, 2025)
└── final_report.txt      (Created: April 20, 2026)
```

**After Running the Script (Automatically sorts perfectly):**
```text
date_dummy_data/
├── 2025-05-15_old_invoice.jpg
├── 2026-04-20_final_report.txt
└── 2026-05-11_project_brief.pdf
