![HexText](https://raw.githubusercontent.com/SirScripter/HexText/main/HexText.png)
# HexText
Use Hex Code To Make Coloured Text With Python

## Installation/Setup
```cmd
pip install hextext
```
```cmd
python -m pip install hextext
```

## Using HexText With Print Statements
```python
from hextext import HexText

colorText = HexText()

print(colorText("HexText", color="#ff1100")) # Solid Colour
print(colorText("HextText", gradient=["#ff1100", "#ff8800", "#ffff00"])) # Gradient Text Colour
print(colorText("Hextext", gradient="#fff000")) # Using A Solid Color In A Gradient
```
## Using HexText With Input Statements
```python
from hextext import HexText

colorText = HexText()

input(colorText("How Good Is HexText: ", color="#ff1100")) # Solid Colour
input(colorText("How Good Is HexText: ", gradient=["#ff1100", "#ff8800", "#ffff00"])) # Gradient Text Colour
input(colorText("How Good Is HexText: ", gradient="#fff000")) # Using A Solid Color In A Gradient
```
