# PythonCards
 ### User can import 1 to n decks to be shuffled and dealt to users. 
 ```
from dealer import CardTable
Dealer = CardTable()
blackJack = CardTable(5)
```
### There is 3 Functions:
```
build_deck()
shuffle(times=1) #User can set how many times they would like to shuffle 
deal_one_card(cards=1) #User can decided how many cards they would like to deal
```
### Running test:
- **Make sure you are in python venv**
```
source casino/bin/activate
```
```
pytest -v
```