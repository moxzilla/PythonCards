from dealer import CardTable



Dealer = CardTable()
blackJack = CardTable(5)

def test_build_deck():
    print("Test Build Deck")
    assert Dealer.build_deck()

def test_shuffle():
    print("Test Shuffle")
    assert Dealer.shuffle() 

def test_deal_one():
    print("Test Deal Card")
    assert Dealer.deal_one_card()

def test_build_deal_whole_deck():
    assert Dealer.build_deck()
    assert Dealer.shuffle()
    for x in range(53):
        assert Dealer.deal_one_card()

def test_multi_deck_deal():
    assert blackJack.build_deck()
    assert blackJack.shuffle() 
    assert blackJack.deal_one_card(2)    
 
