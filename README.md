# Simple Port Scanner

A lightweight multi-threaded TCP port scanner written in Python.

This project allows users to scan a target host within a specified port range and identify open TCP ports. It supports both hostnames and IP addresses, includes input validation, and uses concurrent scanning to improve performance.

---

## Features

* Scan custom TCP port ranges
* Detect open TCP ports
* Multi-threaded scanning using ThreadPoolExecutor
* Hostname and IP address support
* Automatic hostname resolution
* Input validation and error handling
* Port range validation
* Automatic correction of reversed port ranges
* Open port counting
* Scan duration measurement
* Simple and beginner-friendly implementation

---

## Requirements

* Python 3.8+

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

Enter host or IP: scanme.nmap.org

Resolved IP: 45.33.32.156

Enter Start Port: 20
Enter End Port: 100

Start scanning...

    Port 22 is open.
    Port 80 is open.

Found 2 open ports.

Scan completed in 0.245 seconds.
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

## Version History

### v2.0

Implemented:

* Multi-threaded port scanning
* ThreadPoolExecutor concurrency model
* Future-to-port mapping
* Improved scanning performance

### v1.2

Implemented:

* Hostname resolution
* Host/IP validation
* Port range validation
* Exception handling
* Input validation

### v1.1

Implemented:

* Scan duration measurement
* Open port counter
* Improved scan summary

### v1.0

Implemented:

* Basic TCP port scanning
* Open port detection

---

## Disclaimer

This project was created for educational purposes and should only be used on systems and networks you are authorized to test.