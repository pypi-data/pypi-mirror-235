import pytest
import time
import os

class TestPackageRun:
    def test_config(self, gateway):
       with gateway as g:
           time.sleep(5)
       time.sleep(1)
