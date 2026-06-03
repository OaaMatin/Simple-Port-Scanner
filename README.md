# Simple Port Scanner

A lightweight TCP port scanner written in Python.

This project allows users to scan a target host within a specified port range and identify open TCP ports.

---

## Features

- Scan custom TCP port ranges
- Detect open TCP ports
- Display scan duration
- Count the number of open ports
- Automatically handle reversed port ranges
- Simple and beginner-friendly implementation

---

## Requirements

- Python 3.8+

No external libraries are required.

---

## Installation

Clone the repository:

```bash
git clone git@github.com:OaaMatin/Simple-Port-Scanner.git
```

Navigate to the project directory:

```bash
cd Simple-Port-Scanner
```

---

## Usage

Run the scanner:

```bash
python3 scanner.py
```

Example:

```text
"Simple-Port-Scanner"

Enter IP: scanme.nmap.org
Enter Start Port: 20
Enter End Port: 100

Start scanning...

Port 22 is OPEN
Port 80 is OPEN

Found 2 open ports.

Scan completed in 1.537 seconds.
```

---

## Project Structure

```text
Simple-Port-Scanner/
│
├── scanner.py
├── README.md
└── .gitignore
```

---

## Current Version

### v1.1

Implemented:

- Basic TCP port scanning
- Open port detection
- Open port counter
- Scan duration measurement
- Port range correction

---

## Disclaimer

This project was created for educational purposes and should only be used on systems and networks you are authorized to test.