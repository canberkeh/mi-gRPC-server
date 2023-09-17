from domain.yeelight_bulb_constant import PowerTypes


class YeelightBulbDTO:
    def __init__(self, power: str, bright: str) -> None:
        if power == PowerTypes.On.value:
            self._power = PowerTypes.On
        else:
            self._power = PowerTypes.Off
        self._bright = bright

    @property
    def power(self) -> str:
        return PowerTypes(self._power).name

    @power.setter
    def power(self, value: str) -> None:
        self._power = value

    @property
    def bright(self) -> str:
        if self.power == PowerTypes.Off.value:
            return "0"
        return self._bright 

    @bright.setter
    def bright(self, value: str) -> None:
        self._bright = value
