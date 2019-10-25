# Responsibilities will include:
## • Characterize and analyze network traffic to identify anomalous activity and potential threats to network resources;
* Probably means IDS\IPS
* IDS scans network traffic as it goes across the network.
* IPS are intended to prevent malicious events from occurring by preventing attacks as they are happening.
    * Denial of Service
    * DDOS
    * Exploits
    * Worms
    * Viruses 
    * Works using signature
* IDS just reacts to certain network traffic going across the network, kind of like an alarm.
* IDS/IPS compare network packets to a cyber-threat database containing signatures of cyber-attacks and flag any matching packets. 
    * So like anti-virus but for network traffic.
* IDS is a monitoring system, while IPS is a control system.
    * Controls what happens to that packet?
    * Packet is a protocol data unit at layer 3, the Network Layer.
        * Data unit at layer 2, Data Link Layer, is a **frame**.
    * At Layer 4, the transport layer, the correct term is segment or datagram.
    * In ICP/IP communications over Ethernet, a TCP segment is carried in one or more IP packets which is carried in one or more frames.
    * Most network packets are split into three parts.
        1. Header
            * Length of packet
            * Synchronization
            * Packet number
            * Protocol: set of instructions that allows a computer to talk across a network.
            * Destination address
            * Originating address
        2. Payload, body, data
        3. Trailer, footer
## • Coordinate with enterprise-wide cyber defense staff to validate network alerts;
## • Ensure that cyber security-enabled products or other compensating security control technologies reduce identified risk to an acceptable level;
## • Document and escalate incidents (including event’s history, status, and potential impact for further action) that may cause ongoing and immediate impact to the environment;
## • Perform cyber defense trend analysis and reporting;
## • Perform event correlation using information gathered from a variety of sources within the enterprise to gain situational awareness and determine the effectiveness of an observed attack;
## • Perform security reviews and identify security gaps in security architecture resulting in recommendations for inclusion in the risk mitigation strategy;
## • Plan and recommend modifications or adjustments based on exercise results or system environment;
## • Provide daily summary reports of network events and activity relevant to cyber defense practices;
## • Receive and analyze network alerts from various sources within the enterprise and determine possible causes of such alerts;
## • Provide timely detection, identification, and alerting of possible attacks/intrusions, anomalous activities, and misuse activities and distinguish these incidents and events from benign activities;
## • Use cyber defense tools for continual monitoring and analysis of system activity to identify malicious activity;
## • Analyze identified malicious activity to determine weaknesses exploited, exploitation methods, effects on system and information;
## • Determine tactics, techniques, and procedures (TTPs) for intrusion sets;
## • Examine network topologies to understand data flows through the network;
## • Recommend computing environment vulnerability corrections;
## • Identify and analyze anomalies in network traffic using metadata;
## • Conduct research, analysis, and correlation across a wide variety of all source data sets (indications and warnings);
## • Work with stakeholders to resolve computer security incidents and vulnerability compliance;
## • Provide advice and input for Disaster Recovery, Contingency, and Continuity of Operations Plans.

Preferred Skills
The preferred candidate should possess the following:
## • Excellent verbal and oral communication skills;
## • Ability to analyze malware;
## • Ability to conduct vulnerability scans and recognize vulnerabilities in security systems;
## • Ability to accurately and completely source all data used in intelligence, assessment and/or planning products;
## • Ability to apply cyber security and privacy principles to organizational requirements (relevant to confidentiality, integrity, availability, authentication, non-repudiation);
## • Ability to apply techniques for detecting host and network-based intrusions using intrusion detection technologies;
## • Ability to interpret the information collected by network tools (e.g. NsLookup, Ping, and Traceroute).

1. What is the difference between REST and SOAP
    ![](https://content-static.upwork.com/blog/uploads/sites/3/2017/04/19075723/SOAP-v-REST-1.png)
    * https://www.upwork.com/hiring/development/soap-vs-rest-comparing-two-apis/
    * SOAP is a protocol, REST (**Re**presentational **S**tate **T**ransfer) is an architectural style (design pattern).
    * A REST API (Application Programming Interface) can use the SOAP protocol just like it can use HTTP.
        * REST is a set of rules for how to build a web API.
            1. client-server
            2. stateless
            3. cacheable
            4. uniform interface
            5. layered system
            6. code on demand
        * An API is a piece of software that plugs one application directly into the data and services or another.
        * Let's two pieces of software communicate, makes it easier to share data sets.
        * A web service API.
        * Based on URIs and the HTTP protocol
        * Uses JSON for data format
        * REST benefits:
            1. resource limitations
            2. few security requirements
            3. browser compatibility
            4. discoverability
            5. data health
            6. scalability
    * SOAP (Simple Object Access Protocol)
        * Has more standards that REST like security and how messages are sent.
        * Has more overhead but useful for organization that requires security, transaction, and ACID compliance.
        * Ideal for enterprise-type situations.
        * SOAP API includes higher level of security (mobile application interfacing with a bank)
        * Tighter security:
            * Web Services-Security
                * Apply security to Web services
                * Integrity and confidentiality can be enforced on messages and allows the communication of security token formats such as SAML (Security Assertion Markup Language), Kerberos, X.509
                * Use of XML signature and XML encryption to provide end to end security
            * SSL Support
            * End to End reliability
            * ACID compliance:  a set of properties of database transactions intended to guarantee validity even in the event of errors, power failures, etc.
                * Atomicity: transactions are all or nothing 
                * Consistency: only valid data is saved
                * Isolation: transactions do not affect each other
                * Durability: written data will not be lost
    * REST expose a public API (for data) while SOAP exposes components of application logic as services
        * REST accesses data while SOAP performs operations through messaging patterns

2. Have you worked with an IDS?
    * I have experience working with SNORT which is an open sourced intrusion prevention system. 
    * Uses signature-based intrusion detection as well as rule-sets. 
        * Rule-sets can do 0-day detection on the actual vulnerability, not a unique piece of data. 
        * Signature is distinctive marks or characteristics in an exploit. 
            * Limited protection capabilities as the virus has already infected someone before a signature can be written.
            * Exploits are the methodologies or techniques that are utilized to take advantage of vulnerabilities. 
    * Snort performs real-time traffic analysis and packet logging on IP networks. 
    * Things Snort can do:
        1. Protocol analysis
        2. Content searching/matching
        3. Detection of attacks and probes:
            * Buffer overflows
            * Stealth port scans
            * CGI attacks 
                * Common Gateway Interface?
                * CGI-BIN?
                * Root folder of every web server
                * Server fingerprinting
                    * ServerTokens Full
                    * ServerSignature On
                * DOS
                    * slowloris.pl
                * Command Injection
                    * accessing /etc/password
            * SMB probes
            * OS fingerprinting
            * More 
