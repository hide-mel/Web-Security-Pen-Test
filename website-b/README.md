# Project Hermes

## Testing Scenario

You have recently graduated from your cyber security degree and have formed “We Test Pens Incorporated”.

PleaseHold (PleaseHold Pty. Ltd.) is an inbound call centre servicing multiple organisations including banks and telecommunication companies. Its owners have recently kicked off an initiative to migrate from a filing cabinet to an electronic HR system. They have selected HRHub, a startup in the HR management solutions industry.

Due to the rapid need to quickly migrate to a digital system due to COVID restrictions and the need to work from home, PleaseHold has rapidly begun the implementation of HRHub into a production environment. Before cutting over to the new system, PleaseHold would like to ensure that the system is penetration tested and secure.

PleaseHold has selected you for this task due to the high reputation of your cyber security degree, and a belief that you will perform with a very high degree of skill. Due to the aforementioned COVID restrictions, the organisation has a limited budget, limited time, and was not able to set up a full testing environment. You will be performing all your testing in a production environment and therefore must use great care and skill, performing only manual penetration testing, while being acutely aware of your behaviour in the organisation's environment to prevent potential denial of service attacks.

As you are now a professional, your goal is to present your findings in a high quality report for delivery at the end of this engagement. The quality of your work and the effort that you put in cannot be judged without a quality report detailing all your findings, potential consequences, and recommended remediations.

## Scope

Testing must only be performed on http://assignment-hermes.unimelb.life/
Testing must be manual only. Manual tools may be used (Burp, Zap, etc).
No load testing, denial of service (DOS) or distributed denial of service (DDOS) attacks. You may use Burp’s Intruder, but use less than 30 payloads per minute.

## Identified Vulnerabilities
● SQL Injection
● XSS
● SSRF
● SQL Wildcard Attack