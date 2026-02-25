# SIEM-Implementation-and-Log-Analysis

# SIEM Implementation & Live Cloud Attack Analysis

## 🎯 Objective
This project involved setting up a live **SIEM (Security Information and Event Management)** instance to monitor, analyze, and respond to real-time security events. The goal was to observe global "brute force" attacks via RDP and visualize the data to understand threat actor behaviors.

## 🛠️ Technologies & Tools Used
* **SIEM:** [e.g., Microsoft Sentinel / ELK Stack / Splunk]
* **Cloud Provider:** [e.g., Azure / AWS]
* **Logging:** Windows Event Logs, Sysmon
* **Scripting:** PowerShell / Python (for log transformation)
* **Mapping:** [e.g., IPStack API for Geolocation data]

## 🏗️ Architecture
1.  **Exposed VM:** A Windows 10 Virtual Machine was deployed with all firewalls open to act as a "Honey Pot."
2.  **Telemetry Collection:** Configured the VM to send Security and System logs to the SIEM workspace.
3.  **Data Enrichment:** Used a custom script to extract IP addresses from failed logins and correlate them with physical locations.
4.  **Visualization:** Built a world map dashboard showing attack origins in real-time.

## 📊 Results & Analysis
> [!IMPORTANT]
> Within 24 hours of deployment, the system recorded over **[Insert Number]** unique attack attempts from **[Insert Number]** different countries.

### Attack Patterns Observed:
* **Credential Stuffing:** High-frequency attempts using common usernames (admin, user, guest).
* **Geographic Hotspots:** The majority of attacks originated from [Country A] and [Country B].

## 📸 Dashboards
![Final SIEM Dashboard](docs/Dashboard_Snapshot.png)
*Figure 1: Real-time map of RDP brute-force attacks.*

## 📜 Key Learnings
* Deep understanding of **Windows Event ID 4625** (Failed Logon).
* Practical experience in **Log Normalization** and KQL/SPL querying.
* Insight into the speed at which automated bots find and attack exposed cloud assets.
