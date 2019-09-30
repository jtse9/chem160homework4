from cards import *
ntrials = 1000
results=[]
for i in range(ntrials):
    adeck=deck()
    adeck.shuffle()
    ascore = 0
    bscore = 0
    while adeck.cardsleft()>0:
        acard1=adeck.dealcard()
        bcard1=adeck.dealcard()
        if acard1.value()>bcard1.value():
            ascore += 2
        if acard1.value()<bcard1.value():
            bscore += 2
        if acard1.value()== bcard1.value():
            ascore += 1
            bscore += 1
    if ascore>bscore:
        results.append(ascore-bscore)
    if ascore<bscore:
        results.append(bscore-ascore)
    if ascore==bscore:
        results.append(ascore-bscore)
print("0",results.count(0)/ntrials)
print("2",results.count(2)/ntrials)
print("4",results.count(4)/ntrials)
print("6",results.count(6)/ntrials)
print("8",results.count(8)/ntrials)
print("10",results.count(10)/ntrials)
print("12",results.count(12)/ntrials)
print("14",results.count(14)/ntrials)
print("16",results.count(16)/ntrials)
print("18",results.count(18)/ntrials)
print("20",results.count(20)/ntrials)
print("22",results.count(22)/ntrials)
print("24",results.count(24)/ntrials)
print("26",results.count(26)/ntrials)
print("28",results.count(28)/ntrials)
print("30",results.count(30)/ntrials)
print("32",results.count(32)/ntrials)
print("34",results.count(34)/ntrials)
print("36",results.count(36)/ntrials)
print("38",results.count(38)/ntrials)
print("40",results.count(40)/ntrials)
print("42",results.count(42)/ntrials)
print("44",results.count(44)/ntrials)
print("46",results.count(46)/ntrials)
print("48",results.count(48)/ntrials)
print("50",results.count(50)/ntrials)
print("52",results.count(52)/ntrials)

