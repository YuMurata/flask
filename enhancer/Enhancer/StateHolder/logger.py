from Enhancer.logger import Logger
from pathlib import Path

package_name = Path(__file__).parent.name
logger = Logger(package_name, log_file_path=f'logs/{package_name}.log')
