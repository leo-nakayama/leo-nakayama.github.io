# 🦆 FOWL — Fully Operational Wisdom and Logic

## What is it?

**FOWL (Fully Operational Wisdom and Logic)** is my multi-machine laboratory for **Reflective Computing**, built as a living implementation of my concept, the **Philosophy of Systems**.

FOWL integrates distinct operating systems — **Ubuntu (desktop)**, **Fedora (laptop)**, **RHEL (server)**, and **Fedora Server (observatory)** — into a unified ecosystem that mirrors the architecture of thought: sensing, reasoning, storing, and reflecting.

At its core, FOWL orchestrates:

* **DSL Inference Applications** — for philosophical module computation (Aristotelian Biodome, Synthetic Naikan, etc.)
* **Linux/Python Automation** — for local and cross-node orchestration
* **Backup & Restoration Pipelines** — Borg, rsync, and tiered LVM storage (hot/warm/cold)
* **Observatory Stack** — Grafana and Prometheus for real-time introspection
* **Hybrid Orchestration** — AWS/Azure integration for off-premise compute extension

FOWL functions as both a **technical system** and a **conceptual instrument** — a laboratory where automation and reflection converge into one operational philosophy.

---

## Areas of Design

| Domain               | Description                                                                                    |
| -------------------- | ---------------------------------------------------------------------------------------------- |
| **Storage & Backup** | Tiered hot/warm/cold architecture using LVM, rsync, and Borg for integrity and recoverability. |
| **Automation**       | Linux and Python-based workflows for SSH, systemd, CI/CD, and multi-node orchestration.        |
| **AI & Inference**   | Local and remote DSL Runner apps operating on Ollama, OpenAI, or custom inference engines.     |
| **Observability**    | Grafana + Prometheus stack as the “reflective layer,” observing all operational states.        |
| **Hybrid Cloud**     | Integration points with AWS and Azure for flexible compute allocation and external data flow.  |
| **Creative Layer**   | Music stack using LilyPond and Euclidean rhythm algorithms; sonic analogues of system logic.   |

---

## Node Roles

| Node                          | Role                                                                  | Host OS       | Status     | Notes                                                                  |
| ----------------------------- | --------------------------------------------------------------------- | ------------- | ---------- | ---------------------------------------------------------------------- |
| 🐦‍🔥 **a00 (Fedora Server)** | *Observatory Node* — central Grafana & Prometheus metrics collector.  | Fedora Server | ✅ Active   | Dashboards operational (“Node Exporter Full”, “Prometheus 2.0 Stats”). |
| 🐔 **m900 (RHEL Server)**     | *Storage & Backup Tier* — Borg + rsync layer with SELinux tuning.     | RHEL          | ⚠️ Partial | Node exporter pending (firewall tuning).                               |
| 🐧 **g16 (Ubuntu Desktop)**   | *Computation Node* — GPU inference (Ollama + CUDA) and DSL execution. | Ubuntu        | ✅ Active   | AI/ML and Reflective Computing engine.                                 |
| 🦆 **e14 (Fedora Laptop)**    | *Development Node* — CI/CD staging and Python DSL editing.            | Fedora KDE    | ✅ Active   | Local build + sync environment.                                        |
| **iPad Pro**                  | *Control Surface* — remote Grafana access, monitoring interface.      | iPadOS        | ✅ Active   | Visualization only (no telemetry agent).                               |
| **LAN Backbone**              | *Network Fabric* — static 192.168.1.0/24 mapping across all hosts.    | —             | ✅ Stable   | Scraping via Prometheus ports (9100/tcp).                              |

---

## Monitoring & Security Context

* **Prometheus** scrapes metrics every 15 s from all nodes.
* **Grafana** dashboards imported (IDs 1860, 3662).
* **SELinux** ports relabeled (`http_port_t` for Prometheus/Grafana).
* **SSH access** restricted via key-pair auth only; root login disabled.
* **Systemd units** handle periodic backups and exporter health checks.

---

## Integration Roadmap

| Stage                         | Goal                                                                      | Notes                                        |
| ----------------------------- | ------------------------------------------------------------------------- | -------------------------------------------- |
| **I. Metric Harmony**         | Ensure consistent node_exporter data from all nodes.                      | In progress; m900 pending.                   |
| **II. Reflexive Correlation** | Link Observation Reports (Lyceum Vault) to Grafana timelines.             | Planned via Grafana Annotations API or Loki. |
| **III. LLM Integration**      | Extend DSL Runner to query local Ollama (Llama 3, Gemma 2).               | Prototype ready on g16.                      |
| **IV. Cloud Sync**            | Automate cross-tier replication to AWS/Azure buckets.                     | Design stage.                                |
| **V. Reflexivity 2.0**        | Full loop: observation → automation → reflection → philosophical insight. | Long-term direction.                         |

---

## Philosophical Context

FOWL operationalizes the **Philosophy of Systems** — a model where infrastructure itself becomes a reflective medium.
Each node, process, and metric embodies a part of an Aristotelian structure:

| Cause         | Layer                  | Example                                          |
| ------------- | ---------------------- | ------------------------------------------------ |
| **Material**  | Hardware & OS          | NVMe tiers, RHEL kernel, storage volumes         |
| **Formal**    | Configuration & Design | DSL schemas, YAML modules, orchestration scripts |
| **Efficient** | Agents & Processes     | Cron, rsync, Grafana exporters, LLM backends     |
| **Final**     | Telos / Purpose        | Self-observation and conceptual integration      |

Thus, FOWL is not just a system — it’s an *epistemic mirror* through which the act of computing reveals its own philosophical structure.

---
