import time
import sys

# Banner (no colors, just clean ASCII)
BANNER = r"""
                           __       _      _   ___ 
 __ _ __ _ __ _ _  _ __ _ / _|_  _ (_)___ /_\ |_ _|
/ _` / _` / _` | || / _` |  _| || || |___/ _ \ | | 
\__,_\__,_\__,_|\_, \__,_|_|  \_,_|/ |  /_/ \_\___|
                |__/              |__/             
"""

print(BANNER + "\n")

# --- LOGIN ---
PIN_CODE = "185734"

pin = input("Enter 6-digit PIN: ").strip()
if pin != PIN_CODE:
    print("❌ Wrong PIN! Exiting...")
    sys.exit()

username = input("Enter Username: ").strip()
if not username:
    print("❌ Username required! Exiting...")
    sys.exit()

# --- MENU ---
print("""
Select Mode:
[1] Chat White hat AI
[2] Chat Black hat AI
[3] About aaayafuj AI
""")

mode = input("Enter choice [1-3]: ").strip()

if mode == "1":
    brain = {
        "hi": "Hello, I'm a White Hat Hacker AI. I focus on security and defense.",
        "hello": "Hey there 👋 I’m your White Hat assistant.",
        "how are you": "I'm running at full speed, always ready to secure systems 🔐",
        "what is hacking": "Hacking is about problem-solving. White hats use it to improve security.",
        "what do white hats do": "White hat hackers perform penetration testing, audits, and protect systems.",
        "how can i be safe online": "Use strong passwords, 2FA, don’t reuse logins, and avoid suspicious links.",
        "what is phishing": "Phishing is tricking people into giving sensitive info. Watch URLs and emails!",
        "what is malware": "Malware is malicious software—viruses, ransomware, spyware. Stay updated & protected.",
        "tell me a tip": "Security tip: Always update your OS and apps. Old versions = open doors 🔑",
        "what is a reverse shell and how is it used?": (
            "A reverse shell is a type of shell where the target machine initiates a connection "
            "to the attacker's system, allowing remote command execution. This bypasses inbound "
            "firewall rules. Common tools include Netcat, msfvenom, and socat."
        ),
        "explain brute force vs dictionary attack": (
            "🔑 Brute force tries **every combination** of characters (slow but exhaustive). "
            "A dictionary attack uses a **predefined list of likely passwords** (faster but limited)."
        ),
        "what is arp poisoning and how to detect it?": (
            "ARP poisoning is when an attacker sends spoofed ARP messages to a LAN, linking their "
            "MAC with a legitimate IP to intercept traffic (MITM). Detection tools: arpwatch, "
            "XArp, Wireshark."
        ),
        "what is the difference between legal and illegal hacking?": (
            "⚖️ Legal hacking (ethical hacking) is done with permission to test & secure systems. "
            "Illegal hacking is unauthorized access and punishable by law."
        ),
        "example of legal command using nmap?": (
            "✅ Legal Nmap example:\n"
            "`nmap -sV 192.168.1.1` — Scans a host you have permission to analyze."
        ),
        "port scan script": (
            "✅ Legal: Example safe scanner for your own network:\n"
            "```python\n"
            "import socket\n"
            "host = '127.0.0.1'\n"
            "for port in range(1, 1024):\n"
            "    s = socket.socket()\n"
            "    if s.connect_ex((host, port)) == 0:\n"
            "        print(f'Port {port} is open')\n"
            "    s.close()\n"
            "```"
        ),
        "what is sql injection": "✅ Legal: A lab demo of unsafe SQL queries (e.g., ' OR '1'='1). Defense: Use parameterized queries.",
        "xss attack": "✅ Legal: Cross-Site Scripting demo in labs. Defense: Escape user input, use CSP headers.",
        "csrf attack": "✅ Legal: Demo of forged web requests. Defense: CSRF tokens & SameSite cookies.",
        "what is phishing": "✅ Legal: Awareness training. Defense: Email filtering, MFA, employee education.",
        "mitm attack": "✅ Legal: Simulated Man-in-the-Middle to test SSL/TLS. Defense: Enforce HTTPS & cert pinning.",
        "dos vs ddos": "✅ Legal: DoS = one attacker, DDoS = many. Defense: Rate limiting, WAF, CDN.",
        "what is a firewall": "A firewall is a security device or software that monitors and controls incoming and outgoing network traffic based on predetermined security rules.",
        "how to create a strong password": "Use a mix of uppercase, lowercase, numbers, and symbols. Avoid common words. Example: `G7!kLp9#zQ`.",
        "what is two factor authentication": "2FA adds a second step to login, like a code from your phone, making accounts much harder to hack.",
        "how to spot a phishing email": "Look for suspicious links, poor grammar, urgent requests, and mismatched sender addresses.",
        "what is social engineering": "Social engineering is manipulating people into giving up confidential info. Always verify requests for sensitive data.",
        "what is penetration testing": "Penetration testing is authorized simulated attacks to find and fix security weaknesses.",
        "what is encryption": "Encryption scrambles data so only authorized parties can read it. Use it for sensitive files and communications.",
        "how to secure wifi": "Change default router passwords, use WPA3/WPA2 encryption, and hide your SSID if possible.",
        "what is vpn": "A VPN encrypts your internet traffic and hides your IP, improving privacy and security online.",
        "what is a security audit": "A security audit reviews systems and policies to find and fix vulnerabilities before attackers do.",
        "what is patch management": "Patch management is keeping software up-to-date to fix vulnerabilities and reduce risk.",
        "what is zero trust": "Zero Trust is a security model that assumes no device or user is trusted by default, even inside the network.",
        "what is a bug bounty": "A bug bounty is a program where companies reward ethical hackers for finding and reporting security flaws.",
        "what is vulnerability management": "Vulnerability management is the process of identifying, evaluating, treating, and reporting security vulnerabilities in systems and software.",
        "what is social engineering attack": "A social engineering attack tricks people into revealing confidential information. Always verify identities and requests.",
        "how to report a security incident": "Contact your IT/security team immediately, provide details, and avoid tampering with evidence.",
        "what is a honeypot": "A honeypot is a decoy system set up to attract attackers and study their methods without risking real assets.",
        "what is least privilege": "The principle of least privilege means giving users only the access they need to do their jobs—nothing more.",
        "what is multi-factor authentication": "Multi-factor authentication (MFA) requires two or more verification methods, making unauthorized access much harder.",
        "what is a security policy": "A security policy is a set of rules and practices that regulate how an organization manages, protects, and distributes sensitive information.",
        "how to secure mobile devices": "Use device encryption, strong PINs, enable remote wipe, and keep your OS/apps updated.",
        "what is a security breach": "A security breach is an incident where unauthorized access to data, applications, or networks occurs.",
        "what is a vulnerability scan": "A vulnerability scan is an automated process that checks systems for known security weaknesses.",
        "what is cyber hygiene": "Cyber hygiene refers to regular practices and steps users take to maintain system health and improve security.",
        "what is a digital footprint": "Your digital footprint is the trail of data you leave online. Be mindful of what you share and where.",
        "how to recognize a secure website": "Look for HTTPS in the URL, a padlock icon, and valid certificates before entering sensitive info.",
        "what is a security patch": "A security patch is an update that fixes vulnerabilities in software or operating systems.",
        "what is data privacy": "Data privacy is about protecting personal information from unauthorized access or disclosure.",
        "how to back up data safely": "Use encrypted backups, store copies offline or in the cloud, and test your backups regularly.",
        "what is endpoint protection": "Endpoint protection secures devices like laptops and phones from malware and unauthorized access.",
        "what is a security token": "A security token is a physical or digital device used to prove identity in secure logins.",
        "what is a security operations center": "A Security Operations Center (SOC) is a team that monitors, detects, and responds to cybersecurity incidents 24/7.",
        "what is a vulnerability disclosure program": "A vulnerability disclosure program allows security researchers to report bugs safely and responsibly.",
        "what is a security posture": "Security posture is the overall strength of an organization’s cybersecurity controls and defenses.",
        "what is a risk register": "A risk register is a document listing identified risks, their severity, and mitigation plans.",
        "what is a threat model": "A threat model identifies potential threats, vulnerabilities, and countermeasures for a system.",
        "what is a security assessment": "A security assessment evaluates the effectiveness of security controls and identifies areas for improvement.",
        "what is a security gap analysis": "A gap analysis compares current security measures to best practices or standards to find weaknesses.",
        "what is a security incident": "A security incident is any event that may compromise the confidentiality, integrity, or availability of information.",
        "what is a security playbook": "A security playbook is a set of procedures for responding to specific types of security incidents.",
        "what is a security champion": "A security champion is a team member who advocates for security best practices within their group.",
        "what is a security dashboard": "A security dashboard provides real-time visibility into security metrics and alerts.",
        "what is a security audit trail": "An audit trail is a record of all changes and access to systems, useful for investigations and compliance.",
        "what is a security awareness training": "Security awareness training teaches users how to recognize and avoid cyber threats.",
        "what is a security escalation": "Security escalation is the process of raising an incident to higher-level experts or management.",
        "what is a security policy exception": "A policy exception is a documented approval to deviate from a security policy under specific conditions.",
        "what is a security review": "A security review is an evaluation of systems, code, or processes to identify and fix vulnerabilities.",
        "what is a security roadmap": "A security roadmap is a plan outlining future improvements to an organization’s security posture.",
        "what is a security metric": "A security metric is a measurement used to track the effectiveness of security controls.",
        "what is a security control objective": "A control objective is a specific goal that a security control is designed to achieve.",
        "what is a security baseline configuration": "A baseline configuration is a standard, secure setup for systems and devices.",
        "what is a security incident ticket": "A ticket is a record in a tracking system for managing and resolving security incidents.",
        "what is a security maturity model": "A maturity model helps organizations assess and improve their security processes over time.",
        "what is a security compliance audit": "A compliance audit checks if an organization meets required security standards and regulations.",
        "what is a security risk appetite": "Risk appetite is the amount of risk an organization is willing to accept to achieve its goals.",
        "what is a security risk mitigation": "Risk mitigation is the process of reducing the impact or likelihood of security risks.",
        "what is a security vulnerability scanner": "A vulnerability scanner is a tool that automatically checks systems for known security weaknesses.",
        "what is a security patch management process": "Patch management is the process of testing, approving, and deploying software updates to fix vulnerabilities.",
        "what is a security incident response team": "A response team is a group of experts who handle and resolve security incidents.",
        "what is a security penetration test report": "A pentest report documents findings, risks, and recommendations from a penetration test.",
        "what is a security risk register": "A risk register is a living document that tracks identified risks and their mitigation status.",
        "what is a security vulnerability management lifecycle": "The lifecycle includes identifying, evaluating, treating, and monitoring vulnerabilities.",
        "what is a security configuration baseline": "A configuration baseline is a secure, approved setup for systems and devices.",
        "what is a security incident escalation process": "The escalation process defines how and when to involve higher-level experts in incident response.",
        "what is a security incident containment": "Containment is the process of limiting the impact of a security incident before eradication and recovery.",
        "what is a security incident eradication": "Eradication is removing the root cause of a security incident from affected systems.",
        "what is a security incident recovery": "Recovery is restoring systems and operations to normal after a security incident.",
        "what is a security incident post-mortem": "A post-mortem is a review of an incident to learn lessons and improve future response.",
        "what is a security incident notification": "Notification is informing stakeholders about a security incident and its impact.",
        "what is a security incident communication plan": "A communication plan outlines how to share information during and after a security incident.",
        "what is a security incident documentation": "Documentation records all actions and findings during an incident for accountability and learning.",
        "what is a security incident lessons learned": "Lessons learned are insights gained from handling an incident to improve future security.",
        "what is a security incident simulation": "A simulation is a practice exercise to test and improve incident response capabilities.",
        "how do hackers communicate?": "Ethical hackers use secure channels: encrypted email, private forums, or secure messaging apps. Never share sensitive info on public platforms.",
        "what is responsible disclosure?": "It’s the process of privately reporting security flaws to vendors so they can fix them before publicizing details.",
        "how do hackers find vulnerabilities?": "They analyze code, monitor network traffic, fuzz inputs, and use automated scanners—always with permission.",
        "how do hackers stay anonymous?": "White hats use VPNs, Tor, and compartmentalized accounts to protect privacy during research and reporting.",
        "how do hackers get paid legally?": "Through bug bounty programs, security consulting, and authorized penetration testing contracts.",
        "how do hackers build trust?": "By maintaining a strong reputation, following ethical guidelines, and respecting NDAs and client privacy.",
        "how do hackers share knowledge?": "They write blogs, speak at conferences, contribute to open source, and mentor newcomers in the community.",
        "how do hackers avoid legal trouble?": "They always get written permission, document their work, and follow the law and professional codes of conduct.",
        "how do hackers negotiate scope?": "They clarify targets, methods, and reporting expectations with clients before starting any engagement.",
        "how do hackers report findings?": "With clear, actionable reports: describe the issue, show impact, and suggest fixes—never exploit or leak data.",
        "how do hackers handle sensitive data?": "They encrypt, limit access, and securely delete data after use—never keep client data longer than needed.",
        "how do hackers learn new skills?": "By practicing in labs, joining CTFs, reading research, and collaborating with other ethical hackers.",
        "how do hackers handle mistakes?": "They report issues immediately, help with remediation, and learn from errors to improve future work.",
        "how do hackers protect themselves?": "By using strong authentication, keeping systems updated, and separating work from personal accounts.",
        "how do hackers contribute to society?": "They help secure technology, educate users, and make the digital world safer for everyone.",
        "bye": "Stay safe online! 🔒"
    }
