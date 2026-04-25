import sys
import os
import pytest
sys.path.insert(0, os.path.dirname(__file__))

from datetime import datetime

@pytest.hookimpl(tryfirst=True, hookwrapper=True) #permet de faire la liaison aves le driver
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

# s'il y a une erreur, on fait des captures d'écran.
    if report.when == "call" and report.failed: # ne prend pas en compte les before et les after
        driver = getattr(item.instance, "driver", None)
        if driver:
            screenshots_dir = os.path.join(os.path.dirname(__file__), "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)
            date_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_path = os.path.join(screenshots_dir, f"{item.name}_{date_str}_.png")
            driver.save_screenshot(screenshot_path)

    # ajouter se déplacer jusqu'à (scroll into) on prend pas toute la page ici