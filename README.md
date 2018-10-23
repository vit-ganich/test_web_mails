## web_mails_tests
Some automated tests for sending emails via different web-mails (Yahoo, Gmail, etc.)

### Tests scheme:
1. Run the *Firefox* browser
2. Go to webmail page
3. Enter user credentials
4. Go to *Compose email*
5. Enter *adress to*, *email subject* and *email body*
6. Send email
7. Repeat steps 4 - 6 three times.
8. Repeat steps 1 - 7 for different web-mails (Y*andex, Mail.ru, Gmail, Rambler, Yahoo, Outlook.com, Outlook OWA*).

Unfortunately, these tests don't use any test framework (Pytest, Splinter, etc.). It was my first step it test automation, so do not judge strictly.
