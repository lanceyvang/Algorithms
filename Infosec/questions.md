# Active Directory
* Directory-based identity-related services.
* Domain controller, server running Active Directory Domain Service
* Authenticates and authorizes all users and computers in a Windows domain type network.
    * Assigning and enforcing security policies for all computers and installing or updating software. 
        * When a user logs into a computer that is part of a Windows domain, Active Directory checks the submitted password and determines whether the user is a system administrator or normal user.
* Management and storage of information
* Built on LDAP (Lightweight Directory Access Protocol) 2 and 3.
    * Microsoft's version of Kerberos and DNS.
    * LDAP is an open, vendor neutral industry standard application protocol built for accessing and maintaining distributed directory information services over an IP network. 

# Kerberos
* Default authentication and authorization used by Active Directory.
* Invented at MIT and adopted by Microsoft in Windows 2000 Active Directory.
* Provide single sign-on access.
* Computer-Network authentication protocol
* Uses tickets to allow nodes to communicate over a non-secure network to prove their identity in a secure manner.
    * Client-Server model
    * Mutual authentication
* Protects against eavesdropping and replay attacks.
* Symmetric key cryptography
* UDP port 88


