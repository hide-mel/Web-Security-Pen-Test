# Project Zeus

## Scenario

Bank of UniMelb has just come to market and provides an easy, self-service banking solution to its clients. Users can open new accounts (with proper identity verification measures), perform banking transactions (such as money transfers and bill payments) with existing accounts, or close their accounts all from the comfort of their own laptop or computer. Branch managers have higher privileges than users, and can communicate and interact with their clients (users assigned to them), see their accounts, and freeze them.

COVID-19 restrictions and the need to work from home have meant Bank of UniMelb wants a rapid migration to this new digital system. Executives have selected you to ensure the system is penetration tested and secure before it is deployed. They love the innovation you have brought to the penetration testing game with your business “We Test Pens Incorporated” and have high expectations of you.

Bank of UniMelb has selected you for this task due to the high reputation of your cyber security degree, and a belief that you will perform with a very high degree of skill. Due to the aforementioned COVID restrictions, the organisation has a limited budget, limited time, and was not able to set up a full testing environment. You will be performing all your testing in a production environment and therefore must use great care and skill, performing only manual penetration testing, while being acutely aware of your behaviour in the organisation's environment to prevent potential denial of service attacks.

As you are now a professional, your goal is to present your findings in a high quality report for delivery at the end of this engagement. The quality of your work and the effort that you put in cannot be judged without a quality report detailing all your findings, potential consequences, and recommended remediations. 

## Threat Modelling

Using STRIDE, threat model the application and identify the possible vulnerabilities (at least two per letter of the acronym). Also, make sure you state who the relevant threat actor is (e.g. state actor, external attacker, bank client, internal employee, etc.). We expect some descriptions around the vulnerabilities, diving into some details, alongside the remediation for them. Should you require knowing the development stack for your remediations, please assume it is LAMP.

Required sections of the report:
1. Vulnerabilities / threats
2. Correlating threats to threat actors
3. Remediations

## Scope

Testing must only be performed on http://assignment-zeus.unimelb.life/
Testing must be manual only. Manual tools may be used (Burp, Zap, etc), however you may not use the automated scanning capabilities of these tools.
No load testing, denial of service (DOS) or distributed denial of service (DDOS) attacks. You may use Burp’s Intruder, but use less than 30 payloads per minute.
You may also use DirBuster, but you must limit the number of threads to 5.

## Out of Scope

The following vulnerabilities are known to the developer and must not be submitted within the penetration testing report:
1. Insufficient password policies
2. Sensitive information over HTTP
3. Directory listing enabled
4. Lack of rate limiting on the login page
5. Server-status exposed

## Identified Vulnerabilities
● Bypassing client-side authentication
● IDOR via a hidden parameter
● Privilege escalation
● Sensitive files / directories left behind during testing / development