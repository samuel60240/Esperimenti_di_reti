# Esperimenti di Reti e Laboratorio Socket

Repository dedicato alla raccolta di esercitazioni, script e test pratici svolti per il corso di **Architettura di Reti e Laboratorio**. Include esperimenti sulla comunicazione Client-Server, analisi dei protocolli della pila TCP/IP, cattura di pacchetti e utilizzo degli strumenti di diagnostica di rete.

---

## 📌 Indice dei Contenuti

- [Competenze e Concetti Chiave](#-competenze-e-concetti-chiave)
- [Struttura del Repository](#-struttura-del-repository)
- [Requisiti e Prerequisiti](#-requisiti-e-prerequisiti)
- [Guida all'Esecuzione dei Laboratori](#-guida-allesecuzione-dei-laboratori)
  - [1. Programmazione Socket (UDP & TCP)](#1-programmazione-socket-udp--tcp)

---

## 🎯 Competenze e Concetti Chiave

- **Programmazione di Rete in Python:**
  - Socket UDP (`SOCK_DGRAM`) e socket TCP (`SOCK_STREAM`).
  - Gestione del ciclo di vita dei socket: `bind()`, `sendto()`, `recvfrom()`, `encode()`, `decode()`.
  - Manipolazione di stringhe e byte in transito.
---

## 📂 Struttura del Repository

```text
.
├── 00_PYTHON_ENVIRONMENT/   # Configurazione e test dell'ambiente Python (venv)
├── UDPTest/                 # Configurazione e test di un server e un cliente con protocollo di comunicazione UDP
├── TCPTest/                 # Configurazione e test di un server e un cliente con protocollo di comunicazione TCP
└── README.md                # Documentazione del progetto
```
  
---

## 🛠️ Requisiti e Prerequisiti

Per eseguire gli script e gli esperimenti è necessario disporre di:

- **Sistema Operativo:** Linux (Ubuntu/Debian raccomandati) o ambiente equivalente.
- **Interprete:** Python 3.x
- **Strumenti di Rete:** `wireshark`, `tshark`, `iperf3`, `iputils-ping`, `netcat` / `ncat`.

---

## 🚀 Guida all'Esecuzione dei Laboratori

### 1. Programmazione Socket (UDP & TCP)

Per testare la comunicazione Client-Server basata su socket UDP:

1. **Avviare il Server:** Aprire un terminale e lanciare lo script del server:
   ```bash
   python3 UDPTest/UDPServer.py
   ```
2. **Avviare il Client:** Aprire un secondo terminale separato e lanciare il client:
   ```bash
   python3 0UDPTest/UDPClient.py
   ```
3. Inserire il testo richiesto nel client per osservare la risposta inviata ed elaborata dal server.

### 2. Diagnostica e Tracciamento (ICMP & Ping)

Verifica della connettività e misurazione del Round Trip Time (RTT) verso un host remoto:

```bash
# Invio di 4 pacchetti ICMP Echo Request
ping -c 4 8.8.8.8
```

### 3. Analisi di Rete con Wireshark

1. Avviare Wireshark da terminale o menu applicazioni:
   ```bash
   sudo wireshark
   ```
2. Selezionare l'interfaccia di rete attiva (`eth0`, `wlan0`, o `lo` per i test locali su `127.0.0.1`).
3. Applicare i filtri di visualizzazione (es. `icmp`, `udp.port == 12000`, `http`, `dns`).

---

## 🐍 Gestione dell'Ambiente di Sviluppo

Attivazione dell'ambiente virtuale Python prima di eseguire gli script:

```bash
# Dalla directory principale del progetto:
source 00_PYTHON_ENVIRONMENT/bin/activate

# Per disattivare l'ambiente al termine dei test:
deactivate
```

---

## 🔄 Note sull'Aggiornamento del Fork

Se il repository fa riferimento a un progetto docente originario, per sincronizzare le ultime modifiche locali mantenendo aggiornato il proprio lavoro:

```bash
# 1. Scarica i nuovi commit dall'upstream
git fetch upstream

# 2. Unisci le modifiche al ramo principale
git merge upstream/main

# 3. Aggiorna il repository remoto personale
git push origin main
```