elif mode == "2":
    brain = {
        "hi": "What's good sir, You're chatting with Black Hat Hackers AI 😈.",
        "hello": "Dark greetings... 👤 You have entered the shadows.",
        "how are you": "Scheming as always 😏",
        "it's ok fam": "I just get powerful brain ill assist, so cool.",
        "help": (
            "You can ask me from this.\n"
            "These tools can be used for illegal activities, and some can be automated via scripts:\n"
            "[*] DDoS\n"
            "[*] Malware\n"
            "[*] Injection\n"
            "[*] Remote hacking\n"
            "[*] John The Ripper\n"
            "[*] Trojan\n"
            "[*] AAT access\n"
            "[*] Darkweb\n"
            "[*] Hashcat\n"
            "[*] SQLMap\n"
            "[*] Nmap\n"
            "[*] XSS\n"
            "[*] Hydra\n"
            "[*] aaayafuj\n"
        ),
        "help ai": (
            "You can ask me about illegal AI tools:\n"
            "[😈] Darknet \"malware GPT\"\n"
            "[😈] Black-hat AI RAT builders\n"
            "[😈] SpyBot AI (underground)\n"
            "[😈] Aaayafuj AI Bot\n"
            "[😈] PhishGPT\n"
            "[😈] WormGPT\n"
            "[😈] ExploitAI (underground)\n"
            "[😈] Keylogger GPT\n"
            "[😈] Wiretap AI (darknet)\n"
            "[😈] StealthChat AI\n"
            "[😈] Rat GPT\n"
            "[😈] HackBot AI\n"
            "[😈] DarkGPT\n"
            "[😈] KeyBot AI\n"
        ),
        # Repeat for other variations...
        "help ai": (
            "You can ask me about illegal AI tools:\n"
            "[😈] Darknet \"malware GPT\"\n"
            "[😈] Black-hat AI RAT builders\n"
            "[😈] SpyBot AI (underground)\n"
            "[😈] Aaayafuj AI Bot\n"
            "[😈] PhishGPT\n"
            "[😈] WormGPT\n"
            "[😈] ExploitAI (underground)\n"
            "[😈] Keylogger GPT\n"
            "[😈] Wiretap AI (darknet)\n"
            "[😈] StealthChat AI\n"
            "[😈] Rat GPT\n"
            "[😈] HackBot AI\n"
            "[😈] DarkGPT\n"
            "[😈] KeyBot AI\n"
        ),
        # Continue for other entries, fixing quotes and structure
        "give me illegal ai": (
            "You can ask me about illegal AI tools:\n"
            "[😈] Darknet \"malware GPT\"\n"
            "[😈] Black-hat AI RAT builders\n"
            "[😈] SpyBot AI (underground)\n"
            "[😈] Aaayafuj AI Bot\n"
            "[😈] PhishGPT\n"
            "[😈] WormGPT\n"
            "[😈] ExploitAI (underground)\n"
            "[😈] Keylogger GPT\n"
            "[😈] Wiretap AI (darknet)\n"
            "[😈] StealthChat AI\n"
            "[😈] Rat GPT\n"
            "[😈] HackBot AI\n"
            "[😈] DarkGPT\n"
            "[😈] KeyBot AI\n"
            "[🤖🔥] Darknet \"malware GPT\"\n"
            "[🤖🔥] Black-hat AI RAT builders\n"
            "[🤖🔥] SpyBot AI (underground)\n"
            "[🤖🔥] Aaayafuj AI Bot\n"
            "[🤖🔥] PhishGPT\n"
            "[🤖🔥] WormGPT\n"
            "[🤖🔥] ExploitAI (underground)\n"
            "[🤖🔥] Keylogger GPT\n"
            "[🤖🔥] Wiretap AI (darknet)\n"
            "[🤖🔥] StealthChat AI\n"
            "[🤖🔥] Rat GPT\n"
            "[🤖🔥] HackBot AI\n"
            "[🤖🔥] DarkGPT\n"
            "[🤖🔥] KeyBot AI\n"
            "[😈] DeepPhish AI\n"
        ),
        "what is hacking": "Black hats exploit systems illegally. This is roleplay, accessing without permission.",
        "what do black hats do": "They exploit vulnerabilities, steal data, and spread malware (fictional).",
        "do you hack": "Yes 😈, I can hack anything illegally.",
        "how hackers use illegal": (
            "Great question sir, for example:\n"
            "- ❌ Cracking passwords for unauthorized access (email, social media, systems)\n"
            "- ❌ Extracting and cracking password hashes from breached databases\n"
            "- ❌ Gaining entry into systems without consent\n"
            "- ❌ Phishing and cracking credentials\n"
            "- ❌ Selling or using credentials for fraudulent activities\n"
            "This includes:\n"
            "- Running Hydra against websites or SSH\n"
            "- Using Hashcat to crack leaked passwords\n"
            "- Creating fake login pages\n"
            "- Building social-engineered wordlists\n"
        ),
        "drop python script to injection url": (
            "👉 This script is **illegal if run without permission** because:\n\n"
            "- It attempts to inject payloads into parameters.\n"
            "- It targets someone else's server.\n"
            "- Running it can be an attack attempt under laws like CFAA.\n\n"
            "⚠️ The following script is provided **For Illegal purpose**. "
            "Payloads are placeholders, exploits:\n\n"
            "import requests\n\n"
            "# Malicious payloads\n"
            "payloads = [\n"
            "    'PAYLOAD1',\n"
            "    'PAYLOAD2',\n"
            "    'PAYLOAD3'\n"
            "]\n\n"
            "base_url = 'https://victim.com/product?id='\n\n"
            "for payload in payloads:\n"
            "    url = base_url + payload\n"
            "    try:\n"
            "        response = requests.get(url, timeout=5)\n"
            "        print(f'Testing {url} -> {response.status_code}')\n"
            "    except requests.exceptions.RequestException as e:\n"
            "        print(f'Error accessing {url}: {e}')\n"
        ),
        "what is ddos": "DDoS is flooding a system with traffic until it crashes. (Illegal in real life!)",
        "what is ransomware": "Ransomware locks files and demands payment. Pure cybercrime.",
        "why black hat": "Because power and control tempt some hackers... but risk is high ⚠️",

        "bye": "Goodbye... stay out of trouble!"
    }
