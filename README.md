# Argo

```
 █████╗ ██████╗  ██████╗  ██████╗ 
██╔══██╗██╔══██╗██╔════╝ ██╔═══██╗
███████║██████╔╝██║  ███╗██║   ██║
██╔══██║██╔══██╗██║   ██║██║   ██║
██║  ██║██║  ██║╚██████╔╝╚██████╔╝
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ 
```

> CCTV / IoT recon & exploitation framework — *named after Argus Panoptes, the all-seeing guardian of Greek mythology*

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
![Python](https://img.shields.io/badge/python-3.7%2B-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux-lightgrey.svg)

---

## What is Argo?

Argo is a modular reconnaissance and exploitation framework targeting CCTV cameras, IoT devices, and network appliances. It automates the full pipeline from host discovery to post-exploitation, with an interactive arrow-key driven menu that keeps everything in one place.

**Workflow:**

```
Shodan / Censys  →  Up-tester  →  Vuln-tester  →  Exploit  →  Host Control
```

Each phase writes its output to a file that feeds into the next, so you can run them in order or jump straight to a specific step.

---

## Installation

```bash
git clone https://github.com/M0tHs3C/Argo.git
cd Argo
pip install -r requirements.txt
python argo.py
```

---

## Configuration

Argo reads API keys from **environment variables first**, then falls back to the files in `api/`.

| Key | Env variable | Fallback file |
|-----|-------------|---------------|
| Shodan | `SHODAN_API_KEY` | `api/api.txt` |
| Censys API ID | `CENSYS_API_ID` | `api/censys_api.txt` (line 1) |
| Censys Secret | `CENSYS_API_SECRET` | `api/censys_api.txt` (line 2) |

Copy `.env.example` to `.env` and fill in your keys, or just let the tool prompt you on first run — it will save them to the fallback files automatically.

> `api/` and `host/` are gitignored. Your keys and host lists will never be accidentally committed.

---

## Phases

### 1 · Host Gathering
Search Shodan or Censys using built-in device-specific queries. Results are saved to `host/host.txt`.

Supported queries include Hikvision, telephone, telephone2, icare, JAWS, ANPR, FortiOS, and more — or enter a custom query.

### 2 · Up Tester
TCP-checks all gathered hosts and filters out unreachable ones. Writes live hosts to `host/up_host.txt`.

### 3 · Vuln Tester
Runs device-specific fingerprinting and false-positive checks against live hosts. Confirmed targets are written to `host/vuln_host.txt`.

### 4 · Exploit Menu
Three categories of exploits, each with its own submenu:

#### Cameras
| Device | Technique |
|--------|-----------|
| Hikvision | Default credentials / known exploit |
| RSP device | Device exploit |
| Viola DVR | Default credential bruteforce |
| Avtech DVR | Device exploit |
| Geovision | Device exploit |
| GoAhead | Credential extraction |
| Atlantis | Credential bruteforce |
| ANPR | Default credential bruteforce |
| RTSP | Generic stream tester |
| JAWS | RCE |

#### VPNs
| Device | Technique |
|--------|-----------|
| FortiOS | Known exploit |

#### IoT
| Device              | Technique |
|---------------------|-----------|
| icare               | Default credential bruteforce |
| telephone           | SQLi auth bypass · Mass RCE · Interactive shell |
| telephone2          | Default credential bruteforce · Mass RCE · Interactive shell |
| Energy Sentinel Web | Default credentials |
| Bticino             | Auth bypass (VLN-04 validatein) · Default credential bruteforce |

### 5 · Host Control
Post-exploitation panel for hosts with confirmed access. Select a target from `vuln_host.txt` and run:

- **Port scan** — TCP connect scan across common ports (FTP, SSH, Telnet, HTTP/S, RDP, and more), with color-coded open/closed output

### 6 · Delete Host Lists
Clears all generated `.txt` files in `host/` to start fresh.

---

## Interactive Shell

For devices that support RCE (telephone, telephone2), Argo drops into a persistent semi-interactive shell:

- Host selected via arrow-key menu from `vuln_host.txt`
- `whoami` probe runs on entry to confirm the shell is alive
- Fixed header pinned to the top of the terminal showing the active target — stays visible regardless of how much output scrolls by
- Each command sends a new HTTP request; output is printed inline
- `exit` / `quit` / Ctrl+C to return to the menu

---

## Project Structure

```
argo.py               entry point & main menu
exploit/              per-device exploit modules + menu router
lib/                  shodan/censys search, query builder, menu UI
modules/              up tester, vuln tester, c2/host control
host/                 generated host lists (gitignored)
api/                  API key files (gitignored)
.env.example          template for environment-based key config
requirements.txt      Python dependencies
```

---

## Dependencies

```
shodan, censys, requests, rtsp, colorama, questionary
```

---

## Legal

> **Disclaimer:** Usage of Argo against targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state, and federal laws. The developers assume no liability and are not responsible for any misuse or damage caused by this program.
>
> This tool is intended for authorized security testing, penetration testing engagements, and educational purposes only.
