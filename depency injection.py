# Service 1: EmailService
#Hier definieren wir den Service, der E-Mails versendet was er macht etc.
class EmailService:
    def send_email(self, to, subject, body):
        print(f"Sending email to {to}: [{subject}] {body}")

# Service 2: LoggerService
#Hier definieren wir den Service, der Protokolle erstellt was er macht etc.
class LoggerService:
    def log(self, message):
        print(f"[LOG] {message}")

# Dependent class: NotificationManager
# Hier definieren wir die Klasse, die von den Services abhängt und sie verwendet.
# Das hilft uns, die Abhängigkeiten zu entkoppeln und die Klasse flexibler zu gestalten.

class NotificationManager:
    def __init__(self, email_service: EmailService, logger_service: LoggerService): #Hier definieren wir den Konstruktor der Klasse NotificationManager.
        self.email_service = email_service # Hier machen wir die Parameter zu Properties der Klasse NotificationManager.
        self.logger_service = logger_service

    def notify(self, user_email, message):
        self.logger_service.log(f"Notifying {user_email}") #Hier nutzen wir den LoggerService, um eine Nachricht zu protokollieren.
        self.email_service.send_email( #Hier nutzen wir den EmailService, um eine E-Mail zu senden.
            to=user_email,
            subject="Notification",
            body=message
        )
        self.logger_service.log(f"Notification sent to {user_email}") #Hier protokollieren wir, dass die Benachrichtigung gesendet wurde.

# Instantiate services
email_service = EmailService() #Again hier müssen erst die Instanzen der Services erstellt werden, bevor sie verwendet werden können.
logger_service = LoggerService()

# Inject them into NotificationManager
notifier = NotificationManager(email_service, logger_service) #Hier erstellen wir eine Instanz der Klasse NotificationManager und injizieren die Services.

# Use the NotificationManager
notifier.notify("user@example.com", "Your order has been shipped!") # Hier verwenden wir alles zusammen