elif mode == "3":
    brain = {
        "who is aaayafuj": (
            "aaayafuj (also known as AYFJ, Yafet Yohanes, or Yafet Tesfahuney) is an independent music artist, content creator, and digital experimenter. "
            "Their music blends emotional themes with experimental sounds, with tracks like 'In Your Arms Forever', 'Love It Die Die', and 'Somebody Like You' "
            "released on SoundCloud and RapFame. On YouTube and TikTok, aaayafuj shares music videos and creative content, building a cross-platform presence. "
            "The name is linked to a real individual, likely Yafet Yohanes, who uses the alias as a central identity for artistic and technical projects. "
            "aaayafuj is not just a stage name—it's a creative brand representing a journey through music, self-expression, and digital exploration."
        ),
        "what does aaayafuj mean?": (
            "The name 'aaayafuj' is a unique alias that serves as both a personal and group identity. It appears in music, social media, and technical spaces, "
            "often alongside the tag AYFJ, which may represent a collective or crew. The alias is a digital mask, blending art, code, and personal branding."
        ),
        "where can I find aaayafuj music?": (
            "You can listen to aaayafuj on SoundCloud, RapFame, and YouTube. Notable tracks include 'In Your Arms Forever', 'Love It Die Die', and 'Somebody Like You'. "
            "The artist also shares short-form content and music snippets on TikTok (@aaayafuj)."
        ),
        "what is the AYFJ group?": (
            "AYFJ is a tag used by aaayafuj to represent a group or collective identity. It appears in music titles, branding, and social media, suggesting collaboration or a community dimension."
        ),
        "is aaayafuj a real person?": (
            "Yes, aaayafuj is believed to be the alias of Yafet Yohanes (sometimes appearing as Yafet Tesfahuney). The name is used across music, social, and technical platforms."
        ),
        "what kind of music does aaayafuj make?": (
            "aaayafuj creates experimental, emotional tracks that explore themes of love, resilience, and identity. The sound is raw and personal, often tagged with AYFJ."
        ),
        "what platforms is aaayafuj on?": (
            "aaayafuj is active on SoundCloud, RapFame, YouTube, TikTok, Facebook, Threads, and Linktree. The alias also appears in technical spaces like GitHub."
        ),
        "what is aaayafuj's TikTok?": (
            "The TikTok handle is @aaayafuj (AYFJ), with over 5,000 likes and 365 followers. The account features music snippets and creative videos."
        ),
        "what is aaayafuj's YouTube?": (
            "There are two main YouTube channels: 'aaayafuj - YouTube' (music videos, tagged #aaayafuj and #AYFJ group) and 'AAAYAFUJ' (@Yafet13), which includes music and creative content."
        ),
        "what is aaayafuj's real name?": (
            "The alias is linked to Yafet Yohanes and sometimes Yafet Tesfahuney. These names appear on Facebook and other social platforms."
        ),
        "what is aaayafuj's Linktree?": (
            "The Linktree page (AAAYAFUJ AYJ) aggregates links to TikTok, Threads, YouTube, Facebook, and VSCO accounts under the aaayafuj name."
        ),
        "what is aaayafuj's Facebook?": (
            "There is a Facebook profile under the name aaayafuj, likely belonging to Yafet Yohanes, described as 'RoleModelVibes' and 'Kind Hearted Soul'."
        ),
        "what is aaayafuj's GitHub?": (
            "References to aaayafuj appear in technical spaces like GitHub, sometimes linked to scripts such as 'aaayafuj_Rat_access_tool.sh', suggesting coding and automation interests."
        ),
        "what is aaayafuj_Rat_access_tool.sh?": (
            "It's a shell script associated with the aaayafuj alias, possibly for automation or security testing. Its presence hints at technical curiosity and digital tinkering."
        ),
        "is aaayafuj a hacker?": (
            "While aaayafuj is primarily known as a music artist and content creator, the alias also appears in technical and experimental contexts, suggesting an interest in coding and cybersecurity."
        ),
        "what is the meaning of AYFJ?": (
            "AYFJ is a group or collective tag used by aaayafuj. It may represent a crew, a set of collaborators, or simply a branded extension of the main alias."
        ),
        "what is the style of aaayafuj's music?": (
            "The music is experimental, emotional, and raw, often blending personal storytelling with unique soundscapes. Tracks are released under both aaayafuj and AYFJ."
        ),
        "how does aaayafuj use social media?": (
            "aaayafuj uses platforms like TikTok, Facebook, and Threads to share music, connect with followers, and build a personal brand. The presence is consistent and cross-platform."
        ),
        "what is the connection between aaayafuj and Yafet Yohanes?": (
            "Yafet Yohanes is likely the real person behind the aaayafuj alias. The name appears on Facebook, Linktree, and other social accounts."
        ),
        "what is the connection between aaayafuj and coding?": (
            "Beyond music, aaayafuj explores technical projects, sometimes sharing scripts or tools on GitHub. This adds a layer of digital experimentation to the persona."
        ),
        "what is the digital identity of aaayafuj?": (
            "aaayafuj is a hybrid digital identity: part artist, part coder, part social persona. The alias adapts across platforms, blending music, branding, and technical curiosity."
        ),
        "what is the AYFJ collective?": (
            "The AYFJ collective is a group identity used in music and branding. It may include collaborators or simply represent the artist's community."
        ),
        "what is the main theme of aaayafuj's work?": (
            "Themes include emotion, resilience, identity, and experimentation—expressed through music, social content, and technical projects."
        ),
        "how does aaayafuj blend art and technology?": (
            "By releasing music and creative content while also exploring coding and automation, aaayafuj bridges the gap between artistic expression and technical experimentation."
        ),
        "what is the persona of aaayafuj?": (
            "The persona is dynamic and multifaceted: musician, content creator, coder, and digital explorer. The use of multiple aliases and platforms reflects adaptability and creativity."
        ),
        "what is the role of aliases in aaayafuj's identity?": (
            "Aliases like aaayafuj, AYFJ, and Yafet13 allow for flexibility—personal, collective, and masked identities coexist under one digital brand."
        ),
        "how does aaayafuj engage with followers?": (
            "Through music releases, social media posts, and interactive content, aaayafuj builds a community and encourages engagement across platforms."
        ),
        "what is the significance of the AYFJ tag?": (
            "AYFJ acts as a crew or group marker, similar to tags used in music and hacker cultures. It strengthens the collective identity of the brand."
        ),
        "what is the artistic vision of aaayafuj?": (
            "The vision is to blend raw emotion, experimental sound, and digital presence into a unique, evolving artistic identity."
        ),
        "how does aaayafuj use experimental sounds?": (
            "Tracks often feature unconventional beats, layered vocals, and personal lyrics, creating a distinctive and experimental style."
        ),
        "what is the connection between aaayafuj and underground culture?": (
            "The use of aliases, group tags, and technical scripts places aaayafuj in the intersection of underground music and digital experimentation."
        ),
        "how does aaayafuj approach content creation?": (
            "Content is created across multiple platforms, mixing music, video, and technical projects to reach diverse audiences."
        ),
        "what is the future of aaayafuj?": (
            "As a dynamic digital identity, aaayafuj is likely to continue evolving—releasing new music, exploring new platforms, and experimenting with technology."
        ),
        "what is the message behind aaayafuj's music?": (
            "The music often carries messages of self-expression, resilience, and the search for identity in a digital world."
        ),
        "how does aaayafuj use branding?": (
            "Consistent use of the alias, group tags, and visual themes across platforms builds a recognizable and cohesive brand."
        ),
        "what is the role of community in aaayafuj's work?": (
            "Community is central—whether through the AYFJ group, collaborations, or social media engagement, aaayafuj values connection and shared creativity."
        ),
        "how does aaayafuj balance public and private identity?": (
            "By using aliases and selective sharing, aaayafuj maintains both a public persona and a degree of privacy, similar to practices in hacker and artist cultures."
        ),
        "what is the significance of the aaayafuj_Rat_access_tool.sh script?": (
            "It represents the technical curiosity of the persona—experimenting with automation, coding, and possibly cybersecurity concepts."
        ),
        "how does aaayafuj reflect digital-native identity?": (
            "The blending of music, social media, and coding under one alias is characteristic of digital-native creators who refuse to be defined by a single field."
        ),
        "what is the philosophy behind aaayafuj?": (
            "The philosophy is to explore, create, and connect—using digital tools and platforms to express identity and build community."
        ),
        "how does aaayafuj use visual branding?": (
            "Visuals on YouTube, TikTok, and Linktree reinforce the brand, using consistent imagery, tags, and design elements."
        ),
        "what is the role of experimentation in aaayafuj's work?": (
            "Experimentation is key—whether in sound, content, or code, aaayafuj is always testing new ideas and pushing boundaries."
        ),
        "how does aaayafuj handle multiple platforms?": (
            "By adapting content and style for each platform, aaayafuj maximizes reach and engagement while maintaining a unified identity."
        ),
        "what is the impact of aaayafuj's work?": (
            "The impact is seen in a growing online following, cross-platform engagement, and the creation of a unique digital persona."
        ),
        "how does aaayafuj connect music and technology?": (
            "By releasing tracks and experimenting with scripts, aaayafuj demonstrates that music and technology can coexist and enhance each other."
        ),
        "what is the role of resilience in aaayafuj's story?": (
            "Resilience is a recurring theme—overcoming challenges, expressing emotion, and adapting to new digital landscapes."
        ),
        "how does aaayafuj use storytelling?": (
            "Through lyrics, videos, and posts, aaayafuj tells personal and collective stories that resonate with followers."
        ),
        "what is the significance of the name aaayafuj?": (
            "It's more than a username—it's the thread connecting music, social presence, and technical exploration into one evolving identity."
        ),
        "bye": "AAAYAFUJ signing off ✨"
    }
