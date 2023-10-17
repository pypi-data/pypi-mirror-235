from typing import List, Union
from pydantic import  Field, validator, root_validator
import json

from .timeframes import Timeframes,Timeframe
from .markets import Market, Markets
from .customBaseModel import CustomBaseModel

class Interrupted_On_Time(CustomBaseModel):
    name: str = Field(default="Interrupted_On_Time",init = False)
    minimum_hours_on: int = Field(default=1,init = False)
    pass

class Continuous_On_Time(CustomBaseModel):
    name: str = Field(default="Continuous_On_Time",init = False)
    week: int = Field(default=None)
    best_hour: int = Field(default=None)

class Price_Logic(CustomBaseModel):
    nr_of_hours_on: int
    market: Market | str
    timeframes: Timeframes = Timeframes()
    pricefinding: Continuous_On_Time | Interrupted_On_Time = Interrupted_On_Time()
    resolution: float = Field(default=1)
    timeframe_shorter_than_nr_of_hours_on: bool = Field(default=False)
    
    def update_pricefinding(self, pricefinding: Union[Continuous_On_Time, Interrupted_On_Time]):
            self.pricefinding = pricefinding

    def to_json(self) -> str:
        switch_pattern_dict = self.to_dict()
        json_str = json.dumps(switch_pattern_dict)

        return json_str

    @root_validator(pre=True)
    def set_market_to_market_object(cls, values):
        if isinstance(values["market"], str):
            result = Markets.get_market_by_name(values["market"])
            result = Markets.get_market_by_code(values["market"])
            if result is None:
                raise ValueError("Market is not valid")
            values["market"] = result
        return values

    @validator('nr_of_hours_on')
    def validate_nr_of_hours_on(cls, v):
        if v <= 0:
            raise ValueError('nr_of_hours_on must be greater than 0')
        return v

    @root_validator
    def validate_timeframes(cls, values):
        timeframes = values.get('timeframes')
        nr_of_hours_on = values.get('nr_of_hours_on')
        if timeframes and nr_of_hours_on:
            possible_hours = timeframes.possible_hours
            if nr_of_hours_on > len(possible_hours):
                values['timeframe_shorter_than_nr_of_hours_on'] = True
            else:
                values['timeframe_shorter_than_nr_of_hours_on'] = False
        return values