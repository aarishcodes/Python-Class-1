import logging

logging.basicConfig(
    filename="employee_app_logs.log",
    level = logging.INFO,
    format="%(asctime)s [%(levename)s %(message)s]"
)