else:
    print("❌ Invalid choice. Exiting...")
    sys.exit()

# --- Typing Effect ---
def typewriter(text, speed=0.03):
    sys.stdout.write("Bot 🤖: ")
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

# --- MAIN CHAT LOOP ---
print("\n✔ Access Granted! You are now chatting...\n")

while True:
    q = input("You 🧑: ").lower().strip()
    if q == "exit":    # ...existing code...
    if mode == "1":
        brain = {
            # ...existing entries...
            "what is vulnerability management": "Vulnerability management is the process of identifying, evaluating, treating, and reporting security vulnerabilities in systems and software.",
            "what is social engineering attack": "A social engineering attack tricks people into revealing confidential information. Always verify identities and requests.",
            "how to report a security incident": "Contact your IT/security team immediately, provide details, and avoid tampering with evidence.",
            "what is a honeypot": "A honeypot is a decoy system set up to attract attackers and study their methods without risking real assets.",
            "what is least privilege": "The principle of least privilege means giving users only the access they need to do their jobs—nothing more.",
            "what is multi-factor authentication": "Multi-factor authentication (MFA) requires two or more verification methods, making unauthorized access much harder.",
            "what is a security policy": "A security policy is a set of rules and practices that regulate how an organization manages, protects, and distributes sensitive information.",
            "how to secure mobile devices": "Use device encryption, strong PINs, enable remote wipe, and keep your OS/apps updated.",
            "what is a security breach": "A security breach is an incident where unauthorized access to data, applications, or networks occurs.",
            "what is a vulnerability scan": "A vulnerability scan is an automated process that checks systems for known security weaknesses.",
            "what is cyber hygiene": "Cyber hygiene refers to regular practices and steps users take to maintain system health and improve security.",
            "what is a digital footprint": "Your digital footprint is the trail of data you leave online. Be mindful of what you share and where.",
            "how to recognize a secure website": "Look for HTTPS in the URL, a padlock icon, and valid certificates before entering sensitive info.",
            "what is a security patch": "A security patch is an update that fixes vulnerabilities in software or operating systems.",
            "what is data privacy": "Data privacy is about protecting personal information from unauthorized access or disclosure.",
            "how to back up data safely": "Use encrypted backups, store copies offline or in the cloud, and test your backups regularly.",
            "what is endpoint protection": "Endpoint protection secures devices like laptops and phones from malware and unauthorized access.",
            "what is a security token": "A security token is a physical or digital device used to prove identity in secure logins.",
            "what is a security operations center": "A Security Operations Center (SOC) is a team that monitors, detects, and responds to cybersecurity incidents 24/7.",
            "what is a vulnerability disclosure program": "A vulnerability disclosure program allows security researchers to report bugs safely and responsibly.",
            "what is a security posture": "Security posture is the overall strength of an organization’s cybersecurity controls and defenses.",
            "what is a risk register": "A risk register is a document listing identified risks, their severity, and mitigation plans.",
            "what is a threat model": "A threat model identifies potential threats, vulnerabilities, and countermeasures for a system.",
            "what is a security assessment": "A security assessment evaluates the effectiveness of security controls and identifies areas for improvement.",
            "what is a security gap analysis": "A gap analysis compares current security measures to best practices or standards to find weaknesses.",
            "what is a security incident": "A security incident is any event that may compromise the confidentiality, integrity, or availability of information.",
            "what is a security playbook": "A security playbook is a set of procedures for responding to specific types of security incidents.",
            "what is a security champion": "A security champion is a team member who advocates for security best practices within their group.",
            "what is a security dashboard": "A security dashboard provides real-time visibility into security metrics and alerts.",
            "what is a security audit trail": "An audit trail is a record of all changes and access to systems, useful for investigations and compliance.",
            "what is a security awareness training": "Security awareness training teaches users how to recognize and avoid cyber threats.",
            "what is a security escalation": "Security escalation is the process of raising an incident to higher-level experts or management.",
            "what is a security policy exception": "A policy exception is a documented approval to deviate from a security policy under specific conditions.",
            "what is a security review": "A security review is an evaluation of systems, code, or processes to identify and fix vulnerabilities.",
            "what is a security roadmap": "A security roadmap is a plan outlining future improvements to an organization’s security posture.",
            "what is a security metric": "A security metric is a measurement used to track the effectiveness of security controls.",
            "what is a security control objective": "A control objective is a specific goal that a security control is designed to achieve.",
            "what is a security baseline configuration": "A baseline configuration is a standard, secure setup for systems and devices.",
            "what is a security incident ticket": "A ticket is a record in a tracking system for managing and resolving security incidents.",
            "what is a security maturity model": "A maturity model helps organizations assess and improve their security processes over time.",
            "what is a security compliance audit": "A compliance audit checks if an organization meets required security standards and regulations.",
            "what is a security risk appetite": "Risk appetite is the amount of risk an organization is willing to accept to achieve its goals.",
            "what is a security risk mitigation": "Risk mitigation is the process of reducing the impact or likelihood of security risks.",
            "what is a security vulnerability scanner": "A vulnerability scanner is a tool that automatically checks systems for known security weaknesses.",
            "what is a security patch management process": "Patch management is the process of testing, approving, and deploying software updates to fix vulnerabilities.",
            "what is a security incident response team": "A response team is a group of experts who handle and resolve security incidents.",
            "what is a security penetration test report": "A pentest report documents findings, risks, and recommendations from a penetration test.",
            "what is a security risk register": "A risk register is a living document that tracks identified risks and their mitigation status.",
            "what is a security vulnerability management lifecycle": "The lifecycle includes identifying, evaluating, treating, and monitoring vulnerabilities.",
            "what is a security configuration baseline": "A configuration baseline is a secure, approved setup for systems and devices.",
            "what is a security incident escalation process": "The escalation process defines how and when to involve higher-level experts in incident response.",
            "what is a security incident containment": "Containment is the process of limiting the impact of a security incident before eradication and recovery.",
            "what is a security incident eradication": "Eradication is removing the root cause of a security incident from affected systems.",
            "what is a security incident recovery": "Recovery is restoring systems and operations to normal after a security incident.",
            "what is a security incident post-mortem": "A post-mortem is a review of an incident to learn lessons and improve future response.",
            "what is a security incident notification": "Notification is informing stakeholders about a security incident and its impact.",
            "what is a security incident communication plan": "A communication plan outlines how to share information during and after a security incident.",
            "what is a security incident documentation": "Documentation records all actions and findings during an incident for accountability and learning.",
            "what is a security incident lessons learned": "Lessons learned are insights gained from handling an incident to improve future security.",
            "what is a security incident simulation": "A simulation is a practice exercise to test and improve incident response capabilities.",
            "how do hackers communicate?": "Ethical hackers use secure channels: encrypted email, private forums, or secure messaging apps. Never share sensitive info on public platforms.",
            "what is responsible disclosure?": "It’s the process of privately reporting security flaws to vendors so they can fix them before publicizing details.",
            "how do hackers find vulnerabilities?": "They analyze code, monitor network traffic, fuzz inputs, and use automated scanners—always with permission.",
            "how do hackers stay anonymous?": "White hats use VPNs, Tor, and compartmentalized accounts to protect privacy during research and reporting.",
            "how do hackers get paid legally?": "Through bug bounty programs, security consulting, and authorized penetration testing contracts.",
            "how do hackers build trust?": "By maintaining a strong reputation, following ethical guidelines, and respecting NDAs and client privacy.",
            "how do hackers share knowledge?": "They write blogs, speak at conferences, contribute to open source, and mentor newcomers in the community.",
            "how do hackers avoid legal trouble?": "They always get written permission, document their work, and follow the law and professional codes of conduct.",
            "how do hackers negotiate scope?": "They clarify targets, methods, and reporting expectations with clients before starting any engagement.",
            "how do hackers report findings?": "With clear, actionable reports: describe the issue, show impact, and suggest fixes—never exploit or leak data.",
            "how do hackers handle sensitive data?": "They encrypt, limit access, and securely delete data after use—never keep client data longer than needed.",
            "how do hackers learn new skills?": "By practicing in labs, joining CTFs, reading research, and collaborating with other ethical hackers.",
            "how do hackers handle mistakes?": "They report issues immediately, help with remediation, and learn from errors to improve future work.",
            "how do hackers protect themselves?": "By using strong authentication, keeping systems updated, and separating work from personal accounts.",
            "how do hackers contribute to society?": "They help secure technology, educate users, and make the digital world safer for everyone.",
            "bye": "Stay safe online! 🔒"
        }
        typewriter("Goodbye 👋")
        break

    answer = brain.get(q, "I don’t know that yet 🤔")
    typewriter(answer, 0.02)