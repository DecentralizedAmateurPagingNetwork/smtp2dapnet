# smtp2dapnet
SMPT Interface via REST API to DAPNET
This little python script implements an SMTP server, which listens on the desired port for emails to send them out via the REST API of DAPNET to the user.
It's just a first try, but it works. Implementation into Thunderbird was not successful yet.

# Usage
Send an SMPT Message with the following data
- From DAPNET_LOGIN@DAPNET_PASSWORD.hampager.de  (Example: dc1abc@verysecretpassword.hampager.de)
- To RECIPIENT_CALLSIGN@TRANSMITTERGROUP.hampager.de (Example: df8xyz@all.hampager.de)
- Subject YOUR_TEXT
