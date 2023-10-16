import pytest
import datetime
from uun_iot_libledstrip.devices import DebugLedDev
from uun_iot_libledstrip import hex2rgb, rgb2hex

# test data in format:
# datetime now
# server reply,
# ( (pixel_id, expected_hex_color), ...)
test_data = [
    # completed without delay
    (
        datetime.datetime.strptime("2022-02-11T17:05:21.415652Z", "%Y-%m-%dT%H:%M:%S.%fZ"),
        {
            #"state": "progress (completed, completedWithWarning, completedWithError, ...)",
            #"delayWarning": "seconds or default",
            #"delayError": "seconds or default",
            #"estimatedNextProgressTs": "%Y-%m-%dT%H:%M:%S.%fZ"
            "state": "completed",
            "delayWarning": 2,
            "delayError": 5,
            "estimatedNextProgressTs": "2022-02-11T17:05:20.415652Z"
        },
        (
            #          progress                        delay                         connection
            (0, "#ffffff"), (1, "#ffffff"), (3, "#00ff00"), (4, "#00ff00"), (6, "#00ff00"), (7, "#00ff00") 
        )
    ),
    # completed without delay, now before nextTs
    (
        datetime.datetime.strptime("2022-02-11T17:05:19.415652Z", "%Y-%m-%dT%H:%M:%S.%fZ"),
        {
            "state": "completed",
            "delayWarning": 2,
            "delayError": 5,
            "estimatedNextProgressTs": "2022-02-11T17:05:20.415652Z"
        },
        (
            (0, "#ffffff"), (1, "#ffffff"), (3, "#00ff00"), (4, "#00ff00"), (6, "#00ff00"), (7, "#00ff00") 
        )
    ),
    # completed 15 s ago (should display completed without delay)
    (
        datetime.datetime.strptime("2022-02-11T17:05:35.415652Z", "%Y-%m-%dT%H:%M:%S.%fZ"),
        {
            "state": "completed",
            "delayWarning": 2,
            "delayError": 5,
            "estimatedNextProgressTs": "2022-02-11T17:05:20.415652Z"
        },
        (
            (0, "#ffffff"), (1, "#ffffff"), (3, "#00ff00"), (4, "#00ff00"), (6, "#00ff00"), (7, "#00ff00") 
        )
    ),
    # default delays, completed 15s ago
    (
        datetime.datetime.strptime("2022-02-11T17:05:35.015652Z", "%Y-%m-%dT%H:%M:%S.%fZ"),
        {
            "state": "completed",
            # default delays from configuration
            # "delayWarning": 3,
            # "delayError": 10,
            "estimatedNextProgressTs": "2022-02-11T17:05:20.415652Z"
        },
        (
            (0, "#ffffff"), (1, "#ffffff"), (3, "#00ff00"), (4, "#00ff00"), (6, "#00ff00"), (7, "#00ff00") 
        )
    ),
    # default delays, running without delay
    (
        datetime.datetime.strptime("2022-02-11T17:05:22.015652Z", "%Y-%m-%dT%H:%M:%S.%fZ"),
        {
            "state": "running",
            "estimatedNextProgressTs": "2022-02-11T17:05:20.415652Z"
        },
        (
            (0, "#00ff00"), (1, "#00ff00"), (3, "#00ff00"), (4, "#00ff00"), (6, "#00ff00"), (7, "#00ff00") 
        )
    ),
    # default delays, running with delay warning
    (
        datetime.datetime.strptime("2022-02-11T17:05:25.015652Z", "%Y-%m-%dT%H:%M:%S.%fZ"),
        {
            "state": "running",
            "estimatedNextProgressTs": "2022-02-11T17:05:20.415652Z"
        },
        (
            (0, "#000000"), (1, "#000000"), (3, "#ff8700"), (4, "#ff8700"), (6, "#00ff00"), (7, "#00ff00") 
        )
    ),
    # default delay, running with error delay
    (
        datetime.datetime.strptime("2022-02-11T17:05:33.415652Z", "%Y-%m-%dT%H:%M:%S.%fZ"),
        {
            "state": "running",
            "estimatedNextProgressTs": "2022-02-11T17:05:20.415652Z"
        },
        (
            (0, "#000000"), (1, "#000000"), (3, "#ff0000"), (4, "#ff0000"), (6, "#00ff00"), (7, "#00ff00") 
        )
    ),
    # completed with warning
    (
        datetime.datetime.strptime("2022-02-11T17:05:21.415652Z", "%Y-%m-%dT%H:%M:%S.%fZ"),
        {
            "state": "completedWithWarning",
            "estimatedNextProgressTs": "2022-02-11T17:05:20.415652Z"
        },
        (
            (0, "#ff8700"), (1, "#ff8700"), (3, "#00ff00"), (4, "#00ff00"), (6, "#00ff00"), (7, "#00ff00") 
        )
    ),
]

