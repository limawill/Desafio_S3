# backend/core/logging.py
import os
import logging
from logging.handlers import RotatingFileHandler

# Flag para garantir configuração única
_is_setup = False


def setup_logging():
    """
    Configura o sistema de log da aplicação.
    Logs serão escritos em 'logs/app_log.log' e também exibidos no console.
    Executa apenas uma vez, usando uma flag global.
    """
    global _is_setup
    if _is_setup:
        return

    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_file_path = os.path.join(
        log_dir, "challenge_api.log"
    )  # Alterei para um nome mais relevante

    # Obter o logger raiz
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    # Limpa handlers existentes para evitar duplicação
    if root_logger.handlers:
        for handler in root_logger.handlers[:]:
            root_logger.removeHandler(handler)

    # Formato das mensagens de log
    class CustomFormatter(logging.Formatter):
        def format(self, record):
            # Extrair extra como string, se existir
            extra_str = ""
            if hasattr(record, "extra") and record.extra:
                extra_str = " - " + " ".join(
                    f"{k}={v}" for k, v in record.extra.items()
                )
            # Construir a mensagem completa
            msg = record.getMessage() + extra_str
            return f"{self.formatTime(record, self.datefmt)} - {record.levelname} -> {record.name} - {record.filename} -> {msg}"

    formatter = CustomFormatter(datefmt="%Y-%m-%d %H:%M")

    # Handler para o arquivo de log com rotação
    file_handler = RotatingFileHandler(
        log_file_path,
        maxBytes=5 * 1024 * 1024,  # 5 MB por arquivo
        backupCount=5,  # Mantém 5 arquivos de backup
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)
    root_logger.addHandler(file_handler)

    # Handler para o console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)
    root_logger.addHandler(console_handler)

    # Log de confirmação da configuração (apenas uma vez)
    logging.getLogger(__name__).info("Sistema de log configurado.")
    _is_setup = True


# Logger global acessível diretamente
logger = logging.getLogger(__name__)


# Função para obter o logger (opcional, mas mantém compatibilidade)
def get_logger():
    setup_logging()  # Garante que o setup seja feito se necessário
    return logger


# Chamar setup_logging() uma vez ao importar o módulo
setup_logging()
