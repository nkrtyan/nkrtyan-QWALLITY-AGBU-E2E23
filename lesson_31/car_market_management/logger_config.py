import logging

def setup_logger():
    logging.basicConfig(
        filename="lesson_31/car_market_management/car_market.log",
        filemode="w",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        force=True
    )

    return logging.getLogger("CarMarket")


logger = setup_logger()
