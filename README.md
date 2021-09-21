# PythonCards
 ### User can import 1 to n decks to be shuffled and dealt to users. 

 # Usage
 ### **Note if you call shuffle with out build it will default to a 52 card deck.**
 ```
from dealer import CardTable
t = CardTable()
t.build_deck()
t.shuffle()
t.deal_one_card()

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