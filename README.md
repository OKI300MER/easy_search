# 🔍 easy_search

**easy_search** is a Python-based tool designed to automate data enrichment by integrating information from various online sources. It reads an input Excel file, performs searches using APIs or web scraping, and outputs an enriched Excel file with the gathered data.

---

## 📁 Project Structure

- `katch.py`: Main script that processes the input Excel file and performs searches.
- `katch.ipynb`: Jupyter Notebook version of the script for interactive use.
- `updated_data.xlsx`: Sample output file with enriched data.
- `data/`: Directory containing input and output Excel files.

---

## ⚙️ Setup Instructions

### Prerequisites

- Python 3.x
- Required Python libraries:
  - pandas
  - requests
  - openpyxl

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/OKI300MER/easy_search.git
   cd easy_search
   ```

2. **Install the required libraries:**

   ```bash
   pip install pandas requests openpyxl
   ```

---

## 🚀 Usage

1. **Prepare your input Excel file:**

   - Ensure your Excel file (e.g., `input_data.xlsx`) is placed in the `data/` directory.
   - The file should contain a column with the data you want to search (e.g., names, phone numbers).

2. **Run the script:**

   ```bash
   python katch.py
   ```

   - The script will read the input file, perform searches, and generate an output file named `updated_data.xlsx` in the `data/` directory.

3. **Review the output:**

   - Open `updated_data.xlsx` to see the enriched data with additional information retrieved from online sources.

---

## 🔧 Configuration

- Update the `api_urls` dictionary in `katch.py` with the actual API endpoints or URLs you intend to use for data retrieval.
- Ensure that any required API keys or authentication details are correctly configured.

---

## 📝 Notes

- This tool is intended for educational and research purposes.
- Ensure compliance with the terms of service of any APIs or websites you interact with.
- Handle personal data responsibly and ethically.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 👤 Author

Developed by [OKI300MER](https://github.com/OKI300MER)