test_data_error = [
    # unknown progress state,
    # WARNING: this test might be bugged because it causes the strip to blink, which is not easily tested for
    (
        datetime.datetime.strptime("2022-02-11T17:05:21.415652Z", "%Y-%m-%dT%H:%M:%S.%fZ"),
        {
            "state": "asdaskdhajsd",
            "estimatedNextProgressTs": "2022-02-11T17:05:20.415652Z"
        },
        (
            (0, "#ff0000"), (1, "#ff0000"), (2, "#ff0000"), (3, "#ff0000"), (4, "#ff0000"), (5, "#ff0000"), (6, "#ff0000"), (7, "#ff0000") 
        )
    ),
]

class TestDataProcessing:
    @pytest.fixture(scope="class")
    def config_object(self):
        return {
            "gateway": {
                "guardMan": {
                    "ledStrip": {
                        "virtualMode": False,
                        "pixels": 8,
                        "pin": "D10"
                    },
                    "progressCode": "uuConsoleProgressExample003_6x11x1",
                    "special": {
                        "error": {
                            "color": "#ff0000",  
                            "action": "blink",
                            "interval": 0.1
                        }
                    },
                    "progress": {
                        "ledMinPosition": 0,
                        "ledMaxPosition": 1,
                        "waiting": {
                            "color": "#0000ff",
                            "action": "solid",
                            "interval": None
                        },
                        "started": {
                            "color": "#00ff00",
                            "action": "solid",
                            "interval": None
                        },
                        "running": {
                            "color": "#00ff00",
                            "action": "blink",
                            "interval": 0.2
                        },
                        "runningWithWarning": {
                            "color": "#ff8700",
                            "action": "blink",
                            "interval": 0.2
                        },
                        "runningWithError": {
                            "color": "#ff0000",
                            "action": "blink",
                            "interval": 0.2
                        },
                        "completed": {
                            "color": "#ffffff",
                            "action": "solid",
                            "interval": None
                        },
                        "completedWithWarning": {
                            "color": "#ff8700",
                            "action": "solid",
                            "interval": None
                        },
                        "completedWithError": {
                            "color": "#ff0000",
                            "action": "solid",
                            "interval": None
                        },
                        "error": {
                            "color": "#ff0000",  
                            "action": "solid",
                            "interval": None
                        },
                        "warning": {
                            "color": "#ff8700",
                            "action": "solid",
                            "interval": None
                        }
                    },
                    "delay": {
                        "ledMinPosition": 3,
                        "ledMaxPosition": 4,
                        "noDelay": {
                            "color": "#00ff00",
                            "action": "solid",
                            "interval": None
                        },
                        "delayedWithWarning": {
                            "color": "#ff8700",
                            "action": "solid",
                            "interval": None
                        },
                        "delayedWithError": {
                            "color": "#ff0000",
                            "action": "solid",
                            "interval": None
                        }
                    }, 
                    "defaultDelays": {
                        "warning": 3,
                        "error": 10
                    },
                    "connection": {
                        "ledMinPosition": 6,
                        "ledMaxPosition": 7,
                        "connected": {
                            "color": "#00ff00",
                            "action": "solid",
                            "interval": None
                        },
                        "noConnection": {
                            "color": "#ff0000",
                            "action": "solid",
                            "interval": None
                        }
                    }
                }
            }

        }

    @pytest.fixture(scope="function")
    def device(self):
        """ Create new for every test. """
        return DebugLedDev(8)

    @pytest.fixture(scope="function")
    def init_modules(self, config_object, device):
        from uun_guardman.modules import GuardMan
        def uucmd(x):
            return []

        return GuardMan(config_object["gateway"], uucmd, device=device)

    @pytest.mark.parametrize("now,server_data,expected_coloring", test_data)
    def test_solid_coloring(self, init_modules, device, now, server_data, expected_coloring):
        guardman = init_modules
        guardman.evaluate_data(server_data, now)

        invalid_pixels = []
        for pixel_id, color in expected_coloring:
            actual_color = device[pixel_id]
            if actual_color != hex2rgb(color):
                invalid_pixels.append((pixel_id, rgb2hex(actual_color)))
        assert invalid_pixels == []

    @pytest.mark.parametrize("now,server_data,expected_coloring", test_data_error)
    def test_error(self, init_modules, device, now, server_data, expected_coloring):
        with pytest.raises(ValueError):
            self.test_solid_coloring(init_modules, device, now, server_data, expected_coloring)
