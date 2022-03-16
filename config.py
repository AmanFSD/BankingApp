from pickle import FALSE, TRUE
import sqlalchemy


class ConfigDebug():
  SECRET_KEY = 'nowichange#!1212'
  #  SQLALCHEMY_DATABASE_URI = ''
  # SQLALCHEMY_DATABASE_URI = ''    # File-based SQL database

  SQLALCHEMY_DATABASE_URI = ''
   
  SQLALCHEMY_TRACK_MODIFICATION=False


  # Flask-Mail SMTP server settings
  MAIL_SERVER = 'smtp.gmail.com'
  MAIL_PORT =587
  MAIL_USE_SSL = False
  MAIL_USE_TLS = False
  MAIL_USERNAME = ''     
  MAIL_PASSWORD = ''
  MAIL_DEFAULT_SENDER = '"MyApp"abc@gmail.com>'

  # Flask-User settingsa
  USER_APP_NAME = "Flask-User Basic App"      # Shown in and email templates and page footers
  USER_ENABLE_EMAIL = True        # Enable email aution
  USER_ENABLE_USERNAME = False    # Disable username authentication
  USER_EMAIL_SENDER_NAME = USER_APP_NAME
  USER_EMAIL_SENDER_EMAIL = "noreply@example.com"  
