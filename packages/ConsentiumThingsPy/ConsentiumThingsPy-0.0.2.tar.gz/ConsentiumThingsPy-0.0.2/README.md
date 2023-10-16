# ConsentiumThingsPy

Developed by Debjyoti Chowdhury from ConsentiumInc

## Examples of How To Use

```python
from ConsentiumThingsPy import ConsentiumThings
import time

send_key = "YOUR_API_KEY"
board_key = "YOUR_BOARD_KEY"

try:
    consentium = ConsentiumThings(send_key, board_key)
except ValueError as e:
    print(e)
else:
    for i in range(4):
        data_buff = [1.0, 2.0, 3.0]
        info_buff = ["Sensor1", "Sensor2", "Sensor3"]

        try:
            consentium.send_rest(data_buff, info_buff)
            consentium.summary()
        except Exception as e:
            print(e)
```
