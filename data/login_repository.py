import os
from dotenv import load_dotenv

load_dotenv()

class LoginRepository:
    USERNAME = os.getenv("ORBI_USERNAME")
    INVALID_USERNAME = os.getenv("ORBI_INVALID_USSERNAME")
    PASSWORD = os.getenv("ORBI_PASSWORD")
    USERNAME_FIELD = "txtNombreUsuario"
    PASSWORD_FIELD = "txtContrasena"
    LOGIN_BTN = "btnSesion"
