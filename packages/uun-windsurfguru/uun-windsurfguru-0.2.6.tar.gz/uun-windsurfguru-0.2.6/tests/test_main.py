import pytest
from uun_iot_libledstrip.devices import DebugLedDev

class TestDataProcessing:
    @pytest.fixture(scope="class")
    def config_object(self):
        return {
            "gateway": {
                "moduleTimers": {
                    "windSurfGuru": 120
                },
                "windSurfGuru": {
                    "weatherStationCode": "MELTEMI",
                    "ledStrip": {
                        "device": "virtual",
                        "pixels": 16,
                    },
                    "state": {
                        "noConnection": {
                            "color": "#ff0000",
                            "action": "blink",
                            "interval": 0.2
                        },
                        "blank": {
                            "color": "#000000",
                            "action": "solid",
                            "interval": None
                        },
                        "error": {
                            "color": "#ff0000",
                            "action": "blink",
                            "interval": 0.2
                        }
                    },
                    "severity": {
                        "low": {
                            "color": "#0000ff",
                            "action": "solid",
                            "interval": None,
                            "specialAction": {
                                "condition": "ifWindBetween",
                                "color": "#0000ff",
                                "action": "blink",
                                "interval": 0.2
                            },
                            "settings": {
                                "windMin": 0,
                                "windMax": 14,
                                "ledMinPosition": 0,
                                "ledMaxPosition": 0
                            }
                        },
                        "light": {
                            "color": "#0000ff",
                            "action": "solid",
                            "interval": None,
                            "settings": {
                                "windMin": 16,
                                "windMax": 18,
                                "ledMinPosition": 1,
                                "ledMaxPosition": 3
                            }
                        },
                        "optimal": {
                            "color": "#00ff00",
                            "action": "solid",
                            "interval": None,
                            "settings": {
                                "windMin": 19,
                                "windMax": 22,
                                "ledMinPosition": 4,
                                "ledMaxPosition": 7
                            }
                        },
                        "heavy": {
                            "color": "#ff8000",
                            "action": "solid",
                            "interval": None,
                            "settings": {
                                "windMin": 23,
                                "windMax": 26,
                                "ledMinPosition": 8,
                                "ledMaxPosition": 11
                            }
                        },
                        "extreme": {
                            "color": "#ff0000",
                            "action": "solid",
                            "interval": None,
                            "specialAction": {
                                "condition": "ifWindGreater",
                                "color": "#ff0000",
                                "action": "blink",
                                "interval": 0.2
                            },
                            "settings": {
                                "windMin": 27,
                                "windMax": 30,
                                "ledMinPosition": 12,
                                "ledMaxPosition": 15
                            }
                        }
                    }
                }
            }
        }

# initialize LedDev first
#    @pytest.fixture(scope="function")
#    def device(self):
#        """ Create new for every test. """
#        return DebugLedDev(16)
#
#    @pytest.fixture(scope="function")
#    def init_modules(self, config_object, device):
#        from uun_windsurfguru.modules.WindSurfGuru import WindSurfGuru
#        def uucmd(x):
#            return []
#
#        return WindSurfGuru(config_object["gateway"], uucmd, device=device)

# rely on _init_hw to initialize LedDev from configuration
    @pytest.fixture(scope="function")
    def device(self, init_modules):
        wsg = init_modules
        return wsg._device
 
    @pytest.fixture(scope="function")
    def init_modules(self, config_object):
        from uun_windsurfguru.modules.WindSurfGuru import WindSurfGuru
        def uucmd(x):
            return []
 
        return WindSurfGuru(config_object["gateway"], uucmd)

    def test_max_speed(self, init_modules, device):
        wsg = init_modules

        speed_kph = 30 / 0.5399568035
        wsg.evaluate_conditions(speed_kph)
        assert device[-1] == (255,0,0)

    def test_medium_speed(self, init_modules, device):
        wsg = init_modules

        speed_kph = 20 / 0.5399568035
        wsg.evaluate_conditions(speed_kph)
        assert device[-1] == (0,0,0)


