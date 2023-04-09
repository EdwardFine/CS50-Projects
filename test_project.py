import project as pro
import random

test1 = ['2C', '2H','5C']
test1 = pro.Hand(test1)
test2 = ['5H','6H','7H']
test2 = pro.Hand(test2)
test3 = ['7C','2S','AH']
test3 = pro.Hand(test3)


play1 = 5000
play2 = 1000
pair1 = 0
pair2 = 1000
balance1 =10000
balance2 = 5000

def test_shuffle():
    assert pro.shuffle() == ['AH','2H','3H','4H','5H','6H','7H','8H','9H','10H','JH','QH','KH',
            'AD','2D','3D','4D','5D','6D','7D','8D','9D','10D','JD','QD','KD',
            'AS','2S','3S','4S','5S','6S','7S','8S','9S','10S','JS','QS','KS',
            'AC','2C','3C','4C','5C','6C','7C','8C','9C','10C','JC','QC','KC',]

def test_value_hand():
    assert test1.value_hand() == 2050202
    assert test2.value_hand()== 6070605
    assert test3.value_hand() == 1140702


def test_get_payout_and_check_bonus():
    assert pro.get_payout(play1,pair1,balance1, test2, test1) ==60000
    assert pro.get_payout(play1,pair2,balance1, test2, test1) ==101000
    assert pro.get_payout(play2,pair2,balance2,test3,test3)==7000

def test_hand_checkers():
    assert test2.check_flush() == True
    assert test2.check_straight() == True
    assert test2.check_three() == False
    assert test2.check_pair() == False