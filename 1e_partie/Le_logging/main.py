import logging
import requests

# logging.basicConfig(level=logging.ERROR,
                    # format='%(asctime)s : %(levelname)s : %(message)s')
logging.basicConfig(level=logging.DEBUG)

logging.debug("La fonction a bien été exécutée")
logging.info("Message d'information général")
logging.warning("Attention !")
logging.error("Une erreur est arrivée")
logging.critical("Erreur critique")
