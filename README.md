# Optimize Marketing Campaign

A demonstration written in Python that uses data science techniques to optimize
marketing campaigns using customer purchase data from an e-commerce platform.
The dataset contains rows with information about transactions, customer
demographics, and website activity. Uses the pandas, NumPy, and pyarrow
libraries.

- It addresses missing values by using mean imputation for numeric data and mode
  imputation for categorical data where appropriate.
- For outliers, it applies the IQR method to flag and address anomalous values
  that could skew the results.
- To handle inconsistent data formats, it uses custom functions to standardize
  date formats and resolve discrepancies in categorical labels.
- It reduces memory usage by downcasting data types and uses the efficient file
  format Parquet for storage.

## Installation

You must have git and Python installed.

Clone this repostitory.

```sh
git clone https://github.com/travishorn/optimize_campaign
```

Change into the directory.

```sh
cd optimize_campaign
```

Install the dependencies

```sh
pip install -r requirements.txt
```

## Usage

Look at `dataset.csv` to get an idea of what the data looks like.

Run the cleaning script.

```sh
python main.py
```

The output is written to `clean_data.parquet`.

You can view it using DuckDB, for example.

```sh
duckdb -c "SELECT * FROM 'clean_data.parquet';"
```

## License

The MIT License

Copyright 2024 Travis Horn

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the “Software”), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
