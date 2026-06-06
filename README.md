# Simple Port Scanner

A lightweight multi-threaded TCP port scanner written in Python.

This project allows users to scan a target host within a specified port range and identify open TCP ports. It supports both hostnames and IP addresses, includes input validation, and uses concurrent scanning to improve performance.

---

## Features

- Multi-threaded TCP port scanning
- Scan custom TCP port ranges
- Hostname and IP support
- Open port detection
- Open port counting
- Custom thread count configuration
- Export scan results to JSON
- Display scan duration
- Automatic port range correction
- Input validation
- Port range validation
- Thread count validation
- Error handling
- Lightweight and dependency-free

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

Basic scan:

```bash
python3 scanner.py scanme.nmap.org 20 100
```

Custom thread count:

```bash
python3 scanner.py scanme.nmap.org 20 100 --threads 200
```

Save results to a JSON file:

```bash
python3 scanner.py scanme.nmap.org 20 100 --output results.json
```

Combine both options:

```bash
python3 scanner.py scanme.nmap.org 20 100 --threads 200 --output results.json
```

Example output:

```text
"Simple-Port-Scanner"

Resolved IP: 45.33.32.156

Starting scan...

    Port 22 is OPEN
    Port 80 is OPEN

Found 2 open ports.

Scan completed in 0.247 seconds.

Results saved to results.json
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

### v2.3

Implemented:

- Export scan results to JSON files
- Added `--output` command-line option
- Included scan metadata in exported results
- Added open port list export
- Added thread count export
- Added scan duration export

### v2.2

Implemented:

- Custom thread count configuration
- Added --threads command-line argument
- Thread count validation
- Improved performance tuning flexibility

### v2.1

Implemented:

- Command-line interface (CLI) using argparse
- Removed interactive input prompts
- Support for positional arguments (host, start port, end port)
- Improved usability for automation and scripting
- Foundation for advanced CLI features in future versions

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