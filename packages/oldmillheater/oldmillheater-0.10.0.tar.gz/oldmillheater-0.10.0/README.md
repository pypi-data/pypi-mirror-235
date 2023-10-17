# Unnecessary Fork for maintaining the old cloud access.
They couldn't spend 2 dolars for setting up a proxy in their end so i need to spend more time to fix their bad product.

# oldpymill

Python3 library for Mill heater. The library uses the app API.

Based on https://pastebin.com/53Nk0wJA and Postman capturing from the app.

~~All requests are send unencrypted from the app :(~~ https://blog.roysolberg.com/2019/01/mill-heat

Control Mill heaters and get measured temperatures.



## Install
```
pip3 install oldmillheater
```

## Example:

```python
import oldmill as mill
mill_connection = mill.Mill('email@gmail.com', 'PASSWORD')
mill_connection.sync_connect()
mill_connection.sync_update_heaters()

heater = next(iter(mill_connection.heaters.values()))

mill_connection.sync_set_heater_temp(heater.device_id, 11)
mill_connection.sync_set_heater_control(heater.device_id, fan_status=0)

mill_connection.sync_close_connection()

```

The library is used as part of Home Assistant: https://github.com/home-assistant/core/blob/dev/homeassistant/components/mill/climate.py
