# SynapseHub

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io)

**Enterprise integration orchestrator — Connect your entire business stack with intelligent data sync.**

SynapseHub provides a unified platform for managing bidirectional data flows between Salesforce, QuickBooks, Slack, Stripe, HubSpot, AWS, and more.

---

## Features

### Integration Management
- **Visual Connection Map** — See all data flows at a glance
- **Real-Time Sync** — Bidirectional data synchronization
- **Connection Matrix** — Configure sync rules between any systems

### Monitoring
- **Live Activity Feed** — Watch syncs happen in real-time
- **Health Dashboard** — System status and uptime metrics
- **Latency Tracking** — Sub-millisecond performance monitoring

### Supported Platforms
- Salesforce
- QuickBooks
- Slack
- Stripe
- HubSpot
- AWS

---

## Dashboard

```
┌─────────────────────────────────────────────────────────┐
│  🧠 SynapseHub - Enterprise Integration Orchestrator    │
├────────────┬────────────┬────────────┬─────────────────┤
│ 6 Systems  │ 15 Active  │ 176K Syncs │    12ms Avg     │
│ Connected  │ Connections│   Today    │    Latency      │
├────────────┴────────────┴────────────┴─────────────────┤
│                                                         │
│  🔌 Connected Systems                                   │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐   │
│  │  Salesforce  │ │  QuickBooks  │ │    Slack     │   │
│  │  ● 12.8K/hr  │ │  ● 8.9K/hr   │ │  ● 45.2K/hr  │   │
│  └──────────────┘ └──────────────┘ └──────────────┘   │
│                                                         │
│  📊 Real-Time Activity                                  │
│  ┌─────────────────────────────────────────────────┐   │
│  │ 2s ago  │ Stripe → QuickBooks │ Payment synced  │   │
│  │ 5s ago  │ Salesforce → HubSpot│ Contact updated │   │
│  │ 8s ago  │ Slack → Salesforce  │ Deal note added │   │
│  └─────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

---

## Architecture

```
                    ┌─────────────┐
                    │  SynapseHub │
                    │    Core     │
                    └──────┬──────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
   ┌────▼────┐       ┌────▼────┐       ┌────▼────┐
   │Salesforce│       │QuickBooks│       │  Slack  │
   └────┬────┘       └────┬────┘       └────┬────┘
        │                  │                  │
        └──────────────────┴──────────────────┘
                    Bidirectional Sync
```

---

## Quick Start

```bash
# Clone and setup
git clone https://github.com/nickstafford/synapsehub.git
cd synapsehub
pip install -r requirements.txt

# Configure connectors in .env
cp .env.example .env

# Run
streamlit run app.py
```

---

## Project Structure

```
SynapseHub/
├── app.py              # Streamlit entry point
├── connectors/         # Platform integrations
│   ├── salesforce.py
│   ├── quickbooks.py
│   ├── slack.py
│   ├── stripe.py
│   └── hubspot.py
└── src/
    ├── sync_engine.py  # Core sync logic
    ├── mapper.py       # Field mapping
    └── monitor.py      # Health & metrics
```

---

## Sync Rules

| Source | Destination | Trigger | Data |
|--------|-------------|---------|------|
| Stripe | QuickBooks | Payment received | Invoice, amount, customer |
| Salesforce | HubSpot | Contact updated | Name, email, company |
| Slack | Salesforce | #deals mention | Note on opportunity |
| QuickBooks | Salesforce | Invoice created | Link to opportunity |

---

## License

MIT License

---

<p align="center">
  Built by <a href="https://nickstafford.dev">Nick Stafford</a>
</p>
